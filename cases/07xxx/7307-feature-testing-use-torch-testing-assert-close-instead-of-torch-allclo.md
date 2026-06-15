# vllm-project/vllm#7307: [Feature]: Testing - Use `torch.testing.assert_close` instead of `torch.allclose` as a Recommended Practice

| 字段 | 值 |
| --- | --- |
| Issue | [#7307](https://github.com/vllm-project/vllm/issues/7307) |
| 状态 | closed |
| 标签 | good first issue;feature request |
| 评论 | 0; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Feature]: Testing - Use `torch.testing.assert_close` instead of `torch.allclose` as a Recommended Practice

### Issue 正文摘录

### 🚀 The feature, motivation and pitch See https://pytorch.org/docs/stable/testing.html `assert_close` will print the values which violate the allclose condition. `assert torch.allclose` will not This leads to better diagnosability of failed tests

## 候选优化模式

- [Bitwise 确定性与数值等价](../patterns/bitwise_determinism_equivalence.md) - 分数 3: [Feature]: Testing - Use `torch.testing.assert_close` instead of `torch.allclose` as a Recommended Practice good first issue;feature request ### 🚀 The feature, motivation and pitch See https://pytorch.org/docs/stable/te...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: d of `torch.allclose` as a Recommended Practice good first issue;feature request ### 🚀 The feature, motivation and pitch See https://pytorch.org/docs/stable/testing.html `assert_close` will print the values which violat...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: [Feature]: Testing - Use `torch.testing.assert_close` instead of `torch.allclose` as a Recommended Practice good first issue;feature request ### 🚀 The feature, motivation and pitch See https://pytorch.org/docs/stable/te...

## Wiki 抽取状态

- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
