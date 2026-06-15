# vllm-project/vllm#34622: [CI Failure]: B200 Kernels

| 字段 | 值 |
| --- | --- |
| Issue | [#34622](https://github.com/vllm-project/vllm/issues/34622) |
| 状态 | closed |
| 标签 | ci-failure |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [CI Failure]: B200 Kernels

### Issue 正文摘录

### Name of failing test tests/kernels/moe/test_flashinfer.py::test_flashinfer_blockscale_fp8_none_expert_group ### Basic information - [ ] Flaky test - [ ] Can reproduce locally - [ ] Caused by external libraries (e.g. bug in `transformers`) ### 🧪 Describe the failing test ``` FAILED tests/kernels/moe/test_flashinfer.py::test_flashinfer_blockscale_fp8_none_expert_group - RuntimeError: Check failed: (args->n_group != 0) is false: n_group should not be zero for DeepSeekV3 routing ``` ### 📝 History of failing test https://buildkite.com/vllm/ci/builds/51738/tests?sid=019c6541-008b-4e1f-9887-96fe2c674b31&tab=output ### CC List. @mgoin @yewentao256

## 候选优化模式

- [MoE、GEMM 与 Expert Routing](../patterns/moe_gemm_routing.md) - 分数 3: ailure]: B200 Kernels ci-failure ### Name of failing test tests/kernels/moe/test_flashinfer.py::test_flashinfer_blockscale_fp8_none_expert_group ### Basic information - [ ] Flaky test - [ ] Can reproduce locally - [ ] C...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 2: B200 Kernels ci-failure ### Name of failing test tests/kernels/moe/test_flashinfer.py::test_flashinfer_blockscale_fp8_none_expert_group ### Basic information - [ ] Flaky test - [ ] Can reproduce locally - [ ] Caused by...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: [CI Failure]: B200 Kernels ci-failure ### Name of failing test tests/kernels/moe/test_flashinfer.py::test_flashinfer_blockscale_fp8_none_expert_group ### Basic information - [ ] Flaky test - [ ] Can reproduce locally -
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 2: failing test tests/kernels/moe/test_flashinfer.py::test_flashinfer_blockscale_fp8_none_expert_group ### Basic information - [ ] Flaky test - [ ] Can reproduce locally - [ ] Caused by external libraries (e.g. bug in `tra...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 2: e of failing test tests/kernels/moe/test_flashinfer.py::test_flashinfer_blockscale_fp8_none_expert_group ### Basic information - [ ] Flaky test - [ ] Can reproduce locally - [ ] Caused by external libraries (e.g. bug in...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
