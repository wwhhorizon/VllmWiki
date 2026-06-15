# vllm-project/vllm#23865: [Bug]: CI not running all tests/compile tests

| 字段 | 值 |
| --- | --- |
| Issue | [#23865](https://github.com/vllm-project/vllm/issues/23865) |
| 状态 | closed |
| 标签 | bug;torch.compile;stale |
| 评论 | 6; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: CI not running all tests/compile tests

### Issue 正文摘录

### Your current environment n/a ### 🐛 Describe the bug Examples of things that are not tested: - tests/compile/test_config.py - tests/compile/test_functionalization.py A partial list of things that are tested: - https://github.com/vllm-project/vllm/blob/497e763a0b7c99e6359c266d6442b58013b86b67/.buildkite/test-pipeline.yaml#L324-L331 As mentioned in https://github.com/vllm-project/vllm/pull/22682, we should really just update the test command to `pytest tests/compile`, with some opt-outs for some tests that actually need special configurations. This will make this one test take longer but will make things a lot saner for us to maintain. ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: [Bug]: CI not running all tests/compile tests bug;torch.compile;stale ### Your current environment n/a ### 🐛 Describe the bug Examples of things that are not tested: - tests/compile/test_config.py - tests/compile/test_f...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: in. ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: be the bug Examples of things that are not tested: - tests/compile/test_config.py - tests/compile/test_functionalization.py A partial list of things that are tested: - https://github.com/vllm-project/vllm/blob/497e763a0...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: [Bug]: CI not running all tests/compile tests bug;torch.compile;stale ### Your current environment n/a ### 🐛 Describe the bug Examples of things that are not tested: - tests/compile/test_config.py - tests/compile/test_f...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: [Bug]: CI not running all tests/compile tests bug;torch.compile;stale ### Your current environment n/a ### 🐛 Describe the bug Examples of things that are not tested: - tests/compile/test_config.py - tests/compile/test_f...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
