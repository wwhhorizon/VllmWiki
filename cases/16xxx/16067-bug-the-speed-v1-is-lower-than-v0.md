# vllm-project/vllm#16067: [Bug]: The speed v1 is lower than v0

| 字段 | 值 |
| --- | --- |
| Issue | [#16067](https://github.com/vllm-project/vllm/issues/16067) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 4; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | frontend_api;model_support;quantization;sampling_logits |
| 子分类 | precision |
| Operator 关键词 | cuda;fp8;quantization;sampling |
| 症状 | build_error;slowdown |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: The speed v1 is lower than v0

### Issue 正文摘录

### Your current environment Model: RefalMachine/RuadaptQwen2.5-1.5B-instruct Vllm version: 0.8.2. Ubuntu 22.04. Python 3.12. Cuda/nvcc 12.8. 4070ti 16Gb VRAM command: `VLLM_USE_V1=0 vllm serve RefalMachine/RuadaptQwen2.5-1.5B-instruct --device cuda --gpu-memory-utilization 0.98 --enforce-eager --quantization fp8 --port 8002` and also without eager, quantization and with V1 Testing was done on one message at a time ```python import requests import time from pydantic import BaseModel class AnswerResponse(BaseModel): answer: str json_schema = AnswerResponse.model_json_schema() CONFIG = { "base_url": "http://localhost:8002/v1", "api_key": "token", "model_name": "RefalMachine/RuadaptQwen2.5-1.5B-instruct", "params": { "temperature": 0.6, "top_p": 0.9, "frequency_penalty": 1.1, "max_tokens": 256 } } def generate(messages, extra_body=None): speeds = [] n=5 url = f"{CONFIG['base_url']}/chat/completions" headers = { "Authorization": f"Bearer {CONFIG['api_key']}", "Content-Type": "application/json" } body = { "model": CONFIG["model_name"], "messages": messages, } body.update(CONFIG["params"]) if extra_body: body.update(extra_body) response = requests.post(url, headers=headers, json=body) f...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 5: rrent environment Model: RefalMachine/RuadaptQwen2.5-1.5B-instruct Vllm version: 0.8.2. Ubuntu 22.04. Python 3.12. Cuda/nvcc 12.8. 4070ti 16Gb VRAM command: `VLLM_USE_V1=0 vllm serve RefalMachine/RuadaptQwen2.5-1.5B-ins...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 3: B-instruct --device cuda --gpu-memory-utilization 0.98 --enforce-eager --quantization fp8 --port 8002` and also without eager, quantization and with V1 Testing was done on one message at a time ```python import requests...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: ]: The speed v1 is lower than v0 bug;stale ### Your current environment Model: RefalMachine/RuadaptQwen2.5-1.5B-instruct Vllm version: 0.8.2. Ubuntu 22.04. Python 3.12. Cuda/nvcc 12.8. 4070ti 16Gb VRAM command: `VLLM_US...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: aptQwen2.5-1.5B-instruct Vllm version: 0.8.2. Ubuntu 22.04. Python 3.12. Cuda/nvcc 12.8. 4070ti 16Gb VRAM command: `VLLM_USE_V1=0 vllm serve RefalMachine/RuadaptQwen2.5-1.5B-instruct --device cuda --gpu-memory-utilizati...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: [Bug]: The speed v1 is lower than v0 bug;stale ### Your current environment Model: RefalMachine/RuadaptQwen2.5-1.5B-instruct Vllm version: 0.8.2. Ubuntu 22.04. Python 3.12. Cuda/nvcc 12.8. 4070ti 16Gb VRAM command: `VLL...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
