# vllm-project/vllm#30685: [Feature]: fp8 kv cache for finer-grained scaling factors (e.g., per channel).

| 字段 | 值 |
| --- | --- |
| Issue | [#30685](https://github.com/vllm-project/vllm/issues/30685) |
| 状态 | closed |
| 标签 | feature request;stale |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Feature]: fp8 kv cache for finer-grained scaling factors (e.g., per channel).

### Issue 正文摘录

### 🚀 The feature, motivation and pitch Currently, the FP8 KV cache feature (in the FlashMLA interface) only supports per-tensor (scalar) scaling factors. Are you developing support for finer-grained scaling factors (e.g., per-channel)? If so, when can we expect the FP8 KV cache with such finer-grained scaling factors to be completed? ### Alternatives _No response_ ### Additional context _No response_ ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: kv cache for finer-grained scaling factors (e.g., per channel). feature request;stale ### 🚀 The feature, motivation and pitch Currently, the FP8 KV cache feature (in the FlashMLA interface) only supports per-tensor (sca...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 1: [Feature]: fp8 kv cache for finer-grained scaling factors (e.g., per channel). feature request;stale ### 🚀 The feature, motivation and pitch Currently, the FP8 KV cache feature (in the FlashMLA interface) only supports...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: se_ ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [KV Cache 容量、压缩与 Offload](../patterns/kv_cache_capacity_offload.md) - 分数 1: [Feature]: fp8 kv cache for finer-grained scaling factors (e.g., per channel). feature request;stale ### 🚀 The feature, motivation and pitch Currently, the FP8 KV cache feature (in the FlashMLA interface) only supports...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
