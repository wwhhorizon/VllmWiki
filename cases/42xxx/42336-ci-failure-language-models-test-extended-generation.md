# vllm-project/vllm#42336: [CI Failure]: Language Models Test (Extended Generation)

| 字段 | 值 |
| --- | --- |
| Issue | [#42336](https://github.com/vllm-project/vllm/issues/42336) |
| 状态 | open |
| 标签 | ci-failure |
| 评论 | 0; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [CI Failure]: Language Models Test (Extended Generation)

### Issue 正文摘录

### Name of failing test `tests/models/language/generation/test_common.py::test_models[True-False-5-32-bigcode/starcoder2-3b]` and `tests/models/language/generation/test_common.py::test_models[False-False-5-32-bigcode/starcoder2-3b]` ### Basic information - [x] Flaky test - [ ] Can reproduce locally - [ ] Caused by external libraries (e.g. bug in `transformers`) Could not reproduce on 1 x B200. Do not have Hopper on hand atm. ### 🧪 Describe the failing test Generation mismatch ``` Matched tokens: [222, 40, 494, 447, 9009, 98, 828, 366] [2026-05-11T07:29:20Z] hf: '\n# + [markdown] id="5f7o229v00-L"\n# **1950** - ' {59: -4.088154315948486, 58: -4.088154315948486, 56: -4.213154315948486, 55: -4.213154315948486, 54: -4.213154315948486} [2026-05-11T07:29:20Z] vllm: '\n# + [markdown] id="68284477"\n# **1950**\n#\n# - ' {59: Logprob(logprob=-4.071040153503418, rank=1, decoded_token='6'), 56: Logprob(logprob=-4.196040153503418, rank=2, decoded_token='3'), 54: Logprob(logprob=-4.196040153503418, rank=3, decoded_token='1'), 57: Logprob(logprob=-4.196040153503418, rank=4, decoded_token='4'), 55: Logprob(logprob=-4.196040153503418, rank=5, decoded_token='2')} ``` ### 📝 History of failing test...

## 候选优化模式

- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: ernal libraries (e.g. bug in `transformers`) Could not reproduce on 1 x B200. Do not have Hopper on hand atm. ### 🧪 Describe the failing test Generation mismatch ``` Matched tokens: [222, 40, 494, 447, 9009, 98, 828, 36...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: [CI Failure]: Language Models Test (Extended Generation) ci-failure ### Name of failing test `tests/models/language/generation/test_common.py::test_models[True-False-5-32-bigcode/starcoder2-3b]` and `tests/models/langua...
- [Bitwise 确定性与数值等价](../patterns/bitwise_determinism_equivalence.md) - 分数 2: gcode/starcoder2-3b]` ### Basic information - [x] Flaky test - [ ] Can reproduce locally - [ ] Caused by external libraries (e.g. bug in `transformers`) Could not reproduce on 1 x B200. Do not have Hopper on hand atm. #...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: [CI Failure]: Language Models Test (Extended Generation) ci-failure ### Name of failing test `tests/models/language/generation/test_common.py::test_models[True-False-5-32-bigcode/starcoder2-3b]` and `tests/models/languag
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 1: st `tests/models/language/generation/test_common.py::test_models[True-False-5-32-bigcode/starcoder2-3b]` and `tests/models/language/generation/test_common.py::test_models[False-False-5-32-bigcode/starcoder2-3b]` ### Bas...

## Wiki 抽取状态

- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
