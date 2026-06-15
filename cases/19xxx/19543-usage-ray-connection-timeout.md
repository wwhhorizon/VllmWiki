# vllm-project/vllm#19543: [Usage]: Ray connection timeout

| 字段 | 值 |
| --- | --- |
| Issue | [#19543](https://github.com/vllm-project/vllm/issues/19543) |
| 状态 | closed |
| 标签 | usage;ray;stale |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Usage]: Ray connection timeout

### Issue 正文摘录

### Your current environment docker run -d \ > --entrypoint /bin/bash \ > --network host \ -v /data:/data \ vllm:0.7.3-python3.11-cuda12.4-debian12 \ -c "ray start --block --address=127.0.0.1:6379"> --runtime=nvidia \ > --name workernode \ > --shm-size 10.24g \ > --gpus "device=3" \ > -e VLLM_HOST_IP=127.0.0.1 \ > -e MASTER_ADDR=127.0.0.1 \ > -e MASTER_PORT=29500 \ > -v /data:/data \ > harbor.inspur.local/ai-group/vllm:0.7.3-python3.11-cuda12.4-debian12 \ > -c "ray start --block --address=127.0.0.1:6379" cb2dc97286d9e65858472bd6ce020f2694718b012dd6b2d89782fbf1e41eee05 (base) [root@nvidia-h20-1 ~]# docker logs -f workernode [2025-06-13 01:49:41,730 E 1 1] gcs_rpc_client.h:179: Failed to connect to GCS at address 10.108.0.184:6379 within 5 seconds. ### How would you like to use vllm I want to run inference of a [specific model](put link here). I don't know how to integrate it with vllm. ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: e]: Ray connection timeout usage;ray;stale ### Your current environment docker run -d \ > --entrypoint /bin/bash \ > --network host \ -v /data:/data \ vllm:0.7.3-python3.11-cuda12.4-debian12 \ -c "ray start --block --ad...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: --network host \ -v /data:/data \ vllm:0.7.3-python3.11-cuda12.4-debian12 \ -c "ray start --block --address=127.0.0.1:6379"> --runtime=nvidia \ > --name workernode \ > --shm-size 10.24g \ > --gpus "device=3" \ > -e VLLM...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 1: \ vllm:0.7.3-python3.11-cuda12.4-debian12 \ -c "ray start --block --address=127.0.0.1:6379"> --runtime=nvidia \ > --name workernode \ > --shm-size 10.24g \ > --gpus "device=3" \ > -e VLLM_HOST_IP=127.0.0.1 \ > -e MASTER...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: # How would you like to use vllm I want to run inference of a [specific model](put link here). I don't know how to integrate it with vllm. ### Before submitting a new issue... - [x] Make sure you already searched for re...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: [Usage]: Ray connection timeout usage;ray;stale ### Your current environment docker run -d \ > --entrypoint /bin/bash \ > --network host \ -v /data:/data \ vllm:0.7.3-python3.11-cuda12.4-debian12 \ -c "ray start --block...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
