# vllm-project/vllm#34701: [CI Failure]: Entrypoints Integration (Responses API)

| 字段 | 值 |
| --- | --- |
| Issue | [#34701](https://github.com/vllm-project/vllm/issues/34701) |
| 状态 | closed |
| 标签 | ci-failure |
| 评论 | 0; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [CI Failure]: Entrypoints Integration (Responses API)

### Issue 正文摘录

### Name of failing test `entrypoints/openai/responses/test_parsable_context.py::test_mcp_tool_call[Qwen/Qwen3-8B] - AssertionError: assert 'mcp_call' == 'message'` ### Basic information - [x] Flaky test - [ ] Can reproduce locally - [ ] Caused by external libraries (e.g. bug in `transformers`) ### 🧪 Describe the failing test ``` [2026-02-17T07:27:11Z] =================================== FAILURES =================================== -- [2026-02-17T07:27:11Z] ______________________ test_mcp_tool_call[Qwen/Qwen3-8B] _______________________ [2026-02-17T07:27:11Z] [2026-02-17T07:27:11Z] client = [2026-02-17T07:27:11Z] model_name = 'Qwen/Qwen3-8B' [2026-02-17T07:27:11Z] [2026-02-17T07:27:11Z] @pytest.mark.asyncio [2026-02-17T07:27:11Z] @pytest.mark.parametrize("model_name", [MODEL_NAME]) [2026-02-17T07:27:11Z] async def test_mcp_tool_call(client: OpenAI, model_name: str): [2026-02-17T07:27:11Z] response = await client.responses.create( [2026-02-17T07:27:11Z] model=model_name, [2026-02-17T07:27:11Z] input="What is 123 * 456? Use python to calculate the result.", [2026-02-17T07:27:11Z] tools=[{"type": "code_interpreter", "container": {"type": "auto"}}], [2026-02-17T07:27:11Z] extra_body={...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: ntrypoints/openai/responses/test_parsable_context.py::test_mcp_tool_call[Qwen/Qwen3-8B] - AssertionError: assert 'mcp_call' == 'message'` ### Basic information - [x] Flaky test - [ ] Can reproduce locally - [ ] Caused b...
- [Bitwise 确定性与数值等价](../patterns/bitwise_determinism_equivalence.md) - 分数 1: p_call' == 'message'` ### Basic information - [x] Flaky test - [ ] Can reproduce locally - [ ] Caused by external libraries (e.g. bug in `transformers`) ### 🧪 Describe the failing test ``` [2026-02-17T07:27:11Z] =======...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: [CI Failure]: Entrypoints Integration (Responses API) ci-failure ### Name of failing test `entrypoints/openai/responses/test_parsable_context.py::test_mcp_tool_call[Qwen/Qwen3-8B] - AssertionError: assert 'mcp_call' == '
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: : Entrypoints Integration (Responses API) ci-failure ### Name of failing test `entrypoints/openai/responses/test_parsable_context.py::test_mcp_tool_call[Qwen/Qwen3-8B] - AssertionError: assert 'mcp_call' == 'message'` #...

## Wiki 抽取状态

- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
