# vllm-project/vllm#3896: [Bug]: many warnings when building marlin kernel, right operand of "%" is zero

| 字段 | 值 |
| --- | --- |
| Issue | [#3896](https://github.com/vllm-project/vllm/issues/3896) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: many warnings when building marlin kernel, right operand of "%" is zero

### Issue 正文摘录

### Your current environment ```bash marlin_cuda_kernel.cu(455): warning #179-D: right operand of "%" is zero if (group_blocks != -1 && pipe % (group_blocks / thread_k_blocks) == 0) ``` ### 🐛 Describe the bug many warnings when building marlin kernel, right operand of "%" is zero.

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: [Bug]: many warnings when building marlin kernel, right operand of "%" is zero bug ### Your current environment ```bash marlin_cuda_kernel.cu(455): warning #179-D: right operand of "%" is zero if (group_blocks != -1 &&...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: operand of "%" is zero bug ### Your current environment ```bash marlin_cuda_kernel.cu(455): warning #179-D: right operand of "%" is zero if (group_blocks != -1 && pipe % (group_blocks / thread_k_blocks) == 0) ``` ### 🐛...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 1: .cu(455): warning #179-D: right operand of "%" is zero if (group_blocks != -1 && pipe % (group_blocks / thread_k_blocks) == 0) ``` ### 🐛 Describe the bug many warnings when building marlin kernel, right operand of "%" i...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
