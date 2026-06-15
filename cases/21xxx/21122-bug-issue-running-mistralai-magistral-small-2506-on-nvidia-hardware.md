# vllm-project/vllm#21122: [Bug]: Issue running mistralai/Magistral-Small-2506 on NVIDIA hardware

| 字段 | 值 |
| --- | --- |
| Issue | [#21122](https://github.com/vllm-project/vllm/issues/21122) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 4; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | development |
| 工作域 | ci_build;distributed_parallel;frontend_api;model_support |
| 子分类 | env_compat |
| Operator 关键词 | cuda |
| 症状 | crash |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Issue running mistralai/Magistral-Small-2506 on NVIDIA hardware

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug I'm encountering a TypeError: not a string exception when running vLLM (v0.9.2) with the mistralai/Magistral-Small-2506 model on NVIDIA H200 hardeware. To reproduce , run below docker compose file: ``` services: vllm: container_name: vllm image: 121701826775.dkr.ecr.us-east-1.amazonaws.com/nvidia/vllm:v0.9.2 environment: - HUGGING_FACE_HUB_TOKEN= command: - "--model=mistralai/Magistral-Small-2506" - "--dtype=auto" - "--max-model-len=8192" - "--tensor-parallel-size=2" - "--trust-remote-code" volumes: - /mnt/models:/root/.cache/huggingface ports: - 8000:8000 deploy: resources: reservations: devices: - driver: nvidia capabilities: [gpu] ``` Error: ``` vllm | INFO 07-17 07:53:30 [__init__.py:244] Automatically detected platform cuda. vllm | INFO 07-17 07:53:42 [api_server.py:1395] vLLM API server version 0.9.2 vllm | INFO 07-17 07:53:42 [cli_args.py:325] non-default args: {'model': 'mistralai/Magistral-Small-2506', 'trust_remote_code': True, 'max_model_len': 8192} vllm | INFO 07-17 07:53:48 [config.py:841] This model supports multiple tasks: {'embed', 'reward', 'classify', 'generate'}. Defaulting to 'generate'. vllm | INFO 07-17 07:5...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 5: ral-Small-2506 model on NVIDIA H200 hardeware. To reproduce , run below docker compose file: ``` services: vllm: container_name: vllm image: 121701826775.dkr.ecr.us-east-1.amazonaws.com/nvidia/vllm:v0.9.2 environment: -...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: ption when running vLLM (v0.9.2) with the mistralai/Magistral-Small-2506 model on NVIDIA H200 hardeware. To reproduce , run below docker compose file: ``` services: vllm: container_name: vllm image: 121701826775.dkr.ecr...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: [Bug]: Issue running mistralai/Magistral-Small-2506 on NVIDIA hardware bug;stale ### Your current environment ### 🐛 Describe the bug I'm encountering a TypeError: not a string exception when running vLLM (v0.9.2) with t...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: ug]: Issue running mistralai/Magistral-Small-2506 on NVIDIA hardware bug;stale ### Your current environment ### 🐛 Describe the bug I'm encountering a TypeError: not a string exception when running vLLM (v0.9.2) with the...
- [Bitwise 确定性与数值等价](../patterns/bitwise_determinism_equivalence.md) - 分数 1: h the mistralai/Magistral-Small-2506 model on NVIDIA H200 hardeware. To reproduce , run below docker compose file: ``` services: vllm: container_name: vllm image: 121701826775.dkr.ecr.us-east-1.amazonaws.com/nvidia/vllm...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
