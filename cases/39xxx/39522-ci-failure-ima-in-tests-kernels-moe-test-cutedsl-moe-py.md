# vllm-project/vllm#39522: [CI Failure]: IMA in tests/kernels/moe/test_cutedsl_moe.py

| 字段 | 值 |
| --- | --- |
| Issue | [#39522](https://github.com/vllm-project/vllm/issues/39522) |
| 状态 | closed |
| 标签 | ci-failure |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [CI Failure]: IMA in tests/kernels/moe/test_cutedsl_moe.py

### Issue 正文摘录

### Name of failing test tests/kernels/moe/test_cutedsl_moe.py::test_flashinfer_cutedsl_moe_masked[1-2-128-256] ### Basic information - [x] Flaky test - [ ] Can reproduce locally - [ ] Caused by external libraries (e.g. bug in `transformers`) ### 🧪 Describe the failing test I'm seeing this test fail on the 04/09/25 nightly (https://buildkite.com/vllm/ci/builds/60760). It appears to be running in both the `Kernels (B200)` and `Kernels Fp4 MoE Test (B200)` test groups. I'm not able to reproduce this test locally on a B200 machine. Relevant log snippet ``` [06:41:07.520334] coredump: Detected an exception of type CUDBG_EXCEPTION_WARP_ILLEGAL_ADDRESS (14) -- [06:41:07.520340] coredump: - Device: 0 [06:41:07.520342] coredump: - SM: 142 [06:41:07.520345] coredump: - Warp: 0 [06:41:07.520347] coredump: - PC 0x7bdd7b5ef520 [06:41:07.520556] coredump: Stack trace (lane masks: active 0xFFFFFFFF, valid 0xFFFFFFFF): [06:41:07.520563] coredump: #0 0x7bdd7b5efc70 kernel_cutlass_kernel_flashinfergemmkernelsgrouped_gemm_masked_blackwellSm100BlockScaledPersistentDenseGemmKernel_object_at__TiledMMA_ThrLayoutVMNK11110000_PermutationMNK____MMAAtom_ThrID_0 ``` ### 📝 History of failing test The first i...

## 候选优化模式

- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: om/vllm/ci/builds/60760). It appears to be running in both the `Kernels (B200)` and `Kernels Fp4 MoE Test (B200)` test groups. I'm not able to reproduce this test locally on a B200 machine. Relevant log snippet ``` [06:...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 2: re ### Name of failing test tests/kernels/moe/test_cutedsl_moe.py::test_flashinfer_cutedsl_moe_masked[1-2-128-256] ### Basic information - [x] Flaky test - [ ] Can reproduce locally - [ ] Caused by external libraries (e...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: [CI Failure]: IMA in tests/kernels/moe/test_cutedsl_moe.py ci-failure ### Name of failing test tests/kernels/moe/test_cutedsl_moe.py::test_flashinfer_cutedsl_moe_masked[1-2-128-256] ### Basic information - [x] Flaky te
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 2: 760). It appears to be running in both the `Kernels (B200)` and `Kernels Fp4 MoE Test (B200)` test groups. I'm not able to reproduce this test locally on a B200 machine. Relevant log snippet ``` [06:41:07.520334] coredu...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 2: el_cutlass_kernel_flashinfergemmkernelsgrouped_gemm_masked_blackwellSm100BlockScaledPersistentDenseGemmKernel_object_at__TiledMMA_ThrLayoutVMNK11110000_PermutationMNK____MMAAtom_ThrID_0 ``` ### 📝 History of failing test...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
