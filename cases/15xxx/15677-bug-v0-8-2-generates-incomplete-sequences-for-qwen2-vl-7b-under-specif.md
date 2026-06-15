# vllm-project/vllm#15677: [Bug]: v0.8.2 generates incomplete sequences for Qwen2-VL-7B under specific concurrency range

| 字段 | 值 |
| --- | --- |
| Issue | [#15677](https://github.com/vllm-project/vllm/issues/15677) |
| 状态 | closed |
| 标签 | bug;unstale |
| 评论 | 10; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | development |
| 工作域 | ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;speculative_decoding |
| 子分类 | env_compat |
| Operator 关键词 | cuda;operator;triton |
| 症状 | build_error |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: v0.8.2 generates incomplete sequences for Qwen2-VL-7B under specific concurrency range

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug - Model: Vanilla Qwen2-VL-7B-Instruct (Although the "model" field in the response below says "qwen-7b-vl", we verified that the model being used was the HuggingFace Hub version of Qwen2-VL-7B-Instruct.) - GPU: L20 & A800 # Bug Details We constructed a load testing request set with the same prompt but around 100 different images and observed that during load testing with a range of virtual users (vu) between 24 and 44 on L20 GPU, vLLM generated incomplete sequences because eos was emitted prematurely: ``` data: {"id":"chatcmpl-f5f2b9844bdd45cfad93428ece35e3a1","object":"chat.completion.chunk","created":1743141408,"model":"qwen-7b-vl/","choices":[{"index":0,"delta":{"role":"assistant","content":""},"logprobs":null,"finish_reason":null}]} data: {"id":"chatcmpl-f5f2b9844bdd45cfad93428ece35e3a1","object":"chat.completion.chunk","created":1743141408,"model":"qwen-7b-vl/","choices":[{"index":0,"delta":{"content":"This"},"logprobs":null,"finish_reason":null}]} data: {"id":"chatcmpl-f5f2b9844bdd45cfad93428ece35e3a1","object":"chat.completion.chunk","created":1743141408,"model":"qwen-7b-vl/","choices":[{"index":0,"delta":{"content":" image...

## 现有链接修复摘要

#16229 [Bugfix] Merge MM embeddings by index instead of token IDs

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: [Bug]: v0.8.2 generates incomplete sequences for Qwen2-VL-7B under specific concurrency range bug;unstale ### Your current environment ### 🐛 Describe the bug - Model: Vanilla Qwen2-VL-7B-Instruct (Although the "model" f...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: [Bug]: v0.8.2 generates incomplete sequences for Qwen2-VL-7B under specific concurrency range bug;unstale ### Your current environment ### 🐛 Describe the bug - Model: Vanilla Qwen2-VL-7B-Instruct (Although the "model" f...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 3: omplete sequences for Qwen2-VL-7B under specific concurrency range bug;unstale ### Your current environment ### 🐛 Describe the bug - Model: Vanilla Qwen2-VL-7B-Instruct (Although the "model" field in the response below...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 2: tion_tokens":223}} data: {"id":"chatcmpl-207fd97c-955d-47ac-8a44-aef73443fa3f","object":"chat.completion.chunk","created":1743149489,"model":"qwen-7b-vl/","choices":[],"usage":{"prompt_tokens":1058,"total_tokens":1312,"...
- [Bitwise 确定性与数值等价](../patterns/bitwise_determinism_equivalence.md) - 分数 2: s/files/19499858/response-20-vu.txt) # Troubleshooting We were able to reproduce the same issue on vLLM v0.8.0 + A800 GPU, but not on v0.8.2 + A800. The concurrency range that caused the issues is also different with a...

## 关联 PR 证据

| PR | 链接类型 | 置信度 | PR 标题 | 证据 |
| --- | --- | ---: | --- | --- |
| [#16229](https://github.com/vllm-project/vllm/pull/16229) | closes_keyword | 0.95 | [Bugfix] Merge MM embeddings by index instead of token IDs | FIX #15677 FIX #15764 FIX #23891 FIX #23954 FIX #24456 ## Breaking change for model developers This PR has updated `SupportsMultiModal.get_input_embeddings` to support passing `i |

## Wiki 抽取状态

- 后续迭代应在可用时读取完整讨论评论。
