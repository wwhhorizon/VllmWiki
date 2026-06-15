# vllm-project/vllm#18816: [Bug]: Model fails to load in background thread in versions >0.8.5

| 字段 | 值 |
| --- | --- |
| Issue | [#18816](https://github.com/vllm-project/vllm/issues/18816) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 9; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: Model fails to load in background thread in versions >0.8.5

### Issue 正文摘录

Hi, In versions above 0.8.5 (specifically 0.8.5.post1 and 0.9.0), the model fails to load when executed in a background thread. I was able to load it without any issues in version 0.8.4 and earlier. Normally, I use an executor to load the model in a background thread. However, newer versions seem to break this behavior. I've tried multiple approaches but couldn't get it working. The reason I load the model in the background is to ensure the API becomes responsive as soon as possible. Otherwise, Kubernetes triggers a startup timeout, or users may not be able to reach the API at all. Can you please help me resolve this issue? ``` `(RayWorkerWrapper pid=962642) WARNING 05-28 10:18:32 [utils.py:2671] Methods determine_num_available_blocks, device_config, get_cache_block_size_bytes, initialize_cache not implemented in (RayWorkerWrapper pid=962641) INFO 05-28 10:18:37 [gpu_model_runner.py:1549] Model loading took 7.5123 GiB and 3.765386 seconds INFO 05-28 10:18:40 [kv_cache_utils.py:637] GPU KV cache size: 1,014,384 tokens INFO 05-28 10:18:40 [kv_cache_utils.py:640] Maximum concurrency for 131,072 tokens per request: 7.74x INFO 05-28 10:18:40 [kv_cache_utils.py:637] GPU KV cache size: 1...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: [Bug]: Model fails to load in background thread in versions >0.8.5 bug;stale Hi, In versions above 0.8.5 (specifically 0.8.5.post1 and 0.9.0), the model fails to load when executed in a background thread. I was able to...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 3: [Bug]: Model fails to load in background thread in versions >0.8.5 bug;stale Hi, In versions above 0.8.5 (specifically 0.8.5.post1 and 0.9.0), the model fails to load when executed in a background thread. I was able to...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: [Bug]: Model fails to load in background thread in versions >0.8.5 bug;stale Hi, In versions above 0.8.5 (specifically 0.8.5.post1 and 0.9.0), the model fails to load when executed in a background thread. I was able to...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 2: kens per request: 7.74x INFO 05-28 10:18:40 [core.py:167] init engine (profile, create kv cache, warmup model) took 2.21 seconds [2025-05-28 10:18:41] repeat_every.py:57 ERROR: There is no current event loop in thread '...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: ``` ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
