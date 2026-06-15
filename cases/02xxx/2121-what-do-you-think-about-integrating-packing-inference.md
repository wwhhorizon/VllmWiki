# vllm-project/vllm#2121: What do you think about integrating packing inference?

| 字段 | 值 |
| --- | --- |
| Issue | [#2121](https://github.com/vllm-project/vllm/issues/2121) |
| 状态 | closed |
| 标签 | stale |
| 评论 | 5; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> What do you think about integrating packing inference?

### Issue 正文摘录

I see that vLLM does continuous batching, I wonder whether can we incorporate packing into continuous batching. The idea off the top of my head is using the user defined maximum sequence length and maximum token, we can actually concat/pack the input tokens together (in the same continuous fashion). Given: - Amount of input sequences to pack (`amt_input_seq`) - Maximum sequence length (`max_seq_len`) - Maximum tokens to generate (`max_tokens`) - Total input tokens (`total_input_tokens`), where `total_input_tokens` is the total number of tokens from packing a number of different input sequences (`amt_input_seq`) together Condition to optimise for packing: ( `amt_input_seq` * `max_tokens`) + `total_input_tokens` <= `max_seq_len` Basically, instead of continuous batch and pad, we continuous batch and pack to fully utilised the gpu. What do you think?

## 候选优化模式

- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: What do you think about integrating packing inference? stale I see that vLLM does continuous batching, I wonder whether can we incorporate packing into continuous batching. The idea off the top of my head is using the u...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
