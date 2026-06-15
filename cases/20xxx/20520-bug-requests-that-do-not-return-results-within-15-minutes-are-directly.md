# vllm-project/vllm#20520: [Bug]: Requests that do not return results within 15 minutes are directly aborted, and then the request will be added by vllm again...

| 字段 | 值 |
| --- | --- |
| Issue | [#20520](https://github.com/vllm-project/vllm/issues/20520) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 7; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | attention_kv_cache;ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;sampling_logits;scheduler_memory;speculative_decoding |
| 子分类 | throughput |
| Operator 关键词 | cache;cuda;operator;sampling;triton |
| 症状 | build_error;slowdown |
| 根因提示 | env_dependency;shape |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Requests that do not return results within 15 minutes are directly aborted, and then the request will be added by vllm again...

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug I deployed DeepSeek-R1-0528 with 2*8 H20 (96G). When the model generates answers, it is found that requests that do not return results within 15 minutes will be automatically terminated and then re-run by VLLM. Then it will be repeated until the request times out. I have tried export VLLM_ENGINE_ITERATION_TIMEOUT_S=4200 export VLLM_EXECUTE_MODEL_TIMEOUT_SECONDS=4200, and openai-timeout=5000, but these settings **did not work**. How to avoid this problem of repeated requests? How can I get responses to requests that take more than 15 minutes to generate? Or is there something wrong with my deployment or request? ``` # deploy_sh export GLOO_SOCKET_IFNAME=bond1 export NCCL_SOCKET_IFNAME=bond1 export NCCL_IB_GID_INDEX=3 export NCCL_IB_SL=3 export NCCL_CHECK_DISABLE=1 export NCCL_P2P_DISABLE=0 export NCCL_IB_DISABLE=0 export NCCL_LL_THRESHOLD=16384 export NCCL_IB_CUDA_SUPPORT=1 export NCCL_SOCKET_IFNAME=bond1 export UCX_NET_DEVICES=bond1 export NCCL_IB_HCA=mlx5_bond_1,mlx5_bond_5,mlx5_bond_3,mlx5_bond_7,mlx5_bond_4,mlx5_bond_8,mlx5_bond_2,mlx5_bond_6 export NCCL_COLLNET_ENABLE=0 export SHARP_COLL_ENABLE_SAT=0 export NCCL_NET_GDR_LEVEL...

## 候选优化模式

- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 5: [Bug]: Requests that do not return results within 15 minutes are directly aborted, and then the request will be added by vllm again... bug;stale ### Your current environment ### 🐛 Describe the bug I deployed DeepSeek-R1...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: tokens=20000, min_tokens=0, logprobs=None, prompt_logprobs=None, skip_special_tokens=True, spaces_between_special_tokens=True, truncate_prompt_tokens=None, guided_decoding=None, extra_args=None), prompt_token_ids: None,...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: 0 export NCCL_IB_DISABLE=0 export NCCL_LL_THRESHOLD=16384 export NCCL_IB_CUDA_SUPPORT=1 export NCCL_SOCKET_IFNAME=bond1 export UCX_NET_DEVICES=bond1 export NCCL_IB_HCA=mlx5_bond_1,mlx5_bond_5,mlx5_bond_3,mlx5_bond_7,mlx...
- [KV Cache 容量、压缩与 Offload](../patterns/kv_cache_capacity_offload.md) - 分数 2: neration throughput: 1.0 tokens/s, Running: 1 reqs, Waiting: 0 reqs, GPU KV cache usage: 0.0%, Prefix cache hit rate: 0.0% INFO 07-06 16:08:23 [loggers.py:118] Engine 000: Avg prompt throughput: 0.0 tokens/s, Avg genera...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: scribe the bug I deployed DeepSeek-R1-0528 with 2*8 H20 (96G). When the model generates answers, it is found that requests that do not return results within 15 minutes will be automatically terminated and then re-run by...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
