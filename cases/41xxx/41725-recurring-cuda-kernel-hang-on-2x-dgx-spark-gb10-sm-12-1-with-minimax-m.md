# vllm-project/vllm#41725: Recurring CUDA kernel hang on 2x DGX Spark (GB10, sm_12.1) with MiniMax-M2.7-NVFP4, TP=2 across 2 nodes

| 字段 | 值 |
| --- | --- |
| Issue | [#41725](https://github.com/vllm-project/vllm/issues/41725) |
| 状态 | open |
| 标签 |  |
| 评论 | 4; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | distributed_parallel;frontend_api;gemm_linear;hardware_porting;model_support;moe;quantization |
| 子分类 | kernel_eff |
| Operator 关键词 | cuda;kernel;moe;quantization |
| 症状 | build_error;crash |
| 根因提示 | memory_layout |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> Recurring CUDA kernel hang on 2x DGX Spark (GB10, sm_12.1) with MiniMax-M2.7-NVFP4, TP=2 across 2 nodes

### Issue 正文摘录

## Environment - **vLLM version**: 0.19.1 - **Model**: nvidia/MiniMax-M2.7-NVFP4 - **Hardware**: 2x NVIDIA DGX Spark, each with 1x GB10 Superchip (sm_12.1 / CUDA capability 12.1) - **Interconnect**: C2C link (169.254.x.x/16), 900 GB/s, RoCE over enp1s0f0np0 / rocep1s0f0 - **CUDA**: 13.0 - **NCCL**: 2.28.9+cuda13.0 - **PyTorch**: 2.9.0+cu130 - **OS**: Ubuntu (kernel 6.17.0-nvidia) ## Launch configuration ```bash export NCCL_IB_HCA=rocep1s0f0 export NCCL_SOCKET_IFNAME=enp1s0f0np0 export NCCL_P2P_DISABLE=1 export NCCL_NET_GDR_LEVEL=5 export NCCL_DEBUG=WARN export TORCH_NCCL_HEARTBEAT_TIMEOUT_SEC=120 export VLLM_NVFP4_GEMM_BACKEND=flashinfer-cutlass export VLLM_USE_FLASHINFER_MOE_FP4=1 vllm serve nvidia/MiniMax-M2.7-NVFP4 \ --trust-remote-code \ --compilation-config '{"mode":3,"pass_config":{"fuse_minimax_qk_norm":true}}' \ -cc.pass_config.fuse_allreduce_rms=False \ --tensor-parallel-size 2 \ --nnodes 2 \ --node-rank 0 \ # (node-rank 1 on second node, with --headless) --master-addr 169.254.205.76 \ --tool-call-parser minimax_m2 \ --enable-auto-tool-choice \ --gpu-memory-utilization 0.80 \ --enforce-eager \ --moe-backend marlin \ --port 8888 \ --reasoning-parser minimax_m2 ``` ## Sympt...

## 候选优化模式

- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 5: Recurring CUDA kernel hang on 2x DGX Spark (GB10, sm_12.1) with MiniMax-M2.7-NVFP4, TP=2 across 2 nodes ## Environment - **vLLM version**: 0.19.1 - **Model**: nvidia/MiniMax-M2.7-NVFP4 - **Hardware**: 2x NVIDIA DGX Spar...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 3: =WARN export TORCH_NCCL_HEARTBEAT_TIMEOUT_SEC=120 export VLLM_NVFP4_GEMM_BACKEND=flashinfer-cutlass export VLLM_USE_FLASHINFER_MOE_FP4=1 vllm serve nvidia/MiniMax-M2.7-NVFP4 \ --trust-remote-code \ --compilation-config...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: 1) with MiniMax-M2.7-NVFP4, TP=2 across 2 nodes ## Environment - **vLLM version**: 0.19.1 - **Model**: nvidia/MiniMax-M2.7-NVFP4 - **Hardware**: 2x NVIDIA DGX Spark, each with 1x GB10 Superchip (sm_12.1 / CUDA capabilit...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 3: rring CUDA kernel hang on 2x DGX Spark (GB10, sm_12.1) with MiniMax-M2.7-NVFP4, TP=2 across 2 nodes ## Environment - **vLLM version**: 0.19.1 - **Model**: nvidia/MiniMax-M2.7-NVFP4 - **Hardware**: 2x NVIDIA DGX Spark, e...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 3: {"fuse_minimax_qk_norm":true}}' \ -cc.pass_config.fuse_allreduce_rms=False \ --tensor-parallel-size 2 \ --nnodes 2 \ --node-rank 0 \ # (node-rank 1 on second node, with --headless) --master-addr 169.254.205.76 \ --tool-...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
