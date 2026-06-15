# vllm-project/vllm#15304: [Usage]: Generating multiple completions with Qwen QwQ 32B

| 字段 | 值 |
| --- | --- |
| Issue | [#15304](https://github.com/vllm-project/vllm/issues/15304) |
| 状态 | closed |
| 标签 | usage |
| 评论 | 0; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Usage]: Generating multiple completions with Qwen QwQ 32B

### Issue 正文摘录

Running inference using QwQ 32B with n=10, does not generate multiple completions. I need help with how to generate multiple completions for each input query. `llm = LLM(model=MODEL_NAME, max_model_len=2048, enable_prefix_caching=True, quantization="fp8", \ tensor_parallel_size=4, gpu_memory_utilization=0.95, kv_cache_dtype="auto")` `sampling_params = SamplingParams( n=10, temperature = 1.0, top_p=0.95, min_p=0, top_k=40, max_tokens=1024)` with VLLM_USE_V1 = 1

## 候选优化模式

- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 3: = LLM(model=MODEL_NAME, max_model_len=2048, enable_prefix_caching=True, quantization="fp8", \ tensor_parallel_size=4, gpu_memory_utilization=0.95, kv_cache_dtype="auto")` `sampling_params = SamplingParams( n=10, tempera...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: [Usage]: Generating multiple completions with Qwen QwQ 32B usage Running inference using QwQ 32B with n=10, does not generate multiple completions. I need help with how to generate multiple completions for each input qu...

## Wiki 抽取状态

- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
