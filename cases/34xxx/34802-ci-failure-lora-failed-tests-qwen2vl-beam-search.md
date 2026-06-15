# vllm-project/vllm#34802: [CI Failure]: Lora failed tests qwen2vl beam search

| 字段 | 值 |
| --- | --- |
| Issue | [#34802](https://github.com/vllm-project/vllm/issues/34802) |
| 状态 | closed |
| 标签 | ci-failure |
| 评论 | 0; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [CI Failure]: Lora failed tests qwen2vl beam search

### Issue 正文摘录

### Name of failing test `lora/test_qwenvl.py::test_qwen2vl_lora_beam_search` ### Basic information - [ ] Flaky test - [x] Can reproduce locally - [ ] Caused by external libraries (e.g. bug in `transformers`) ### 🧪 Describe the failing test ``` FAILED tests/lora/test_qwenvl.py::test_qwen2vl_lora_beam_search - AssertionError: Generated texts [' system\nYou are a helpful assistant. \n user\n <|im... ``` ### 📝 History of failing test https://buildkite.com/vllm/ci/builds/52052/steps/canvas?jid=019c6f8d-c523-4302-9bc8-601a0b791fdb ### CC List. @alex-jw-brooks

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: [CI Failure]: Lora failed tests qwen2vl beam search ci-failure ### Name of failing test `lora/test_qwenvl.py::test_qwen2vl_lora_beam_search` ### Basic information - [ ] Flaky test - [x] Can reproduce locally - [ ] Caus
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: [CI Failure]: Lora failed tests qwen2vl beam search ci-failure ### Name of failing test `lora/test_qwenvl.py::test_qwen2vl_lora_beam_search` ### Basic information - [ ] Flaky test - [x] Can reproduce locally - [ ] Cause...
- [Bitwise 确定性与数值等价](../patterns/bitwise_determinism_equivalence.md) - 分数 1: 2vl_lora_beam_search` ### Basic information - [ ] Flaky test - [x] Can reproduce locally - [ ] Caused by external libraries (e.g. bug in `transformers`) ### 🧪 Describe the failing test ``` FAILED tests/lora/test_qwenvl....
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: [CI Failure]: Lora failed tests qwen2vl beam search ci-failure ### Name of failing test `lora/test_qwenvl.py::test_qwen2vl_lora_beam_search` ### Basic information - [ ] Flaky test - [x] Can reproduce locally - [ ] Cause...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: [CI Failure]: Lora failed tests qwen2vl beam search ci-failure ### Name of failing test `lora/test_qwenvl.py::test_qwen2vl_lora_beam_search` ### Basic information - [ ] Flaky test - [x] Can reproduce locally - [ ] Cause...

## Wiki 抽取状态

- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
