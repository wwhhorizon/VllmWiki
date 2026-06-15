# vllm-project/vllm#7322: [Feature]: DeepSeek-Coder-V2-Instruct-FP8 on 8xA100

| 字段 | 值 |
| --- | --- |
| Issue | [#7322](https://github.com/vllm-project/vllm/issues/7322) |
| 状态 | closed |
| 标签 | feature request |
| 评论 | 8; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Feature]: DeepSeek-Coder-V2-Instruct-FP8 on 8xA100

### Issue 正文摘录

### 🚀 The feature, motivation and pitch VLLM has announced support for running llama3.1-405b-fp8 on 8xA100. This is the [blog](https://blog.vllm.ai/2024/07/23/llama31.html) Does vllm support running DeepSeek-Coder-V2-Instruct-FP8 on 8xA100? However, I notice that vLLM uses Triton for its FusedMoE kernel, which doesn't support the FP8 Marlin mixed-precision. See https://github.com/sgl-project/sglang/issues/989#issuecomment-2275698772 Is there any work around? ### Alternatives _No response_ ### Additional context _No response_

## 候选优化模式

- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: pSeek-Coder-V2-Instruct-FP8 on 8xA100? However, I notice that vLLM uses Triton for its FusedMoE kernel, which doesn't support the FP8 Marlin mixed-precision. See https://github.com/sgl-project/sglang/issues/989#issuecom...
- [Bitwise 确定性与数值等价](../patterns/bitwise_determinism_equivalence.md) - 分数 1: iton for its FusedMoE kernel, which doesn't support the FP8 Marlin mixed-precision. See https://github.com/sgl-project/sglang/issues/989#issuecomment-2275698772 Is there any work around? ### Alternatives _No response_ #...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: n for its FusedMoE kernel, which doesn't support the FP8 Marlin mixed-precision. See https://github.com/sgl-project/sglang/issues/989#issuecomment-2275698772 Is there any work around? ### Alternatives _No response_ ###...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 1: [Feature]: DeepSeek-Coder-V2-Instruct-FP8 on 8xA100 feature request ### 🚀 The feature, motivation and pitch VLLM has announced support for running llama3.1-405b-fp8 on 8xA100. This is the [blog](https://blog.vllm.ai/202...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: [Feature]: DeepSeek-Coder-V2-Instruct-FP8 on 8xA100 feature request ### 🚀 The feature, motivation and pitch VLLM has announced support for running llama3.1-405b-fp8 on 8xA100. This is the [blog](https://blog.vllm.ai/202...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
