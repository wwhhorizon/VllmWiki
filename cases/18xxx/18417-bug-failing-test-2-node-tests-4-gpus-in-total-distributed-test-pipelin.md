# vllm-project/vllm#18417: [Bug][Failing Test]  2-node-tests-4-gpus-in-total - distributed/test_pipeline_parallel.py::test_tp_*

| 字段 | 值 |
| --- | --- |
| Issue | [#18417](https://github.com/vllm-project/vllm/issues/18417) |
| 状态 | closed |
| 标签 | bug;ci-failure |
| 评论 | 4; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;frontend_api;model_support;moe;sampling_logits |
| 子分类 |  |
| Operator 关键词 | cuda;kernel;moe |
| 症状 | build_error;crash;mismatch |
| 根因提示 | env_dependency |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug][Failing Test]  2-node-tests-4-gpus-in-total - distributed/test_pipeline_parallel.py::test_tp_*

### Issue 正文摘录

### Your current environment Still failing on main as of commit 9609327fa4 ### 🐛 Describe the bug Failing test: https://buildkite.com/organizations/vllm/analytics/suites/ci-1/tests?branch=main&commit=Search&period=1day&query=test_tp_language_generation ``` FAILED distributed/test_pipeline_parallel.py::test_tp_language_generation[microsoft/Phi-3.5-MoE-instruct-parallel_setup26-ray-1-auto-test_options26] ```

## 现有链接修复摘要

#18543 [Bugfix] Use random hidden states in dummy sampler run

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: s-4-gpus-in-total - distributed/test_pipeline_parallel.py::test_tp_* bug;ci-failure ### Your current environment Still failing on main as of commit 9609327fa4 ### 🐛 Describe the bug Failing test: https://buildkite.com/o...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: .com/organizations/vllm/analytics/suites/ci-1/tests?branch=main&commit=Search&period=1day&query=test_tp_language_generation ``` FAILED distributed/test_pipeline_parallel.py::test_tp_language_generation[microsoft/Phi-3.5...
- [Bitwise 确定性与数值等价](../patterns/bitwise_determinism_equivalence.md) - 分数 1: _api;model_support;moe;sampling_logits cuda;kernel;moe build_error;crash;mismatch env_dependency #18543 [Bugfix] Use random hidden states in dummy sampler run Your current environment
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: st_options26] ``` correctness ci_build;distributed_parallel;frontend_api;model_support;moe;sampling_logits cuda;kernel;moe build_error;crash;mismatch env_dependency #18543 [Bugfix] Use random hidden states in dummy samp...
- [MoE、GEMM 与 Expert Routing](../patterns/moe_gemm_routing.md) - 分数 1: test_pipeline_parallel.py::test_tp_language_generation[microsoft/Phi-3.5-MoE-instruct-parallel_setup26-ray-1-auto-test_options26] ``` correctness ci_build;distributed_parallel;frontend_api;model_support;moe;sampling_log...

## 关联 PR 证据

| PR | 链接类型 | 置信度 | PR 标题 | 证据 |
| --- | --- | ---: | --- | --- |
| [#18543](https://github.com/vllm-project/vllm/pull/18543) | closes_keyword | 0.95 | [Bugfix] Use random hidden states in dummy sampler run | FIX #18417 FIX #18418 FIX #18425 FIX #18459 FIX #18462 FIX #18466 FIX #18498 FIX #18525 |

## Wiki 抽取状态

- 后续迭代应在可用时读取完整讨论评论。
