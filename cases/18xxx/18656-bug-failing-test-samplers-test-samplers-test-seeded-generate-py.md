# vllm-project/vllm#18656: [Bug][Failing Test]: Samplers Test - samplers/test_seeded_generate.py

| 字段 | 值 |
| --- | --- |
| Issue | [#18656](https://github.com/vllm-project/vllm/issues/18656) |
| 状态 | closed |
| 标签 | bug;ci-failure |
| 评论 | 0; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug][Failing Test]: Samplers Test - samplers/test_seeded_generate.py

### Issue 正文摘录

### Your current environment N/A ### 🐛 Describe the bug `samplers/test_seeded_generate.py::test_random_sample_with_seed` has been failing on main since #17731 https://buildkite.com/organizations/vllm/analytics/suites/ci-1/tests/7615b2b4-ca19-80d3-ab9c-5b2395cd950a?period=7days&tags=scm.branch%3Amain cc @shadeMe @mgoin @aarnphm ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: Bug][Failing Test]: Samplers Test - samplers/test_seeded_generate.py bug;ci-failure ### Your current environment N/A ### 🐛 Describe the bug `samplers/test_seeded_generate.py::test_random_sample_with_seed` has been faili...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: hm ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), whi...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: [Bug][Failing Test]: Samplers Test - samplers/test_seeded_generate.py bug;ci-failure ### Your current environment N/A ### 🐛 Describe the bug `samplers/test_seeded_generate.py::test_random_sample_with_seed` has been fail...

## Wiki 抽取状态

- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
