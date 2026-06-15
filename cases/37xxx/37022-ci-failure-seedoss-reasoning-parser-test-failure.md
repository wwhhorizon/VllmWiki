# vllm-project/vllm#37022: [CI Failure]: Seedoss reasoning parser test failure

| 字段 | 值 |
| --- | --- |
| Issue | [#37022](https://github.com/vllm-project/vllm/issues/37022) |
| 状态 | open |
| 标签 | ci-failure |
| 评论 | 0; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [CI Failure]: Seedoss reasoning parser test failure

### Issue 正文摘录

### Name of failing test tests/reasoning/test_seedoss_reasoning_parser.py ### Basic information - [ ] Flaky test - [x] Can reproduce locally - [ ] Caused by external libraries (e.g. bug in `transformers`) ### 🧪 Describe the failing test ``` FAILED tests/reasoning/test_seedoss_reasoning_parser.py::test_simple_reasoning[True] - AssertionError: assert None == 'This is a reasoning section' FAILED tests/reasoning/test_seedoss_reasoning_parser.py::test_complete_reasoning[True] - AssertionError: assert None == 'This is a reasoning section' FAILED tests/reasoning/test_seedoss_reasoning_parser.py::test_no_content[True] - AssertionError: assert None == 'This is content' FAILED tests/reasoning/test_seedoss_reasoning_parser.py::test_multiple_lines[True] - AssertionError: assert None == 'This\nThat' FAILED tests/reasoning/test_seedoss_reasoning_parser.py::test_with_start_token[True] - AssertionError: Both content and reasoning content are present in the delta message FAILED tests/reasoning/test_seedoss_reasoning_parser.py::test_only_end_token[True] - AssertionError: assert None == 'Some reasoning' FAILED tests/reasoning/test_seedoss_reasoning_parser.py::test_no_tokens[True] - AssertionError: a...

## 候选优化模式

- [Bitwise 确定性与数值等价](../patterns/bitwise_determinism_equivalence.md) - 分数 1: s_reasoning_parser.py ### Basic information - [ ] Flaky test - [x] Can reproduce locally - [ ] Caused by external libraries (e.g. bug in `transformers`) ### 🧪 Describe the failing test ``` FAILED tests/reasoning/test_se...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: [CI Failure]: Seedoss reasoning parser test failure ci-failure ### Name of failing test tests/reasoning/test_seedoss_reasoning_parser.py ### Basic information - [ ] Flaky test - [x] Can reproduce locally - [ ] Caused b
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: ling test tests/reasoning/test_seedoss_reasoning_parser.py ### Basic information - [ ] Flaky test - [x] Can reproduce locally - [ ] Caused by external libraries (e.g. bug in `transformers`) ### 🧪 Describe the failing te...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: [CI Failure]: Seedoss reasoning parser test failure ci-failure ### Name of failing test tests/reasoning/test_seedoss_reasoning_parser.py ### Basic information - [ ] Flaky test - [x] Can reproduce locally - [ ] Caused by...

## Wiki 抽取状态

- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
