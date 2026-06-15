# vllm-project/vllm#18452: [Bug]: v0.8.5.post1 Eagle3 broken with llama3-70b

| 字段 | 值 |
| --- | --- |
| Issue | [#18452](https://github.com/vllm-project/vllm/issues/18452) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 5; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | attention_kv_cache;distributed_parallel;frontend_api;model_support;scheduler_memory |
| 子分类 | throughput |
| Operator 关键词 | cache;cuda |
| 症状 | crash;slowdown |
| 根因提示 | env_dependency;memory_layout |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: v0.8.5.post1 Eagle3 broken with llama3-70b

### Issue 正文摘录

### Your current environment vllm v0.8.5.post1 NVIDIA-SMI 550.90.07 Driver Version: 550.90.07 CUDA Version: 12.4 NVIDIA H100 80GB HBM3 ### 🐛 Describe the bug The vllm 0.8.5.post1 works on meta-llama/Llama-3.1-8B-Instruct with eagle3, but when i change the model to meta-llama/Llama-3.3-70B-Instruct and send the request, it will be broken, please help to figure out, thanks a lot. Start script: ``` export VLLM_LOGGING_LEVEL=DEBUG export VLLM_USE_V1=1 python3 -m vllm.entrypoints.openai.api_server \ --model meta-llama/Llama-3.3-70B-Instruct \ --disable-log-requests --port 8080 \ --served-model-name zoom_llama_3_70b \ --tensor-parallel-size 4 \ --device cuda \ --speculative_config '{"method": "eagle3", "model": "yuhuili/EAGLE3-LLaMA3.3-Instruct-70B", "num_speculative_tokens": 2}' ``` Error Log: ``` DEBUG 05-21 02:19:18 [loggers.py:111] Engine 000: Avg prompt throughput: 0.0 tokens/s, Avg generation throughput: 0.0 tokens/s, Running: 0 reqs, Waiting: 0 reqs, GPU KV cache usage: 0.0%, Prefix cache hit rate: 0.0% DEBUG 05-21 02:19:28 [loggers.py:111] Engine 000: Avg prompt throughput: 0.0 tokens/s, Avg generation throughput: 0.0 tokens/s, Running: 0 reqs, Waiting: 0 reqs, GPU KV cache usag...

## 候选优化模式

- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 6: [Bug]: v0.8.5.post1 Eagle3 broken with llama3-70b bug;stale ### Your current environment vllm v0.8.5.post1 NVIDIA-SMI 550.90.07 Driver Version: 550.90.07 CUDA Version: 12.4 NVIDIA H100 80GB HBM3 ### 🐛 Describe the bug T...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 4: a3-70b bug;stale ### Your current environment vllm v0.8.5.post1 NVIDIA-SMI 550.90.07 Driver Version: 550.90.07 CUDA Version: 12.4 NVIDIA H100 80GB HBM3 ### 🐛 Describe the bug The vllm 0.8.5.post1 works on meta-llama/Lla...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: [Bug]: v0.8.5.post1 Eagle3 broken with llama3-70b bug;stale ### Your current environment vllm v0.8.5.post1 NVIDIA-SMI 550.90.07 Driver Version: 550.90.07 CUDA Version: 12.4 NVIDIA H100 80GB HBM3 ### 🐛 Describe the bug T...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: environment vllm v0.8.5.post1 NVIDIA-SMI 550.90.07 Driver Version: 550.90.07 CUDA Version: 12.4 NVIDIA H100 80GB HBM3 ### 🐛 Describe the bug The vllm 0.8.5.post1 works on meta-llama/Llama-3.1-8B-Instruct with eagle3, bu...
- [KV Cache 容量、压缩与 Offload](../patterns/kv_cache_capacity_offload.md) - 分数 3: --disable-log-requests --port 8080 \ --served-model-name zoom_llama_3_70b \ --tensor-parallel-size 4 \ --device cuda \ --speculative_config '{"method": "eagle3", "model": "yuhuili/EAGLE3-LLaMA3.3-Instruct-70B", "num_spe...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
