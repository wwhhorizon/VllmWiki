# vllm-project/vllm#1511: Switch the linter and formatter to `ruff`

| 字段 | 值 |
| --- | --- |
| Issue | [#1511](https://github.com/vllm-project/vllm/issues/1511) |
| 状态 | closed |
| 标签 |  |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> Switch the linter and formatter to `ruff`

### Issue 正文摘录

This issue proposes switching the linter (pylint) and formatter (yapf) to ruff https://github.com/astral-sh/ruff. The benefit of `ruff` are speed and wide adoption. `ruff` is 100x faster than both of them. `ruff` is used by almost every modern Python packages. This means contributors are more likely to use ruff than pylint + yapf combo. The further downside of `yapf` includes the limited 80 characters formatting and non-deterministic formatting. Once the formatting PR gets merged, I will send the a message, including scripts and patch to help rebasing on-going PRs.

## 候选优化模式

- [Bitwise 确定性与数值等价](../patterns/bitwise_determinism_equivalence.md) - 分数 2: her downside of `yapf` includes the limited 80 characters formatting and non-deterministic formatting. Once the formatting PR gets merged, I will send the a message, including scripts and patch to help rebasing on-going...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: Switch the linter and formatter to `ruff` This issue proposes switching the linter (pylint) and formatter (yapf) to ruff https://github.com/astral-sh/ruff. The benefit of `ruff` are speed and wide adoption. `ruff` is 10...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: downside of `yapf` includes the limited 80 characters formatting and non-deterministic formatting. Once the formatting PR gets merged, I will send the a message, including scripts and patch to help rebasing on-going PRs.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
