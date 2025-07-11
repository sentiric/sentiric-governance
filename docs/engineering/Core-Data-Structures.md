# 🧬 Sentiric: Çekirdek Veri Yapıları (v2.0 - SQLModel & Multi-Tenancy)

Bu doküman, hem çalışma zamanı (Redis) hem de kalıcı (PostgreSQL) veri yapılarımızı tanımlar. **`SQLModel`**, `Pydantic`'in veri doğrulama gücünü `SQLAlchemy`'nin ORM yetenekleriyle birleştirir.

## 1. Çalışma Zamanı Veri Yapıları (Pydantic - Redis için)

Bu modeller, bir çağrının yaşam döngüsü boyunca Redis'te tutulan anlık durumu temsil eder.

```python
from pydantic import BaseModel, Field
from typing import List, Dict, Any, Optional
from datetime import datetime

class TaskState(BaseModel):
    task_name: str
    state_data: Dict[str, Any] = Field(default_factory=dict)
    start_time: datetime = Field(default_factory=datetime.utcnow)

class CallContext(BaseModel):
    """Bir çağrının yaşam döngüsü boyunca durumunu tutan nesne."""
    call_sid: str
    trace_id: str
    tenant_id: str  # Ürünleştirme için Müşteri ID'si
    caller_id: str
    
    task_stack: List[TaskState] = Field(default_factory=list) # Görev yığınını yönetmek için
    
    interaction_history: List[Dict[str, Any]] = Field(default_factory=list)
    
    call_start_time: datetime = Field(default_factory=datetime.utcnow)
    last_interaction_time: datetime = Field(default_factory=datetime.utcnow)

    class Config:
        validate_assignment = True
```

## 2. Kalıcı Veri Modelleri (SQLModel - PostgreSQL için)

Bu modeller, veritabanında kalıcı olarak saklanacak olan verileri tanımlar ve **çoklu kullanım (multi-tenancy)** mimarisini destekler.

```python
from typing import List, Optional
from sqlmodel import Field, Relationship, SQLModel
from datetime import datetime

class Tenant(SQLModel, table=True):
    """Platformu kullanan her bir müşteriyi temsil eder."""
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str = Field(index=True, unique=True)
    is_active: bool = True
    
    calls: List["Call"] = Relationship(back_populates="tenant")
    users: List["User"] = Relationship(back_populates="tenant")

class User(SQLModel, table=True):
    """Dashboard'a erişimi olan kullanıcılar."""
    id: Optional[int] = Field(default=None, primary_key=True)
    email: str = Field(unique=True, index=True)
    hashed_password: str
    
    tenant_id: int = Field(foreign_key="tenant.id")
    tenant: Tenant = Relationship(back_populates="users")

class Call(SQLModel, table=True):
    """Her bir telefon çağrısının ana kaydı."""
    id: Optional[int] = Field(default=None, primary_key=True)
    call_sid: str = Field(unique=True, index=True)
    caller_id: str
    start_time: datetime
    end_time: Optional[datetime] = None
    status: str # e.g., "completed", "failed", "abandoned"
    
    tenant_id: int = Field(foreign_key="tenant.id")
    tenant: Tenant = Relationship(back_populates="calls")
    
    # JSONB tipinde transkript ve diğer meta veriler saklanabilir
    full_transcript: Optional[Dict] = Field(default=None)

# Diğer modeller (Tasks, Interactions vb.) benzer şekilde tanımlanabilir.
```
