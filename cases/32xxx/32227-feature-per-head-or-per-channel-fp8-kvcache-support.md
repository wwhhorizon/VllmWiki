# vllm-project/vllm#32227: [Feature]: per head or per channel fp8 kvcache support?

| 字段 | 值 |
| --- | --- |
| Issue | [#32227](https://github.com/vllm-project/vllm/issues/32227) |
| 状态 | closed |
| 标签 | feature request;stale |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Feature]: per head or per channel fp8 kvcache support?

### Issue 正文摘录

### 🚀 The feature, motivation and pitch Hello, I’d like to ask about the current FP8 KV cache quantization, which uses per-tensor scaling. I heard you’re developing finer-grained quantization schemes, such as per-channel or per-head quantization. Could you share more details on how this would be implemented? Specifically: Will the scale factors be packed together with the KV cache tensors (e.g., appended after the KV data), similar to what DeepSpeed v3.2 does? Will the RoPE (Rotary Position Embedding) components be handled separately and kept in higher precision (i.e., not quantized to FP8)? Will the 576-dimensional hidden dimension be further partitioned into smaller groups for FP8 quantization (e.g., per head or sub-head groups)? I previously tried the per-tensor quantization scheme, but the results were unsatisfactory. I then implemented a per-head quantization approach myself (treating the 576-dim vector as one group per head), but still observed accuracy degradation on the test set during long-sequence generation. Do you have any suggestions on how to mitigate this issue? ### Alternatives _No response_ ### Additional context _No response_ ### Before submitting a new issue......

## 候选优化模式

- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 3: [Feature]: per head or per channel fp8 kvcache support? feature request;stale ### 🚀 The feature, motivation and pitch Hello, I’d like to ask about the current FP8 KV cache quantization, which uses per-tensor scaling. I...
- [Bitwise 确定性与数值等价](../patterns/bitwise_determinism_equivalence.md) - 分数 2: Position Embedding) components be handled separately and kept in higher precision (i.e., not quantized to FP8)? Will the 576-dimensional hidden dimension be further partitioned into smaller groups for FP8 quantization (...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: )? Will the 576-dimensional hidden dimension be further partitioned into smaller groups for FP8 quantization (e.g., per head or sub-head groups)? I previously tried the per-tensor quantization scheme, but the results we...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: [Feature]: per head or per channel fp8 kvcache support? feature request;stale ### 🚀 The feature, motivation and pitch Hello, I’d like to ask about the current FP8 KV cache quantization, which uses per-tensor scaling. I...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 2: (treating the 576-dim vector as one group per head), but still observed accuracy degradation on the test set during long-sequence generation. Do you have any suggestions on how to mitigate this issue? ### Alternatives _...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
