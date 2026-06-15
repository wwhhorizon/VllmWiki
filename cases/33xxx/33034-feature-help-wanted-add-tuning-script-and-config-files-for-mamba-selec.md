# vllm-project/vllm#33034: [Feature][Help Wanted]: Add tuning script and config files for Mamba selective_state_update kernel

| 字段 | 值 |
| --- | --- |
| Issue | [#33034](https://github.com/vllm-project/vllm/issues/33034) |
| 状态 | closed |
| 标签 | help wanted;good first issue;feature request |
| 评论 | 11; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Feature][Help Wanted]: Add tuning script and config files for Mamba selective_state_update kernel

### Issue 正文摘录

### 🚀 The feature, motivation and pitch # Background This PR introduces an optimization for `selective_state_update` on Blackwell: https://github.com/vllm-project/vllm/pull/32873 This optimization is GPU specific and hard coded in the code. # Fused MoE tuning Fused MoE offers a more generic tuning mechanism: Configuration files for fused MoE can be generated using the script `benchmarks/kernels/benchmark_moe.py` The `benchmark_moe.py` script generates JSON files like the following: `vllm/model_executor/layers/fused_moe/configs/E=128,N=1024,device_name=NVIDIA_H200.json` vLLM can auto-detect the file and use the relevant config for optimal performance. # Requirements The same capability should be added for `selective_state_update`: * Support for JSON config (instead of hard coded values in the code). * A new benchmark script (similar to `benchmark_moe.py`) that can generate the JSON files. ### Alternatives _No response_ ### Additional context Related PRs (not merged): https://github.com/vllm-project/vllm/pull/22728 ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentati...

## 候选优化模式

- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 4: round This PR introduces an optimization for `selective_state_update` on Blackwell: https://github.com/vllm-project/vllm/pull/32873 This optimization is GPU specific and hard coded in the code. # Fused MoE tuning Fused...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: [Feature][Help Wanted]: Add tuning script and config files for Mamba selective_state_update kernel help wanted;good first issue;feature request ### 🚀 The feature, motivation and pitch # Background This PR introduces an...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 2: sm: Configuration files for fused MoE can be generated using the script `benchmarks/kernels/benchmark_moe.py` The `benchmark_moe.py` script generates JSON files like the following: `vllm/model_executor/layers/fused_moe/...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: s://github.com/vllm-project/vllm/pull/32873 This optimization is GPU specific and hard coded in the code. # Fused MoE tuning Fused MoE offers a more generic tuning mechanism: Configuration files for fused MoE can be gen...
- [MoE、GEMM 与 Expert Routing](../patterns/moe_gemm_routing.md) - 分数 1: This optimization is GPU specific and hard coded in the code. # Fused MoE tuning Fused MoE offers a more generic tuning mechanism: Configuration files for fused MoE can be generated using the script `benchmarks/kernels/...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
