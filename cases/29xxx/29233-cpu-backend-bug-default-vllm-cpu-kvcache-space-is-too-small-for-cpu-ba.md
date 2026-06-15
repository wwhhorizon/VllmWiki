# vllm-project/vllm#29233: [CPU Backend] [Bug]: Default VLLM_CPU_KVCACHE_SPACE is too small for CPU Backend

| 字段 | 值 |
| --- | --- |
| Issue | [#29233](https://github.com/vllm-project/vllm/issues/29233) |
| 状态 | closed |
| 标签 | bug;cpu |
| 评论 | 4; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [CPU Backend] [Bug]: Default VLLM_CPU_KVCACHE_SPACE is too small for CPU Backend

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug If a user tries to run a model with a decent max_model_len, they're very l likely to run into memory issues allocating enough kv cache space since the default value is 4GB (too small) for the CPU backend ``` (EngineCore_DP0 pid=64528) ERROR 11-18 13:44:09 [core.py:842] ValueError: To serve at least one request with the models's max seq len (40960), (4.38 GiB KV cache is needed, which is larger than the available KV cache memory (4.00 GiB). Based on the available memory, the estimated maximum model length is 37376. Try increasing `gpu_memory_utilization` or decreasing `max_model_len` when initializing the engine. ``` We should either default to similar behavior as the gpu backend, such as 80% of available memory or even 50% of available memory to be conservative. Even if that is not possible, why do we have VLLM_CPU_KVCACHE_SPACE instead of using the kv_cache_memory_bytes argument? ### Reproducer: - build vllm on CPU: `VLLM_TARGET_DEVICE=cpu python3 setup.py bdist_wheel` - then run: `vllm bench throughput --input_len 32` - you'll get this error complaining that you don't have enough memory allocated for your kv cache ``` (EngineCo...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: instead of using the kv_cache_memory_bytes argument? ### Reproducer: - build vllm on CPU: `VLLM_TARGET_DEVICE=cpu python3 setup.py bdist_wheel` - then run: `vllm bench throughput --input_len 32` - you'll get this error...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: [CPU Backend] [Bug]: Default VLLM_CPU_KVCACHE_SPACE is too small for CPU Backend bug;cpu ### Your current environment ### 🐛 Describe the bug If a user tries to run a model with a decent max_model_len, they're very l lik...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: current environment ### 🐛 Describe the bug If a user tries to run a model with a decent max_model_len, they're very l likely to run into memory issues allocating enough kv cache space since the default value is 4GB (too...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 2: _TARGET_DEVICE=cpu python3 setup.py bdist_wheel` - then run: `vllm bench throughput --input_len 32` - you'll get this error complaining that you don't have enough memory allocated for your kv cache ``` (EngineCore_DP0 p...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: [CPU Backend] [Bug]: Default VLLM_CPU_KVCACHE_SPACE is too small for CPU Backend bug;cpu ### Your current environment ### 🐛 Describe the bug If a user tries to run a model with a decent max_model_len, they're very l like

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
