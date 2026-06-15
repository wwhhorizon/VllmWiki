# vllm-project/vllm#28402: [CI Failure]: Nightly MM Models Extended (3)

| 字段 | 值 |
| --- | --- |
| Issue | [#28402](https://github.com/vllm-project/vllm/issues/28402) |
| 状态 | closed |
| 标签 | ci-failure |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [CI Failure]: Nightly MM Models Extended (3)

### Issue 正文摘录

### Name of failing test [2025-11-09T06:15:40Z] FAILED models/multimodal/generation/test_common.py::test_custom_inputs_models[llava_onevision-multiple-images-test_case5] - AssertionError: Test0: ### Basic information - [ ] Flaky test - [ ] Can reproduce locally - [ ] Caused by external libraries (e.g. bug in `transformers`) ### 🧪 Describe the failing test Looks like numerics mismatch between HF and VLLM ``` [2025-11-09T06:15:40Z] FAILED models/multimodal/generation/test_common.py::test_custom_inputs_models[llava_onevision-multiple-images-test_case5] - AssertionError: Test0: -- | [2025-11-09T06:15:40Z] Matched tokens: [785] | [2025-11-09T06:15:40Z] hf: "The image captures the iconic Tokyo Tower, a renowned landmark in Tokyo, Japan. The tower, a symbol of Tokyo's rich history and architectural prowess, stands majestically in the background, its white and red color scheme adding a vibrant contrast to the clear blue sky. The tower's intricate lattice structure, a testament to its historical significance, is adorned with numerous windows that reflect the sunlight, adding to its grandeur. The tower's white and red color scheme is echoed in the cherry blossom trees that surround it, thei...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: [CI Failure]: Nightly MM Models Extended (3) ci-failure ### Name of failing test [2025-11-09T06:15:40Z] FAILED models/multimodal/generation/test_common.py::test_custom_inputs_models[llava_onevision-multiple-images-test_...
- [Bitwise 确定性与数值等价](../patterns/bitwise_determinism_equivalence.md) - 分数 3: ssertionError: Test0: ### Basic information - [ ] Flaky test - [ ] Can reproduce locally - [ ] Caused by external libraries (e.g. bug in `transformers`) ### 🧪 Describe the failing test Looks like numerics mismatch betwe...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: [CI Failure]: Nightly MM Models Extended (3) ci-failure ### Name of failing test [2025-11-09T06:15:40Z] FAILED models/multimodal/generation/test_common.py::test_custom_inputs_models[llava_onevision-multiple-images-test_c
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: `transformers`) ### 🧪 Describe the failing test Looks like numerics mismatch between HF and VLLM ``` [2025-11-09T06:15:40Z] FAILED models/multimodal/generation/test_common.py::test_custom_inputs_models[llava_onevision-m...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: leasant day.\n\nThe' {1156: Logprob(logprob=-0.8410025835037231, rank=1, decoded_token=' first'), 2168: Logprob(logprob=-1.1222525835037231, rank=2, decoded_token=' image'), 2086: Logprob(logprob=-1.5441275835037231, ra...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
