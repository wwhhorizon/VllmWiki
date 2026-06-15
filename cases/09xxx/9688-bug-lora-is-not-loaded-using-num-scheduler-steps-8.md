# vllm-project/vllm#9688: [Bug]: lora is not loaded using `num_scheduler_steps=8`

| 字段 | 值 |
| --- | --- |
| Issue | [#9688](https://github.com/vllm-project/vllm/issues/9688) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | development |
| 工作域 | frontend_api;model_support;quantization;sampling_logits |
| 子分类 | debug |
| Operator 关键词 | cuda;fp8;sampling |
| 症状 |  |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: lora is not loaded using `num_scheduler_steps=8`

### Issue 正文摘录

### 🐛 Describe the bug When I run lora request using `num_scheduler_steps` > 1, even if I give a wrong lora path, it doesn't report an error, but gives wrong result. ### The bug can be reproduced by this code. ``` import os import torch from typing import List, Optional, Tuple import pandas as pd from huggingface_hub import snapshot_download from vllm import EngineArgs, LLMEngine, RequestOutput, SamplingParams from vllm.lora.request import LoRARequest def create_test_prompts( lora_path: str ) -> List[Tuple[str, SamplingParams, Optional[LoRARequest]]]: return [ ( "What happens when you put oil into water?", # noqa: E501 SamplingParams(temperature=1e-7, max_tokens=128, top_k =1, top_p = 1e-5, stop_token_ids=[32003]), LoRARequest("sql-lora", 1, lora_path)), ] def process_requests(engine: LLMEngine, test_prompts: List[Tuple[str, SamplingParams, Optional[LoRARequest]]]): """Continuously process a list of prompts and handle the outputs.""" request_id = 0 while test_prompts or engine.has_unfinished_requests(): if test_prompts: prompt, sampling_params, lora_request = test_prompts.pop(0) engine.add_request(str(request_id), prompt, sampling_params, lora_request=lora_request) request_id += 1...

## 候选优化模式

- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 3: > LLMEngine: """Initialize the LLMEngine.""" model_path = "/data/quant_fp8/vicuna-13b-v1.5-fp8/" engine_args = EngineArgs(model=model_path, enable_lora=True, max_loras=16, max_lora_rank=64,
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 3: [Bug]: lora is not loaded using `num_scheduler_steps=8` bug;stale ### 🐛 Describe the bug When I run lora request using `num_scheduler_steps` > 1, even if I give a wrong lora path, it doesn't report an error, but gives w...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: ut gives wrong result. ### The bug can be reproduced by this code. ``` import os import torch from typing import List, Optional, Tuple import pandas as pd from huggingface_hub import snapshot_download from vllm import E...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: /not/exist/' test_prompts = create_test_prompts(lora_path) torch.cuda.cudart().cudaProfilerStart() process_requests(engine, test_prompts) torch.cuda.cudart().cudaProfilerStop() if __name__ == '__main__': main() ``` ###...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: torch from typing import List, Optional, Tuple import pandas as pd from huggingface_hub import snapshot_download from vllm import EngineArgs, LLMEngine, RequestOutput, SamplingParams from vllm.lora.request import LoRARe...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
