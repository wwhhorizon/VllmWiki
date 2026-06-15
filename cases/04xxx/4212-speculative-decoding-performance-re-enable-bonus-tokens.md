# vllm-project/vllm#4212: [Speculative decoding] [Performance]: Re-enable bonus tokens

| 字段 | 值 |
| --- | --- |
| Issue | [#4212](https://github.com/vllm-project/vllm/issues/4212) |
| 状态 | closed |
| 标签 | performance |
| 评论 | 12; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Speculative decoding] [Performance]: Re-enable bonus tokens

### Issue 正文摘录

### Proposal to improve performance In https://github.com/vllm-project/vllm/pull/3951 we disable bonus tokens (token sampled from verifier model assuming all proposal tokens are accepted) because its KV is not generated for the draft model. We can fix this by "prefilling" the KV of bonus tokens in the draft model. Note that for proposal methods not requiring KV (e.g. prompt lookup), we can re-enable bonus tokens and get a speedup there. The impact of this performance improvement depends on the speculation length. For low K, e.g. 1, where the probability of accepting the single spec token is high (~= how aligned the draft model and target model are on the sequence), it has high impact because accepting 1 token allows us to emit 2 tokens (1 speculative and 1 bonus). Since we disable bonus tokens, we can now only emit 1 token (the accepted speculative one). For higher K the impact is less as the likelihood of accepting all speculative tokens is exponentially lower. https://github.com/vllm-project/vllm/blob/323f27b9048713cdbab31995265975842a937167/vllm/model_executor/layers/rejection_sampler.py#L311-L315

## 候选优化模式

- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 3: [Speculative decoding] [Performance]: Re-enable bonus tokens performance ### Proposal to improve performance In https://github.com/vllm-project/vllm/pull/3951 we disable bonus tokens (token sampled from verifier model as
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: ject/vllm/pull/3951 we disable bonus tokens (token sampled from verifier model assuming all proposal tokens are accepted) because its KV is not generated for the draft model. We can fix this by "prefilling" the KV of bo...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
