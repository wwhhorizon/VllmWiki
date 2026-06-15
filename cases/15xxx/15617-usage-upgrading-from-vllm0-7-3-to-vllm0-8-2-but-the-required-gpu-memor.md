# vllm-project/vllm#15617: [Usage]: Upgrading from vllm0.7.3 to vllm0.8.2, but the required GPU memory significantly increases.

| 字段 | 值 |
| --- | --- |
| Issue | [#15617](https://github.com/vllm-project/vllm/issues/15617) |
| 状态 | closed |
| 标签 | usage |
| 评论 | 5; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | attention_kv_cache;ci_build;frontend_api;model_support |
| 子分类 | memory |
| Operator 关键词 | cache;cuda |
| 症状 | oom;slowdown |
| 根因提示 | shape |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Usage]: Upgrading from vllm0.7.3 to vllm0.8.2, but the required GPU memory significantly increases.

### Issue 正文摘录

### Your current environment ``` I use docker to run vllm I own 8 NVIDIA GeForce RTX 4090 24564MiB ``` ### How would you like to use vllm I upgraded from vllm0.7.3 to vllm0.8.2, but the required GPU memory increased dramatically, --max-model-len needs to be reduced by more than half to start, and frequent OOM (Out of Memory) occurs during operation, and the inference speed is extremely slow. vllm0.8.2 command: --gpu-memory-utilization 0.95 --port 18081 --max-model-len 116160 --enable-reasoning --reasoning-parser deepseek_r1 vllm0.7.3 command: --gpu-memory-utilization 0.90 --port 18081 --max-model-len 53008 --enable-reasoning --reasoning-parser deepseek_r1 On version 0.8.2, I had to repeatedly try to reduce --gpu-memory-utilization and --max-model-len in order to get the model to run. the error like: ERROR 03-27 16:43:19 [core.py:343] ValueError: To serve at least one request with the models's max seq len (116160), (4.43 GB KV cache is needed, which is larger than the available KV cache memory (3.48 GB). Try increasing gpu_memory_utilization or decreasing max_model_len when initializing the engine. ERROR 03-27 17:34:18 [core.py:343] RuntimeError: CUDA out of memory occurred when wa...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: y significantly increases. usage ### Your current environment ``` I use docker to run vllm I own 8 NVIDIA GeForce RTX 4090 24564MiB ``` ### How would you like to use vllm I upgraded from vllm0.7.3 to vllm0.8.2, but the...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: current environment ``` I use docker to run vllm I own 8 NVIDIA GeForce RTX 4090 24564MiB ``` ### How would you like to use vllm I upgraded from vllm0.7.3 to vllm0.8.2, but the required GPU memory increased dramatically...
- [KV Cache 容量、压缩与 Offload](../patterns/kv_cache_capacity_offload.md) - 分数 3: [Usage]: Upgrading from vllm0.7.3 to vllm0.8.2, but the required GPU memory significantly increases. usage ### Your current environment ``` I use docker to run vllm I own 8 NVIDIA GeForce RTX 4090 24564MiB ``` ### How w...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: to vllm0.8.2, but the required GPU memory increased dramatically, --max-model-len needs to be reduced by more than half to start, and frequent OOM (Out of Memory) occurs during operation, and the inference speed is extr...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: ke: ERROR 03-27 16:43:19 [core.py:343] ValueError: To serve at least one request with the models's max seq len (116160), (4.43 GB KV cache is needed, which is larger than the available KV cache memory (3.48 GB). Try inc...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
