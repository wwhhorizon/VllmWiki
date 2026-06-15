# vllm-project/vllm#34713: [Bug]: mkdocs --strict fails on 'device' arg in pp_handler.py docstring

| 字段 | 值 |
| --- | --- |
| Issue | [#34713](https://github.com/vllm-project/vllm/issues/34713) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: mkdocs --strict fails on 'device' arg in pp_handler.py docstring

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug Local mkdocs build & RTD docs build fails in strict mode due to a griffe warning from a docstring/signature mismatch. As a result, recent PRs that trigger RTDs are failing (so this is not specific to one feature PR). ex1. https://app.readthedocs.org/projects/vllm/builds/31441093/ in https://github.com/vllm-project/vllm/pull/32513 ex2. https://app.readthedocs.org/projects/vllm/builds/31441662/#306688356--1476 in https://github.com/vllm-project/vllm/pull/34679 and many more I can also reproduce it locally: ```text python -m mkdocs build --clean --strict ... WARNING - griffe: vllm/v1/worker/gpu/pp_handler.py:73: No type or annotation for parameter 'device' WARNING - griffe: vllm/v1/worker/gpu/pp_handler.py:73: Parameter 'device' does not appear in the function signature ... ``` ### Proposed fix Regression source appears to be #34666 (commit 04925b220), where device was removed from the function signature but left in the docstring args of vllm/v1/worker/gpu/pp_handler.py. so removing stale 'device' entry from the docstring Args section would fix this. I will submit a proposed fix soon ### Before submitting a new issue... - [x] Make s...

## 候选优化模式

- [Bitwise 确定性与数值等价](../patterns/bitwise_determinism_equivalence.md) - 分数 2: fails in strict mode due to a griffe warning from a docstring/signature mismatch. As a result, recent PRs that trigger RTDs are failing (so this is not specific to one feature PR). ex1. https://app.readthedocs.org/proje...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: ug ### Your current environment ### 🐛 Describe the bug Local mkdocs build & RTD docs build fails in strict mode due to a griffe warning from a docstring/signature mismatch. As a result, recent PRs that trigger RTDs are...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: ails in strict mode due to a griffe warning from a docstring/signature mismatch. As a result, recent PRs that trigger RTDs are failing (so this is not specific to one feature PR). ex1. https://app.readthedocs.org/projec...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 2: ice' does not appear in the function signature ... ``` ### Proposed fix Regression source appears to be #34666 (commit 04925b220), where device was removed from the function signature but left in the docstring args of v...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: t in the docstring args of vllm/v1/worker/gpu/pp_handler.py. so removing stale 'device' entry from the docstring Args section would fix this. I will submit a proposed fix soon ### Before submitting a new issue... - [x]...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
