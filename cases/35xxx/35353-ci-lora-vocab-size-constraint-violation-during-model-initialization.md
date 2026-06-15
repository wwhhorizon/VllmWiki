# vllm-project/vllm#35353: [CI] LoRA vocab size constraint violation during model initialization

| 字段 | 值 |
| --- | --- |
| Issue | [#35353](https://github.com/vllm-project/vllm/issues/35353) |
| 状态 | closed |
| 标签 | ci-failure |
| 评论 | 0; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [CI] LoRA vocab size constraint violation during model initialization

### Issue 正文摘录

## Name of failing test - `lora/test_mixtral.py::test_mixtral_lora[4]` ## Basic information - [ ] Flaky test - [ ] Can reproduce locally - [ ] Caused by external libraries **Affected jobs:** Distributed Tests (4 GPUs)(A100) **Category:** test ## Describe the failing test During LoRA model loading, the create_lora_weights() function in logits_processor.py raises ValueError because the model's vocabulary size does not meet the required constraint. The error occurs when initializing LoRA modules as part of the LoRA manager creation during model loading. The constraint requires vocab size to be greater than 32000 and less than or equal to 258048. This indicates either a bug in the vocab size constraint logic, an incompatibility between the test model configuration and LoRA requirements, or the test attempting to use a model with an invalid vocab size for LoRA. ``` ValueError: When using LoRA, vocab size must be > 32000 and <= 258048 ``` ## Relevant builds - [Build #53243](https://buildkite.com/vllm/ci/builds/53243) (c97234c0) - [Distributed Tests (4 GPUs)(A100)](https://buildkite.com/vllm/ci/builds/53243#019c96d2-5c00-42ee-a566-3c220fe61078) ## History of failing test - **First seen:*...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: [CI] LoRA vocab size constraint violation during model initialization ci-failure ## Name of failing test - `lora/test_mixtral.py::test_mixtral_lora[4]` ## Basic information - [ ] Flaky test - [ ] Can reproduce locally -...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: [CI] LoRA vocab size constraint violation during model initialization ci-failure ## Name of failing test - `lora/test_mixtral.py::test_mixtral_lora[4]` ## Basic information - [ ] Flaky test - [ ] Can reproduce locally
- [Bitwise 确定性与数值等价](../patterns/bitwise_determinism_equivalence.md) - 分数 1: :test_mixtral_lora[4]` ## Basic information - [ ] Flaky test - [ ] Can reproduce locally - [ ] Caused by external libraries **Affected jobs:** Distributed Tests (4 GPUs)(A100) **Category:** test ## Describe the failing...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: sed by external libraries **Affected jobs:** Distributed Tests (4 GPUs)(A100) **Category:** test ## Describe the failing test During LoRA model loading, the create_lora_weights() function in logits_processor.py raises V...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: aint violation during model initialization ci-failure ## Name of failing test - `lora/test_mixtral.py::test_mixtral_lora[4]` ## Basic information - [ ] Flaky test - [ ] Can reproduce locally - [ ] Caused by external lib...

## Wiki 抽取状态

- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
