# vllm-project/vllm#18166: [HELP WANTED] Fix Failing Spec Decoding Test

| 字段 | 值 |
| --- | --- |
| Issue | [#18166](https://github.com/vllm-project/vllm/issues/18166) |
| 状态 | closed |
| 标签 | bug;good first issue |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [HELP WANTED] Fix Failing Spec Decoding Test

### Issue 正文摘录

### Issue We are seeing a test failure related to EAGLE on V0. We would appreciate anyone who can help addressing it. ```bash pytest -s -v tests/spec_decode/e2e/test_eagle_correctness.py::test_eagle_e2e_greedy_correctness_with_preemption ``` PR which disables the test: https://github.com/vllm-project/vllm/pull/18165 If anyone has capacity to help out with re-enabling this, we would greatly appreciate it!

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: ssue We are seeing a test failure related to EAGLE on V0. We would appreciate anyone who can help addressing it. ```bash pytest -s -v tests/spec_decode/e2e/test_eagle_correctness.py::test_eagle_e2e_greedy_correctness_wi...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: ate anyone who can help addressing it. ```bash pytest -s -v tests/spec_decode/e2e/test_eagle_correctness.py::test_eagle_e2e_greedy_correctness_with_preemption ``` PR which disables the test: https://github.com/vllm-proj...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: [HELP WANTED] Fix Failing Spec Decoding Test bug;good first issue ### Issue We are seeing a test failure related to EAGLE on V0. We would appreciate anyone who can help addressing it. ```bash pytest -s -v tests/spec_dec...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
