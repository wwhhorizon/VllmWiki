# vllm-project/vllm#29147: [Bug]: vllm0.11.1 Triton Error [CUDA] misaligned address in DeepGEMM (fp8_m_grouped_gemm) when running Qwen-MoE with TorchCompile on H200

| 字段 | 值 |
| --- | --- |
| Issue | [#29147](https://github.com/vllm-project/vllm/issues/29147) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 6; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;frontend_api;gemm_linear;hardware_porting;model_support;moe;quantization;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cuda;fp8;moe;operator;sampling;triton |
| 症状 | build_error;nan_inf |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: vllm0.11.1 Triton Error [CUDA] misaligned address in DeepGEMM (fp8_m_grouped_gemm) when running Qwen-MoE with TorchCompile on H200

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug ## reproduce 0. docker image https://hub.docker.com/layers/vllm/vllm-openai/v0.11.1/images/sha256-e4896bdb93ffab61032f8992624928c198363b5085a0c9ac2af8a7f992de89a2 1. start the ray on 4 machines ``` ray start --head --port 6398 #machine 1 ray start --address "xxx:6398" #machine 2,3,4 ``` 2. start vllm on machine 1 - same issue when unset VLLM_USE_DEEP_GEMM or --enforce-eager ``` VLLM_USE_DEEP_GEMM=0 VLLM_ALLOW_LONG_MAX_MODEL_LEN=1 VLLM_MOE_ROUTING_SIMULATION_STRATEGY="uniform_random" UCX_NET_DEVICES="mlx5_0:1,mlx5_1:1,mlx5_2:1,mlx5_3:1,mlx5_4:1,mlx5_5:1,mlx5_6:1,mlx5_7:1" GLOO_SOCKET_IFNAME=bond0 NCCL_SOCKET_IFNAME=bond0 vllm serve "/models/models--Qwen--Qwen3-235B-A22B-Instruct-2507-FP8/snapshots/ba82a1060073fa0ecdc70d7b1922ec071f60cf3e" --max-model-len 435000 -dp 32 --data-parallel-size-local 8 --data-parallel-backend=ray --max-num-seqs 64 --enable-expert-parallel --no-enable-prefix-caching --distributed-executor-backend ray --kv-transfer-config '{ "kv_connector": "DecodeBenchConnector", "kv_role": "kv_both", "kv_connector_extra_config": { "fill_mean": 0.015, "fill_std": 0.0 } }' --load-format dummy --all2all-backend deepep_low_...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 5: address in DeepGEMM (fp8_m_grouped_gemm) when running Qwen-MoE with TorchCompile on H200 bug ### Your current environment ### 🐛 Describe the bug ## reproduce 0. docker image https://hub.docker.com/layers/vllm/vllm-opena...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 4: [Bug]: vllm0.11.1 Triton Error [CUDA] misaligned address in DeepGEMM (fp8_m_grouped_gemm) when running Qwen-MoE with TorchCompile on H200 bug ### Your current environment ### 🐛 Describe the bug ## reproduce 0. docker im...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: [CUDA] misaligned address in DeepGEMM (fp8_m_grouped_gemm) when running Qwen-MoE with TorchCompile on H200 bug ### Your current environment ### 🐛 Describe the bug ## reproduce 0. docker image https://hub.docker.com/laye...
- [MoE、GEMM 与 Expert Routing](../patterns/moe_gemm_routing.md) - 分数 4: [Bug]: vllm0.11.1 Triton Error [CUDA] misaligned address in DeepGEMM (fp8_m_grouped_gemm) when running Qwen-MoE with TorchCompile on H200 bug ### Your current environment ### 🐛 Describe the bug ## reproduce 0. docker im...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 3: [Bug]: vllm0.11.1 Triton Error [CUDA] misaligned address in DeepGEMM (fp8_m_grouped_gemm) when running Qwen-MoE with TorchCompile on H200 bug ### Your current environment ### 🐛 Describe the bug ## reproduce 0. docker im...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
