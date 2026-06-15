# vllm-project/vllm#13607: [Bug]: Error When VLLM_USE_TRITON_FLASH_ATTN=True on 2*8H100

| 字段 | 值 |
| --- | --- |
| Issue | [#13607](https://github.com/vllm-project/vllm/issues/13607) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 4; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;frontend_api;model_support |
| 子分类 | race_cond |
| Operator 关键词 | cuda;kernel |
| 症状 | build_error;crash;mismatch |
| 根因提示 | env_dependency |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Error When VLLM_USE_TRITON_FLASH_ATTN=True on 2*8H100

### Issue 正文摘录

### Your current environment 2 * 8H100 in Docker vLLM: v0.7.2 ### 🐛 Describe the bug 2 * 8H100 Node, I tried [run_cluster.sh](https://github.com/vllm-project/vllm/blob/main/examples/online_serving/run_cluster.sh) and run successfully. My run_cluster command is like below: `bash run_cluster.sh vllm/vllm-openai:v0.7.2 10.133.0.16 --head /nfs/hf_models/ -e VLLM_HOST_IP=10.133.0.16 -e NCCL_DEBUG=INFO -e NCCL_IB_HCA=mlx5_0:1,mlx5_1:1,mlx5_2:1,mlx5_3:1,mlx5_4:1,mlx5_5:1,mlx5_6:1,mlx5_8:1 -e NCCL_SOCKET_IFNAME=bond0 -e GLOO_SOCKET_IFNAME=bond0 -e NCCL_IB_GID_INDEX=3 -e NCCL_IB_CUDA_SUPPORT=1 -e NCCL_IB_DISABLE=0 -e NCCL_NVLS_ENABLE=0` and vllm serve command: `vllm serve /root/.cache/huggingface/DeepSeek-R1/ --served-model-name vllm --tensor-parallel-size 8 --pipeline-parallel-size 2 --trust-remote-code --max-model-len 32768 --distributed-executor-backend ray --enable-prefix-caching --enable-chunked-prefill --max-num-batched-tokens 32768` After set enviorment `VLLM_USE_TRITON_FLASH_ATTN=True VLLM_ATTENTION_BACKEND=FLASHINFER VLLM_USE_FLASHINFER_SAMPLER=1 `, error occurred while starting vllm serve and server will hang until timeout Log ``` (RayWorkerWrapper pid=335, ip=10.133.0.17) WARNIN...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 5: TTN=True on 2*8H100 bug;stale ### Your current environment 2 * 8H100 in Docker vLLM: v0.7.2 ### 🐛 Describe the bug 2 * 8H100 Node, I tried [run_cluster.sh](https://github.com/vllm-project/vllm/blob/main/examples/online_...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 5: [Bug]: Error When VLLM_USE_TRITON_FLASH_ATTN=True on 2*8H100 bug;stale ### Your current environment 2 * 8H100 in Docker vLLM: v0.7.2 ### 🐛 Describe the bug 2 * 8H100 Node, I tried [run_cluster.sh](https://github.com/vll...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 4: [Bug]: Error When VLLM_USE_TRITON_FLASH_ATTN=True on 2*8H100 bug;stale ### Your current environment 2 * 8H100 in Docker vLLM: v0.7.2 ### 🐛 Describe the bug 2 * 8H100 Node, I tried [run_cluster.sh](https://github.com/vll...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: ow: `bash run_cluster.sh vllm/vllm-openai:v0.7.2 10.133.0.16 --head /nfs/hf_models/ -e VLLM_HOST_IP=10.133.0.16 -e NCCL_DEBUG=INFO -e NCCL_IB_HCA=mlx5_0:1,mlx5_1:1,mlx5_2:1,mlx5_3:1,mlx5_4:1,mlx5_5:1,mlx5_6:1,mlx5_8:1 -...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 3: [Bug]: Error When VLLM_USE_TRITON_FLASH_ATTN=True on 2*8H100 bug;stale ### Your current environment 2 * 8H100 in Docker vLLM: v0.7.2 ### 🐛 Describe the bug 2 * 8H100 Node, I tried [run_cluster.sh](https://github.com/vll...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
