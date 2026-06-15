# vllm-project/vllm#33094: [CI Failure]: Entrypoints Test (Responses)

| 字段 | 值 |
| --- | --- |
| Issue | [#33094](https://github.com/vllm-project/vllm/issues/33094) |
| 状态 | closed |
| 标签 | ci-failure |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [CI Failure]: Entrypoints Test (Responses)

### Issue 正文摘录

### Name of failing test `entrypoints/openai/responses/test_harmony.py::test_mcp_tool_multi_turn[openai/gpt-oss-20b]` ### Basic information - [x] Flaky test - [ ] Can reproduce locally - [ ] Caused by external libraries (e.g. bug in `transformers`) ### 🧪 Describe the failing test ``` [2026-01-26T13:36:30Z] > assert tool_call_found, "MCP tool call not found in output_messages" -- [2026-01-26T13:36:30Z] E AssertionError: MCP tool call not found in output_messages ``` ### 📝 History of failing test example failure: https://buildkite.com/vllm/ci/builds/48475#019bfa75-2124-4130-833e-b296366716b5 ### CC List. _No response_

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: [CI Failure]: Entrypoints Test (Responses) ci-failure ### Name of failing test `entrypoints/openai/responses/test_harmony.py::test_mcp_tool_multi_turn[openai/gpt-oss-20b]` ### Basic information - [x] Flaky test - [ ] C
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: points/openai/responses/test_harmony.py::test_mcp_tool_multi_turn[openai/gpt-oss-20b]` ### Basic information - [x] Flaky test - [ ] Can reproduce locally - [ ] Caused by external libraries (e.g. bug in `transformers`) #...
- [Bitwise 确定性与数值等价](../patterns/bitwise_determinism_equivalence.md) - 分数 1: [openai/gpt-oss-20b]` ### Basic information - [x] Flaky test - [ ] Can reproduce locally - [ ] Caused by external libraries (e.g. bug in `transformers`) ### 🧪 Describe the failing test ``` [2026-01-26T13:36:30Z] > asser...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: [CI Failure]: Entrypoints Test (Responses) ci-failure ### Name of failing test `entrypoints/openai/responses/test_harmony.py::test_mcp_tool_multi_turn[openai/gpt-oss-20b]` ### Basic information - [x] Flaky test - [ ] Ca...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
