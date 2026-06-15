# vllm-project/vllm#2442: Bad performance when using tp = 4 on V100

| 字段 | 值 |
| --- | --- |
| Issue | [#2442](https://github.com/vllm-project/vllm/issues/2442) |
| 状态 | closed |
| 标签 |  |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | distributed_parallel;frontend_api;gemm_linear |
| 子分类 |  |
| Operator 关键词 | cuda;kernel |
| 症状 |  |
| 根因提示 |  |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> Bad performance when using tp = 4 on V100

### Issue 正文摘录

Hi I'm benchmarking vLLM on 4 * V100, and I see the performance is no better when using multiple gpus. Seems the nccl takes most of the time. Have you ever seen this issue? ``` ==54415== Profiling result: Type Time(%) Time Calls Avg Min Max Name GPU activities: 84.32% 1.7242ms 2 862.08us 613.95us 1.1102ms ncclKernel_AllReduce_RING_LL_Sum_half(ncclDevComm*, unsigned long, ncclWork*) 10.27% 210.01us 3 70.004us 29.151us 118.18us void cutlass::Kernel (cutlass_70_wmma_tensorop_f16_s161616gemm_f16_16 x16_64x2_tn_align8Params) 3.11% 63.648us 1 63.648us 63.648us 63.648us void cutlass::Kernel (cutlass_70_wmma_tensorop_s161616gemm_f16_16x16_64x2 _tn_align8Params) 0.60% 12.288us 2 6.1440us 6.0480us 6.2400us void vllm::rms_norm_kernel (c10::Half*, vllm::rms_norm_kernel const *, vllm::rms_norm_kernel const , fl oat, int, int) 0.41% 8.3840us 1 8.3840us 8.3840us 8.3840us void vllm::paged_attention_v1_kernel (unsigned short*, vllm::paged_attention_v1_kernel const *, vllm::paged_attention_v1_kernel const , vllm::paged_attention_v1_kernel const , int const *, float, int const , int const , int, float const *, int, int, int) 0.36% 7.3600us 2 3.6800us 3.2320us 4.1280us void at::native::vectorized_ele...

## 现有链接修复摘要

#39242 [ROCm] Add MLA dual RMS norm fusion (Q, KV) pass for DeepSeek/Kimi-K2 | #40386 [ROCm] Hotfix: guard MLA dual RMS norm fusion against older AITer versions

## 候选优化模式

- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 2: 10.27% 210.01us 3 70.004us 29.151us 118.18us void cutlass::Kernel (cutlass_70_wmma_tensorop_f16_s161616gemm_f16_16 x16_64x2_tn_align8Params) 3.11% 63.648us 1 63.648us 63.648us 63.648us void cutlass::Kernel (cutlass_70_w...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: ed_elementwise_kernel , at::detail::Array >(int, c10 ::Half, at::native::CUDAFunctor_add ) 0.23% 4.8000us 1 4.8000us 4.8000us 4.8000us void vllm::rotary_embedding_kernel (long const *, c10::Half*, c10::Half, long const...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 2: Bad performance when using tp = 4 on V100 Hi I'm benchmarking vLLM on 4 * V100, and I see the performance is no better when using multiple gpus. Seems the nccl takes most of the time. Have you ever seen this issue? ```...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: #40386 [ROCm] Hotfix: guard MLA dual RMS norm fusion against older AITer versions Hi I'm benchmarking vLLM on 4 * V100, and I see the performance is no better when using multiple gpus.
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 1: 22.398us 8 2.7990us 716ns 12.717us cudaOccupancyMaxActiveBlocksPerMultiprocessorWithFlags 3.22% 16.920us 17 995ns 233ns 10.630us cudaGetLastError 2.99% 15.737us 16 983ns 636ns 1.9210us cudaSetDevice

## 关联 PR 证据

| PR | 链接类型 | 置信度 | PR 标题 | 证据 |
| --- | --- | ---: | --- | --- |
| [#39242](https://github.com/vllm-project/vllm/pull/39242) | mentioned | 0.6 | [ROCm] Add MLA dual RMS norm fusion (Q, KV) pass for DeepSeek/Kimi-K2 | table above) ## Related - AITer `fused_qk_rmsnorm` HIP kernel: [ROCm/aiter#2442](https://github.com/ROCm/aiter/pull/2442) |
| [#40386](https://github.com/vllm-project/vllm/pull/40386) | mentioned | 0.6 | [ROCm] Hotfix: guard MLA dual RMS norm fusion against older AITer versions | k_norm_rope_cache_quant.fused_qk_rmsnorm, which was added in AITer PR #2442. The upstream Dockerfile.rocm_base pins aiter v0.1.10.post3 which does not include this kernel, causing… |

## Wiki 抽取状态

- 后续迭代应在可用时读取完整讨论评论。
