# vllm-project/vllm#26871: [Bug]: The system generates an error when using dual graphics cards; version 10.1.1 functions correctly, but version 10.2/11.0 triggers an error upon execution.

| 字段 | 值 |
| --- | --- |
| Issue | [#26871](https://github.com/vllm-project/vllm/issues/26871) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 6; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | attention_kv_cache;ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;moe;quantization;sampling_logits;scheduler_memory;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | attention;cuda;moe;operator;quantization;sampling;triton |
| 症状 | build_error;crash;nan_inf;slowdown |
| 根因提示 | dtype;env_dependency;memory_layout |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: The system generates an error when using dual graphics cards; version 10.1.1 functions correctly, but version 10.2/11.0 triggers an error upon execution.

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug When I use only a single graphics card, the system can start up normally. Below are Docker configuration files, logs, and environment information. I encountered this issue when upgrading from version 10.1.1 to 10.2. [The system generates an error when using dual graphics cards; version 10.1.1 functions correctly, but version 10.2 triggers an error upon execution.](https://github.com/vllm-project/vllm/issues/25813) ```yml services: vllm-openai-8000: runtime: nvidia # 使用所有gpu deploy: resources: reservations: devices: - driver: nvidia count: all capabilities: - gpu command: > --model /models/safetensors/cpatonn/Qwen3-Next-80B-A3B-Instruct-AWQ-4bit --served-model-name Qwen/Qwen3-Next-80B-A3B-Instruct-AWQ-4bit --gpu-memory-utilization 0.8 --kv-cache-dtype auto --enable-expert-parallel --tensor-parallel-size 2 --enable-auto-tool-choice --tool-call-parser hermes environment: - NCCL_DEBUG=INFO volumes: - ./models/.cache/huggingface:/root/.cache/huggingface - ./models/safetensors:/models/safetensors dns: - 8.8.8.8 ports: - 8001:8000 ipc: host image: vllm/vllm-openai:v0.11.0 ``` error log ```log INFO 10-14 01:25:52 [__init__.py:216] Automa...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 6: [Bug]: The system generates an error when using dual graphics cards; version 10.1.1 functions correctly, but version 10.2/11.0 triggers an error upon execution. bug;stale ### Your current environment ### 🐛 Describe the...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 6: s correctly, but version 10.2/11.0 triggers an error upon execution. bug;stale ### Your current environment ### 🐛 Describe the bug When I use only a single graphics card, the system can start up normally. Below are Dock...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 5: single graphics card, the system can start up normally. Below are Docker configuration files, logs, and environment information. I encountered this issue when upgrading from version 10.1.1 to 10.2. [The system generates...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 4: B-Instruct-AWQ-4bit --gpu-memory-utilization 0.8 --kv-cache-dtype auto --enable-expert-parallel --tensor-parallel-size 2 --enable-auto-tool-choice --tool-call-parser hermes environment: - NCCL_DEBUG=INFO volumes: - ./mo...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 4: (APIServer pid=1) INFO 10-14 01:26:10 [config.py:376] Setting attention block size to 544 tokens to ensure that attention page size is >= mamba page size. (APIServer pid=1) INFO 10-14 01:26:10 [config.py:397] Padding ma...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
