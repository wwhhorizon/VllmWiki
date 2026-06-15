# vllm-project/vllm#22041: [RFC]: Reduce Unit Test to Speed Up CI

| 字段 | 值 |
| --- | --- |
| Issue | [#22041](https://github.com/vllm-project/vllm/issues/22041) |
| 状态 | closed |
| 标签 | RFC;ci/build |
| 评论 | 17; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [RFC]: Reduce Unit Test to Speed Up CI

### Issue 正文摘录

### Motivation. https://github.com/vllm-project/vllm/pull/21764 Currently CI spent a lot of time in kernel unit test, even longer than 3 hours, but you know they are just kernels. So we aim to simplify some unit tests to make CI faster. ### Proposed Change. #### 1. Reduce Test Cases For example, we can reduce the amount of shapes ```bash MNK_FACTORS = [ (1, 128, 128), (1, 512, 512), (1, 128, 7168), (1, 1024, 7168), (1, 4608, 128), (1, 4608, 512), (1, 4608, 7168), (83, 128, 128), (83, 512, 512), (83, 1024, 7168), (83, 4608, 512), (83, 4608, 7168), (128, 128, 128), (128, 512, 512), (128, 1024, 7168), (128, 4608, 512), (128, 4608, 7168), (2048, 128, 128), (2048, 1024, 7168), (2048, 4608, 512), (2048, 4608, 7168), (8192, 128, 128), (8192, 512, 512), (8192, 128, 7168), (8192, 1024, 7168), (8192, 4608, 512), (8192, 4608, 7168), ] -> MNK_FACTORS = [ (1, 128, 128), (1, 1024, 7168), (1, 4608, 128), (83, 512, 512), (128, 128, 128), (128, 1024, 7168), (2048, 1024, 7168), (2048, 4608, 512), (8192, 512, 512), (8192, 4608, 512), (8192, 4608, 7168), ] ``` #### 2. Refactor test type ```bash wentao@gpu66:~/vllm-source/tests/kernels/moe$ ls __init__.py test_modular_kernel_combinations.py __pycache_...

## 候选优化模式

- [MoE、GEMM 与 Expert Routing](../patterns/moe_gemm_routing.md) - 分数 6: 2. Refactor test type ```bash wentao@gpu66:~/vllm-source/tests/kernels/moe$ ls __init__.py test_modular_kernel_combinations.py __pycache__ test_moe.py modular_kernel_tools test_moe_align_block_size.py parallel_utils.py...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 5: test_moe_permute_unpermute.py test_batched_moe.py test_mxfp4_moe.py test_block_fp8.py test_nvfp4_moe.py test_block_int8.py test_pplx_cutlass_moe.py test_count_expert_num_tokens.py test_pplx_moe.py test_cutlass_grouped_g...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 3: test_nvfp4_moe.py test_block_int8.py test_pplx_cutlass_moe.py test_count_expert_num_tokens.py test_pplx_moe.py test_cutlass_grouped_gemm.py test_rocm_aiter_topk.py test_cutlass_moe.py test_silu_mul_fp8_quant_deep_gemm.p...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: [RFC]: Reduce Unit Test to Speed Up CI RFC;ci/build ### Motivation. https://github.com/vllm-project/vllm/pull/21764 Currently CI spent a lot of time in kernel unit test, even longer than 3 hours, but you know they are j...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: rt_num_tokens.py test_pplx_moe.py test_cutlass_grouped_gemm.py test_rocm_aiter_topk.py test_cutlass_moe.py test_silu_mul_fp8_quant_deep_gemm.py test_deepep_deepgemm_moe.py test_triton_moe_ptpc_fp8.py test_deepep_moe.py...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
