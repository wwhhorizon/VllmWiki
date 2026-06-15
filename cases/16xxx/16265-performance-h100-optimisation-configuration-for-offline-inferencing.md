# vllm-project/vllm#16265: [Performance]: H100 Optimisation Configuration For Offline Inferencing

| 字段 | 值 |
| --- | --- |
| Issue | [#16265](https://github.com/vllm-project/vllm/issues/16265) |
| 状态 | closed |
| 标签 | performance;stale |
| 评论 | 4; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | model_support;quantization |
| 子分类 | memory |
| Operator 关键词 | fp8 |
| 症状 |  |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Performance]: H100 Optimisation Configuration For Offline Inferencing

### Issue 正文摘录

### Discussion to improve performance I am using the offline inferencing using LLM.generate and testing this on A100 and H100 on LLAMA3.2-3B. I only see a marginal upgrade in performance on H100 ( only 1.3x faster than A100 ) .H100 used is of type PCI-e General scenario is I expect to see a ~2x performance on H100 compared to A100. Is there some tuning parameter that I am missing ? This is my setting . MAX tokens is set at 33000. ```python llm = LLM(model=model_path, tensor_parallel_size=1, max_model_len=MAX_TOKENS, max_num_batched_tokens=MAX_TOKENS, enforce_eager=False, max_seq_len_to_capture=MAX_TOKENS, enable_chunked_prefill=True, dtype="bfloat16", disable_log_stats=True, # kv_cache_dtype="fp8", # calculate_kv_scales=True, gpu_memory_utilization=0.95) ``` Is there some configuration that I can try to make this faster ? My GPU memory utilisation on H100 Having 1 GPU per node gpu utilization % ### Report of performance regression _No response_ ### Misc discussion on performance Performance upgrade of H100 and optimisations that can work ### Your current environment (if you think it is necessary) ```text The output of `python collect_env.py` ``` ### Before submitting a new issue.....

## 候选优化模式

- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 6: ure=MAX_TOKENS, enable_chunked_prefill=True, dtype="bfloat16", disable_log_stats=True, # kv_cache_dtype="fp8", # calculate_kv_scales=True, gpu_memory_utilization=0.95) ``` Is there some configuration that I c
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: [Performance]: H100 Optimisation Configuration For Offline Inferencing performance;stale ### Discussion to improve performance I am using the offline inferencing using LLM.generate and testing this on A100 and H100 on L...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: [Performance]: H100 Optimisation Configuration For Offline Inferencing performance;stale ### Discussion to improve performance I am using the offline inferencing using LLM.generate and testing this on A100 and H100 on L...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: [Performance]: H100 Optimisation Configuration For Offline Inferencing performance;stale ### Discussion to improve performance I am using the offline inferencing using LLM.generate and testing this on A100 and H100 on L...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: ce]: H100 Optimisation Configuration For Offline Inferencing performance;stale ### Discussion to improve performance I am using the offline inferencing using LLM.generate and testing this on A100 and H100 on LLAMA3.2-3B...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
