# vllm-project/vllm#13872: [Bug]: V1 does not support torch compile

| 字段 | 值 |
| --- | --- |
| Issue | [#13872](https://github.com/vllm-project/vllm/issues/13872) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: V1 does not support torch compile

### Issue 正文摘录

### Your current environment using docker ### 🐛 Describe the bug WARNING 02-25 21:31:47 config.py:3473] `torch.compile` is turned on, but the model /root/.cache/huggingface/hub/deepseek-ai/DeepSeek-V3 does not support it. Please open an issue on GitHubif you want it to be supported. ### Replenish Here is how to start Node1 ```bash services: v3-1-vllm: container_name: v3-1-vllm image: vllm/vllm-openai:latest privileged: true deploy: resources: reservations: devices: - driver: nvidia count: all capabilities: [gpu] shm_size: "1024g" ipc: "host" network_mode: "host" volumes: - /data/deepseek-v3:/root/.cache/huggingface - /data/torchcache-v3:/root/torchcache environment: - VLLM_HOST_IP=10.0.251.33 - GLOO_SOCKET_IFNAME=ens12f0np0 - NCCL_SOCKET_IFNAME=ibs1 - NCCL_IB_ALLOW=1 - NCCL_IB_DISABLE=0 - NCCL_IB_CUDA_SUPPORT=1 - NCCL_IB_HCA=ibp1 - NCCL_IB_RETRY_CNT=13 - NCCL_IB_GID_INDEX=3 - NCCL_NET_GDR_LEVEL=2 - NCCL_IB_TIMEOUT=22 - NCCL_DEBUG=INFO - NCCL_P2P_LEVEL=NVL - NCCL_CROSS_NIC=1 - NCCL_NET_GDR_LEVEL=SYS entrypoint: - /bin/bash - -c - | (nohup ray start --disable-usage-stats --block --head --port=6379 > /init.log 2>&1 &) sleep 10 && python3 -m vllm.entrypoints.openai.api_server \ --serv...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: vironment using docker ### 🐛 Describe the bug WARNING 02-25 21:31:47 config.py:3473] `torch.compile` is turned on, but the model /root/.cache/huggingface/hub/deepseek-ai/DeepSeek-V3 does not support it. Please open an i...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 3: [Bug]: V1 does not support torch compile bug;stale ### Your current environment using docker ### 🐛 Describe the bug WARNING 02-25 21:31:47 config.py:3473] `torch.compile` is turned on, but the model /root/.cache/hugging...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: [Bug]: V1 does not support torch compile bug;stale ### Your current environment using docker ### 🐛 Describe the bug WARNING 02-25 21:31:47 config.py:3473] `torch.compile` is turned on, but the model /root/.cache/hugging...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: E=ibs1 - NCCL_IB_ALLOW=1 - NCCL_IB_DISABLE=0 - NCCL_IB_CUDA_SUPPORT=1 - NCCL_IB_HCA=ibp1 - NCCL_IB_RETRY_CNT=13 - NCCL_IB_GID_INDEX=3 - NCCL_NET_GDR_LEVEL=2 - NCCL_IB_TIMEOUT=22 - NCCL_DEBUG=INFO - NCCL_P2P_LEVEL=NVL -...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 1: sh - -c - | (nohup ray start --disable-usage-stats --block --head --port=6379 > /init.log 2>&1 &) sleep 10 && python3 -m vllm.entrypoints.openai.api_server \ --served-model-name "deepseek/deepseek-v3" \ --model /root/.c...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
