# vllm-project/vllm#23322: [Usage]: Optimization of CUDA Graph Memory Usage during Sampling Prewarming in kvcache

| 字段 | 值 |
| --- | --- |
| Issue | [#23322](https://github.com/vllm-project/vllm/issues/23322) |
| 状态 | closed |
| 标签 | usage;stale |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | attention_kv_cache;model_support;sampling_logits;scheduler_memory |
| 子分类 | memory |
| Operator 关键词 | cuda;sampling |
| 症状 | oom |
| 根因提示 |  |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Usage]: Optimization of CUDA Graph Memory Usage during Sampling Prewarming in kvcache

### Issue 正文摘录

### Your current environment I noticed that when the kvcache is allocated and CUDA graph is enabled, it occupies significant GPU memory during both forward propagation and sampling. However, in gpuworker.py, the function compile_or_warm_up pre-warms the sampler, and it would be beneficial to leverage the OOM (Out Of Memory) error handling to avoid unexpected runtime OOM issues. Currently, there seems to be a check for whether the CUDA graph occupies memory space, but I suggest modifying the _dummy_run input of the sampler during the pre-warm stage to be max-num-batched-tokens. This change would allow us to verify all scenarios, especially since there are instances where the memory usage during forward propagation exceeds that of concurrent sampling. By implementing this adjustment, we can ensure better memory management and avoid OOM errors during runtime. Thank you for considering this improvement! ### How would you like to use vllm I want to run inference of a [specific model](put link here). I don't know how to integrate it with vllm. ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right c...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: forward propagation and sampling. However, in gpuworker.py, the function compile_or_warm_up pre-warms the sampler, and it would be beneficial to leverage the OOM (Out Of Memory) error handling to avoid unexpected runtim...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: [Usage]: Optimization of CUDA Graph Memory Usage during Sampling Prewarming in kvcache usage;stale ### Your current environment I noticed that when the kvcache is allocated and CUDA graph is enabled, it occupies signifi...
- [KV Cache 容量、压缩与 Offload](../patterns/kv_cache_capacity_offload.md) - 分数 2: kvcache is allocated and CUDA graph is enabled, it occupies significant GPU memory during both forward propagation and sampling. However, in gpuworker.py, the function compile_or_warm_up pre-warms the sampler, and it wo...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: n of CUDA Graph Memory Usage during Sampling Prewarming in kvcache usage;stale ### Your current environment I noticed that when the kvcache is allocated and CUDA graph is enabled, it occupies significant GPU memory duri...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: # How would you like to use vllm I want to run inference of a [specific model](put link here). I don't know how to integrate it with vllm. ### Before submitting a new issue... - [x] Make sure you already searched for re...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
