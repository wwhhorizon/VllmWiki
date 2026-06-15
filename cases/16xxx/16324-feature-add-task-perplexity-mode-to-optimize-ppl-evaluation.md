# vllm-project/vllm#16324: [Feature]: Add task perplexity mode to optimize PPL evaluation

| 字段 | 值 |
| --- | --- |
| Issue | [#16324](https://github.com/vllm-project/vllm/issues/16324) |
| 状态 | closed |
| 标签 | feature request;stale |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Feature]: Add task perplexity mode to optimize PPL evaluation

### Issue 正文摘录

### 🚀 The feature, motivation and pitch When testing 2/3/4-bit quantized LLaMA 2 models (7B/13B/70B) on a single A40 GPU using `lm-evaluation-harness`, I ran into issues with `generate` mode for perplexity (PPL) tasks: 1. PPL evaluation typically uses `generate` mode with `prompt_log_probs=0` and `max_tokens=1`. 2. The current implementation reuses the response log-prob calculation for prompt log-probs. However, the number of new response tokens (≈ number of requests) is much smaller than the total number of prompt tokens. Since response log-probs are computed assuming short outputs, the code uses a memory-heavy approach that easily leads to OOM when applied to long prompts — requiring reduced `gpu_memory_utilization`. see https://github.com/vllm-project/vllm/blob/24f6b9a71397539a3d02c801963220b0e9a2aef9/vllm/model_executor/layers/sampler.py#L268-L284 3. Lowering `gpu_memory_utilization` introduces another issue: it keeps KV cache around, causing errors. (This can be mitigated by lowering `max_model_len`, but it's a workaround. However, setting `max_model_len` too low may lead to a large number of requests, which in turn could cause OOM issues.) see https://github.com/vllm-project...

## 候选优化模式

- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: owever, the number of new response tokens (≈ number of requests) is much smaller than the total number of prompt tokens. Since response log-probs are computed assuming short outputs, the code uses a memory-heavy approac...
- [KV Cache 容量、压缩与 Offload](../patterns/kv_cache_capacity_offload.md) - 分数 2: hort outputs, the code uses a memory-heavy approach that easily leads to OOM when applied to long prompts — requiring reduced `gpu_memory_utilization`. see https://github.com/vllm-project/vllm/blob/24f6b9a71397539a3d02c...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: ## 🚀 The feature, motivation and pitch When testing 2/3/4-bit quantized LLaMA 2 models (7B/13B/70B) on a single A40 GPU using `lm-evaluation-harness`, I ran into issues with `generate` mode for perplexity (PPL) tasks: 1...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: [Feature]: Add task perplexity mode to optimize PPL evaluation feature request;stale ### 🚀 The feature, motivation and pitch When testing 2/3/4-bit quantized LLaMA 2 models (7B/13B/70B) on a single A40 GPU using `lm-eva...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 2: [Feature]: Add task perplexity mode to optimize PPL evaluation feature request;stale ### 🚀 The feature, motivation and pitch When testing 2/3/4-bit quantized LLaMA 2 models (7B/13B/70B) on a single A40 GPU using `lm-eva...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
