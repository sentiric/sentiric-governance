import os
import sys
import json
import argparse
from typing import List, Dict, Any, Set, Optional, Tuple, Union
import re
from fnmatch import fnmatch

# Enhanced configuration for included/excluded paths and extensions
DEFAULT_INCLUDE_DIRS = ["."]
DEFAULT_INCLUDE_EXTENSIONS = [
    # Config files
    ".toml", ".yaml", ".yml", ".json", ".ini", ".cfg", ".conf",
    
    # Scripts
    ".py", ".sh", ".bat", ".ps1", ".cmd",
    
    # Web
    ".html", ".css", ".js", ".jsx", ".ts", ".tsx",
    
    # Documentation
    ".md", ".txt", ".rst",
    
    # Source code
    ".go", ".rs", ".cpp", ".c", ".h", ".hpp", ".java", ".kt", ".scala",
    ".swift", ".m", ".php", ".rb", ".pl", ".lua",
    
    # Build/config
    "Dockerfile", "docker-compose*.yml", "Makefile", "Procfile", "Jenkinsfile",
    ".gitignore", ".dockerignore", ".editorconfig", ".eslintrc", ".prettierrc",
    
    # Data formats
    ".csv", ".xml", ".proto", ".sql",
    
    # Project files
    "*.mod", "*.sum", "go.mod", "go.sum", "requirements.txt", "package.json",
    "Cargo.toml", "pom.xml", "build.gradle", "*.gradle"

    # env
    ".env.example", ".env.docker"
]

DEFAULT_EXCLUDE_PATTERNS = [
    # Version control
    ".git", ".svn", ".hg",
    
    # Build artifacts
    "build", "dist", "bin", "out", "target", "debug", "release",
    "*.egg-info", "*.pyc", "*.so", "*.pyd", "*.class",
    
    # Dependency directories
    "node_modules", "vendor", ".bundle", "jspm_packages",
    
    # Cache and temp files
    "__pycache__", ".cache", ".tmp", "temp", "tmp",
    
    # IDE specific
    ".vscode", ".idea", ".vs", "*.suo", "*.ntvs*", "*.njsproj", "*.sln",
    
    # Virtual environments
    ".venv", "venv", "env", ".env", "ENV",
    
    # Logs and datasets
    "logs", ".logs", "*.log", "dataset", ".dataset", "data", ".data",
    
    # Output folders
    ".output", "output", "artifacts", "coverage", ".nyc_output",
    
    # Documentation builds
    "docs/_build", "site", "_site", "public", "dist",
    
    # System files
    ".DS_Store", "Thumbs.db", "desktop.ini",
    
    # Lock files
    "package-lock.json", "yarn.lock", "*.lock", "Cargo.lock", "Gemfile.lock",
    "Pipfile.lock", "composer.lock",
    
    # Minified/bundled files
    "*.min.js", "*.min.css", "bundle.js", "*.bundle.js",
    
    # Generated files
    "*.d.ts", "*.map", "*.snap",
    
    # Custom exclusions
    "project_snapshot_full.txt", "checkpoints", "reports",
    
    # Binary files
    "*.exe", "*.dll", "*.o", "*.a", "*.lib", "*.dylib", "*.jar", "*.war",
    
    # Images and media
    "*.png", "*.jpg", "*.jpeg", "*.gif", "*.bmp", "*.tiff", "*.ico",
    "*.mp3", "*.wav", "*.mp4", "*.avi", "*.mov",
    
    # Archives
    "*.zip", "*.tar", "*.gz", "*.7z", "*.rar",
    
    # Database files
    "*.db", "*.sqlite", "*.sqlite3", "*.mdb"
]

# Flutter projeleri için özel ayarlar
FLUTTER_INCLUDE_DIRS = ["lib", "assets", "test"]  # Sadece bu dizinleri tarar
FLUTTER_INCLUDE_EXTENSIONS = [
    ".dart", 
    ".yaml", 
    ".md", 
    "pubspec.yaml",
    ".txt"
]
FLUTTER_EXCLUDE_PATTERNS = [
    "build/",
    ".dart_tool/",
    ".idea/",
    "ios/",
    "android/",
    "web/",
    "linux/",
    "windows/",
    "macos/",
    "*.iml",
    ".flutter-plugins*",
    ".metadata"
]

# Language specific exclude patterns
LANGUAGE_SPECIFIC_EXCLUDES = {
    "python": ["*.py[cod]", "__pycache__", ".pytest_cache", ".mypy_cache"],
    "nodejs": ["node_modules", "*.min.js", "dist", "build"],
    "rust": ["target", "Cargo.lock"],
    "go": ["vendor", "*.test"],
    "java": ["*.class", "target", "build"],
    "ruby": ["Gemfile.lock", ".bundle", "vendor"]
}

FILE_HEADER_TEMPLATE = "========== FILE: {file_path} =========="
SNAPSHOT_INFO_TEMPLATE = """PROJE KOD SNAPSHOT (TAM)
Toplam {total_files_placeholder} dosya bulundu ve eklendi.
Dahil Edilen Dizinler: {included_dirs_placeholder}
Dahil Edilen Uzantılar: {included_extensions_placeholder}
Hariç Tutulan Desenler/Yollar: {excluded_patterns_placeholder}
================================================================================
"""

def detect_project_type(base_dir: str) -> List[str]:
    """Detect project type based on configuration files."""
    project_types = []
    
    if os.path.exists(os.path.join(base_dir, "package.json")):
        project_types.append("nodejs")
    if os.path.exists(os.path.join(base_dir, "Cargo.toml")):
        project_types.append("rust")
    if os.path.exists(os.path.join(base_dir, "go.mod")):
        project_types.append("go")
    if os.path.exists(os.path.join(base_dir, "requirements.txt")) or \
       os.path.exists(os.path.join(base_dir, "setup.py")):
        project_types.append("python")
    if os.path.exists(os.path.join(base_dir, "pom.xml")) or \
       os.path.exists(os.path.join(base_dir, "build.gradle")):
        project_types.append("java")
    if os.path.exists(os.path.join(base_dir, "Gemfile")):
        project_types.append("ruby")
    
    return project_types

def clean_code_comments(content: str, file_extension: str) -> str:
    """Removes most comments from code, attempting to preserve shebangs and type hints."""
    if file_extension not in [".py", ".sh", ".bat", ".js", ".ts", ".go", ".rs", ".cpp", ".c", ".h"]: 
        return content
    
    lines = content.splitlines()
    cleaned_lines = []
    
    for line in lines:
        stripped_line = line.strip()
        
        # Preserve shebangs in any file type
        if stripped_line.startswith("#!/"):
            cleaned_lines.append(line)
            continue
            
        # Language-specific comment handling
        if file_extension == ".py":
            if stripped_line.startswith(("# type:", "# noqa", "# pylint:", "# fmt:")): 
                cleaned_lines.append(line)
            elif "#" in line and not stripped_line.startswith("#"):
                cleaned_lines.append(line.split("#", 1)[0].rstrip())
            elif not stripped_line.startswith("#"):
                cleaned_lines.append(line)
                
        elif file_extension in (".sh", ".bash"):
            if not stripped_line.startswith("#"):
                cleaned_lines.append(line)
                
        elif file_extension == ".bat":
            if not stripped_line.lower().startswith("rem "):
                cleaned_lines.append(line)
                
        elif file_extension in (".js", ".ts", ".go", ".rs", ".cpp", ".c", ".h"):
            # Handle both single-line and multi-line comments
            if "//" in line and not stripped_line.startswith("//"):
                cleaned_lines.append(line.split("//", 1)[0].rstrip())
            elif not stripped_line.startswith("//"):
                cleaned_lines.append(line)
                
        else:
            cleaned_lines.append(line)
    
    return "\n".join(cleaned_lines)

def should_exclude(
    item_path: str, 
    root_path: str, 
    exclude_patterns: List[str],
    project_types: Optional[List[str]] = None
) -> bool:
    """Enhanced exclusion check with better pattern matching."""
    if project_types is None:
        project_types = []
    
    normalized_item_path = os.path.normpath(item_path)
    normalized_root_path = os.path.normpath(os.path.abspath(root_path))
    
    try:
        relative_item_path = os.path.relpath(normalized_item_path, normalized_root_path)
    except ValueError:
        relative_item_path = normalized_item_path
    
    relative_item_path_slashes = relative_item_path.replace(os.sep, "/")
    filename = os.path.basename(normalized_item_path)

    # First check language-specific excludes
    for lang in project_types:
        for pattern in LANGUAGE_SPECIFIC_EXCLUDES.get(lang, []):
            if fnmatch(filename, pattern) or fnmatch(relative_item_path_slashes, pattern):
                return True

    # Then check general excludes
    for pattern in exclude_patterns:
        # Handle wildcard patterns
        if fnmatch(filename, pattern) or fnmatch(relative_item_path_slashes, pattern):
            return True
            
    return False

def collect_project_files_full(
    output_file: str,
    include_dirs: Optional[List[str]] = None,
    include_extensions: Optional[List[str]] = None,
    exclude_patterns: Optional[List[str]] = None,
    base_dir: str = ".",
    clean_comments: bool = False,
    max_file_size: Optional[int] = 1024 * 1024,  # 1MB default max size
) -> None:
    if include_dirs is None: 
        include_dirs = DEFAULT_INCLUDE_DIRS
    if include_extensions is None: 
        include_extensions = DEFAULT_INCLUDE_EXTENSIONS
    if exclude_patterns is None: 
        exclude_patterns = DEFAULT_EXCLUDE_PATTERNS

    abs_base_dir = os.path.abspath(base_dir)
    project_types = detect_project_type(abs_base_dir)
    
    snapshot_content_header = SNAPSHOT_INFO_TEMPLATE.format(
        total_files_placeholder="{total_files_counter}",
        included_dirs_placeholder=", ".join(include_dirs),
        included_extensions_placeholder=", ".join(include_extensions),
        excluded_patterns_placeholder=", ".join(exclude_patterns),
    )

    all_found_relative_paths: Set[str] = set()
    content_parts: List[str] = [snapshot_content_header]
    processed_files_count = 0
    skipped_files_count = 0
    skipped_due_to_size = 0

    for inc_dir_pattern in include_dirs:
        current_scan_dir = os.path.abspath(os.path.join(abs_base_dir, inc_dir_pattern))
        if not os.path.exists(current_scan_dir):
            print(f"Warning: Include directory '{inc_dir_pattern}' (resolved to '{current_scan_dir}') does not exist. Skipping.")
            continue

        for root, dirs, files in os.walk(current_scan_dir, topdown=True):
            # Filter directories in-place to prevent os.walk from entering excluded ones
            dirs[:] = [
                d for d in dirs
                if not should_exclude(
                    os.path.join(root, d), 
                    abs_base_dir, 
                    exclude_patterns,
                    project_types
                )
            ]
            
            for file_name in files:
                file_path = os.path.join(root, file_name)
                relative_file_path = os.path.relpath(file_path, abs_base_dir)
                display_path = relative_file_path.replace(os.sep, "/")

                # Skip if already processed
                if display_path in all_found_relative_paths:
                    continue 

                # Apply exclusion patterns to files
                if should_exclude(file_path, abs_base_dir, exclude_patterns, project_types):
                    skipped_files_count += 1
                    continue

                # Check file size if max_file_size is set
                if max_file_size is not None:
                    try:
                        file_size = os.path.getsize(file_path)
                        if file_size > max_file_size:
                            print(f"Skipping large file: {display_path} ({file_size} bytes)")
                            skipped_due_to_size += 1
                            continue
                    except OSError as e:
                        print(f"Warning: Could not check size of {display_path}: {e}")
                        continue

                _, file_extension = os.path.splitext(file_name)
                filename_lower = file_name.lower()
                
                # Check if file should be included
                should_include = (
                    any(fnmatch(filename_lower, ext.lower()) for ext in include_extensions if ext.startswith('*')) or
                    any(fnmatch(filename_lower, f"*{ext.lower()}") for ext in include_extensions if ext.startswith('.')) or
                    filename_lower in [ext.lower() for ext in include_extensions if not ext.startswith(('*', '.'))]
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
                    except UnicodeDecodeError:
                        print(f"Skipping binary file: {display_path}")
                        skipped_files_count += 1
                    except Exception as e:
                        print(f"Error reading file {relative_file_path}: {e}")
                        content_parts.append(f"\nError reading file {relative_file_path}: {e}\n")

    final_header_with_count = content_parts[0].replace("{total_files_counter}", str(processed_files_count))
    content_parts[0] = final_header_with_count

    with open(output_file, "w", encoding="utf-8") as f:
        f.write("".join(content_parts))

    print(f"\nProject snapshot (full) generated: {output_file}")
    print(f"Total files processed: {processed_files_count + skipped_files_count + skipped_due_to_size}")
    print(f"Files included: {processed_files_count}")
    print(f"Files excluded by patterns: {skipped_files_count}")
    print(f"Files skipped due to size: {skipped_due_to_size}")
    if project_types:
        print(f"Detected project types: {', '.join(project_types)}")

def restore_from_full_snapshot(
    snapshot_file: str,
    target_dir: str = ".",
    dry_run: bool = False,
    overwrite_existing: bool = False,
) -> None:
    print(f"Restoring project from snapshot: {snapshot_file}")
    if dry_run: 
        print("DRY RUN: No files will be written.")

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
        
        print(f"Processing file: {relative_file_path} -> {target_file_path}")

        if os.path.exists(target_file_path) and not overwrite_existing:
            print(f"  SKIPPED: File already exists (overwrite_existing is False).")
            files_skipped += 1
            continue

        if os.path.exists(target_file_path) and overwrite_existing:
            print(f"  OVERWRITING: Existing file.")
            files_overwritten += 1

        if not dry_run:
            try:
                os.makedirs(os.path.dirname(target_file_path), exist_ok=True)
                with open(target_file_path, "w", encoding="utf-8") as f:
                    f.write(content_part)
                files_restored += 1
            except Exception as e:
                print(f"  ERROR: Could not write file: {e}")
        else:
            if not os.path.exists(os.path.dirname(target_file_path)):
                print(f"  DRY RUN: Would create directory {os.path.dirname(target_file_path)}")
            print(f"  DRY RUN: Would write {len(content_part)} bytes to file")
            files_restored += 1

    print("\n--- Restoration Summary ---")
    print(f"Total files in snapshot: {files_restored + files_skipped}")
    print(f"Files processed for restoration: {files_restored}")
    if not dry_run:
        print(f"Files actually written/overwritten: {files_restored - files_skipped}")
        print(f"Files overwritten: {files_overwritten}")
    print(f"Files skipped (already exist and overwrite=False): {files_skipped}")

def main():
    parser = argparse.ArgumentParser(
        description="Enhanced Project Snapshot Tool",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter
    )
    subparsers = parser.add_subparsers(dest="command", required=True)

    # Collect command
    parser_collect = subparsers.add_parser(
        "collect", 
        help="Collect project files into a single snapshot file.",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter
    )
    parser_collect.add_argument(
        "output_file",
        type=str,
        nargs="?",
        default="project_snapshot_full.txt",
        help="Path to the output snapshot file",
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
        help="Base directory for the project",
    )
    parser_collect.add_argument(
        "--clean-comments",
        action="store_true",
        help="Attempt to remove comments from collected code files",
    )
    parser_collect.add_argument(
        "--max-size",
        type=int,
        default=1024*1024,  # 1MB
        help="Maximum file size to include (in bytes). Set to 0 for no limit.",
    )
    parser_collect.add_argument(
        "--no-size-limit",
        action="store_true",
        help="Disable file size limit (equivalent to --max-size=0)",
    )

    # Restore command
    parser_restore = subparsers.add_parser(
        "restore", 
        help="Restore project files from a snapshot.",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter
    )
    parser_restore.add_argument(
        "snapshot_file", 
        type=str, 
        help="Path to the snapshot file to restore from"
    )
    parser_restore.add_argument(
        "--target-dir",
        type=str,
        default=".",
        help="Directory where files will be restored",
    )
    parser_restore.add_argument(
        "--dry-run",
        action="store_true",
        help="Simulate restoration without writing any files",
    )
    parser_restore.add_argument(
        "--overwrite",
        action="store_true",
        dest="overwrite_existing",
        help="Overwrite files if they already exist in the target directory",
    )

    args = parser.parse_args()

    if args.command == "collect":
        final_include_dirs = args.include_dirs if args.include_dirs is not None else DEFAULT_INCLUDE_DIRS
        final_include_extensions = args.include_extensions if args.include_extensions is not None else DEFAULT_INCLUDE_EXTENSIONS
        final_exclude_patterns = args.exclude_patterns if args.exclude_patterns is not None else DEFAULT_EXCLUDE_PATTERNS
        
        max_file_size = 0 if args.no_size_limit else args.max_size
        
        collect_project_files_full(
            output_file=args.output_file,
            include_dirs=final_include_dirs,
            include_extensions=final_include_extensions,
            exclude_patterns=final_exclude_patterns,
            base_dir=args.base_dir,
            clean_comments=args.clean_comments,
            max_file_size=max_file_size,
        )
    elif args.command == "restore":
        restore_from_full_snapshot(
            snapshot_file=args.snapshot_file,
            target_dir=args.target_dir,
            dry_run=args.dry_run,
            overwrite_existing=args.overwrite,
        )

if __name__ == "__main__":
    print("Enhanced Project Snapshot Tool")
    print("Collects project files into a single snapshot file or restores from a snapshot.")
    print("Use 'collect' to create a snapshot and 'restore' to restore files from it.")    
    main()