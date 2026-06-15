# vllm-project/vllm#2549: Doubts about KV Cache and Obtaining LogProbs

| 字段 | 值 |
| --- | --- |
| Issue | [#2549](https://github.com/vllm-project/vllm/issues/2549) |
| 状态 | closed |
| 标签 |  |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> Doubts about KV Cache and Obtaining LogProbs

### Issue 正文摘录

Hi Thanks for the great library! I need to run inference on a ton of sequences and get their log probabilities. I have approximately 100K sequences which can be binned into groups of 100 which share a significant amount of common prefix. For example, I have 100 sequences which start with 'Wikipedia was built in' and have different suffixes. Does the library automatically figure out the optimal KV Cache? or can I specify it somehow? If I build batches of say size 200 where one batch might have 100 sequences starting with 'Wikipedia was built in' and another 100 starting with 'Google was built in', will the vLLM engine automatically optimize the KV cache to reuse the computation done for the prefix? Since I only need the Log Probs and I don't really need the next generated token, I've set max tokens to be generated as 1 but can I somehow eliminate the generation process and only get the log probs?

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: s the library automatically figure out the optimal KV Cache? or can I specify it somehow? If I build batches of say size 200 where one batch might have 100 sequences starting with 'Wikipedia was built in' and another 10...
- [KV Cache 容量、压缩与 Offload](../patterns/kv_cache_capacity_offload.md) - 分数 1: Doubts about KV Cache and Obtaining LogProbs Hi Thanks for the great library! I need to run inference on a ton of sequences and get their log probabilities. I have approximately 100K sequences which can be binned into g...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
