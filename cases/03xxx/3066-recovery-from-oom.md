# vllm-project/vllm#3066: Recovery from OOM

| 字段 | 值 |
| --- | --- |
| Issue | [#3066](https://github.com/vllm-project/vllm/issues/3066) |
| 状态 | closed |
| 标签 | stale |
| 评论 | 4; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> Recovery from OOM

### Issue 正文摘录

I am instantiating an LLM class for local inference. I noticed that when an OOM error happens in `vllm.LLM.llm_engine.step()` and I capture it, previous requests are not aborted and would mess up with my next call to `LLM.generate`. I was wondering what is the proper way of recovering from OOM errors during inference?

## 候选优化模式

- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: Recovery from OOM stale I am instantiating an LLM class for local inference. I noticed that when an OOM error happens in `vllm.LLM.llm_engine.step()` and I capture it, previous requests are not aborted and would mess up...
- [KV Cache 容量、压缩与 Offload](../patterns/kv_cache_capacity_offload.md) - 分数 1: Recovery from OOM stale I am instantiating an LLM class for local inference. I noticed that when an OOM error happens in `vllm.LLM.llm_engine.step()` and I capture it, previous requests are not aborted and would mess up...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
