# vllm-project/vllm#37596: [CI Failure]:  mi355_1: Language Models Test (PPL)

| 字段 | 值 |
| --- | --- |
| Issue | [#37596](https://github.com/vllm-project/vllm/issues/37596) |
| 状态 | closed |
| 标签 | rocm;ci-failure |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [CI Failure]:  mi355_1: Language Models Test (PPL)

### Issue 正文摘录

### Name of failing test `pytest -s -v tests/models/language/generation_ppl_test/test_qwen.py::test_ppl[model_info2]` ### Basic information - [ ] Flaky test - [x] Can reproduce locally - [ ] Caused by external libraries (e.g. bug in `transformers`) ### 🧪 Describe the failing test There is currently an error: ```log (EngineCore pid=1578061) INFO 03-19 20:12:53 [gpu_model_runner.py:4601] Model loading took 1.59 GiB memory and 1.009335 seconds (EngineCore pid=1578061) /app/vllm/vllm/model_executor/layers/utils.py:188: UserWarning: Failed validator: GCN_ARCH_NAME (Triggered internally at /app/pytorch/aten/src/ATen/hip/tunable/Tunable.cpp:364.) (EngineCore pid=1578061) return torch.nn.functional.linear(x, weight, bias) :0:rocdevice.cpp :3675: 1143953758580 us: Callback: Queue 0x7eb85a100000 aborting with error : HSA_STATUS_ERROR_MEMORY_APERTURE_VIOLATION: The agent attempted to access memory beyond the largest legal address. code: 0x29 FAILED ``` It's reproducible by: `HIP_VISIBLE_DEVICES=7 pytest -s -v tests/models/language/generation_ppl_test/test_qwen.py::test_ppl[model_info2]` Even with `enforce_eager` set to `True` error happens. ### 📝 History of failing test https://buildkite.com...

## 候选优化模式

- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 4: [CI Failure]: mi355_1: Language Models Test (PPL) rocm;ci-failure ### Name of failing test `pytest -s -v tests/models/language/generation_ppl_test/test_qwen.py::test_ppl[model_info2]` ### Basic information - [ ] Flaky t...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: [CI Failure]: mi355_1: Language Models Test (PPL) rocm;ci-failure ### Name of failing test `pytest -s -v tests/models/language/generation_ppl_test/test_qwen.py::test_ppl[model_info2]` ### Basic information - [ ] Flaky t...
- [Bitwise 确定性与数值等价](../patterns/bitwise_determinism_equivalence.md) - 分数 2: est_ppl[model_info2]` ### Basic information - [ ] Flaky test - [x] Can reproduce locally - [ ] Caused by external libraries (e.g. bug in `transformers`) ### 🧪 Describe the failing test There is currently an error: ```lo...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: [CI Failure]: mi355_1: Language Models Test (PPL) rocm;ci-failure ### Name of failing test `pytest -s -v tests/models/language/generation_ppl_test/test_qwen.py::test_ppl[model_info2]` ### Basic information - [ ] Flaky
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: t, bias) :0:rocdevice.cpp :3675: 1143953758580 us: Callback: Queue 0x7eb85a100000 aborting with error : HSA_STATUS_ERROR_MEMORY_APERTURE_VIOLATION: The agent attempted to access memory beyond the largest legal address....

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
