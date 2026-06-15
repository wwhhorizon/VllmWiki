# vllm-project/vllm#35688: [CI Failure][Tool Calling]:

| 字段 | 值 |
| --- | --- |
| Issue | [#35688](https://github.com/vllm-project/vllm/issues/35688) |
| 状态 | closed |
| 标签 | ci-failure |
| 评论 | 0; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [CI Failure][Tool Calling]:

### Issue 正文摘录

### Name of failing test `entrypoints/openai/test_completion_with_function_calling.py` ### Basic information - [x] Flaky test - [ ] Can reproduce locally - [ ] Caused by external libraries (e.g. bug in `transformers`) ### 🧪 Describe the failing test ``` [2026-03-01T23:38:13Z] FAILED entrypoints/openai/test_completion_with_function_calling.py::test_no_args_tool_call[-Qwen/Qwen3-0.6B] - assert None is not None -- [2026-03-01T23:38:13Z] + where None = ChatCompletionMessage(content=None, refusal=None, role='assistant', annotations=None, audio=None, function_call=None, tool_calls=[], reasoning='\nOkay, the user asked, "What time is it now?" and I used the get_current_time function. The response came back as 2026-03-01T22:41:19.910311. Now I need to present this information clearly. Let me check if the date and time are correct. The current date and time in the response is March 1st, 2026, at 22:41. I should format the answer to show the date and time in a user-friendly way. Maybe add the time in hours and minutes. Also, make sure to mention the time zone if applicable, but since the response doesn\'t specify, I\'ll just state the current time. Alright, that should cover it.\n').content...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: [CI Failure][Tool Calling]: ci-failure ### Name of failing test `entrypoints/openai/test_completion_with_function_calling.py` ### Basic information - [x] Flaky test - [ ] Can reproduce locally - [ ] Caused by external
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: ntrypoints/openai/test_completion_with_function_calling.py` ### Basic information - [x] Flaky test - [ ] Can reproduce locally - [ ] Caused by external libraries (e.g. bug in `transformers`) ### 🧪 Describe the failing t...
- [Bitwise 确定性与数值等价](../patterns/bitwise_determinism_equivalence.md) - 分数 1: _function_calling.py` ### Basic information - [x] Flaky test - [ ] Can reproduce locally - [ ] Caused by external libraries (e.g. bug in `transformers`) ### 🧪 Describe the failing test ``` [2026-03-01T23:38:13Z] FAILED...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: date and time are correct. The current date and time in the response is March 1st, 2026, at 22:41. I should format the answer to show the date and time in a user-friendly way. Maybe add the time in hours and minutes. Al...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: [CI Failure][Tool Calling]: ci-failure ### Name of failing test `entrypoints/openai/test_completion_with_function_calling.py` ### Basic information - [x] Flaky test - [ ] Can reproduce locally - [ ] Caused by external l...

## Wiki 抽取状态

- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
