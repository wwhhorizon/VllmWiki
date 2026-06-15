# vllm-project/vllm#15928: [Bug]: Issue when serving DeepSeek V3 with vLLM v1 in MI308

| 字段 | 值 |
| --- | --- |
| Issue | [#15928](https://github.com/vllm-project/vllm/issues/15928) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | attention_kv_cache;ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;speculative_decoding |
| 子分类 | kernel_eff |
| Operator 关键词 | cache;cuda;operator;triton |
| 症状 | build_error;crash |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Issue when serving DeepSeek V3 with vLLM v1 in MI308

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug In branch main, from commit e6e3c55ef28f30bca855399419c61bb70af03db2, while serving DeepSeek V3 with vLLM v1, ``` export NCCL_IB_PCI_RELAXED_ORDERING=1 export NCCL_NET_GDR_LEVEL=3 export UCX_IB_PCI_RELAXED_ORDERING=on export UCX_TLS=self,sm,rc_x export NCCL_IB_HCA=mlx5_0:1 export NCCL_MIN_NCHANNELS=112 # vLLM env var export VLLM_FP8_PADDING=0 export VLLM_USE_TRITON_FLASH_ATTN=0 export VLLM_MLA_DISABLE=1 export VLLM_USE_ROCM_FP8_FLASH_ATTN=1 export VLLM_ALLOW_LONG_MAX_MODEL_LEN=0 export VLLM_ROCM_USE_AITER=0 export VLLM_ROCM_USE_AITER_LINEAR=0 export VLLM_ROCM_USE_AITER_MOE=0 export VLLM_ROCM_USE_AITER_FP8_BLOCK_SCALED_MOE=0 export VLLM_ROCM_USE_AITER_RMSNORM=0 export VLLM_ROCM_USE_AITER_RMSNORM_DYNAMICQUANT=0 export VLLM_ROCM_USE_AITER_PAGED_ATTN=0 export VLLM_ROCM_USE_AITER_W8A8_BLOCK_GEMM=0 export VLLM_ROCM_FP8_PADDING=1 export VLLM_USE_V1=1 vllm serve /workspace/models/DeepSeek_v3 \ --trust-remote-code \ --max-model-len=32768 \ --max-num-batched-token=32768 \ --max-num-seqs=1024 \ --tensor-parallel-size=8 \ --gpu-memory-utilization=0.90 \ --disable-log-requests ``` I encountered the following error: ``` ... [1;36m(VllmWorker...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: bb70af03db2, while serving DeepSeek V3 with vLLM v1, ``` export NCCL_IB_PCI_RELAXED_ORDERING=1 export NCCL_NET_GDR_LEVEL=3 export UCX_IB_PCI_RELAXED_ORDERING=on export UCX_TLS=self,sm,rc_x export NCCL_IB_HCA=mlx5_0:1 ex...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 4: ET_GDR_LEVEL=3 export UCX_IB_PCI_RELAXED_ORDERING=on export UCX_TLS=self,sm,rc_x export NCCL_IB_HCA=mlx5_0:1 export NCCL_MIN_NCHANNELS=112 # vLLM env var export VLLM_FP8_PADDING=0 export VLLM_USE_TRITON_FLASH_ATTN=0 exp...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 3: _NCHANNELS=112 # vLLM env var export VLLM_FP8_PADDING=0 export VLLM_USE_TRITON_FLASH_ATTN=0 export VLLM_MLA_DISABLE=1 export VLLM_USE_ROCM_FP8_FLASH_ATTN=1 export VLLM_ALLOW_LONG_MAX_MODEL_LEN=0 export VLLM_ROCM_USE_AIT...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 3: B_HCA=mlx5_0:1 export NCCL_MIN_NCHANNELS=112 # vLLM env var export VLLM_FP8_PADDING=0 export VLLM_USE_TRITON_FLASH_ATTN=0 export VLLM_MLA_DISABLE=1 export VLLM_USE_ROCM_FP8_FLASH_ATTN=1 export VLLM_ALLOW_LONG_MAX_MODEL_...
- [MoE、GEMM 与 Expert Routing](../patterns/moe_gemm_routing.md) - 分数 3: E_AITER=0 export VLLM_ROCM_USE_AITER_LINEAR=0 export VLLM_ROCM_USE_AITER_MOE=0 export VLLM_ROCM_USE_AITER_FP8_BLOCK_SCALED_MOE=0 export VLLM_ROCM_USE_AITER_RMSNORM=0 export VLLM_ROCM_USE_AITER_RMSNORM_DYNAMICQUANT=0 exp...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
