# vllm-project/vllm#2005: BUG: de-initialize model parallel

| 字段 | 值 |
| --- | --- |
| Issue | [#2005](https://github.com/vllm-project/vllm/issues/2005) |
| 状态 | closed |
| 标签 |  |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> BUG: de-initialize model parallel

### Issue 正文摘录

The following command `pytest tests/samplers/` complains ``` FAILED tests/samplers/test_logprobs.py::test_get_prompt_logprobs[half-facebook/opt-125m] - AssertionError: tensor model parallel group is already initialized ``` with the stack trace revealing [code in initialize_model_parallel](https://github.com/vllm-project/vllm/blob/1aa13615103c2ea47e36710a9b2e17dfe1909143/vllm/model_executor/parallel_utils/parallel_state.py#L64-L65) as follows: ``` rank = torch.distributed.get_rank() # Build the tensor model-parallel groups. global _TENSOR_MODEL_PARALLEL_GROUP > assert _TENSOR_MODEL_PARALLEL_GROUP is None, ( "tensor model parallel group is already initialized") E AssertionError: tensor model parallel group is already initialized vllm/model_executor/parallel_utils/parallel_state.py:64: AssertionError ``` However, if I run `tests/samplers/test_logprobs.py::test_get_prompt_logprob` along, it passes. A similar case is `pytest tests/models/`, which complains the following assertion failures: ``` FAILED tests/models/test_models.py::test_models[128-half-meta-llama/Llama-2-7b-hf] - OSError: You are trying to access a gated repo. FAILED tests/models/test_models.py::test_models[128-half-mistr...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: BUG: de-initialize model parallel The following command `pytest tests/samplers/` complains ``` FAILED tests/samplers/test_logprobs.py::test_get_prompt_logprobs[half-facebook/opt-125m] - AssertionError: tensor model para...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: as follows: ``` rank = torch.distributed.get_rank() # Build the tensor model-parallel groups. global _TENSOR_MODEL_PARALLEL_GROUP > assert _TENSOR_MODEL_PARALLEL_GROUP is None, ( "tensor model parallel group is already...
- [KV Cache 容量、压缩与 Offload](../patterns/kv_cache_capacity_offload.md) - 分数 1: ed FAILED tests/models/test_models.py::test_models[128-half-bigscience/bloom-560m] - AssertionError: tensor model parallel group is already initialized FAILED tests/models/test_models.py::test_models[128-half-mosaicml/m...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: BUG: de-initialize model parallel The following command `pytest tests/samplers/` complains ``` FAILED tests/samplers/test_logprobs.py::test_get_prompt_logprobs[half-facebook/opt-125m] - AssertionError: tensor model para...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
