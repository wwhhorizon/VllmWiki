# vllm-project/vllm#34804: [CI Failure]: Lora failed tests lora/test_default_mm_loras.py

| 字段 | 值 |
| --- | --- |
| Issue | [#34804](https://github.com/vllm-project/vllm/issues/34804) |
| 状态 | closed |
| 标签 | ci-failure |
| 评论 | 0; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [CI Failure]: Lora failed tests lora/test_default_mm_loras.py

### Issue 正文摘录

### Name of failing test `lora/test_default_mm_loras.py` ### Basic information - [ ] Flaky test - [x] Can reproduce locally - [ ] Caused by external libraries (e.g. bug in `transformers`) ### 🧪 Describe the failing test `lora/test_default_mm_loras.py::test_active_default_mm_lora` ``` AssertionError: assert False -- E + where False = ('Spoken text: The first words I spoke in the original chronograph, a little piece of practical poetry. Mary had a little lamb, it slept with quite a snow, and everywhere that Mary went, the lamb was sure to go.') E + where = ' Can you transcribe this audio? Certainly! Here is the transcription of the audio you provided:\n\nThe first words I spoke in the original phonograph record: A little piece of practical poetry. Mary had a little lamb; its fleece was white as snow, and everywhere that Mary went, the lamb was sure to go.'.endswith ``` `lora/test_default_mm_loras.py::test_default_mm_lora_does_not_expand_string_reqs` ``` E KeyError: 'prompt_text' ``` ### 📝 History of failing test https://buildkite.com/vllm/ci/builds/52052/steps/canvas?jid=019c6f8d-c524-48e4-bbd8-dff962e89889 ### CC List. @alex-jw-brooks

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: [CI Failure]: Lora failed tests lora/test_default_mm_loras.py ci-failure ### Name of failing test `lora/test_default_mm_loras.py` ### Basic information - [ ] Flaky test - [x] Can reproduce locally - [ ] Caused by exter
- [Bitwise 确定性与数值等价](../patterns/bitwise_determinism_equivalence.md) - 分数 1: _default_mm_loras.py` ### Basic information - [ ] Flaky test - [x] Can reproduce locally - [ ] Caused by external libraries (e.g. bug in `transformers`) ### 🧪 Describe the failing test `lora/test_default_mm_loras.py::te...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 1: t_mm_loras.py::test_active_default_mm_lora` ``` AssertionError: assert False -- E + where False = ('Spoken text: The first words I spoke in the original chronograph, a little piece of practical poetry. Mary had a little...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: e ### Name of failing test `lora/test_default_mm_loras.py` ### Basic information - [ ] Flaky test - [x] Can reproduce locally - [ ] Caused by external libraries (e.g. bug in `transformers`) ### 🧪 Describe the failing te...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: [CI Failure]: Lora failed tests lora/test_default_mm_loras.py ci-failure ### Name of failing test `lora/test_default_mm_loras.py` ### Basic information - [ ] Flaky test - [x] Can reproduce locally - [ ] Caused by extern...

## Wiki 抽取状态

- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
