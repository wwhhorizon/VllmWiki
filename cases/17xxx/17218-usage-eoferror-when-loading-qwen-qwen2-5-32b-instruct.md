# vllm-project/vllm#17218: [Usage]: EOFError when loading Qwen/Qwen2.5-32B-Instruct

| 字段 | 值 |
| --- | --- |
| Issue | [#17218](https://github.com/vllm-project/vllm/issues/17218) |
| 状态 | closed |
| 标签 | usage;stale |
| 评论 | 5; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Usage]: EOFError when loading Qwen/Qwen2.5-32B-Instruct

### Issue 正文摘录

### Your current environment ```text I try to load "Qwen/Qwen2.5-32B-Instruct" using the latest vllm version (0.8.3), but keep getting EOFError. Should I change to 0.7.3? I change to 7B but get the same error, so I think it's not due to GPU or memory. Anyone met the same issue? ``` ```python llm = LLM(model = "Qwen/Qwen2.5-32B-Instruct", tokenizer = "Qwen/Qwen2.5-32B-Instruct", download_dir = ".....", dtype='bfloat16', distributed_executor_backend="mp", tensor_parallel_size=2, gpu_memory_utilization = 0.9, max_model_len = 5000) ``` ```python EOFError Traceback (most recent call last) ----> File /projectnb/vllm/utils.py:1096, in deprecate_args. .wrapper. .inner(*args, **kwargs) [1089](file:///projectnb/lib/python3.12/site-packages/vllm/utils.py?line=1088) msg += f" {additional_message}" [1091](file:///projectnb/conda_envs/env_factchecking/lib/python3.12/site-packages/vllm/utils.py?line=1090) warnings.warn( [1092](file:///projectnb/conda_envs/env_factchecking/lib/python3.12/site-packages/vllm/utils.py?line=1091) DeprecationWarning(msg), [1093](file:///projectnb/conda_envs/env_factchecking/lib/python3.12/site-packages/vllm/utils.py?line=1092) stacklevel=3, # The inner function takes...

## 候选优化模式

- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 4: n/Qwen2.5-32B-Instruct", download_dir = ".....", dtype='bfloat16', distributed_executor_backend="mp", tensor_parallel_size=2, gpu_memory_utilization = 0.9, max_model_len = 5000) ``` ```python EOFError
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: [Usage]: EOFError when loading Qwen/Qwen2.5-32B-Instruct usage;stale ### Your current environment ```text I try to load "Qwen/Qwen2.5-32B-Instruct" using the latest vllm version (0.8.3), but keep getting EOFError. Shoul...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: ```text I try to load "Qwen/Qwen2.5-32B-Instruct" using the latest vllm version (0.8.3), but keep getting EOFError. Should I change to 0.7.3? I change to 7B but get the same error, so I think it's not due to GPU or memo...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 3: [Usage]: EOFError when loading Qwen/Qwen2.5-32B-Instruct usage;stale ### Your current environment ```text I try to load "Qwen/Qwen2.5-32B-Instruct" using the latest vllm version (0.8.3), but keep getting EOFError. Shoul...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: ".....", dtype='bfloat16', distributed_executor_backend="mp", tensor_parallel_size=2, gpu_memory_utilization = 0.9, max_model_len = 5000) ``` ```python EOFError Traceback (most recent call last) ---

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
