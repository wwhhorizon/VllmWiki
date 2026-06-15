# vllm-project/vllm#34996: [Feature][CI]: `test_functionalization.py` should compare outputs

| 字段 | 值 |
| --- | --- |
| Issue | [#34996](https://github.com/vllm-project/vllm/issues/34996) |
| 状态 | closed |
| 标签 | feature request |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Feature][CI]: `test_functionalization.py` should compare outputs

### Issue 正文摘录

### 🚀 The feature, motivation and pitch https://github.com/vllm-project/vllm/blob/main/tests/compile/passes/test_functionalization.py should compare the test outputs from the functionalized model and the defunctionalized model, which are expected to be identical. I tried doing this as part of #33443, but ran into issues with the RMSNorm tests e.g. `TestFusedAddRMSNorm` having significantly different output values. This is probably a good first issue, can we have it marked as such for a community contributor? cc @ProExpertProg ### Alternatives _No response_ ### Additional context _No response_ ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: [Feature][CI]: `test_functionalization.py` should compare outputs feature request ### 🚀 The feature, motivation and pitch https://github.com/vllm-project/vllm/blob/main/tests/compile/passes/test_functionalization.py sho...
- [Bitwise 确定性与数值等价](../patterns/bitwise_determinism_equivalence.md) - 分数 1: s with the RMSNorm tests e.g. `TestFusedAddRMSNorm` having significantly different output values. This is probably a good first issue, can we have it marked as such for a community contributor? cc @ProExpertProg ### Alt...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: se_ ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: tionalization.py should compare the test outputs from the functionalized model and the defunctionalized model, which are expected to be identical. I tried doing this as part of #33443, but ran into issues with the RMSNo...
- [MoE、GEMM 与 Expert Routing](../patterns/moe_gemm_routing.md) - 分数 1: ssue, can we have it marked as such for a community contributor? cc @ProExpertProg ### Alternatives _No response_ ### Additional context _No response_ ### Before submitting a new issue... - [x] Make sure you already sea...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
