# vllm-project/vllm#43549: [Doc]: Mention Ascend NPU in the main quickstart

| 字段 | 值 |
| --- | --- |
| Issue | [#43549](https://github.com/vllm-project/vllm/issues/43549) |
| 状态 | closed |
| 标签 |  |
| 评论 | 0; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Doc]: Mention Ascend NPU in the main quickstart

### Issue 正文摘录

## Problem The main vLLM quickstart currently lists installation paths for NVIDIA CUDA, AMD ROCm, and Google TPU, but it does not mention Ascend NPU / vLLM Ascend. For users who have Ascend NPUs, or users who arrive at the main vLLM quickstart while looking for non-CUDA accelerator instructions, this makes the supported path harder to discover. The Ascend project already has a dedicated quick start at: https://docs.vllm.ai/projects/ascend/en/latest/quick_start.html ## Suggested improvement Add an "Ascend NPU" installation tab or note to `docs/getting_started/quickstart.md`, similar to the existing Google TPU entry, that points users to the vLLM Ascend quick start. The main quickstart should probably avoid duplicating the full Ascend setup because the Ascend instructions depend on NPU hardware, driver/CANN versions, and container images. A short pointer would be enough to make the supported path discoverable. ## Proposed validation This is a documentation-only change. Validation can include: - `git diff --check` - documentation formatting / link validation if available ## References - Main quickstart: https://github.com/vllm-project/vllm/blob/main/docs/getting_started/quickstart.md...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: the main quickstart ## Problem The main vLLM quickstart currently lists installation paths for NVIDIA CUDA, AMD ROCm, and Google TPU, but it does not mention Ascend NPU / vLLM Ascend. For users who have Ascend NPUs, or...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: The main vLLM quickstart currently lists installation paths for NVIDIA CUDA, AMD ROCm, and Google TPU, but it does not mention Ascend NPU / vLLM Ascend. For users who have Ascend NPUs, or users who arrive at the main vL...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: ly change. Validation can include: - `git diff --check` - documentation formatting / link validation if available ## References - Main quickstart: https://github.com/vllm-project/vllm/blob/main/docs/getting_started/quic...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: s a dedicated quick start at: https://docs.vllm.ai/projects/ascend/en/latest/quick_start.html ## Suggested improvement Add an "Ascend NPU" installation tab or note to `docs/getting_started/quickstart.md`, similar to the...

## Wiki 抽取状态

- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
