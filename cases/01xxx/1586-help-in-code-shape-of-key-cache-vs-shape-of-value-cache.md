# vllm-project/vllm#1586: Help in code: Shape of Key cache vs shape of value cache:

| 字段 | 值 |
| --- | --- |
| Issue | [#1586](https://github.com/vllm-project/vllm/issues/1586) |
| 状态 | closed |
| 标签 |  |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> Help in code: Shape of Key cache vs shape of value cache:

### Issue 正文摘录

Our team is trying to implement BART and similar Encoder-Decoder Architecture for vllm. While exploring the code, we have ran into a curious question: The shape of cache while using GPT2 is as follows for key and value: key_cache : `[34652, 12, 8, 16, 8]` value_cache: `[34652, 12, 64, 16]` Here, the last 4 dims for key_cache are : [num_heads, head_size/x, num_tokens_per_block, x] The question is: 1. Role of x? 2. Why is the shape different for key and value 3. What is 34652 in the above shape? Kindly point us in the right direction on where we could learn more about this. Thanks.

## 候选优化模式

- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: cache: Our team is trying to implement BART and similar Encoder-Decoder Architecture for vllm. While exploring the code, we have ran into a curious question: The shape of cache while using GPT2 is as follows for key and...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 1: last 4 dims for key_cache are : [num_heads, head_size/x, num_tokens_per_block, x] The question is: 1. Role of x? 2. Why is the shape different for key and value 3. What is 34652 in the above shape? Kindly point us in th...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: of value cache: Our team is trying to implement BART and similar Encoder-Decoder Architecture for vllm. While exploring the code, we have ran into a curious question: The shape of cache while using GPT2 is as follows fo...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
