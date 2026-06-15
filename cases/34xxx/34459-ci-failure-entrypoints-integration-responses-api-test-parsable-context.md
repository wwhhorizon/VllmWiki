# vllm-project/vllm#34459: [CI Failure]: Entrypoints Integration (Responses API) (test_parsable_context.py)

| 字段 | 值 |
| --- | --- |
| Issue | [#34459](https://github.com/vllm-project/vllm/issues/34459) |
| 状态 | open |
| 标签 | stale;ci-failure |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [CI Failure]: Entrypoints Integration (Responses API) (test_parsable_context.py)

### Issue 正文摘录

### Name of failing test `entrypoints/openai/responses/test_parsable_context.py::test_mcp_tool_call[Qwen/Qwen3-8B]` ### Basic information - [ ] Flaky test - [x] Can reproduce locally - [ ] Caused by external libraries (e.g. bug in `transformers`) ### 🧪 Describe the failing test The [CI test](https://buildkite.com/vllm/ci/builds/51276/steps/canvas?jid=019c50a7-7dd3-4209-bd17-54b05423c563&tab=output) failed on Feb 12, 2026 nightly CI run. ``` [2026-02-12T07:46:44Z] =================================== FAILURES =================================== -- [2026-02-12T07:46:44Z] ______________________ test_mcp_tool_call[Qwen/Qwen3-8B] _______________________ [2026-02-12T07:46:44Z] [2026-02-12T07:46:44Z] client = [2026-02-12T07:46:44Z] model_name = 'Qwen/Qwen3-8B' [2026-02-12T07:46:44Z] [2026-02-12T07:46:44Z] @pytest.mark.asyncio [2026-02-12T07:46:44Z] @pytest.mark.parametrize("model_name", [MODEL_NAME]) [2026-02-12T07:46:44Z] async def test_mcp_tool_call(client: OpenAI, model_name: str): [2026-02-12T07:46:44Z] response = await client.responses.create( [2026-02-12T07:46:44Z] model=model_name, [2026-02-12T07:46:44Z] input="What is 123 * 456? Use python to calculate the result.", [2026-02-12T07...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: ntrypoints/openai/responses/test_parsable_context.py::test_mcp_tool_call[Qwen/Qwen3-8B]` ### Basic information - [ ] Flaky test - [x] Can reproduce locally - [ ] Caused by external libraries (e.g. bug in `transformers`)...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: [CI Failure]: Entrypoints Integration (Responses API) (test_parsable_context.py) stale;ci-failure ### Name of failing test `entrypoints/openai/responses/test_parsable_context.py::test_mcp_tool_call[Qwen/Qwen3-8B]` ### B
- [Bitwise 确定性与数值等价](../patterns/bitwise_determinism_equivalence.md) - 分数 1: _call[Qwen/Qwen3-8B]` ### Basic information - [ ] Flaky test - [x] Can reproduce locally - [ ] Caused by external libraries (e.g. bug in `transformers`) ### 🧪 Describe the failing test The [CI test](https://buildkite.co...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: ure]: Entrypoints Integration (Responses API) (test_parsable_context.py) stale;ci-failure ### Name of failing test `entrypoints/openai/responses/test_parsable_context.py::test_mcp_tool_call[Qwen/Qwen3-8B]` ### Basic inf...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: [CI Failure]: Entrypoints Integration (Responses API) (test_parsable_context.py) stale;ci-failure ### Name of failing test `entrypoints/openai/responses/test_parsable_context.py::test_mcp_tool_call[Qwen/Qwen3-8B]` ### B...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
