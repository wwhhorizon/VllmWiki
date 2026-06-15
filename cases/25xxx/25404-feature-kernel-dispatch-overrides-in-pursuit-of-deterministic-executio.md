# vllm-project/vllm#25404: [Feature]: Kernel Dispatch Overrides (in pursuit of deterministic execution)

| 字段 | 值 |
| --- | --- |
| Issue | [#25404](https://github.com/vllm-project/vllm/issues/25404) |
| 状态 | closed |
| 标签 | feature request |
| 评论 | 9; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Feature]: Kernel Dispatch Overrides (in pursuit of deterministic execution)

### Issue 正文摘录

### 🚀 The feature, motivation and pitch I am working towards high-fidelity (+ bit-wise) numerical stability and would like overrides to be possible and easy to configure. For reference, please see the proof of concept from Horace here: #24583 and associated blog post: https://thinkingmachines.ai/blog/defeating-nondeterminism-in-llm-inference/ ## Per-kernel Overrides The proposal here is to ease the vLLM framework in that direction by exposing low-level overrides for kernel dispatching. Rather than a global "deterministic" override, these would be *per* kernel and ultimately live in configuration files that enumerate all overrides needed for a given service. For example, https://github.com/vllm-project/vllm/blob/main/csrc/layernorm_kernels.cu#L416 ```diff + auto deterministic = parse_env(KERN_OVERRIDE_FUSED_ADD_RMS_NORM_DETERMINISTIC) - if (ptrs_are_aligned && offsets_are_multiple_of_vector_width) { + if (ptrs_are_aligned && offsets_are_multiple_of_vector_width && !deterministic) { LAUNCH_FUSED_ADD_RMS_NORM(8); } else { LAUNCH_FUSED_ADD_RMS_NORM(0); } ``` By exposing configurable overrides (with a single layer of indirection in the form of configuration files), we allow users to ex...

## 候选优化模式

- [Bitwise 确定性与数值等价](../patterns/bitwise_determinism_equivalence.md) - 分数 4: [Feature]: Kernel Dispatch Overrides (in pursuit of deterministic execution) feature request ### 🚀 The feature, motivation and pitch I am working towards high-fidelity (+ bit-wise) numerical stability and would like ove...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: erence, please see the proof of concept from Horace here: #24583 and associated blog post: https://thinkingmachines.ai/blog/defeating-nondeterminism-in-llm-inference/ ## Per-kernel Overrides The proposal here is to ease...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 2: [Feature]: Kernel Dispatch Overrides (in pursuit of deterministic execution) feature request ### 🚀 The feature, motivation and pitch I am working towards high-fidelity (+ bit-wise) numerical stability and would like ove...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: ciated blog post: https://thinkingmachines.ai/blog/defeating-nondeterminism-in-llm-inference/ ## Per-kernel Overrides The proposal here is to ease the vLLM framework in that direction by exposing low-level overrides for...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 2: [Feature]: Kernel Dispatch Overrides (in pursuit of deterministic execution) feature request ### 🚀 The feature, motivation and pitch I am working towards high-fidelity (+ bit-wise) numerical stability and would like ove...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
