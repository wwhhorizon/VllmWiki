# vllm-project/vllm#7553: [Misc]:  gpu-memory-utilization and Memory-Usage （by nvidia-smi）

| 字段 | 值 |
| --- | --- |
| Issue | [#7553](https://github.com/vllm-project/vllm/issues/7553) |
| 状态 | closed |
| 标签 | stale |
| 评论 | 7; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | attention_kv_cache;distributed_parallel;frontend_api;model_support |
| 子分类 | memory |
| Operator 关键词 | cache;cuda |
| 症状 | oom |
| 根因提示 | env_dependency;shape |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Misc]:  gpu-memory-utilization and Memory-Usage （by nvidia-smi）

### Issue 正文摘录

### Anything you want to discuss about vllm. I run the model on the server with 4 x NVIDIA GeForce RTX 4090 cards： CUDA_VISIBLE_DEVICES=4,5,6,7 python -m vllm.entrypoints.openai.api_server --served-model-name Yi-1.5-34B-Chat --model /workspace/sdb/models/Yi/Yi-1.5-34B-Chat/ --port 8001 --gpu-memory-utilization 0.9 --swap-space 0 --tensor-parallel-size 4 Memory-Usage showed by nvidia-smi is 23859MiB / 24564MiB on each card; when I disable the cuda grapy by --enforce-eager， the memory-usage is changed to 21395MiB / 24564MiB (close to the value 24564 * 0.9). **23859 - 21395 = 2464 MiB is consumed by the cuda grapy. Too much! Is this normal？** When inference，batch size = 4(input length = 2k for each query)，**oom occurs**. BTW, when we set gpu-memory-utilization = 0.9, it means that 24564(for RTX 4090) * 0.9 can be used for model and kv cache? vllm version: 0.5.4; ``` CUDA_VISIBLE_DEVICES=4,5,6,7 python -m vllm.entrypoints.openai.api_server --served-model-name Yi-1.5-34B-Chat --model /workspace/sdb/models/Yi/Yi-1.5-34B-Chat/ --port 8001 --gpu-memory-utilization 0.9 --swap-space 0 --tensor-parallel-size 4 +---------------------------------------------------------------------------------...

## 候选优化模式

- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: [Misc]: gpu-memory-utilization and Memory-Usage （by nvidia-smi） stale ### Anything you want to discuss about vllm. I run the model on the server with 4 x NVIDIA GeForce RTX 4090 cards： CUDA_VISIBLE_DEVICES=4,5,6,7 pytho...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: hat 24564(for RTX 4090) * 0.9 can be used for model and kv cache? vllm version: 0.5.4; ``` CUDA_VISIBLE_DEVICES=4,5,6,7 python -m vllm.entrypoints.openai.api_server --served-model-name Yi-1.5-34B-Chat --model /workspace...
- [KV Cache 容量、压缩与 Offload](../patterns/kv_cache_capacity_offload.md) - 分数 2: al？** When inference，batch size = 4(input length = 2k for each query)，**oom occurs**. BTW, when we set gpu-memory-utilization = 0.9, it means that 24564(for RTX 4090) * 0.9 can be used for model and kv cache? vllm versi...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: vidia-smi） stale ### Anything you want to discuss about vllm. I run the model on the server with 4 x NVIDIA GeForce RTX 4090 cards： CUDA_VISIBLE_DEVICES=4,5,6,7 python -m vllm.entrypoints.openai.api_server --served-mode...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: [Misc]: gpu-memory-utilization and Memory-Usage （by nvidia-smi） stale ### Anything you want to discuss about vllm. I run the model on the server with 4 x NVIDIA GeForce RTX 4090 cards： CUDA_VISIBLE_DEVICES=4,5,6,7 pytho...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
