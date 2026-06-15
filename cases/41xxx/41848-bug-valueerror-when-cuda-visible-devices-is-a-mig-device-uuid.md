# vllm-project/vllm#41848: [Bug]: ValueError when CUDA_VISIBLE_DEVICES is a MIG device UUID

| 字段 | 值 |
| --- | --- |
| Issue | [#41848](https://github.com/vllm-project/vllm/issues/41848) |
| 状态 | open |
| 标签 |  |
| 评论 | 0; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | development |
| 工作域 | model_support |
| 子分类 | env_compat |
| Operator 关键词 | cuda |
| 症状 | crash |
| 根因提示 | env_dependency |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: ValueError when CUDA_VISIBLE_DEVICES is a MIG device UUID

### Issue 正文摘录

## Describe the bug vLLM crashes on startup when `CUDA_VISIBLE_DEVICES` is set to a MIG device UUID (e.g. `MIG-377e0049-554c-540b-93c6-d0976f8426cb`). This blocks any deployment of vLLM on MIG-partitioned H100/A100 GPUs using UUID-based device assignment. ## Environment - **vLLM version:** 0.20.1 - **Python:** 3.12 - **GPU:** NVIDIA H100 80 GB HBM3 SXM5, MIG enabled (`2g.20gb` partition) - **CUDA driver:** 580.105.08 / CUDA 13.0, torch 2.11.0+cu130 - **OS:** Ubuntu 24.04 ## Steps to reproduce ```bash # Enable MIG and create partitions sudo nvidia-smi -i 0 -mig 1 sudo nvidia-smi mig -cgi 2g.20gb,1g.10gb -C # Note the MIG UUID nvidia-smi -L # GPU 0: NVIDIA H100 80GB HBM3 # MIG 2g.20gb Device 0: (UUID: MIG-377e0049-554c-540b-93c6-d0976f8426cb) # Run vLLM targeting the MIG instance by UUID (CUDA-recommended approach) CUDA_VISIBLE_DEVICES="MIG-377e0049-554c-540b-93c6-d0976f8426cb" \ vllm serve TinyLlama/TinyLlama-1.1B-Chat-v1.0 --port 8001 ``` ## Error ``` File ".../vllm/platforms/interface.py", line 230, in device_id_to_physical_device_id return int(physical_device_id) ^^^^^^^^^^^^^^^^^^^^^^^ ValueError: invalid literal for int() with base 10: 'MIG-377e0049-554c-540b-93c6-d0976f8426cb...

## 现有链接修复摘要

#41850 platforms: handle MIG device UUID in device_id_to_physical_device_id

## 候选优化模式

- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 5: [Bug]: ValueError when CUDA_VISIBLE_DEVICES is a MIG device UUID ## Describe the bug vLLM crashes on startup when `CUDA_VISIBLE_DEVICES` is set to a MIG device UUID (e.g. `MIG-377e0049-554c-540b-93c6-d0976f8426cb`). Thi...
- [Bitwise 确定性与数值等价](../patterns/bitwise_determinism_equivalence.md) - 分数 2: 5.08 / CUDA 13.0, torch 2.11.0+cu130 - **OS:** Ubuntu 24.04 ## Steps to reproduce ```bash # Enable MIG and create partitions sudo nvidia-smi -i 0 -mig 1 sudo nvidia-smi mig -cgi 2g.20gb,1g.10gb -C # Note the MIG UUID nv...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: /A100 GPUs using UUID-based device assignment. ## Environment - **vLLM version:** 0.20.1 - **Python:** 3.12 - **GPU:** NVIDIA H100 80 GB HBM3 SXM5, MIG enabled (`2g.20gb` partition) - **CUDA driver:** 580.105.08 / CUDA...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: LE_DEVICES="MIG-377e0049-554c-540b-93c6-d0976f8426cb" \ vllm serve TinyLlama/TinyLlama-1.1B-Chat-v1.0 --port 8001 ``` ## Error ``` File ".../vllm/platforms/interface.py", line 230, in device_id_to_physical_device_id ret...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: UID to logical device 0 transparently, so when `int()` fails the correct fallback is to return `device_id` unchanged. ## Suggested fix ```python device_ids = os.environ[cls.device_control_env_var].split(",") physical_de...

## 关联 PR 证据

| PR | 链接类型 | 置信度 | PR 标题 | 证据 |
| --- | --- | ---: | --- | --- |
| [#41850](https://github.com/vllm-project/vllm/pull/41850) | closes_keyword | 0.95 | platforms: handle MIG device UUID in device_id_to_physical_device_id | Fixes #41848. When `CUDA_VISIBLE_DEVICES` is set to a MIG device UUID (e.g. `MIG-377e0049-554c-540b-93c6-d0976f8426cb`), `device_id_to_physical_device_id()` raises `ValueError` an |

## Wiki 抽取状态

- 后续迭代应在可用时读取完整讨论评论。
