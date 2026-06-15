# vllm-project/vllm#21277: [CI Failure]:  Classification test failure for Qwen2.5-1.5B-apeach model in half precision

| 字段 | 值 |
| --- | --- |
| Issue | [#21277](https://github.com/vllm-project/vllm/issues/21277) |
| 状态 | closed |
| 标签 | ci-failure |
| 评论 | 5; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [CI Failure]:  Classification test failure for Qwen2.5-1.5B-apeach model in half precision

### Issue 正文摘录

### Name of failing test FAILED models/test_transformers.py::test_classify[half-jason9693/Qwen2.5-1.5B-apeach] - AssertionError: assert False ### Basic information - [ ] Flaky test - [ ] Can reproduce locally - [ ] Caused by external libraries (e.g. bug in `transformers`) ### 🧪 Describe the failing test During test execution for the jason9693/Qwen2.5-1.5B-apeach model using half-precision dtype, the classification test test_classify failed due to output mismatch between vLLM and Hugging Face implementations. ``` [2025-07-20T11:45:11Z] > assert torch.allclose(hf_output, vllm_output, -- | [2025-07-20T11:45:11Z] 1e-3 if dtype == "float" else 1e-2) | [2025-07-20T11:45:11Z] E AssertionError: assert False | [2025-07-20T11:45:11Z] E + where False = (tensor([0.0413, 0.9585]), tensor([0.0409, 0.9591]), 0.01) | [2025-07-20T11:45:11Z] E + where = .allclose ``` If it returns True when manually run locally, that's indeed quite strange. ``` import torch tensor1 = torch.tensor([0.0413, 0.9585], dtype=torch.half) tensor2 = torch.tensor([0.0409, 0.9591], dtype=torch.half) print(torch.allclose(tensor1, tensor2,0.01)) # output true ``` ### 📝 History of failing test Ref to https://buildkite.com/vllm/...

## 候选优化模式

- [Bitwise 确定性与数值等价](../patterns/bitwise_determinism_equivalence.md) - 分数 5: ure]: Classification test failure for Qwen2.5-1.5B-apeach model in half precision ci-failure ### Name of failing test FAILED models/test_transformers.py::test_classify[half-jason9693/Qwen2.5-1.5B-apeach] - AssertionErro...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: [CI Failure]: Classification test failure for Qwen2.5-1.5B-apeach model in half precision ci-failure ### Name of failing test FAILED models/test_transformers.py::test_classify[half-jason9693/Qwen2.5-1.5B-apeach] - Asser...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: [CI Failure]: Classification test failure for Qwen2.5-1.5B-apeach model in half precision ci-failure ### Name of failing test FAILED models/test_transformers.py::test_classify[half-jason9693/Qwen2.5-1.5B-apeach] - Asser
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 1: ecution for the jason9693/Qwen2.5-1.5B-apeach model using half-precision dtype, the classification test test_classify failed due to output mismatch between vLLM and Hugging Face implementations. ``` [2025-07-20T11:45:11...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: sion dtype, the classification test test_classify failed due to output mismatch between vLLM and Hugging Face implementations. ``` [2025-07-20T11:45:11Z] > assert torch.allclose(hf_output, vllm_output, -- | [2025-07-20T...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
