# vllm-project/vllm#33539: [Bug]: When using NIXL for PD separation on GB series cards, the MNNVL protocol cannot be used

| 字段 | 值 |
| --- | --- |
| Issue | [#33539](https://github.com/vllm-project/vllm/issues/33539) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 0; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | distributed_parallel;frontend_api;model_support;moe |
| 子分类 | kernel_eff |
| Operator 关键词 | cuda;moe |
| 症状 |  |
| 根因提示 | env_dependency |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: When using NIXL for PD separation on GB series cards, the MNNVL protocol cannot be used

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug The startup command for VLLM is as follows: ``` # Prefill - Tray 0 export VLLM_NIXL_SIDE_CHANNEL_HOST=10.0.8.10 UCX_CUDA_IPC_ENABLE_MNNVL=y UCX_PROTO_INFO=y vllm serve --gpu-memory-utilization=0.85 --tokenizer-mode=deepseek_v32 --no-enable-expert-parallel --model /home/ubuntu/DeepSeek-V3.2 --kv-transfer-config '{"kv_connector":"NixlConnector","kv_role":"kv_both","kv_buffer_device":"cuda"}' -tp 2 -dp 4 -dpl 2 -dpa 10.0.8.10 -dpr 0 # Prefill - Tray 1 export VLLM_NIXL_SIDE_CHANNEL_HOST=10.0.8.11 UCX_CUDA_IPC_ENABLE_MNNVL=y UCX_PROTO_INFO=y vllm serve --gpu-memory-utilization=0.85 --tokenizer-mode=deepseek_v32 --no-enable-expert-parallel --model /home/ubuntu/DeepSeek-V3.2 --kv-transfer-config '{"kv_connector":"NixlConnector","kv_role":"kv_both","kv_buffer_device":"cuda"}' -tp 2 -dp 4 -dpl 2 -dpa 10.0.8.10 -dpr 2 # Decode - Tray 2 export VLLM_NIXL_SIDE_CHANNEL_HOST=10.0.8.14 UCX_CUDA_IPC_ENABLE_MNNVL=y UCX_PROTO_INFO=y vllm serve --gpu-memory-utilization=0.85 --tokenizer-mode=deepseek_v32 --no-enable-expert-parallel --model /home/ubuntu/DeepSeek-V3.2 --kv-transfer-config '{"kv_connector":"NixlConnector","kv_role":"kv_both","kv_buffer_...

## 现有链接修复摘要

#33558 [Core] Add option to allocate CUDA Fabric memory (required for MNNVL)

## 候选优化模式

- [MoE、GEMM 与 Expert Routing](../patterns/moe_gemm_routing.md) - 分数 3: --gpu-memory-utilization=0.85 --tokenizer-mode=deepseek_v32 --no-enable-expert-parallel --model /home/ubuntu/DeepSeek-V3.2 --kv-transfer-config '{"kv_connector":"NixlConnector","kv_role":"kv_both","kv_buffer_device":"cu...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: ``` # Prefill - Tray 0 export VLLM_NIXL_SIDE_CHANNEL_HOST=10.0.8.10 UCX_CUDA_IPC_ENABLE_MNNVL=y UCX_PROTO_INFO=y vllm serve --gpu-memory-utilization=0.85 --tokenizer-mode=deepseek_v32 --no-enable-expert-parallel --model...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: ization=0.85 --tokenizer-mode=deepseek_v32 --no-enable-expert-parallel --model /home/ubuntu/DeepSeek-V3.2 --kv-transfer-config '{"kv_connector":"NixlConnector","kv_role":"kv_both","kv_buffer_device":"cuda"}' -tp 2 -dp 4...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: ## 🐛 Describe the bug The startup command for VLLM is as follows: ``` # Prefill - Tray 0 export VLLM_NIXL_SIDE_CHANNEL_HOST=10.0.8.10 UCX_CUDA_IPC_ENABLE_MNNVL=y UCX_PROTO_INFO=y vllm serve --gpu-memory-utilization=0.85...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: ormance distributed_parallel;frontend_api;model_support;moe cuda;moe env_dependency #33558 [Core] Add option to allocate CUDA Fabric memory (required for MNNVL) Your current environment

## 关联 PR 证据

| PR | 链接类型 | 置信度 | PR 标题 | 证据 |
| --- | --- | ---: | --- | --- |
| [#33558](https://github.com/vllm-project/vllm/pull/33558) | closes_keyword | 0.95 | [Core] Add option to allocate CUDA Fabric memory (required for MNNVL) | Fixes vLLM #33539. Similar to PR #33540. Originally discussed in https://github.com/ai-dynamo/nixl/issues/1240. ## Test Plan Basic run as done in #33540. Need to run with `VLLM_CU |

## Wiki 抽取状态

- 后续迭代应在可用时读取完整讨论评论。
