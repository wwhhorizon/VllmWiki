# vllm-project/vllm#6274: [Feature]: Expose Lora lineage information from /v1/models

| 字段 | 值 |
| --- | --- |
| Issue | [#6274](https://github.com/vllm-project/vllm/issues/6274) |
| 状态 | closed |
| 标签 | feature request |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Feature]: Expose Lora lineage information from /v1/models

### Issue 正文摘录

### 🚀 The feature, motivation and pitch ``` python -m vllm.entrypoints.openai.api_server \ --model /workspace/meta-llama/Llama-2-7b-hf \ --enable-lora \ --lora-modules sql-lora=~/.cache/huggingface/hub/models--yard1--llama-2-7b-sql-lora-test/ ``` The `/v1/models` response from above setup can not expose the lineage between lora and base models. In below example, root always points to the base_model. ## Current Status 1. Base model will either use `--model` or `--served-model-name`. If user use local path, then the `id` and `root` would not be model id like OpenAI. 2. Lora model card information is from LoraRequest which doesn't have base_model at this moment. Technically, we can assume they are all adapters to base model. This may break later once the engine supports multiple models. ``` { "object": "list", "data": [ { "id": "/workspace/meta-llama/Llama-2-7b-hf", "object": "model", "created": 1715644056, "owned_by": "vllm", "root": "/workspace/meta-llama/Llama-2-7b-hf", "parent": null, "permission": [ { ..... } ] }, { "id": "sql-lora", "object": "model", "created": 1715644056, "owned_by": "vllm", "root": "/workspace/meta-llama/Llama-2-7b-hf", "parent": null, "permission": [ { .......

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 5: [Feature]: Expose Lora lineage information from /v1/models feature request ### 🚀 The feature, motivation and pitch ``` python -m vllm.entrypoints.openai.api_server \ --model /workspace/meta-llama/Llama-2-7b-hf \ --enabl...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: [Feature]: Expose Lora lineage information from /v1/models feature request ### 🚀 The feature, motivation and pitch ``` python -m vllm.entrypoints.openai.api_server \ --model /workspace/meta-llama/Llama-2-7b-hf \ --enabl...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: ache/huggingface/hub/models--yard1--llama-2-7b-sql-lora-test/snapshots/0dfa347e8877a4d4ed19ee56c140fa518470028c/", "parent": meta-llama/Llama-2-7b-hf, "permission": [ { .... } ] } ] } ``` I am drafting a PR to address t...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: les sql-lora=~/.cache/huggingface/hub/models--yard1--llama-2-7b-sql-lora-test/ ``` The `/v1/models` response from above setup can not expose the lineage between lora and base models. In below example, root always points...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
