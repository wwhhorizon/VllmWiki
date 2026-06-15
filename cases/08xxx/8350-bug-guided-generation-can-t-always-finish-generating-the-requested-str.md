# vllm-project/vllm#8350: [Bug]: guided generation can't always finish generating the requested structure

| 字段 | 值 |
| --- | --- |
| Issue | [#8350](https://github.com/vllm-project/vllm/issues/8350) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 15; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | frontend_api;model_support;sampling_logits |
| 子分类 | latency_reg |
| Operator 关键词 | cuda |
| 症状 | crash |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: guided generation can't always finish generating the requested structure

### Issue 正文摘录

So it appears that guided generation returns the requested structure like json only if the model has an infinite number of tokens it can generate, but otherwise very often it fails to close the structure, e.g. if it's a simple `{ "key": "value" }` json schema and the new tokens are limited, it'll often return `{ "key": "value`. I understand why this is happening - it's because the guiding can only guide when it has a subset of legal tokens to be used next, but if it's any token it can exhaust the full max_length and by the time it discovered it's unfinished it's too late to wrap up the structure. Here is how to reproduce this problem: ``` from vllm import LLM, SamplingParams model_name_or_path = "TinyLlama/TinyLlama-1.1B-Chat-v0.6" schema = '{ "type": "object", "properties": { "age": { "type": "integer"}, "description": { "type": "string"} }, "required": ["age", "description"] }' model = LLM( model=model_name_or_path, tokenizer=model_name_or_path, tokenizer_mode="auto", tensor_parallel_size=1, trust_remote_code=True, enforce_eager=True, dtype="bfloat16", gpu_memory_utilization=0.8, guided_decoding_backend="outlines", ) prompt = "Give an example of a person's profile that fits this...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: up the structure. Here is how to reproduce this problem: ``` from vllm import LLM, SamplingParams model_name_or_path = "TinyLlama/TinyLlama-1.1B-Chat-v0.6" schema = '{ "type": "object", "properties": { "age": { "type":...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 3: parallel_size=1, trust_remote_code=True, enforce_eager=True, dtype="bfloat16", gpu_memory_utilization=0.8, guided_decoding_backend="outlines", ) prompt = "Give an example of a person's profile that fits this JSON schema...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: guided generation returns the requested structure like json only if the model has an infinite number of tokens it can generate, but otherwise very often it fails to close the structure, e.g. if it's a simple `{ "key": "...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: n"] }' model = outlines.models.transformers(model_name_or_path, device='cuda:0') generator = outlines.generate.json(model, schema) prompt = "Give an example of a person's profile that fits this JSON schema: {schema}" fo...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: [Bug]: guided generation can't always finish generating the requested structure bug So it appears that guided generation returns the requested structure like json only if the model has an infinite number of tokens it ca...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
