# vllm-project/vllm#28102: [Bug]: switching between multiple LoRAs in multimodal scenario takes long time

| 字段 | 值 |
| --- | --- |
| Issue | [#28102](https://github.com/vllm-project/vllm/issues/28102) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 4; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: switching between multiple LoRAs in multimodal scenario takes long time

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug ```python import os from typing import Dict, Any, List, Optional from typing import NamedTuple, Optional from vllm import LLM, EngineArgs, SamplingParams from vllm.lora.request import LoRARequest from pathlib import Path from dataclasses import asdict import base64, io from PIL import Image import json from time import time from tool.logger import setup_logger logger = setup_logger(__name__) IMAGE_MIN_PIXES = 784 IMAGE_MAX_PIXES = 12600000 MAX_TOKENS = 2048 CUTOFF_LEN = 30000 TEMPERATURE = 0.0 BASE_MODEL_DIR = "Qwen2.5-VL-7B-Instruct" MODEL_CONFIG = { "pi": { "system_prompt": """You are an expert in foreign trade document analysis. """, "user_prompt": """ put your prompt here. """, "lora_adapter_path": "../pi_lora", "lora_id": 1 }, "foreign_company_card": { "system_prompt": """ You are an expert in infomation extraction. """, "user_prompt": """ put your prompt here. """, "lora_adapter_path": "../foreign_company_card_lora", "lora_id": 2 } } class ModelRequestData(NamedTuple): engine_args: EngineArgs prompts: list[str] stop_token_ids: Optional[list[int]] = None lora_requests: Optional[list[LoRARequest]] = None class MultiLoraOcrInf...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 5: [Bug]: switching between multiple LoRAs in multimodal scenario takes long time bug;stale ### Your current environment ### 🐛 Describe the bug ```python import os from typing import Dict, Any, List, Optional from typing i...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 3: engine_args = EngineArgs( model=str(model_path), dtype='bfloat16', max_model_len=cutoff_len, max_num_seqs=5, mm_processor_kwargs={ "min_pixels": image_min_pixels, "max_pixels": image_max_pixels,
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 3: tching between multiple LoRAs in multimodal scenario takes long time bug;stale ### Your current environment ### 🐛 Describe the bug ```python import os from typing import Dict, Any, List, Optional from typing import Name...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: stale ### Your current environment ### 🐛 Describe the bug ```python import os from typing import Dict, Any, List, Optional from typing import NamedTuple, Optional from vllm import LLM, EngineArgs, SamplingParams from vl...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: _data is None: logger.error(f"image data is too large or too small") return {"output": "", "time": 0, "lora_adapter_name": lora_adapter_name} # 检查传入的lora_adapter_name是否在MODEL_CONFIG中存在对应键值对 if lora_adapter_name not in M...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
