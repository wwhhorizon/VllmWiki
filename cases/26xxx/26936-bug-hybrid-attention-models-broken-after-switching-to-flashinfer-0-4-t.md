# vllm-project/vllm#26936: [Bug]: Hybrid Attention models broken after switching to flashinfer 0.4 (tested on Granite 4.0 H, Qwen3-Next, Jamba-3B, Nemotron-H-8b)

| 字段 | 值 |
| --- | --- |
| Issue | [#26936](https://github.com/vllm-project/vllm/issues/26936) |
| 状态 | open |
| 标签 | bug;unstale |
| 评论 | 28; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | attention_kv_cache;ci_build;distributed_parallel;frontend_api;gemm_linear;hardware_porting;model_support;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | attention;cuda;operator;sampling;triton |
| 症状 | build_error;nan_inf |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Hybrid Attention models broken after switching to flashinfer 0.4 (tested on Granite 4.0 H, Qwen3-Next, Jamba-3B, Nemotron-H-8b)

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug (reported earlier in https://github.com/flashinfer-ai/flashinfer/issues/1931) After upgrading vllm (compiled from source) and flashinfer (to 0.4.0), I noticed that Qwen3-Next-80b has lost a lot of precision and can't use tools and talks nonsense after the 2nd conversation turn. If I switch the backend to "FLASH_ATTN", the problem goes away. This makes me think that the problem is likely in flashinfer. Trying to isolate the problem: - Switching to flash_attn backend, everything works normally. - Switching the model to Qwen3-4b, everything works normally. - Switching to an older version of vllm with flashinfer 0.3.0, everything works normally. - Unfortunately, I cannot try the latest vllm version with flashinfer 0.3.0 or the old version of vllm with flashinfer 0.4.0 because vllm is apparently locked to a given flashinfer version due to some function call parameters. I am unsure if the problem is due to some error in which vllm uses flashinfer 0.4.0 or if the error is entirely within flashinfer, which could have introduced a bug that may only cause a loss of precision in the special attention mechanism of Qwen3-Next. Note that I'm r...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 5: /github.com/flashinfer-ai/flashinfer/issues/1931) After upgrading vllm (compiled from source) and flashinfer (to 0.4.0), I noticed that Qwen3-Next-80b has lost a lot of precision and can't use tools and talks nonsense a...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 3: [Bug]: Hybrid Attention models broken after switching to flashinfer 0.4 (tested on Granite 4.0 H, Qwen3-Next, Jamba-3B, Nemotron-H-8b) bug;unstale ### Your current environment ### 🐛 Describe the bug (reported earlier in...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: that may only cause a loss of precision in the special attention mechanism of Qwen3-Next. Note that I'm running on NVIDIA sm120 GPUs, Any confirmation of the problem or suggestions appreciated. ### Before submitting a n...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: [Bug]: Hybrid Attention models broken after switching to flashinfer 0.4 (tested on Granite 4.0 H, Qwen3-Next, Jamba-3B, Nemotron-H-8b) bug;unstale ### Your current environment ### 🐛 Describe the bug (reported earlier in...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: 0.4 (tested on Granite 4.0 H, Qwen3-Next, Jamba-3B, Nemotron-H-8b) bug;unstale ### Your current environment ### 🐛 Describe the bug (reported earlier in https://github.com/flashinfer-ai/flashinfer/issues/1931) After upgr...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
