# vllm-project/vllm#18418: [Bug][Failing Test] entrypoints-test - test_v1_v2_api_consistency_single_prompt_tokens

| 字段 | 值 |
| --- | --- |
| Issue | [#18418](https://github.com/vllm-project/vllm/issues/18418) |
| 状态 | closed |
| 标签 | bug;ci-failure |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | attention_kv_cache;ci_build;distributed_parallel;frontend_api;model_support;sampling_logits;scheduler_memory |
| 子分类 |  |
| Operator 关键词 | cuda;kernel;operator;sampling |
| 症状 | build_error;crash;mismatch |
| 根因提示 | env_dependency |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug][Failing Test] entrypoints-test - test_v1_v2_api_consistency_single_prompt_tokens

### Issue 正文摘录

### Your current environment Still failing on main as of commit bca55b556f ### 🐛 Describe the bug Failing tests: https://buildkite.com/organizations/vllm/analytics/suites/ci-1/tests?branch=main&period=2days&query=test_v1_v2_api_consistency_single_prompt_tokens&commit=Search ``` FAILED entrypoints/llm/test_generate.py::test_v1_v2_api_consistency_single_prompt_tokens[prompt_token_ids0] - vllm.v1.engine.exceptions.EngineDeadError: EngineCore encountered an issue. See stack trace (above) for the root cause. FAILED entrypoints/llm/test_generate.py::test_v1_v2_api_consistency_single_prompt_tokens[prompt_token_ids1] - vllm.v1.engine.exceptions.EngineDeadError: EngineCore encountered an issue. See stack trace (above) for the root cause. FAILED entrypoints/llm/test_generate.py::test_v1_v2_api_consistency_single_prompt_tokens[prompt_token_ids2] - vllm.v1.engine.exceptions.EngineDeadError: EngineCore encountered an issue. See stack trace (above) for the root cause. FAILED entrypoints/llm/test_generate.py::test_v1_v2_api_consistency_single_prompt_tokens[prompt_token_ids3] - vllm.v1.engine.exceptions.EngineDeadError: EngineCore encountered an issue. See stack trace (above) for the root cause....

## 现有链接修复摘要

#18543 [Bugfix] Use random hidden states in dummy sampler run

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: ] entrypoints-test - test_v1_v2_api_consistency_single_prompt_tokens bug;ci-failure ### Your current environment Still failing on main as of commit bca55b556f ### 🐛 Describe the bug Failing tests: https://buildkite.com/...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: iod=2days&query=test_v1_v2_api_consistency_single_prompt_tokens&commit=Search ``` FAILED entrypoints/llm/test_generate.py::test_v1_v2_api_consistency_single_prompt_tokens[prompt_token_ids0] - vllm.v1.engine.exceptions.E...
- [Bitwise 确定性与数值等价](../patterns/bitwise_determinism_equivalence.md) - 分数 1: _logits;scheduler_memory cuda;kernel;operator;sampling build_error;crash;mismatch env_dependency #18543 [Bugfix] Use random hidden states in dummy sampler run Your current environment
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: orrectness attention_kv_cache;ci_build;distributed_parallel;frontend_api;model_support;sampling_logits;scheduler_memory cuda;kernel;operator;sampling build_error;crash;mismatch env_dependency #18543 [Bugfix] Use random...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: ci_build;distributed_parallel;frontend_api;model_support;sampling_logits;scheduler_memory cuda;kernel;operator;sampling build_error;crash;mismatch env_dependency #18543 [Bugfix] Use random hidden states in dummy sampler...

## 关联 PR 证据

| PR | 链接类型 | 置信度 | PR 标题 | 证据 |
| --- | --- | ---: | --- | --- |
| [#18543](https://github.com/vllm-project/vllm/pull/18543) | closes_keyword | 0.95 | [Bugfix] Use random hidden states in dummy sampler run | FIX #18418 FIX #18425 FIX #18459 FIX #18462 FIX #18466 FIX #18498 FIX #18525 |

## Wiki 抽取状态

- 后续迭代应在可用时读取完整讨论评论。
