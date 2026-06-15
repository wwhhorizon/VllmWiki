# vllm-project/vllm#4104: [Doc]: Will both the prompts and generated kv cache reuse if `enable_prefix_caching` flag is ON? 

| 字段 | 值 |
| --- | --- |
| Issue | [#4104](https://github.com/vllm-project/vllm/issues/4104) |
| 状态 | closed |
| 标签 | documentation |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Doc]: Will both the prompts and generated kv cache reuse if `enable_prefix_caching` flag is ON? 

### Issue 正文摘录

### 📚 The doc issue will both the prompts and generated kv cache reuse if `enable_prefix_caching` flag is ON? In SGLang paper, they describe RadixAttention: ```text Instead of discarding the KV cache after finishing a generation request, our approach retains the KV cache for both prompts and generation results in a radix tree. ``` Assuming the first request is A and that vllm generates B, if the second request is A+B+C, will A+B already be cached? ### Suggest a potential alternative/fix _No response_

## 候选优化模式

- [KV Cache 容量、压缩与 Offload](../patterns/kv_cache_capacity_offload.md) - 分数 1: [Doc]: Will both the prompts and generated kv cache reuse if `enable_prefix_caching` flag is ON? documentation ### 📚 The doc issue will both the prompts and generated kv cache reuse if `enable_prefix_caching` flag is ON...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: ```text Instead of discarding the KV cache after finishing a generation request, our approach retains the KV cache for both prompts and generation results in a radix tree. ``` Assuming the first request is A and that vl...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
