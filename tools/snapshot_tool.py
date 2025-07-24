import os
import sys
import json
import argparse
from typing import List, Dict, Any, Set, Optional, Tuple
import re

# Enhanced configuration for included/excluded paths and extensions
DEFAULT_INCLUDE_DIRS = ["."]
DEFAULT_INCLUDE_EXTENSIONS = [
    ".toml",
    ".py",
    ".yaml",
    ".yml",
    ".json",
    ".md",
    ".txt",
    ".html",
    ".bat",
    ".sh",
    ".jsx",
    ".js",
    ".json",
    ".css",
    "Dockerfile",  # Explicitly include Dockerfile
    "docker-compose.yml",  # Common docker-compose filename
    "Makefile",
    "Procfile",
    ".env",
    ".gitignore",
    ".dockerignore",
    ".proto",
    ".go",
    ".mod",
    ".sum",
    ".rs",
    ".cpp",
    ".c",
    ".h",
    ".ts",
    ".tsx"

]
DEFAULT_EXCLUDE_PATTERNS = [    
    "__pycache__",
    ".git",
    ".venv",
    ".vscode",
    ".idea",
    "build",
    "dist",
    "*.egg-info",
    "*.pyc",
    "*.so",
    "*.pyd",
    ".pytest_cache",
    ".mypy_cache",
    ".dataset",
    "dataset",
    ".logs",
    "logs",
    ".output",
    "output",
    "inputs",
    "outputs",
    ".tmp",
    "checkpoints",
    "reports",
    "docs/_build",
    "site",
    "node_modules",
    ".DS_Store",
    "Thumbs.db",
    "package-lock.json",  # Explicitly exclude package-lock.json
    "yarn.lock",         # Explicitly exclude yarn.lock
    "*.lock",            # General lock files
    "*.min.js",          # Minified JS files
    "*.min.css",         # Minified CSS files
    "project_snapshot.txt",
]

FILE_HEADER_TEMPLATE = "========== FILE: {file_path} =========="
SNAPSHOT_INFO_TEMPLATE = """PROJE KOD SNAPSHOT (TAM)
Toplam {total_files_placeholder} dosya bulundu ve eklendi.
Dahil Edilen Dizinler: {included_dirs_placeholder}
Dahil Edilen Uzantılar: {included_extensions_placeholder}
Hariç Tutulan Desenler/Yollar: {excluded_patterns_placeholder}
================================================================================
"""

def clean_code_comments(content: str, file_extension: str) -> str:
    """Removes most comments from code, attempting to preserve shebangs and type hints."""
    if file_extension not in [".py", ".sh", ".bat"]: return content
    lines = content.splitlines()
    cleaned_lines = []
    for line in lines:
        stripped_line = line.strip()
        if file_extension == ".py":
            # Preserve special comments like '# type:' and shebangs
            if stripped_line.startswith("# type:") or stripped_line.startswith("# noqa"): 
                cleaned_lines.append(line)
            elif stripped_line.startswith("#!/"): 
                cleaned_lines.append(line)
            # Remove inline comments
            elif "#" in line and not stripped_line.startswith("#"): 
                cleaned_lines.append(line.split("#", 1)[0].rstrip())
            # Remove full-line comments
            elif stripped_line.startswith("#"):
                continue # Skip full line comments
            else: 
                cleaned_lines.append(line)
        elif file_extension == ".sh":
            if stripped_line.startswith("#!/"): 
                cleaned_lines.append(line)
            elif not stripped_line.startswith("#"): 
                cleaned_lines.append(line)
        elif file_extension == ".bat":
            if not stripped_line.lower().startswith("rem "): 
                cleaned_lines.append(line)
        else: 
            cleaned_lines.append(line)
    return "\n".join(cleaned_lines)


def should_exclude(item_path: str, root_path: str, exclude_patterns: List[str]) -> bool:
    """Enhanced exclusion check with better pattern matching."""
    normalized_item_path = os.path.normpath(item_path)
    normalized_root_path = os.path.normpath(os.path.abspath(root_path))
    
    try:
        relative_item_path = os.path.relpath(normalized_item_path, normalized_root_path)
    except ValueError:
        relative_item_path = normalized_item_path
    
    relative_item_path_slashes = relative_item_path.replace(os.sep, "/")
    filename = os.path.basename(normalized_item_path)

    for pattern in exclude_patterns:
        # Exact filename match (e.g., "package-lock.json")
        if filename == pattern:
            return True
            
        # Extension pattern (e.g., "*.lock")
        if pattern.startswith("*.") and filename.endswith(pattern[1:]):
            return True
            
        # Directory name match (e.g., "node_modules")
        if "/" not in pattern and "." not in pattern and not pattern.startswith("*"):
            path_segments = relative_item_path_slashes.split("/")
            if pattern in path_segments:
                return True
                
        # Path prefix match (e.g., "docs/_build")
        if pattern in relative_item_path_slashes:
            return True
            
    return False


def collect_project_files_full(
    output_file: str,
    include_dirs: Optional[List[str]] = None,
    include_extensions: Optional[List[str]] = None,
    exclude_patterns: Optional[List[str]] = None,
    base_dir: str = ".",
    clean_comments: bool = False,
) -> None:
    if include_dirs is None: include_dirs = DEFAULT_INCLUDE_DIRS
    if include_extensions is None: include_extensions = DEFAULT_INCLUDE_EXTENSIONS
    if exclude_patterns is None: exclude_patterns = DEFAULT_EXCLUDE_PATTERNS

    abs_base_dir = os.path.abspath(base_dir)
    
    snapshot_content_header = SNAPSHOT_INFO_TEMPLATE.format(
        total_files_placeholder="{total_files_counter}",
        included_dirs_placeholder=", ".join(include_dirs),
        included_extensions_placeholder=", ".join(include_extensions),
        excluded_patterns_placeholder=", ".join(exclude_patterns),
    )

    all_found_relative_paths: Set[str] = set()
    content_parts: List[str] = [snapshot_content_header]
    processed_files_count = 0

    for inc_dir_pattern in include_dirs:
        current_scan_dir = os.path.abspath(os.path.join(abs_base_dir, inc_dir_pattern))
        if not os.path.exists(current_scan_dir):
            print(f"Warning: Include directory '{inc_dir_pattern}' (resolved to '{current_scan_dir}') does not exist. Skipping.")
            continue

        for root, dirs, files in os.walk(current_scan_dir, topdown=True):
            # Filter directories in-place to prevent os.walk from entering excluded ones
            dirs[:] = [
                d for d in dirs
                if not should_exclude(os.path.join(root, d), abs_base_dir, exclude_patterns)
            ]
            
            for file_name in files:
                file_path = os.path.join(root, file_name)
                relative_file_path = os.path.relpath(file_path, abs_base_dir)
                display_path = relative_file_path.replace(os.sep, "/")

                # Skip if already processed
                if display_path in all_found_relative_paths:
                    continue 

                # Apply exclusion patterns to files
                if should_exclude(file_path, abs_base_dir, exclude_patterns):
                    continue

                _, file_extension = os.path.splitext(file_name)
                filename_lower = file_name.lower()
                
                # Check if file should be included based on:
                # 1. Extension match (e.g., ".py")
                # 2. Full filename match (e.g., "Dockerfile")
                # 3. Extensionless but in include_extensions (e.g., "Makefile")
                should_include = (
                    file_extension.lower() in [ext.lower() for ext in include_extensions if ext.startswith('.')] or
                    filename_lower in [ext.lower() for ext in include_extensions if not ext.startswith('.')] or
                    (not file_extension and filename_lower in [ext.lower() for ext in include_extensions if not ext.startswith('.')])
                )
                
                if should_include:
                    all_found_relative_paths.add(display_path)
                    try:
                        with open(file_path, "r", encoding="utf-8", errors="ignore") as f:
                            file_content = f.read()
                        
                        if clean_comments:
                            file_content = clean_code_comments(file_content, file_extension)
                        
                        content_parts.append(f"\n{FILE_HEADER_TEMPLATE.format(file_path=display_path)}\n")
                        content_parts.append(file_content)
                        processed_files_count += 1
                    except Exception as e:
                        print(f"Error reading file {relative_file_path}: {e}")
                        content_parts.append(f"\nError reading file {relative_file_path}: {e}\n")

    final_header_with_count = content_parts[0].replace("{total_files_counter}", str(processed_files_count))
    content_parts[0] = final_header_with_count

    with open(output_file, "w", encoding="utf-8") as f:
        f.write("".join(content_parts))

    print(f"Project snapshot (full) generated: {output_file}")
    print(f"Total {processed_files_count} files included.")


def restore_from_full_snapshot(
    snapshot_file: str,
    target_dir: str = ".",
    dry_run: bool = False,
    overwrite_existing: bool = False,
) -> None:
    print(f"Restoring project from snapshot: {snapshot_file}")
    if dry_run: print("DRY RUN: No files will be written.")

    try:
        with open(snapshot_file, "r", encoding="utf-8") as f:
            full_content = f.read()
    except FileNotFoundError:
        print(f"Error: Snapshot file '{snapshot_file}' not found.")
        return
    except Exception as e:
        print(f"Error reading snapshot file: {e}")
        return

    file_block_pattern = re.compile(
        r"^========== FILE: (.*?) ==========\n"
        r"(.*?)"
        r"(?=\n========== FILE: |\Z)",
        re.MULTILINE | re.DOTALL
    )
    
    info_header_last_line = SNAPSHOT_INFO_TEMPLATE.splitlines()[-1]
    content_start_index = full_content.find(info_header_last_line)
    if content_start_index == -1:
        print("Error: Could not find the end of the snapshot info header.")
        return
    
    content_to_parse = full_content[content_start_index + len(info_header_last_line):].lstrip('\n')

    files_restored = 0
    files_skipped = 0
    files_overwritten = 0
    
    matches = file_block_pattern.finditer(content_to_parse)

    for match in matches:
        relative_file_path = match.group(1).strip()
        content_part = match.group(2) 

        os_specific_relative_path = relative_file_path.replace("/", os.sep)
        target_file_path = os.path.join(target_dir, os_specific_relative_path)
        
        print(f"Processing file: {relative_file_path} (Content length: {len(content_part)}) -> {target_file_path}")

        if os.path.exists(target_file_path) and not overwrite_existing:
            print(f"  SKIPPED: File '{target_file_path}' already exists (overwrite_existing is False).")
            files_skipped += 1
            continue

        if os.path.exists(target_file_path) and overwrite_existing:
            print(f"  OVERWRITING: File '{target_file_path}'.")
            files_overwritten += 1

        if not dry_run:
            try:
                os.makedirs(os.path.dirname(target_file_path), exist_ok=True)
                with open(target_file_path, "w", encoding="utf-8") as f:
                    f.write(content_part)
                files_restored += 1
            except Exception as e:
                print(f"  ERROR: Could not write file '{target_file_path}': {e}")
        else:
            if not os.path.exists(os.path.dirname(target_file_path)):
                print(f"  DRY RUN: Would create directory {os.path.dirname(target_file_path)}")
            print(f"  DRY RUN: Would write {len(content_part)} bytes to {target_file_path}")
            files_restored += 1

    print("\n--- Restoration Summary ---")
    print(f"Files processed for restoration: {files_restored}")
    if not dry_run:
        print(f"Files actually written/overwritten: {files_restored - files_skipped}")
        print(f"Files overwritten: {files_overwritten}")
    print(f"Files skipped (already exist and overwrite=False): {files_skipped}")


def main():
    parser = argparse.ArgumentParser(description="Enhanced Project Snapshot Tool")
    subparsers = parser.add_subparsers(dest="command", required=True)

    parser_collect = subparsers.add_parser(
        "collect", help="Collect project files into a single snapshot file."
    )
    parser_collect.add_argument(
        "output_file",
        type=str,
        default="project_snapshot_full.txt",
        nargs="?",
        help="Path to the output snapshot file (default: project_snapshot_full.txt)",
    )
    parser_collect.add_argument(
        "--include-dir",
        action="append",
        dest="include_dirs",
        help="Directory to include (relative to base_dir or absolute). Can be used multiple times.",
    )
    parser_collect.add_argument(
        "--include-ext",
        action="append",
        dest="include_extensions",
        help="File extension to include (e.g., .py, .md). Can be used multiple times.",
    )
    parser_collect.add_argument(
        "--exclude-pattern",
        action="append",
        dest="exclude_patterns",
        help="Pattern/path to exclude. Can be used multiple times.",
    )
    parser_collect.add_argument(
        "--base-dir",
        type=str,
        default=".",
        help="Base directory for the project (default: current directory).",
    )
    parser_collect.add_argument(
        "--clean-comments",
        action="store_true",
        help="Attempt to remove comments from collected code files (.py, .sh, .bat).",
    )

    parser_restore = subparsers.add_parser(
        "restore", help="Restore project files from a snapshot."
    )
    parser_restore.add_argument(
        "snapshot_file", type=str, help="Path to the snapshot file to restore from."
    )
    parser_restore.add_argument(
        "--target-dir",
        type=str,
        default=".",
        help="Directory where files will be restored (default: current directory).",
    )
    parser_restore.add_argument(
        "--dry-run",
        action="store_true",
        help="Simulate restoration without writing any files.",
    )
    parser_restore.add_argument(
        "--overwrite",
        action="store_true",
        dest="overwrite_existing",
        help="Overwrite files if they already exist in the target directory.",
    )

    args = parser.parse_args()

    if args.command == "collect":
        final_include_dirs = args.include_dirs if args.include_dirs is not None else DEFAULT_INCLUDE_DIRS
        final_include_extensions = args.include_extensions if args.include_extensions is not None else DEFAULT_INCLUDE_EXTENSIONS
        final_exclude_patterns = args.exclude_patterns if args.exclude_patterns is not None else DEFAULT_EXCLUDE_PATTERNS
        
        collect_project_files_full(
            output_file=args.output_file,
            include_dirs=final_include_dirs,
            include_extensions=final_include_extensions,
            exclude_patterns=final_exclude_patterns,
            base_dir=args.base_dir,
            clean_comments=args.clean_comments,
        )
    elif args.command == "restore":
        restore_from_full_snapshot(
            snapshot_file=args.snapshot_file,
            target_dir=args.target_dir,
            dry_run=args.dry_run,
            overwrite_existing=args.overwrite_existing,
        )


if __name__ == "__main__":
    print("Enhanced Project Snapshot Tool")
    print("Collects project files into a single snapshot file or restores from a snapshot.")
    print("Use 'collect' to create a snapshot and 'restore' to restore files from it.")    
    main()