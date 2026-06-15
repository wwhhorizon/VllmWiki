# vllm-project/vllm#39722: Gibberish with flashinfer_nvlink_two_sided on GB200/arm64

| 字段 | 值 |
| --- | --- |
| Issue | [#39722](https://github.com/vllm-project/vllm/issues/39722) |
| 状态 | open |
| 标签 |  |
| 评论 | 0; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> Gibberish with flashinfer_nvlink_two_sided on GB200/arm64

### Issue 正文摘录

## Summary On GB200/arm64, `Qwen/Qwen3-30B-A3B-Instruct-2507` with expert parallel enabled and `--all2all-backend flashinfer_nvlink_two_sided` produces gibberish outputs. This isn't specific to Qwen, seeing the same with GLM etc. ## Environment Hardware: - GB200 - arm64 - 4 GPUs in a single pod / node Software versions: - `vllm==0.19.0` - `torch==2.10.0+cu128` - `flashinfer-python==0.6.7.post3` - `flashinfer-cubin==0.6.7.post3` - `flashinfer-jit-cache==0.6.7.post3+cu128` - `deep-ep==1.1.0+814e508` - `deep-gemm==2.3.0+477618c` - `nixl==0.10.1` - `nixl-cu12==1.0.0` ## Repro command ```bash export HF_HUB_CACHE=/scratch/model-cache export HF_HUB_OFFLINE=1 export VLLM_ENGINE_READY_TIMEOUT_S=4200 export VLLM_HOST_IP=$POD_IP export UCX_NET_DEVICES=mlx5_2:1 export UCX_IB_GID_INDEX=3 export NVSHMEM_CUMEM_HANDLE_TYPE=FABRIC export NVSHMEM_HCA_PE_MAPPING=mlx5_2:1:4 export NVSHMEM_REMOTE_TRANSPORT=ibdevx export NVSHMEM_IB_ENABLE_IBGDA=1 export VLLM_USE_FLASHINFER_MOE_FP16=1 vllm serve \ /scratch/model-cache/models--Qwen--Qwen3-30B-A3B-Instruct-2507/snapshots/0d7cf23991f47feeb3a57ecb4c9cee8ea4a17bfe \ --served-model-name Qwen/Qwen3-30B-A3B-Instruct-2507 \ --host 0.0.0.0 \ --port 8000 \ --trust...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: Gibberish with flashinfer_nvlink_two_sided on GB200/arm64 ## Summary On GB200/arm64, `Qwen/Qwen3-30B-A3B-Instruct-2507` with expert parallel enabled and `--all2all-backend flashinfer_nvlink_two_sided` produces gibberish...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: flashinfer_nvlink_two_sided on GB200/arm64 ## Summary On GB200/arm64, `Qwen/Qwen3-30B-A3B-Instruct-2507` with expert parallel enabled and `--all2all-backend flashinfer_nvlink_two_sided` produces gibberish outputs. This...
- [MoE、GEMM 与 Expert Routing](../patterns/moe_gemm_routing.md) - 分数 3: rm64 ## Summary On GB200/arm64, `Qwen/Qwen3-30B-A3B-Instruct-2507` with expert parallel enabled and `--all2all-backend flashinfer_nvlink_two_sided` produces gibberish outputs. This isn't specific to Qwen, seeing the sam...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 2: Gibberish with flashinfer_nvlink_two_sided on GB200/arm64 ## Summary On GB200/arm64, `Qwen/Qwen3-30B-A3B-Instruct-2507` with expert parallel enabled and `--all2all-backend flashinfer_nvlink_two_sided` produces gibberish...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: Gibberish with flashinfer_nvlink_two_sided on GB200/arm64 ## Summary On GB200/arm64, `Qwen/Qwen3-30B-A3B-Instruct-2507` with expert parallel enabled and `--all2all-backend flashinfer_nvlink_two_sided` produces gibberish...

## Wiki 抽取状态

- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
