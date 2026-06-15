# vllm-project/vllm#43941: [Bug]: Infinite loop in EngineCore during multimodal cache eviction after 400/500 sequence with reused image

| 字段 | 值 |
| --- | --- |
| Issue | [#43941](https://github.com/vllm-project/vllm/issues/43941) |
| 状态 | open |
| 标签 | bug |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | development |
| 工作域 | ci_build;frontend_api;hardware_porting;model_support;multimodal_vlm;sampling_logits;speculative_decoding |
| 子分类 | env_compat |
| Operator 关键词 | cuda;gemm;operator;sampling;triton |
| 症状 | build_error |
| 根因提示 | env_dependency;race_condition |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Infinite loop in EngineCore during multimodal cache eviction after 400/500 sequence with reused image

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug ## Describe the bug When serving multimodal models, a specific sequence of requests causes the `EngineCore` to enter an infinite loop during multimodal (mm) cache eviction, resulting in completely unresponsive requests. ## Steps to reproduce 1. Send a multimodal request containing an image where the total token count exceeds the model's context limit. The server correctly returns a `400 Bad Request` (context limit exceeded). 2. Send a new request containing the **exact same image** from step 1, but with a token count within the context limit. The server returns a `500 Internal Server Error`, and the logs print: `Expected a cached item for mm_hash='xxx'`. 3. Continue sending new requests with **different images**. When `EngineCore` triggers the multimodal cache eviction/reclamation process, it falls into an infinite loop, causing the service to hang and all subsequent requests to time out. ## Expected behavior - Step 2 should be processed successfully and return a valid response. - Step 3 should handle mm-cache eviction normally without deadlocks or infinite loops. ## Actual behavior - Step 2 fails with a 500 error and logs a cach...

## 候选优化模式

- [Bitwise 确定性与数值等价](../patterns/bitwise_determinism_equivalence.md) - 分数 3: he eviction, resulting in completely unresponsive requests. ## Steps to reproduce 1. Send a multimodal request containing an image where the total token count exceeds the model's context limit. The server correctly retu...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: scribe the bug ## Describe the bug When serving multimodal models, a specific sequence of requests causes the `EngineCore` to enter an infinite loop during multimodal (mm) cache eviction, resulting in completely unrespo...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: [Bug]: Infinite loop in EngineCore during multimodal cache eviction after 400/500 sequence with reused image bug ### Your current environment ### 🐛 Describe the bug ## Describe the bug When serving multimodal models, a...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 3: Describe the bug When serving multimodal models, a specific sequence of requests causes the `EngineCore` to enter an infinite loop during multimodal (mm) cache eviction, resulting in completely unresponsive requests. ##...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: n between the two multimodal caches maintained by vLLM: 1. **Dual Cache Architecture**: vLLM maintains two separate mm-caches: one in the service preprocessing stage (`BaseMultiModalProcessor`) and another in the infere...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
