# vllm-project/vllm#43090: [CI Failure]: Language Models Tests (Hybrid) 1 - granite-4.0-tiny-preview prefix caching regression

| 字段 | 值 |
| --- | --- |
| Issue | [#43090](https://github.com/vllm-project/vllm/issues/43090) |
| 状态 | open |
| 标签 |  |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [CI Failure]: Language Models Tests (Hybrid) 1 - granite-4.0-tiny-preview prefix caching regression

### Issue 正文摘录

### Name of failing test `tests/models/language/generation/test_hybrid.py::test_models[5-64-ibm-granite/granite-4.0-tiny-preview]` ### Basic information - [ ] Flaky test - [ ] Can reproduce locally - [ ] Caused by external libraries (e.g. bug in `transformers`) ### 🧪 Describe the failing test [url](https://buildkite.com/vllm/ci/builds/66835/list?jid=019e3ed4-272d-4aa8-9928-abd3851b42eb&tab=output) The test compares vllm outputs between cached and uncached runs for the hybrid (Mamba/SSM) model `ibm-granite/granite-4.0-tiny-preview`. The assertion `output_id_0 in logprobs_elem_1` fails — the top token from one run isn't in the top-k logprobs of the other run when prefix caching is involved. The outputs diverge between cached and uncached paths. For example in Test1, `vllm_no_cache` produces `"china"` (rank 1) while `vllm_partial_cache` has `"china"` drop to rank 2 with `"\n"` tied at the same logprob. This is a prefix caching correctness issue for hybrid/SSM models. ``` FAILED models/language/generation/test_hybrid.py::test_models[5-64-ibm-granite/granite-4.0-tiny-preview] - AssertionError: Test1: ``` Example divergence: ``` vllm_no_cache: 'china' rank=1, logprob=-3.011 vllm_partial...

## 候选优化模式

- [KV Cache 容量、压缩与 Offload](../patterns/kv_cache_capacity_offload.md) - 分数 3: for relevance. The most likely root cause is PR #42766 which changes how KV cache block tables are initialized: - Introduces `kernel_block_sizes` that can differ from logical `block_sizes` - Changes block table sizing:...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 3: ance. The most likely root cause is PR #42766 which changes how KV cache block tables are initialized: - Introduces `kernel_block_sizes` that can differ from logical `block_sizes` - Changes block table sizing: `max_num_...
- [Bitwise 确定性与数值等价](../patterns/bitwise_determinism_equivalence.md) - 分数 2: te-4.0-tiny-preview]` ### Basic information - [ ] Flaky test - [ ] Can reproduce locally - [ ] Caused by external libraries (e.g. bug in `transformers`) ### 🧪 Describe the failing test [url](https://buildkite.com/vllm/c...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: [CI Failure]: Language Models Tests (Hybrid) 1 - granite-4.0-tiny-preview prefix caching regression ### Name of failing test `tests/models/language/generation/test_hybrid.py::test_models[5-64-ibm-granite/granite-4.0-tiny
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: [CI Failure]: Language Models Tests (Hybrid) 1 - granite-4.0-tiny-preview prefix caching regression ### Name of failing test `tests/models/language/generation/test_hybrid.py::test_models[5-64-ibm-granite/granite-4.0-tin...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
