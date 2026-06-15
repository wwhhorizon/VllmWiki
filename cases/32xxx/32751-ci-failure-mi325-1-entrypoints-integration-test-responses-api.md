# vllm-project/vllm#32751: [CI Failure]:  mi325_1 Entrypoints Integration Test (Responses API)

| 字段 | 值 |
| --- | --- |
| Issue | [#32751](https://github.com/vllm-project/vllm/issues/32751) |
| 状态 | closed |
| 标签 | ci-failure |
| 评论 | 5; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [CI Failure]:  mi325_1 Entrypoints Integration Test (Responses API)

### Issue 正文摘录

### Name of failing test `pytest -v -s tests/entrypoints/openai/responses` ### Basic information - [ ] Flaky test - [x] Can reproduce locally - [ ] Caused by external libraries (e.g. bug in `transformers`) ### 🧪 Describe the failing test The test fails if run with the rest of the test group but passes if run individually `tests/entrypoints/openai/responses/test_harmony.py::test_mcp_tool_multi_turn[openai/gpt-oss-20b]`. The log is that: ```log MCP tool call not found in output. Got types: ['reasoning', 'message'] ``` ### 📝 History of failing test First failure as of: https://buildkite.com/vllm/amd-ci/builds/3319

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: [CI Failure]: mi325_1 Entrypoints Integration Test (Responses API) ci-failure ### Name of failing test `pytest -v -s tests/entrypoints/openai/responses` ### Basic information - [ ] Flaky test - [x] Can reproduce local
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: ing test `pytest -v -s tests/entrypoints/openai/responses` ### Basic information - [ ] Flaky test - [x] Can reproduce locally - [ ] Caused by external libraries (e.g. bug in `transformers`) ### 🧪 Describe the failing te...
- [Bitwise 确定性与数值等价](../patterns/bitwise_determinism_equivalence.md) - 分数 1: nts/openai/responses` ### Basic information - [ ] Flaky test - [x] Can reproduce locally - [ ] Caused by external libraries (e.g. bug in `transformers`) ### 🧪 Describe the failing test The test fails if run with the res...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: [CI Failure]: mi325_1 Entrypoints Integration Test (Responses API) ci-failure ### Name of failing test `pytest -v -s tests/entrypoints/openai/responses` ### Basic information - [ ] Flaky test - [x] Can reproduce locally...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
