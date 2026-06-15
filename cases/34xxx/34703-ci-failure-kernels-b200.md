# vllm-project/vllm#34703: [CI Failure]: Kernels (B200)

| 字段 | 值 |
| --- | --- |
| Issue | [#34703](https://github.com/vllm-project/vllm/issues/34703) |
| 状态 | open |
| 标签 | stale;ci-failure |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [CI Failure]: Kernels (B200)

### Issue 正文摘录

### Name of failing test `tests/kernels/moe/test_flashinfer.py::test_flashinfer_blockscale_fp8_none_expert_group` ### Basic information - [ ] Flaky test - [x] Can reproduce locally - [ ] Caused by external libraries (e.g. bug in `transformers`) ### 🧪 Describe the failing test ``` FAILED tests/kernels/moe/test_flashinfer.py::test_flashinfer_blockscale_fp8_none_expert_group - RuntimeError: Check failed: (args->n_group != 0) is false: n_group should not be zero for DeepSeekV3 routing -- ``` ### 📝 History of failing test Failing since https://github.com/vllm-project/vllm/pull/34494 fixed by: https://github.com/vllm-project/vllm/pull/34673 ### CC List. _No response_

## 候选优化模式

- [MoE、GEMM 与 Expert Routing](../patterns/moe_gemm_routing.md) - 分数 3: Kernels (B200) stale;ci-failure ### Name of failing test `tests/kernels/moe/test_flashinfer.py::test_flashinfer_blockscale_fp8_none_expert_group` ### Basic information - [ ] Flaky test - [x] Can reproduce locally - [ ]...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 2: B200) stale;ci-failure ### Name of failing test `tests/kernels/moe/test_flashinfer.py::test_flashinfer_blockscale_fp8_none_expert_group` ### Basic information - [ ] Flaky test - [x] Can reproduce locally - [ ] Caused by...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 2: ailing test `tests/kernels/moe/test_flashinfer.py::test_flashinfer_blockscale_fp8_none_expert_group` ### Basic information - [ ] Flaky test - [x] Can reproduce locally - [ ] Caused by external libraries (e.g. bug in `tr...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 2: of failing test `tests/kernels/moe/test_flashinfer.py::test_flashinfer_blockscale_fp8_none_expert_group` ### Basic information - [ ] Flaky test - [x] Can reproduce locally - [ ] Caused by external libraries (e.g. bug in...
- [Bitwise 确定性与数值等价](../patterns/bitwise_determinism_equivalence.md) - 分数 1: p8_none_expert_group` ### Basic information - [ ] Flaky test - [x] Can reproduce locally - [ ] Caused by external libraries (e.g. bug in `transformers`) ### 🧪 Describe the failing test ``` FAILED tests/kernels/moe/test_...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
