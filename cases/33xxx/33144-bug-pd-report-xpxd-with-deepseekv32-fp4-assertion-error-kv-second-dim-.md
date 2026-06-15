# vllm-project/vllm#33144: [Bug]: PD report xpxd with deepseekv32 fp4  Assertion error kv.second.dim()==1

| 字段 | 值 |
| --- | --- |
| Issue | [#33144](https://github.com/vllm-project/vllm/issues/33144) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | attention_kv_cache;ci_build;distributed_parallel;frontend_api;gemm_linear;hardware_porting;model_support;quantization;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | attention;cuda;operator;sampling;triton |
| 症状 | build_error;crash;nan_inf |
| 根因提示 | dtype;env_dependency;shape |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: PD report xpxd with deepseekv32 fp4  Assertion error kv.second.dim()==1

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug ```bash # prefill export PYTHONHASHSEED=0 export VLLM_USE_FLASHINFER_MOE_FP4=1 export VLLM_TARGET_DEVICE=cuda export UCX_NET_DEVICES=mlx5_bond_0:1 export VLLM_NIXL_SIDE_CHANNEL_HOST=10.13.21.21 export CUDA_VISIBLE_DEVICES=0,1,2,3 export VLLM_NIXL_SIDE_CHANNEL_PORT=5600 export VLLM_NIXL_SIDE_CHANNEL_HOST=10.13.21.21 vllm serve /mnt/nfs/models/nvidia/DeepSeek-V3.2-NVFP4 --served-model-name deepseek-ai/DeepSeek-V3.2-NVFP4 \ --tensor-parallel-size 2 --data-parallel-size 2 \ --no-enable-prefix-caching \ --max-num-batched-tokens 20480 --tokenizer-mode deepseek_v32 --kv-transfer-config '{"kv_connector":"NixlConnector","kv_role":"kv_both","kv_load_failure_policy":"fail","kv_buffer_device":"cuda"}' --port 8100 # decode export VLLM_NIXL_SIDE_CHANNEL_HOST=10.13.21.22 export VLLM_NIXL_SIDE_CHANNEL_PORT=5601 export VLLM_USE_FLASHINFER_MOE_FP4=1 export CUDA_VISIBLE_DEVICES=2,3 export VLLM_TARGET_DEVICE=cuda export UCX_NET_DEVICES=mlx5_bond_0:1 vllm serve /mnt/nfs/models/nvidia/DeepSeek-V3.2-NVFP4 --served-model-name deepseek-ai/DeepSeek-V3.2-NVFP4 \ --tensor-parallel-size 2 --no-enable-prefix-caching \ --max-num-batched-tokens 20480 --kv-trans...

## 候选优化模式

- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 5: [Bug]: PD report xpxd with deepseekv32 fp4 Assertion error kv.second.dim()==1 bug ### Your current environment ### 🐛 Describe the bug ```bash # prefill export PYTHONHASHSEED=0 export VLLM_USE_FLASHINFER_MOE_FP4=1 export...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: 647864) ERROR 01-27 04:48:51 [multiproc_executor.py:822] return TorchCompileWithNoGuardsWrapper.__call__(self, *args, **kwargs) # type: ignore[arg-type] (Worker_DP0_TP0 pid=1647863) ERROR 01-27 04:48:51 [multiproc_execu...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 4: 1 bug ### Your current environment ### 🐛 Describe the bug ```bash # prefill export PYTHONHASHSEED=0 export VLLM_USE_FLASHINFER_MOE_FP4=1 export VLLM_TARGET_DEVICE=cuda export UCX_NET_DEVICES=mlx5_bond_0:1 export VLLM_NI...
- [MoE、GEMM 与 Expert Routing](../patterns/moe_gemm_routing.md) - 分数 3: ug ```bash # prefill export PYTHONHASHSEED=0 export VLLM_USE_FLASHINFER_MOE_FP4=1 export VLLM_TARGET_DEVICE=cuda export UCX_NET_DEVICES=mlx5_bond_0:1 export VLLM_NIXL_SIDE_CHANNEL_HOST=10.13.21.21 export CUDA_VISIBLE_DE...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 2: cribe the bug ```bash # prefill export PYTHONHASHSEED=0 export VLLM_USE_FLASHINFER_MOE_FP4=1 export VLLM_TARGET_DEVICE=cuda export UCX_NET_DEVICES=mlx5_bond_0:1 export VLLM_NIXL_SIDE_CHANNEL_HOST=10.13.21.21 export CUDA...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
