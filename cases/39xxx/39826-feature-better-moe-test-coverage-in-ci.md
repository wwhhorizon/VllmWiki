# vllm-project/vllm#39826: [Feature]: Better MoE Test Coverage in CI

| 字段 | 值 |
| --- | --- |
| Issue | [#39826](https://github.com/vllm-project/vllm/issues/39826) |
| 状态 | closed |
| 标签 | feature request |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Feature]: Better MoE Test Coverage in CI

### Issue 正文摘录

### 🚀 The feature, motivation and pitch This issue requests for better MoE test coverage in CI. The current coverage has failed to catch obvious MoE functional bugs like described in https://github.com/vllm-project/vllm/pull/38989, suggesting clear missing coverage. Besides, there are many MoE backends as well as PrepareAndFinalize backends (Allreduce, A2A, etc), which may have requirements for activation or weight dtypes. The compatibility is defined in functions like `_supports_parallel_config` in MoE backend or [custom condition checks](https://github.com/vllm-project/vllm/pull/39717) (which is added after hitting issues as uncaught from test). We should ensure these combinations are exhaustively tested in the CI via unit tests, instead of seeing unhandled errors or garbage output when used. `test_modular_kernel_combinations.py` seems designed to provide such coverage. However, it has clear missing coverage, as indicated by the uncaught bugs. In addition, it uses [config.is_valid](https://github.com/vllm-project/vllm/blob/e64b39ea7114d7294db1da9766f5f9a88ef4ed25/tests/kernels/moe/modular_kernel_tools/common.py#L258) to define test coverage. Yet it may be better to check for gra...

## 候选优化模式

- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 2: [Feature]: Better MoE Test Coverage in CI feature request ### 🚀 The feature, motivation and pitch This issue requests for better MoE test coverage in CI. The current coverage has failed to catch obvious MoE functional b...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: l/38989, suggesting clear missing coverage. Besides, there are many MoE backends as well as PrepareAndFinalize backends (Allreduce, A2A, etc), which may have requirements for activation or weight dtypes. The compatibili...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: [Feature]: Better MoE Test Coverage in CI feature request ### 🚀 The feature, motivation and pitch This issue requests for better MoE test coverage in CI. The current coverage has failed to catch obvious MoE functional b...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 1: lreduce, A2A, etc), which may have requirements for activation or weight dtypes. The compatibility is defined in functions like `_supports_parallel_config` in MoE backend or [custom condition checks](https://github.com/...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: se_ ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
