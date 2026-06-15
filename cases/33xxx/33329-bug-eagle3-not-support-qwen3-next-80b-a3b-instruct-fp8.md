# vllm-project/vllm#33329: [Bug]: Eagle3 not support Qwen3-Next-80B-A3B-Instruct-FP8

| 字段 | 值 |
| --- | --- |
| Issue | [#33329](https://github.com/vllm-project/vllm/issues/33329) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | attention_kv_cache;distributed_parallel;model_support;quantization;speculative_decoding |
| 子分类 | kernel_eff |
| Operator 关键词 | cuda;fp8 |
| 症状 | crash |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Eagle3 not support Qwen3-Next-80B-A3B-Instruct-FP8

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug CUDA_VISIBLE_DEVICES=6,7 python -m vllm.entrypoints.openai.api_server \ --model /model-download/Qwen3-Next-80B-A3B-Instruct-FP8 \ --served-model-name fp8 \ --trust-remote-code \ --tensor-parallel-size 2 \ --max-model-len 131072 \ --gpu-memory-utilization 0.75 \ --port 7868 \ --host 0.0.0.0 \ --dtype auto \ --kv-cache-dtype auto \ --disable-log-requests \ --speculative-config '{"method":"eagle3","model": "/mnt/workspace/dt_training/zxj/models/SGLang-EAGLE3-Qwen3-Next-80B-A3B-Instruct-FP8-SpecForge-Meituan", "num_speculative_tokens": 5}' (Worker_TP1 pid=2440933) INFO 01-29 17:34:27 [cuda.py:427] Using FLASH_ATTN backend. Loading safetensors checkpoint shards: 0% Completed | 0/8 [00:00<?, ?it/s] Loading safetensors checkpoint shards: 12% Completed | 1/8 [00:03<00:22, 3.17s/it] Loading safetensors checkpoint shards: 25% Completed | 2/8 [00:06<00:20, 3.43s/it] Loading safetensors checkpoint shards: 38% Completed | 3/8 [00:10<00:17, 3.49s/it] Loading safetensors checkpoint shards: 50% Completed | 4/8 [00:13<00:13, 3.48s/it] Loading safetensors checkpoint shards: 62% Completed | 5/8 [00:17<00:10, 3.50s/it] Loading safetensors checkpoint...

## 候选优化模式

- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 4: [Bug]: Eagle3 not support Qwen3-Next-80B-A3B-Instruct-FP8 bug;stale ### Your current environment ### 🐛 Describe the bug CUDA_VISIBLE_DEVICES=6,7 python -m vllm.entrypoints.openai.api_server \ --model /model-download/Qwe...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 4: [Bug]: Eagle3 not support Qwen3-Next-80B-A3B-Instruct-FP8 bug;stale ### Your current environment ### 🐛 Describe the bug CUDA_VISIBLE_DEVICES=6,7 python -m vllm.entrypoints.openai.api_server \ --model /model-download/Qwe...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: [Bug]: Eagle3 not support Qwen3-Next-80B-A3B-Instruct-FP8 bug;stale ### Your current environment ### 🐛 Describe the bug CUDA_VISIBLE_DEVICES=6,7 python -m vllm.entrypoints.openai.api_server \ --model /model-download/Qwe...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: t-FP8 bug;stale ### Your current environment ### 🐛 Describe the bug CUDA_VISIBLE_DEVICES=6,7 python -m vllm.entrypoints.openai.api_server \ --model /model-download/Qwen3-Next-80B-A3B-Instruct-FP8 \ --served-model-name f...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: rker_TP1 pid=2440933) INFO 01-29 17:34:27 [cuda.py:427] Using FLASH_ATTN backend. Loading safetensors checkpoint shards: 0% Completed | 0/8 [00:00<?, ?it/s] Loading safetensors checkpoint shards: 12% Completed | 1/8 [00...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
