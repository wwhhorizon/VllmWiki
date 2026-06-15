# vllm-project/vllm#6785: [Feature]: Evaluate multiple ngram speculations in speculative decoding

| 字段 | 值 |
| --- | --- |
| Issue | [#6785](https://github.com/vllm-project/vllm/issues/6785) |
| 状态 | closed |
| 标签 | feature request;stale |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Feature]: Evaluate multiple ngram speculations in speculative decoding

### Issue 正文摘录

### 🚀 The feature, motivation and pitch During the ngram-spec-decode stage, I've always had a question: In RAG, there isn't just one document relevant to the answer; why don't we first let the large model generate 3 tokens, and then take all possible results in the N-gram? In simpler terms, imagine you're looking for an object in several rooms but can only carry three things at once. You might want to pick up some important items now so you won't forget them when carrying more stuff later. This way, you make sure your search is efficient and effective. ### Alternatives _No response_ ### Additional context _No response_

## 候选优化模式

- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 4: [Feature]: Evaluate multiple ngram speculations in speculative decoding feature request;stale ### 🚀 The feature, motivation and pitch During the ngram-spec-decode stage, I've always had a question: In RAG, there isn't j...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: but can only carry three things at once. You might want to pick up some important items now so you won't forget them when carrying more stuff later. This way, you make sure your search is efficient and effective. ### Al...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: rget them when carrying more stuff later. This way, you make sure your search is efficient and effective. ### Alternatives _No response_ ### Additional context _No response_
- [KV Cache 容量、压缩与 Offload](../patterns/kv_cache_capacity_offload.md) - 分数 1: ram? In simpler terms, imagine you're looking for an object in several rooms but can only carry three things at once. You might want to pick up some important items now so you won't forget them when carrying more stuff...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: st one document relevant to the answer; why don't we first let the large model generate 3 tokens, and then take all possible results in the N-gram? In simpler terms, imagine you're looking for an object in several rooms...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
