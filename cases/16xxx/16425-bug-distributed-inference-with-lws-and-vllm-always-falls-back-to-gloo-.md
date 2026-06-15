# vllm-project/vllm#16425: [Bug]: Distributed Inference with LWS and vLLM always falls back to gloo instead of RDMA when RDMA is configured

| 字段 | 值 |
| --- | --- |
| Issue | [#16425](https://github.com/vllm-project/vllm/issues/16425) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | ci_build;distributed_parallel;model_support |
| 子分类 |  |
| Operator 关键词 | cuda;operator |
| 症状 |  |
| 根因提示 | env_dependency |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Distributed Inference with LWS and vLLM always falls back to gloo instead of RDMA when RDMA is configured

### Issue 正文摘录

### Your current environment I am running through the distributed inference example with LWS found [here](https://docs.vllm.ai/en/latest/deployment/frameworks/lws.html). I have 2 nodes with 8 H100s each, and am trying to use this to serve inference with RDMA enabled. I have attached my container environment to the issue. [container_env.txt](https://github.com/user-attachments/files/19689841/container_env.txt) I was able to run distributed inference without RDMA using the example on LWS with replicas == 1 and size == 2. However, when I added my RDMA configuration, my setup always falls back to gloo and fails: ``` 2025-04-10 10:47:14,557 ERROR worker.py:422 -- Unhandled error (suppress with 'RAY_IGNORE_UNHANDLED_ERRORS=1'): ray::RayWorkerWrapper.execute_method() (pid=1477, ip=10.140.51.37, actor_id=a772570b97ba2115e835168103000000, repr= ) ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ File "/usr/local/lib/python3.12/dist-packages/vllm/worker/worker_base.py", line 621, in execute_method raise e File "/usr/local/lib/python3.12/dist-packages/vllm/worker/worker_base.py", line 612, in execute_method return run_method(self, method, args, kwargs) ^^^^^^^^^^^^^^^^^^^^...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 6: d line `sleep 9999`, and then run the following test script: ```python3 import os import torch import torch.distributed as dist dist.init_process_group(backend="nccl") local_rank = int(os.environ.get("LOCAL_RANK", 0)) d...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: vllm.ai/en/latest/deployment/frameworks/lws.html). I have 2 nodes with 8 H100s each, and am trying to use this to serve inference with RDMA enabled. I have attached my container environment to the issue. [container_env....
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: with LWS and vLLM always falls back to gloo instead of RDMA when RDMA is configured bug ### Your current environment I am running through the distributed inference example with LWS found [here](https://docs.vllm.ai/en/l...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 2: l: ```yaml apiVersion: leaderworkerset.x-k8s.io/v1 kind: LeaderWorkerSet metadata: name: vllm spec: replicas: 1 leaderWorkerTemplate: size: 2 restartPolicy: None leaderTemplate: metadata: labels: role: leader spec: cont...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: distributed_environment _WORLD = init_world_group(ranks, local_rank, backend) ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ File "/usr/local/lib/python3.12/dist-packages/vllm/distributed/parallel_state.py", line 716, in...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
