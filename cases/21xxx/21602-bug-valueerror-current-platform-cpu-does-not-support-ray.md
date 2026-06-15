# vllm-project/vllm#21602: [Bug]: ValueError: current platform cpu does not support ray.

| 字段 | 值 |
| --- | --- |
| Issue | [#21602](https://github.com/vllm-project/vllm/issues/21602) |
| 状态 | closed |
| 标签 | feature request;ray;stale |
| 评论 | 8; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: ValueError: current platform cpu does not support ray.

### Issue 正文摘录

### 🚀 The feature, motivation and pitch When I try to run vllm on ray, it raises this error: ``` venv/lib/python3.11/site-packages/vllm/executor/ray_utils.py", line 304, in initialize_ray_cluster raise ValueError( ValueError: current platform cpu does not support ray. ``` My test device does not have a GPU accelerator. According to the documentation, vllm supports running on CPU only. I hope to run vllm on Ray with a CPU backend. Minimal reproducible code: ```python import vllm if __name__ == '__main__': kwargs = {'disable_log_requests': True, 'enable_prefix_caching': True, 'enable_chunked_prefill': True, 'max_num_batched_tokens': 4096, 'max_model_len': 4096, 'distributed_executor_backend': 'ray', 'task': 'generate', 'model': 'Qwen/Qwen3-4B'} engine_args = vllm.AsyncEngineArgs( **kwargs, ) engine = vllm.AsyncLLMEngine.from_engine_args(engine_args) print(engine) ``` vllm version: latest main 9532a6d5631bbf906f992806379516ed569c447d ray version: 2.48.0 ### Alternatives Not to use vllm. ### Additional context _No response_ ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [docu...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: CPU only. I hope to run vllm on Ray with a CPU backend. Minimal reproducible code: ```python import vllm if __name__ == '__main__': kwargs = {'disable_log_requests': True, 'enable_prefix_caching': True, 'enable_chunked_...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 3: [Bug]: ValueError: current platform cpu does not support ray. feature request;ray;stale ### 🚀 The feature, motivation and pitch When I try to run vllm on ray, it raises this error: ``` venv/lib/python3.11/site-packages/...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: unked_prefill': True, 'max_num_batched_tokens': 4096, 'max_model_len': 4096, 'distributed_executor_backend': 'ray', 'task': 'generate', 'model': 'Qwen/Qwen3-4B'} engine_args = vllm.AsyncEngineArgs( **kwargs, ) engine =...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: vllm supports running on CPU only. I hope to run vllm on Ray with a CPU backend. Minimal reproducible code: ```python import vllm if __name__ == '__main__': kwargs = {'disable_log_requests': True, 'enable_prefix_caching...
- [Bitwise 确定性与数值等价](../patterns/bitwise_determinism_equivalence.md) - 分数 1: ning on CPU only. I hope to run vllm on Ray with a CPU backend. Minimal reproducible code: ```python import vllm if __name__ == '__main__': kwargs = {'disable_log_requests': True, 'enable_prefix_caching': True, 'enable_...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
