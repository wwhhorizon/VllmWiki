# vllm-project/vllm#39211: FP8 MoE ep_scatter Triton illegal-address on H200 in GLM-5-FP8 prefill path

| 字段 | 值 |
| --- | --- |
| Issue | [#39211](https://github.com/vllm-project/vllm/issues/39211) |
| 状态 | closed |
| 标签 |  |
| 评论 | 0; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | activation_norm;ci_build;distributed_parallel;frontend_api;gemm_linear;hardware_porting;moe;quantization;sampling_logits |
| 子分类 |  |
| Operator 关键词 | cuda;fp8;gemm;kernel;moe;operator;sampling;triton |
| 症状 | build_error;crash |
| 根因提示 | dtype;env_dependency;race_condition;shape |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> FP8 MoE ep_scatter Triton illegal-address on H200 in GLM-5-FP8 prefill path

### Issue 正文摘录

### Summary `vllm`'s Triton `deep_gemm_utils.ep_scatter -> _fwd_kernel_ep_scatter_2` can hit `CUDA_ERROR_ILLEGAL_ADDRESS` on Hopper/H200 in the FP8 MoE prefill path used by `deepep_high_throughput`. This was first observed while serving `zai-org/GLM-5-FP8` with: - `vllm==0.19.0` - `torch==2.10.0+cu128` - `triton==3.6.0` - `deep-ep==1.2.1+73b6ea4` - `deep-gemm==2.3.0+477618c` - 2 prefill nodes + 2 decode nodes - prefill `all2all_backend=deepep_high_throughput` - expert parallel enabled - DeepGEMM enabled With `CUDA_LAUNCH_BLOCKING=1`, the first failing op is no longer generic DeepGEMM launch fallout; it is the Triton scatter kernel used by the standard DeepGEMM path: - `vllm.model_executor.layers.fused_moe.deep_gemm_moe.DeepGemmExperts.apply` - `vllm.model_executor.layers.fused_moe.deep_gemm_utils.deepgemm_moe_permute` - `vllm.model_executor.layers.fused_moe.deep_gemm_utils.ep_scatter` - `_fwd_kernel_ep_scatter_2` ### Full-server failure context In the full server run, the first failing worker was consistently prefill `NODE_RANK=1`, DP/EP rank 10. With `CUDA_LAUNCH_BLOCKING=1`, the stack tightened to: ```text File ".../deep_gemm_moe.py", line 275, in apply a1q, a1q_scale, expert_id...

## 候选优化模式

- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 7: FP8 MoE ep_scatter Triton illegal-address on H200 in GLM-5-FP8 prefill path ### Summary `vllm`'s Triton `deep_gemm_utils.ep_scatter -> _fwd_kernel_ep_scatter_2` can hit `CUDA_ERROR_ILLEGAL_ADDRESS` on Hopper/H200 in the
- [MoE、GEMM 与 Expert Routing](../patterns/moe_gemm_routing.md) - 分数 7: FP8 MoE ep_scatter Triton illegal-address on H200 in GLM-5-FP8 prefill path ### Summary `vllm`'s Triton `deep_gemm_utils.ep_scatter -> _fwd_kernel_ep_scatter_2` can hit `CUDA_ERROR_ILLEGAL_ADDRESS` on Hopper/H200 in the...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 5: g standalone script reproduces the fault outside the full server stack. Important detail: the repro is size-sensitive. - `--num-tokens 65536` passes - `--num-tokens 131072` fails with `Triton Error [CUDA]: an illegal me...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 4: FP8 MoE ep_scatter Triton illegal-address on H200 in GLM-5-FP8 prefill path ### Summary `vllm`'s Triton `deep_gemm_utils.ep_scatter -> _fwd_kernel_ep_scatter_2` can hit `CUDA_ERROR_ILLEGAL_ADDRESS` on Hopper/H200 in the...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 4: oughput` - expert parallel enabled - DeepGEMM enabled With `CUDA_LAUNCH_BLOCKING=1`, the first failing op is no longer generic DeepGEMM launch fallout; it is the Triton scatter kernel used by the standard DeepGEMM path:...

## Wiki 抽取状态

- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
