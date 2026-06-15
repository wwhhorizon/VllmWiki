# vllm-project/vllm#34160: [CI Failure]:  mi325_1: Entrypoints Unit Tests

| 字段 | 值 |
| --- | --- |
| Issue | [#34160](https://github.com/vllm-project/vllm/issues/34160) |
| 状态 | closed |
| 标签 | ci-failure |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [CI Failure]:  mi325_1: Entrypoints Unit Tests

### Issue 正文摘录

### Name of failing test `pytest -s -v tests/entrypoints/openai/tool_parsers/test_openai_tool_parser.py` ### Basic information - [ ] Flaky test - [x] Can reproduce locally - [ ] Caused by external libraries (e.g. bug in `transformers`) ### 🧪 Describe the failing test There was a recent regression in this test group related to GPT-OSS. Specifically, the new torch 2.10 version is breaking GPT-OSS: https://github.com/vllm-project/vllm/pull/30525 There's already a PR up to fix this regression: https://github.com/vllm-project/vllm/pull/34153 The tests are passing with this patch. ### 📝 History of failing test https://buildkite.com/vllm/amd-ci/builds/4400/steps/canvas

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: [CI Failure]: mi325_1: Entrypoints Unit Tests ci-failure ### Name of failing test `pytest -s -v tests/entrypoints/openai/tool_parsers/test_openai_tool_parser.py` ### Basic information - [ ] Flaky test - [x] Can reprod
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: entrypoints/openai/tool_parsers/test_openai_tool_parser.py` ### Basic information - [ ] Flaky test - [x] Can reproduce locally - [ ] Caused by external libraries (e.g. bug in `transformers`) ### 🧪 Describe the failing t...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 2: [CI Failure]: mi325_1: Entrypoints Unit Tests ci-failure ### Name of failing test `pytest -s -v tests/entrypoints/openai/tool_parsers/test_openai_tool_parser.py` ### Basic information - [ ] Flaky test - [x] Can reproduc...
- [Bitwise 确定性与数值等价](../patterns/bitwise_determinism_equivalence.md) - 分数 1: penai_tool_parser.py` ### Basic information - [ ] Flaky test - [x] Can reproduce locally - [ ] Caused by external libraries (e.g. bug in `transformers`) ### 🧪 Describe the failing test There was a recent regression in t...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
