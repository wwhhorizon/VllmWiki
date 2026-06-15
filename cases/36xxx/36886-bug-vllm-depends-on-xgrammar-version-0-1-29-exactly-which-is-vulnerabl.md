# vllm-project/vllm#36886: [Bug]: `vllm` depends on `xgrammar` version `0.1.29` exactly which is vulnerable to CVE-2026-25048

| 字段 | 值 |
| --- | --- |
| Issue | [#36886](https://github.com/vllm-project/vllm/issues/36886) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: `vllm` depends on `xgrammar` version `0.1.29` exactly which is vulnerable to CVE-2026-25048

### Issue 正文摘录

### Your current environment https://github.com/vllm-project/vllm/blob/7f1f36bf91860aed64aea58e61b23c01cf85d551/requirements/common.txt#L27 https://github.com/advisories/GHSA-7rgv-gqhr-fxg3 ### 🐛 Describe the bug https://github.com/advisories/GHSA-7rgv-gqhr-fxg3 The required xgrammar version has a high vulnerability ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: [Bug]: `vllm` depends on `xgrammar` version `0.1.29` exactly which is vulnerable to CVE-2026-25048 bug ### Your current environment https://github.com/vllm-project/vllm/blob/7f1f36bf91860aed64aea58e61b23c01cf85d551/requ...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: ity ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
