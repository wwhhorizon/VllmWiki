# vllm-project/vllm#9995: [Bug]: For speculative decoding with a draft model, the "determine_num_available_blocks" only considers the memory usage of the target model

| 字段 | 值 |
| --- | --- |
| Issue | [#9995](https://github.com/vllm-project/vllm/issues/9995) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | attention_kv_cache;distributed_parallel;model_support;speculative_decoding |
| 子分类 | memory |
| Operator 关键词 | cache;cuda |
| 症状 | oom |
| 根因提示 | shape |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: For speculative decoding with a draft model, the "determine_num_available_blocks" only considers the memory usage of the target model

### Issue 正文摘录

### Your current environment unrelated ### Model Input Dumps unrelated ### 🐛 Describe the bug For speculative decoding with a draft model, my understanding is that the `determine_num_available_blocks` only considers the target model's memory usage: https://github.com/vllm-project/vllm/blob/main/vllm/spec_decode/spec_decode_worker.py#L361-L362. It does not consider the memory usage of the draft model, and it might cause cuda OOM. For example, in one of my experiment, I used llama3.1-70b-instruct as the target model and llama3.1-8b-instruct as the draft model. I set `tensor-parallel-size` as 4 and set the `speculative-draft-tensor-parallel-size` as 1 to reduce the communication overhead. If I set a high value for `gpu_memory_utilization`, for example, 0.99, it would throw OOM error because it overestimated the available kv cache size during profile run. If I set a quite smaller value of `gpu_memory_utilization`, for example, 0.8, it does not have enough memory. Thus, it might be tedious for users of vLLM to set this value and the OOM error is unexpected during the run time. **Misc**: For parameter `speculative-draft-tensor-parallel-size`, vLLM only supports two modes: either not set...

## 候选优化模式

- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 4: [Bug]: For speculative decoding with a draft model, the "determine_num_available_blocks" only considers the memory usage of the target model bug;stale ### Your current environment unrelated ### Model Input Dumps unrelat...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: oes not consider the memory usage of the draft model, and it might cause cuda OOM. For example, in one of my experiment, I used llama3.1-70b-instruct as the target model and llama3.1-8b-instruct as the draft model. I se...
- [KV Cache 容量、压缩与 Offload](../patterns/kv_cache_capacity_offload.md) - 分数 2: ot consider the memory usage of the draft model, and it might cause cuda OOM. For example, in one of my experiment, I used llama3.1-70b-instruct as the target model and llama3.1-8b-instruct as the draft model. I set `te...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: [Bug]: For speculative decoding with a draft model, the "determine_num_available_blocks" only considers the memory usage of the target model bug;stale ### Your current environment unrelated ### Model Input Dumps unrelat...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 2: ow OOM error because it overestimated the available kv cache size during profile run. If I set a quite smaller value of `gpu_memory_utilization`, for example, 0.8, it does not have enough memory. Thus, it might be tedio...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
