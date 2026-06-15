# vllm-project/vllm#38098: [CI Failure]: LM Eval Large Models (H200)

| 字段 | 值 |
| --- | --- |
| Issue | [#38098](https://github.com/vllm-project/vllm/issues/38098) |
| 状态 | closed |
| 标签 | ci-failure |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | development |
| 工作域 | ci_build;model_support;quantization |
| 子分类 |  |
| Operator 关键词 | fp8 |
| 症状 |  |
| 根因提示 | dtype |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [CI Failure]: LM Eval Large Models (H200)

### Issue 正文摘录

### Name of failing test `tests/evals/gsm8k/test_gsm8k_correctness.py --config-list-file=configs/models-h200.txt -k "Nemotron-3-Super-120B-A12B-BF16"` ### Basic information - [ ] Flaky test - [x] Can reproduce locally - [ ] Caused by external libraries (e.g. bug in `transformers`) ### 🧪 Describe the failing test Too low gsm8k metric for `Nemotron-3-Super-120B-A12B-BF16`. `nvidia/NVIDIA-Nemotron-3-Super-120B-A12B-FP8` passes the eval test with `0.91` value. Locally ``` E AssertionError: GSM8K metric too low: 0.7968 = (0.93 - 0.08) ``` Draft acceptance rate for BF16 is lower than for FP8 (check buildkite logs) ### 📝 History of failing test https://buildkite.com/vllm/ci/builds/57706/steps/canvas?sid=019d1e6f-177a-4d18-aa98-e841764f2152&tab=output ### CC List. _No response_

## 候选优化模式

- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 4: -config-list-file=configs/models-h200.txt -k "Nemotron-3-Super-120B-A12B-BF16"` ### Basic information - [ ] Flaky test - [x] Can reproduce locally - [ ] Caused by external libraries (e.g. bug in `transformers`) ### 🧪 De...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: [CI Failure]: LM Eval Large Models (H200) ci-failure ### Name of failing test `tests/evals/gsm8k/test_gsm8k_correctness.py --config-list-file=configs/models-h200.txt -k "Nemotron-3-Super-120B-A12B-BF16"` ### Basic infor...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: [CI Failure]: LM Eval Large Models (H200) ci-failure ### Name of failing test `tests/evals/gsm8k/test_gsm8k_correctness.py --config-list-file=configs/models-h200.txt -k "Nemotron-3-Super-120B-A12B-BF16"` ### Basic infor
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 2: [CI Failure]: LM Eval Large Models (H200) ci-failure ### Name of failing test `tests/evals/gsm8k/test_gsm8k_correctness.py --config-list-file=configs/models-h200.txt -k "Nemotron-3-Super-120B-A12B-BF16"` ### Basic infor...
- [Bitwise 确定性与数值等价](../patterns/bitwise_determinism_equivalence.md) - 分数 1: uper-120B-A12B-BF16"` ### Basic information - [ ] Flaky test - [x] Can reproduce locally - [ ] Caused by external libraries (e.g. bug in `transformers`) ### 🧪 Describe the failing test Too low gsm8k metric for `Nemotron...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
