# vllm-project/vllm#14093: [Bug][Ray]: Pipeline parallelism fails on the same host

| 字段 | 值 |
| --- | --- |
| Issue | [#14093](https://github.com/vllm-project/vllm/issues/14093) |
| 状态 | closed |
| 标签 | bug;ray;stale |
| 评论 | 8; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | attention_kv_cache;ci_build;distributed_parallel;frontend_api;model_support;quantization;scheduler_memory |
| 子分类 | memory |
| Operator 关键词 | attention;cuda;kernel;operator;quantization |
| 症状 | crash |
| 根因提示 | dtype;env_dependency;memory_layout;race_condition |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug][Ray]: Pipeline parallelism fails on the same host

### Issue 正文摘录

### Your current environment Using the 0.7.3 ghcr.io/sasha0552/vllm:v0.7.3 (pascal docker from [pascal-pkgs-ci](https://github.com/sasha0552/pascal-pkgs-ci)) and the same version directly from vllm Head: ``` docker run -d --rm \ --entrypoint /bin/bash \ --network host \ --runtime=nvidia \ --name headnode \ --shm-size 10.24g \ --gpus "device=0" \ -e VLLM_HOST_IP=0.0.0.0 \ -e MASTER_ADDR=127.0.0.1 \ -e MASTER_PORT=29500 \ -e NCCL_DEBUG=INFO \ -e NCCL_SOCKET_IFNAME=br0 \ -e NCCL_PCI_BUS_ID="00000000:01:00.0" \ -v /media/bkutasi/60824A4F824A29BC/Other_projects/koboldcpp_precompiled:/models \ vllm/vllm-openai:v0.7.3 -c "ray start --block --head --port=6379 --node-ip-address=0.0.0.0 --dashboard-host=0.0.0.0" ``` Worker: ``` docker run -d --rm \ --entrypoint /bin/bash \ --network host \ --runtime=nvidia \ --name workernode \ --shm-size 10.24g \ --gpus "device=1" \ -e VLLM_HOST_IP=127.0.0.1 \ -e MASTER_ADDR=127.0.0.1 \ -e MASTER_PORT=29500 \ -e NCCL_DEBUG=INFO \ -e NCCL_SOCKET_IFNAME=br0 \ -e NCCL_PCI_BUS_ID="00000000:03:00.0" \ -v /media/bkutasi/60824A4F824A29BC/Other_projects/koboldcpp_precompiled:/models \ ghcr.io/sasha0552/vllm:v0.7.3 -c "ray start --block --address=127.0.0.1:6379" ``...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 6: rrent environment Using the 0.7.3 ghcr.io/sasha0552/vllm:v0.7.3 (pascal docker from [pascal-pkgs-ci](https://github.com/sasha0552/pascal-pkgs-ci)) and the same version directly from vllm Head: ``` docker run -d --rm \ -...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 3: Ray starts on both successfully. Head ray status: ```bash ======== Autoscaler status: 2025-03-02 03:52:57.914139 ======== Node status --------------------------------------------------------------- Active: 1 node_90e689...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: [Bug][Ray]: Pipeline parallelism fails on the same host bug;ray;stale ### Your current environment Using the 0.7.3 ghcr.io/sasha0552/vllm:v0.7.3 (pascal docker from [pascal-pkgs-ci](https://github.com/sasha0552/pascal-p...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 2: ldcpp_precompiled:/models \ vllm/vllm-openai:v0.7.3 -c "ray start --block --head --port=6379 --node-ip-address=0.0.0.0 --dashboard-host=0.0.0.0" ``` Worker: ``` docker run -d --rm \ --entrypoint /bin/bash \ --network ho...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: -v /media/bkutasi/60824A4F824A29BC/Other_projects/koboldcpp_precompiled:/models \ vllm/vllm-openai:v0.7.3 -c "ray start --block --head --port=6379 --node-ip-address=0.0.0.0 --dashboard-host=0.0.0.0" ``` Worker: ``` dock...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
