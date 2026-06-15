# vllm-project/vllm#2935: How can i get metrics like {gpu_cache_usage, cpu_cache_usage, time_to_first_tokens, time_per_output_tokens, time_per_output_tokens} when using offline inference 

| 字段 | 值 |
| --- | --- |
| Issue | [#2935](https://github.com/vllm-project/vllm/issues/2935) |
| 状态 | closed |
| 标签 |  |
| 评论 | 0; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> How can i get metrics like {gpu_cache_usage, cpu_cache_usage, time_to_first_tokens, time_per_output_tokens, time_per_output_tokens} when using offline inference 

### Issue 正文摘录

Is there any metris api to call. For example : (Wrong ) start = time.perf_counter() # FIXME(woosuk): Do not use internal method. llm._run_engine(use_tqdm=True) end = time.perf_counter() Stats = llm.llm_engine._get_stats() llm.llm_engine.stat_logger._log_prometheus(Stats) return end - start Thanks a lot

## Wiki 抽取状态

- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
