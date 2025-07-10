# 🧬 Sentiric: Çekirdek Veri Yapıları

Bu doküman, Sentiric platformu içindeki servisler ve modüller arasında dolaşan temel veri yapılarının (kontratların) tanımıdır. Bu yapılar, sistemin tutarlılığı için esastır ve `Pydantic` modelleri olarak implemente edilecektir.

## 1. TaskResult

Bir `BaseTask`'ın `execute()` metodu tarafından döndürülen standart sonuç nesnesi. `agent-worker`'ın bir sonraki adımı belirlemesini sağlar.

```python
from pydantic import BaseModel, Field
from typing import Optional, Dict, Any

class TaskResult(BaseModel):
    """Bir görev adımının sonucunu temsil eder."""

    is_successful: bool = Field(
        ..., description="Adımın başarıyla tamamlanıp tamamlanmadığı."
    )
    is_task_finished: bool = Field(
        False, description="Bu adımın görevin tamamını bitirip bitirmediği."
    )
    next_prompt: Optional[str] = Field(
        None, description="Eğer görev devam ediyorsa, kullanıcıya sorulacak bir sonraki soru."
    )
    collected_data: Dict[str, Any] = Field(
        default_factory=dict, description="Bu adımda kullanıcıdan toplanan yapılandırılmış veri."
    )
    failure_reason: Optional[str] = Field(
        None, description="Eğer adım başarısız olduysa, nedeni."
    )
```

## 2. CallContext

Her bir çağrı boyunca Redis'te yaşayan ve çağrının tüm durumunu tutan ana nesne.

```python
from pydantic import BaseModel, Field
from typing import List, Dict, Any, Optional
from datetime import datetime

class CallContext(BaseModel):
    """Bir çağrının yaşam döngüsü boyunca durumunu tutan nesne."""

    call_sid: str = Field(..., description="Telefoni sağlayıcısından gelen benzersiz çağrı ID'si.")
    trace_id: str = Field(..., description="Dağıtık izleme için benzersiz trace ID.")
    
    caller_id: str = Field(..., description="Arayan kişinin telefon numarası.")
    customer_info: Optional[Dict[str, Any]] = Field(None, description="CRM'den çekilen müşteri bilgileri.")
    
    active_task_name: Optional[str] = Field(None, description="Şu anda aktif olan görevin adı.")
    task_state: Dict[str, Any] = Field(default_factory=dict, description="Aktif görevin kendi iç durumu.")
    
    interaction_history: List[Dict[str, Any]] = Field(
        default_factory=list, description="Kullanıcı ve sistem arasındaki diyalog geçmişi."
    )
    
    call_start_time: datetime = Field(default_factory=datetime.utcnow)
    last_interaction_time: datetime = Field(default_factory=datetime.utcnow)

    class Config:
        validate_assignment = True # Alanlar güncellendiğinde yeniden validasyon yapar.
```
