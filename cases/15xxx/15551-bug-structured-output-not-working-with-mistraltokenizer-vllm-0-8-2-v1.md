# vllm-project/vllm#15551: [Bug]: Structured Output not working with MistralTokenizer (vLLM 0.8.2, V1)

| 字段 | 值 |
| --- | --- |
| Issue | [#15551](https://github.com/vllm-project/vllm/issues/15551) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 4; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | attention_kv_cache;frontend_api;model_support;scheduler_memory |
| 子分类 | throughput |
| Operator 关键词 | cache |
| 症状 | build_error;slowdown |
| 根因提示 | env_dependency |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Structured Output not working with MistralTokenizer (vLLM 0.8.2, V1)

### Issue 正文摘录

Despite https://github.com/vllm-project/vllm/pull/14625 which aims to support structured-outputs with mistral tokenizr, it doesn't seem to work with vllm 0.8.2 which includes this PR. to reproduce: ``` vllm serve mistralai/Ministral-8B-Instruct-2410 --tokenizer_mode mistral --config_format mistral --load_format mistral --max-model-len 4096 --gpu-memory-utilization 0.95 ``` (the memory limits args are just to make it run in RTX 4090) and a simplified version of the [Structured Outputs](https://docs.vllm.ai/en/latest/features/structured_outputs.html) example from vllm docs: ```python from pydantic import BaseModel from enum import Enum from openai import OpenAI class CarDescription(BaseModel): brand: str model: str car_type: str json_schema = CarDescription.model_json_schema() client = OpenAI( base_url="http://localhost:8000/v1", api_key="-", ) completion = client.chat.completions.create( model="mistralai/Ministral-8B-Instruct-2410", messages=[ { "role": "user", "content": "Generate a JSON with the brand, model and car_type of the most iconic car from the 90's", } ], extra_body={"guided_json": json_schema}, seed=42 ) print(completion.choices[0].message.content) ``` runs for very lon...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 5: emory limits args are just to make it run in RTX 4090) and a simplified version of the [Structured Outputs](https://docs.vllm.ai/en/latest/features/structured_outputs.html) example from vllm docs: ```python from pydanti...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: -utilization 0.95 ``` (the memory limits args are just to make it run in RTX 4090) and a simplified version of the [Structured Outputs](https://docs.vllm.ai/en/latest/features/structured_outputs.html) example from vllm...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: lm serve mistralai/Ministral-8B-Instruct-2410 --tokenizer_mode mistral --config_format mistral --load_format mistral --max-model-len 4096 --gpu-memory-utilization 0.95 ``` (the memory limits args are just to make it run...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 3: od od od od od od od ... ``` b.t.w maybe it's expected but first request is blocked few seconds when the server prints: ``` [2025-03-26 16:13:24] INFO tekken.py:114: Adding special tokens , ..., [2025-03-26 16:13:24] IN...
- [Bitwise 确定性与数值等价](../patterns/bitwise_determinism_equivalence.md) - 分数 2: izr, it doesn't seem to work with vllm 0.8.2 which includes this PR. to reproduce: ``` vllm serve mistralai/Ministral-8B-Instruct-2410 --tokenizer_mode mistral --config_format mistral --load_format mistral --max-model-l...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
