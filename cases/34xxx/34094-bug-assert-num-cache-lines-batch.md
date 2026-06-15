# vllm-project/vllm#34094: [Bug]: assert num_cache_lines >= batch

| 字段 | 值 |
| --- | --- |
| Issue | [#34094](https://github.com/vllm-project/vllm/issues/34094) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 7; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | ci_build;distributed_parallel;model_support |
| 子分类 | memory |
| Operator 关键词 | cuda;operator |
| 症状 | build_error;crash |
| 根因提示 | env_dependency;shape |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: assert num_cache_lines >= batch

### Issue 正文摘录

### Your current environment ``` (APIServer pid=1) INFO 02-08 08:36:10 [utils.py:325] (APIServer pid=1) INFO 02-08 08:36:10 [utils.py:325] █ █ █▄ ▄█ (APIServer pid=1) INFO 02-08 08:36:10 [utils.py:325] ▄▄ ▄█ █ █ █ ▀▄▀ █ version 0.15.0 (APIServer pid=1) INFO 02-08 08:36:10 [utils.py:325] █▄█▀ █ █ █ █ model Qwen/Qwen3-Coder-Next (APIServer pid=1) INFO 02-08 08:36:10 [utils.py:325] ▀▀ ▀▀▀▀▀ ▀▀▀▀▀ ▀ ▀ (APIServer pid=1) INFO 02-08 08:36:10 [utils.py:325] ``` nvidia-smi ``` +-----------------------------------------------------------------------------------------+ | NVIDIA-SMI 570.133.20 Driver Version: 570.133.20 CUDA Version: 12.8 | |-----------------------------------------+------------------------+----------------------+ | GPU Name Persistence-M | Bus-Id Disp.A | Volatile Uncorr. ECC | | Fan Temp Perf Pwr:Usage/Cap | Memory-Usage | GPU-Util Compute M. | | | | MIG M. | |=========================================+========================+======================| | 0 NVIDIA H100 NVL On | 00000000:03:00.0 Off | 0 | | N/A 31C P0 60W / 400W | 0MiB / 95830MiB | 0% Default | | | | Disabled | +-----------------------------------------+------------------------+----------------------+ | 1 NVIDIA...

## 现有链接修复摘要

#34571 [Bugfix] Cap FULL decode cudagraph sizes for Mamba/hybrid models (#34094)

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 6: er pid=1) INFO 02-08 08:36:10 [utils.py:325] ▄▄ ▄█ █ █ █ ▀▄▀ █ version 0.15.0 (APIServer pid=1) INFO 02-08 08:36:10 [utils.py:325] █▄█▀ █ █ █ █ model Qwen/Qwen3-Coder-Next (APIServer pid=1) INFO 02-08 08:36:10 [utils.py...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 4: ▀ ▀ (APIServer pid=1) INFO 02-08 08:36:10 [utils.py:325] ``` nvidia-smi ``` +-----------------------------------------------------------------------------------------+ | NVIDIA-SMI 570.133.20 Driver Version: 570.133.20...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: er pid=1) INFO 02-08 08:36:10 [utils.py:325] █▄█▀ █ █ █ █ model Qwen/Qwen3-Coder-Next (APIServer pid=1) INFO 02-08 08:36:10 [utils.py:325] ▀▀ ▀▀▀▀▀ ▀▀▀▀▀ ▀ ▀ (APIServer pid=1) INFO 02-08 08:36:10 [utils.py:325] ``` nvid...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 2: docker-compose.yaml ``` services: vllm: image: vllm/vllm-openai:latest volumes: - /root/.cache/huggingface:/root/.cache/huggingface ports: - "8000:8000" ipc: host runtime: nvidia deploy: resources: reservations: devices:
- [KV Cache 容量、压缩与 Offload](../patterns/kv_cache_capacity_offload.md) - 分数 1: GI CI PID Type Process name GPU Memory | | ID ID Usage | |=========================================================================================| | No running processes

## 关联 PR 证据

| PR | 链接类型 | 置信度 | PR 标题 | 证据 |
| --- | --- | ---: | --- | --- |
| [#34571](https://github.com/vllm-project/vllm/pull/34571) | closes_keyword | 0.95 | [Bugfix] Cap FULL decode cudagraph sizes for Mamba/hybrid models (#34094) | Fixes: #34094 For hybrid Mamba/attention models (e.g., Qwen3-Coder-Next), CUDA graph capture can fail with `assert num_cache_lines >= batch` in `causal_conv1d_update` when the FUL |

## Wiki 抽取状态

- 后续迭代应在可用时读取完整讨论评论。
