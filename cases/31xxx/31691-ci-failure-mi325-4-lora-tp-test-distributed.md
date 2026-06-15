# vllm-project/vllm#31691: [CI Failure]:  mi325_4: LoRA TP Test (Distributed)

| 字段 | 值 |
| --- | --- |
| Issue | [#31691](https://github.com/vllm-project/vllm/issues/31691) |
| 状态 | closed |
| 标签 | ci-failure |
| 评论 | 7; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [CI Failure]:  mi325_4: LoRA TP Test (Distributed)

### Issue 正文摘录

### Name of failing test `pytest -s -v lora/test_olmoe_tp.py::test_olmoe_lora` ### Basic information - [ ] Flaky test - [x] Can reproduce locally - [ ] Caused by external libraries (e.g. bug in `transformers`) ### 🧪 Describe the failing test This is a temporary CI failure after merging https://github.com/vllm-project/vllm/pull/31533. There is already a PR that fixes this failure https://github.com/vllm-project/vllm/pull/31663 ### 📝 History of failing test https://buildkite.com/vllm/amd-ci/builds/2342 ### CC List. _No response_

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: [CI Failure]: mi325_4: LoRA TP Test (Distributed) ci-failure ### Name of failing test `pytest -s -v lora/test_olmoe_tp.py::test_olmoe_lora` ### Basic information - [ ] Flaky test - [x] Can reproduce locally - [ ] Caus
- [Bitwise 确定性与数值等价](../patterns/bitwise_determinism_equivalence.md) - 分数 1: .py::test_olmoe_lora` ### Basic information - [ ] Flaky test - [x] Can reproduce locally - [ ] Caused by external libraries (e.g. bug in `transformers`) ### 🧪 Describe the failing test This is a temporary CI failure aft...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: test `pytest -s -v lora/test_olmoe_tp.py::test_olmoe_lora` ### Basic information - [ ] Flaky test - [x] Can reproduce locally - [ ] Caused by external libraries (e.g. bug in `transformers`) ### 🧪 Describe the failing te...
- [MoE、GEMM 与 Expert Routing](../patterns/moe_gemm_routing.md) - 分数 1: tributed) ci-failure ### Name of failing test `pytest -s -v lora/test_olmoe_tp.py::test_olmoe_lora` ### Basic information - [ ] Flaky test - [x] Can reproduce locally - [ ] Caused by external libraries (e.g. bug in `tra...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: [CI Failure]: mi325_4: LoRA TP Test (Distributed) ci-failure ### Name of failing test `pytest -s -v lora/test_olmoe_tp.py::test_olmoe_lora` ### Basic information - [ ] Flaky test - [x] Can reproduce locally - [ ] Caused...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
