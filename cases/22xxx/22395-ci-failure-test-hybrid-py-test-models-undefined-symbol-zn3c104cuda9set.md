# vllm-project/vllm#22395: [CI Failure]: test_hybrid.py::test_models undefined symbol: _ZN3c104cuda9SetDeviceEab

| 字段 | 值 |
| --- | --- |
| Issue | [#22395](https://github.com/vllm-project/vllm/issues/22395) |
| 状态 | closed |
| 标签 | ci-failure |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [CI Failure]: test_hybrid.py::test_models undefined symbol: _ZN3c104cuda9SetDeviceEab

### Issue 正文摘录

### Name of failing test models/language/generation/test_hybrid.py::test_models[5-64-state-spaces/mamba-130m-hf] ### Basic information - [x] Flaky test - [ ] Can reproduce locally - [ ] Caused by external libraries (e.g. bug in `transformers`) ### 🧪 Describe the failing test Failing with this error: ``` ImportError: /usr/local/lib/python3.12/dist-packages/selective_scan_cuda.cpython-312-x86_64-linux-gnu.so: undefined symbol: _ZN3c104cuda9SetDeviceEab ``` - 7-day reliability in the 90s percent - https://buildkite.com/organizations/vllm/analytics/suites/ci-1/tests?branch=main&commit=Search&period=7days&query=test_hybrid - 1-day reliability as low as 28 percent - https://buildkite.com/organizations/vllm/analytics/suites/ci-1/tests?branch=main&commit=Search&period=1day&query=test_hybrid ### 📝 History of failing test appears to have gotten a lot worse in the last week at some point ### CC List. _No response_

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: [CI Failure]: test_hybrid.py::test_models undefined symbol: _ZN3c104cuda9SetDeviceEab ci-failure ### Name of failing test models/language/generation/test_hybrid.py::test_models[5-64-state-spaces/mamba-130m-hf] ### Basi
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: [CI Failure]: test_hybrid.py::test_models undefined symbol: _ZN3c104cuda9SetDeviceEab ci-failure ### Name of failing test models/language/generation/test_hybrid.py::test_models[5-64-state-spaces/mamba-130m-hf] ### Basic...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: [CI Failure]: test_hybrid.py::test_models undefined symbol: _ZN3c104cuda9SetDeviceEab ci-failure ### Name of failing test models/language/generation/test_hybrid.py::test_models[5-64-state-spaces/mamba-130m-hf] ### Basic...
- [Bitwise 确定性与数值等价](../patterns/bitwise_determinism_equivalence.md) - 分数 1: paces/mamba-130m-hf] ### Basic information - [x] Flaky test - [ ] Can reproduce locally - [ ] Caused by external libraries (e.g. bug in `transformers`) ### 🧪 Describe the failing test Failing with this error: ``` Import...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: [CI Failure]: test_hybrid.py::test_models undefined symbol: _ZN3c104cuda9SetDeviceEab ci-failure ### Name of failing test models/language/generation/test_hybrid.py::test_models[5-64-state-spaces/mamba-130m-hf] ### Basic...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
