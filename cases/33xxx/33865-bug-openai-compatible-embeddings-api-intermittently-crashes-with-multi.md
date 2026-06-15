# vllm-project/vllm#33865: [Bug]: OpenAI-compatible Embeddings API intermittently crashes with multimodal cache assertion (`Expected a cached item for mm_hash`) on Qwen3-VL-Embedding-8B

| 字段 | 值 |
| --- | --- |
| Issue | [#33865](https://github.com/vllm-project/vllm/issues/33865) |
| 状态 | open |
| 标签 | bug;unstale |
| 评论 | 6; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: OpenAI-compatible Embeddings API intermittently crashes with multimodal cache assertion (`Expected a cached item for mm_hash`) on Qwen3-VL-Embedding-8B

### Issue 正文摘录

### 🐛 Describe the bug Using vLLM `serve` with the OpenAI-compatible **Embeddings API** to run **Qwen3-VL-Embedding-8B**, the server intermittently crashes while pre-processing embedding requests. The crash is an assertion inside the multimodal feature cache: ``` AssertionError: Expected a cached item for mm_hash='...' ``` After that, the API server hits a second assertion: ``` AssertionError: assert req_state.detokenizer is not None ``` This suggests the request fails during `preprocess_add_request()` when the engine tries to retrieve multimodal features from `mm_receiver_cache`, but the cache entry for the computed `mm_hash` is missing; then the output handler processes an incomplete request state. ## Environment / deployment - API: OpenAI-compatible **Embeddings** endpoint - Deployment: cloud vendor managed model inference service (default settings; limited ability to tune internal worker settings) - Model: `Qwen3-VL-Embedding-8B` - Launch command: ```bash vllm serve /mnt/data \ --runner pooling \ --dtype bfloat16 \ --tensor-parallel-size 2 \ --max-model-len 65536 \ --trust-remote-code ``` ## Steps to reproduce This occurs intermittently under real traffic. We don’t have a 100%...

## 候选优化模式

- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 3: Launch command: ```bash vllm serve /mnt/data \ --runner pooling \ --dtype bfloat16 \ --tensor-parallel-size 2 \ --max-model-len 65536 \ --trust-remote-code ``` ## Steps to reproduce This occurs intermittently under real...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: [Bug]: OpenAI-compatible Embeddings API intermittently crashes with multimodal cache assertion (`Expected a cached item for mm_hash`) on Qwen3-VL-Embedding-8B bug;unstale ### 🐛 Describe the bug Using vLLM `serve` with t...
- [Bitwise 确定性与数值等价](../patterns/bitwise_determinism_equivalence.md) - 分数 2: ize 2 \ --max-model-len 65536 \ --trust-remote-code ``` ## Steps to reproduce This occurs intermittently under real traffic. We don’t have a 100% minimal repro yet, but it happens when sending embedding requests with mu...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: on (`Expected a cached item for mm_hash`) on Qwen3-VL-Embedding-8B bug;unstale ### 🐛 Describe the bug Using vLLM `serve` with the OpenAI-compatible **Embeddings API** to run **Qwen3-VL-Embedding-8B**, the server intermi...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: ce, the internal runtime might use multiple processes/workers or request routing patterns that could make multimodal caches non-sticky across workers. - The error strongly looks like a multimodal cache inconsistency / r...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
