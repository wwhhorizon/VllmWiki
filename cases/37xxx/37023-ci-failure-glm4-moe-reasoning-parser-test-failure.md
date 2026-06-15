# vllm-project/vllm#37023: [CI Failure]: GLM4 moe reasoning parser test failure

| 字段 | 值 |
| --- | --- |
| Issue | [#37023](https://github.com/vllm-project/vllm/issues/37023) |
| 状态 | open |
| 标签 | ci-failure |
| 评论 | 0; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [CI Failure]: GLM4 moe reasoning parser test failure

### Issue 正文摘录

### Name of failing test tests/reasoning/test_glm4_moe_reasoning_parser.py ### Basic information - [ ] Flaky test - [x] Can reproduce locally - [ ] Caused by external libraries (e.g. bug in `transformers`) ### 🧪 Describe the failing test ``` FAILED tests/reasoning/test_glm4_moe_reasoning_parser.py::test_reasoning[without_think] - AssertionError: assert 'This is the rest' == None FAILED tests/reasoning/test_glm4_moe_reasoning_parser.py::test_reasoning[without_think_stream] - AssertionError: assert 'This is the rest' == None FAILED tests/reasoning/test_glm4_moe_reasoning_parser.py::test_reasoning[only_open_tag] - AssertionError: assert 'This is a reasoning section' == None ``` ### 📝 History of failing test - This PR (https://github.com/vllm-project/vllm/pull/33221) deleted the dedicated Glm4MoeModelReasoningParser (and Holo2ReasoningParser) and replaced them with the generic DeepSeekV3ReasoningWithThinkingParser, which delegates to DeepSeekR1ReasoningParser. - The original GLM4 parser had different behavior from DeepSeek R1: - GLM4: Requires both and to identify reasoning. Without both tags, text is treated as content (return None, model_output). - R1: Treats text without tags as re...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: ing test tests/reasoning/test_glm4_moe_reasoning_parser.py ### Basic information - [ ] Flaky test - [x] Can reproduce locally - [ ] Caused by external libraries (e.g. bug in `transformers`) ### 🧪 Describe the failing te...
- [Bitwise 确定性与数值等价](../patterns/bitwise_determinism_equivalence.md) - 分数 1: e_reasoning_parser.py ### Basic information - [ ] Flaky test - [x] Can reproduce locally - [ ] Caused by external libraries (e.g. bug in `transformers`) ### 🧪 Describe the failing test ``` FAILED tests/reasoning/test_gl...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: [CI Failure]: GLM4 moe reasoning parser test failure ci-failure ### Name of failing test tests/reasoning/test_glm4_moe_reasoning_parser.py ### Basic information - [ ] Flaky test - [x] Can reproduce locally - [ ] Caused
- [MoE、GEMM 与 Expert Routing](../patterns/moe_gemm_routing.md) - 分数 1: [CI Failure]: GLM4 moe reasoning parser test failure ci-failure ### Name of failing test tests/reasoning/test_glm4_moe_reasoning_parser.py ### Basic information - [ ] Flaky test - [x] Can reproduce locally - [ ] Caused...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: [CI Failure]: GLM4 moe reasoning parser test failure ci-failure ### Name of failing test tests/reasoning/test_glm4_moe_reasoning_parser.py ### Basic information - [ ] Flaky test - [x] Can reproduce locally - [ ] Caused...

## Wiki 抽取状态

- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
