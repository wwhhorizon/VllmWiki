# vllm-project/vllm#15855: [Bug]: CI flake - v1/engine/test_llm_engine.py::test_parallel_sampling[True]

| 字段 | 值 |
| --- | --- |
| Issue | [#15855](https://github.com/vllm-project/vllm/issues/15855) |
| 状态 | closed |
| 标签 | bug;ci/build;stale;v1 |
| 评论 | 5; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: CI flake - v1/engine/test_llm_engine.py::test_parallel_sampling[True]

### Issue 正文摘录

### Your current environment ... ### 🐛 Describe the bug Saw V1 test failing with this yesterday, went away with recheck: ``` [2025-03-31T17:33:47Z] _________________________ test_parallel_sampling[True] _________________________ [2025-03-31T17:33:47Z] [2025-03-31T17:33:47Z] vllm_model = [2025-03-31T17:33:47Z] example_prompts = ['vLLM is a high-throughput and memory-efficient inference and serving engine for LLMs.\n', 'Briefly describe the majo...me.\n', 'Analyze the impact of the COVID-19 pandemic on global economic structures and future business models.\n', ...] [2025-03-31T17:33:47Z] [2025-03-31T17:33:47Z] def test_parallel_sampling(vllm_model, example_prompts) -> None: [2025-03-31T17:33:47Z] """Test passes if parallel sampling `n>1` yields `n` unique completions. [2025-03-31T17:33:47Z] [2025-03-31T17:33:47Z] Args: [2025-03-31T17:33:47Z] vllm_model: VllmRunner instance under test. [2025-03-31T17:33:47Z] example_prompt: test fixture providing prompts for testing. [2025-03-31T17:33:47Z] """ [2025-03-31T17:33:47Z] sampling_params_list, n_list = _get_test_sampling_params(example_prompts) [2025-03-31T17:33:47Z] model: LLM = vllm_model.model [2025-03-31T17:33:47Z] outputs = model.gene...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: [Bug]: CI flake - v1/engine/test_llm_engine.py::test_parallel_sampling[True] bug;ci/build;stale;v1 ### Your current environment ... ### 🐛 Describe the bug Saw V1 test failing with this yesterday, went away with recheck:...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: v1/engine/test_llm_engine.py::test_parallel_sampling[True] bug;ci/build;stale;v1 ### Your current environment ... ### 🐛 Describe the bug Saw V1 test failing with this yesterday, went away with recheck: ``` [2025-03-31T1...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 2: [Bug]: CI flake - v1/engine/test_llm_engine.py::test_parallel_sampling[True] bug;ci/build;stale;v1 ### Your current environment ... ### 🐛 Describe the bug Saw V1 test failing with this yesterday, went away with recheck:...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: ``` ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: _____________________ [2025-03-31T17:33:47Z] [2025-03-31T17:33:47Z] vllm_model = [2025-03-31T17:33:47Z] example_prompts = ['vLLM is a high-throughput and memory-efficient inference and serving engine for LLMs.\n', 'Brie...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
