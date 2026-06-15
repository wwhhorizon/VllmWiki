# vllm-project/vllm#28084: [Feature]: Improve MoE pre-amble (router, quantization, etc.) perf for DSv3.1

| 字段 | 值 |
| --- | --- |
| Issue | [#28084](https://github.com/vllm-project/vllm/issues/28084) |
| 状态 | closed |
| 标签 | feature request;stale |
| 评论 | 6; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | distributed_parallel;frontend_api;moe;quantization |
| 子分类 |  |
| Operator 关键词 | kernel;moe;quantization |
| 症状 |  |
| 根因提示 |  |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Feature]: Improve MoE pre-amble (router, quantization, etc.) perf for DSv3.1

### Issue 正文摘录

### 🚀 The feature, motivation and pitch For low concurrency cases, the kernels running after the all reduce and before the first fused_moe kernel, take a similar amount of time as the first fused_moe kernel. These kernels all run with very few CTAs in the low concurrency case utilizing only a small fraction of the GPU, and the number of kernels means we lose a lot of time to inter-kernel spacing as well. For concurrency 4 on H200 with EP8: Even when running with shared experts in a second stream, the stream running MoE sees: ``` trtion_red_fused__to_copy_add_mean_moe_forward_shared_mul_pow_rsqrt_0: 3.6us nvjet_tst_64x8_64x16_4x1_v_bz_splitK_TNT: 4.6us splitKreduce_kernel: 2.3us triton_poi_fused__to_copy_add_sigmoid_unsqueeze_0: 1.9us topk_with_k2_kernel: 1.8us group_idx_and_topk_idx_kernel: 7.3us triton_poi_fused__to_copy_0: 1.0us per_token_group_quant_8bit_kernel: 2.2us moe_align_block_size_kernel: 3.5us moe_count_and_sort_expert_token_kenrel: 1.1us unrolled_elemetwise_kernel: 1.6us index_elementwise_kernel: 2.5us Total with inter-kernel spacing: 39.8us fused_moe: 40.1us ``` And on the shared expert stream: ``` memcpy DtoD: 1.2us per_token_group_quant_8bit_kernel: 2.2us vectorize...

## 候选优化模式

- [MoE、GEMM 与 Expert Routing](../patterns/moe_gemm_routing.md) - 分数 5: [Feature]: Improve MoE pre-amble (router, quantization, etc.) perf for DSv3.1 feature request;stale ### 🚀 The feature, motivation and pitch For low concurrency cases, the kernels running after the all reduce and before...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 2: jet_tst_64x8_64x16_4x1_v_bz_splitK_TNT: 4.6us splitKreduce_kernel: 2.3us triton_poi_fused__to_copy_add_sigmoid_unsqueeze_0: 1.9us topk_with_k2_kernel: 1.8us group_idx_and_topk_idx_kernel: 7.3us triton_poi_fused__to_copy...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 2: [Feature]: Improve MoE pre-amble (router, quantization, etc.) perf for DSv3.1 feature request;stale ### 🚀 The feature, motivation and pitch For low concurrency cases, the kernels running after the all reduce and before...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: all run with very few CTAs in the low concurrency case utilizing only a small fraction of the GPU, and the number of kernels means we lose a lot of time to inter-kernel spacing as well. For concurrency 4 on H200 with EP...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: prove MoE pre-amble (router, quantization, etc.) perf for DSv3.1 feature request;stale ### 🚀 The feature, motivation and pitch For low concurrency cases, the kernels running after the all reduce and before the first fus...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
