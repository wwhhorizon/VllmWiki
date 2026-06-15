# vllm-project/vllm#2559: Will vLLM supports Self-Speculative Decoding ？

| 字段 | 值 |
| --- | --- |
| Issue | [#2559](https://github.com/vllm-project/vllm/issues/2559) |
| 状态 | closed |
| 标签 |  |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> Will vLLM supports Self-Speculative Decoding ？

### Issue 正文摘录

github repo: https://github.com/dilab-zju/self-speculative-decoding Using partial layers for guess, and achive about 1.78x speed up. No draft model, the only thing needed to be cared is kv cache. Seems supports samping decoding. Cause the hidden size and intermediate size is same，so the kv cache is reusable, the only thing need to do is to kv cache memory reclaim when reject tokens. What will the future of VLLM speculative sampling look like? Is there a rough plan? @cadedaniel @LiuXiaoxuanPKU

## 候选优化模式

- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: Will vLLM supports Self-Speculative Decoding ？ github repo: https://github.com/dilab-zju/self-speculative-decoding Using partial layers for guess, and achive about 1.78x speed up. No draft model, the only thing needed t...
- [KV Cache 容量、压缩与 Offload](../patterns/kv_cache_capacity_offload.md) - 分数 1: ut 1.78x speed up. No draft model, the only thing needed to be cared is kv cache. Seems supports samping decoding. Cause the hidden size and intermediate size is same，so the kv cache is reusable, the only thing need to...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: ing partial layers for guess, and achive about 1.78x speed up. No draft model, the only thing needed to be cared is kv cache. Seems supports samping decoding. Cause the hidden size and intermediate size is same，so the k...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
