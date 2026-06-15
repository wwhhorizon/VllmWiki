# vllm-project/vllm#8706: [Usage]: Is there any difference between max_tokens and max_model_len?

| 字段 | 值 |
| --- | --- |
| Issue | [#8706](https://github.com/vllm-project/vllm/issues/8706) |
| 状态 | closed |
| 标签 | usage;stale |
| 评论 | 8; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Usage]: Is there any difference between max_tokens and max_model_len?

### Issue 正文摘录

### Your current environment ```text vllm=0.5.4 ``` llm = LLM( model=MODEL_NAME, trust_remote_code=True, gpu_memory_utilization=0.5, max_model_len=2048, tensor_parallel_size=2 ), sampling_params = SamplingParams( stop_token_ids=stop_token_ids, use_beam_search=True, temperature=0, best_of=3, max_tokens=1024 ), Is there any difference between max_tokens and max_model_len?

## 候选优化模式

- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: ams = SamplingParams( stop_token_ids=stop_token_ids, use_beam_search=True, temperature=0, best_of=3, max_tokens=1024 ), Is there any difference between max_tokens and max_model_len?
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: [Usage]: Is there any difference between max_tokens and max_model_len? usage;stale ### Your current environment ```text vllm=0.5.4 ``` llm = LLM( model=MODEL_NAME, trust_remote_code=True, gpu_memory_utilization=0.5, max...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: ge]: Is there any difference between max_tokens and max_model_len? usage;stale ### Your current environment ```text vllm=0.5.4 ``` llm = LLM( model=MODEL_NAME, trust_remote_code=True, gpu_memory_utilization=0.5, max_mod...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
