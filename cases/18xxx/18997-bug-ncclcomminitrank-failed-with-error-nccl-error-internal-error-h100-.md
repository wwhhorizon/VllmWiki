# vllm-project/vllm#18997: [Bug]: ncclCommInitRank failed with error: NCCL error: internal error (H100, KubeRay, DeepSeek, TP=8, PP=2)

| 字段 | 值 |
| --- | --- |
| Issue | [#18997](https://github.com/vllm-project/vllm/issues/18997) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;sampling_logits;speculative_decoding |
| 子分类 | race_cond |
| Operator 关键词 | cuda;kernel;operator;sampling;triton |
| 症状 | build_error;crash;nan_inf |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: ncclCommInitRank failed with error: NCCL error: internal error (H100, KubeRay, DeepSeek, TP=8, PP=2)

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug Hi vLLM team; cross posting an [issue](https://github.com/NVIDIA/nccl/issues/1726) from NCCL here. I'm attempting to run a vLLM server using KubeRay on AWS EKS and am encountering the error message below. This configuration (DeepSeek-V2-LIte, TP=8, PP=2) works on two 8xA100 nodes, but fails with the same configuration on two 8xH100 nodes. I'm able to run the model with different configurations on H100s, e.g. TP=2, PP=2. Shared memory (/dev/shm) is 20GB for the cluster. Tried also setting `NCCL_SOCKET_IFNAME` to no avail. The only differences I'm aware of between the A100 vs. H100 nodes are driver version (550.163.01 and 570.133.20 respectively) and kernel version (5.10.236-228.935.amzn2.x86_64 and 6.1.134-152.225.amzn2023.x86_64 respectively). Any debugging tips greatly appreciated. Thanks! Related issues: #7896, #7466, #10419. Error (full log [tp8pp2.log](https://github.com/user-attachments/files/20536730/tp8pp2.log)): ``` sixteen-gpu-gpu-group-worker-rERROR 05-30 22:22:26 [pynccl.py:153] [DEBUG] ncclCommInitRank failed with error: NCCL error: internal error - please report this issue to the NCCL developers ERROR 05-30 22:22:26...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 5: only differences I'm aware of between the A100 vs. H100 nodes are driver version (550.163.01 and 570.133.20 respectively) and kernel version (5.10.236-228.935.amzn2.x86_64 and 6.1.134-152.225.amzn2023.x86_64 respectivel...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 4: [Bug]: ncclCommInitRank failed with error: NCCL error: internal error (H100, KubeRay, DeepSeek, TP=8, PP=2) bug ### Your current environment ### 🐛 Describe the bug Hi vLLM team; cross posting an [issue](https://github.c...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 3: rker_base.py:620] Error executing method 'init_device'. This might cause deadlock in distributed execution. ERROR 05-30 22:22:26 [worker_base.py:620] Traceback (most recent call last): ERROR 05-30 22:22:26 [worker_base....
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: ing KubeRay on AWS EKS and am encountering the error message below. This configuration (DeepSeek-V2-LIte, TP=8, PP=2) works on two 8xA100 nodes, but fails with the same configuration on two 8xH100 nodes. I'm able to run...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: pport;sampling_logits;speculative_decoding cuda;kernel;operator;sampling;triton build_error;crash;nan_inf dtype;env_dependency Your current environment

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
