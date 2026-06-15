# vllm-project/vllm#8121: [Usage]: Why Smaller max_num_batched_tokens achieves better ITL

| 字段 | 值 |
| --- | --- |
| Issue | [#8121](https://github.com/vllm-project/vllm/issues/8121) |
| 状态 | closed |
| 标签 | usage |
| 评论 | 0; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Usage]: Why Smaller max_num_batched_tokens achieves better ITL

### Issue 正文摘录

I have carefully read many issues/docs/webpages about `max_num_batched_tokens `, but I am confused about why smaller `max_num_batched_tokens` achieves better ITL because there are fewer prefills interrupting decodes. In my point of view, if the model parallelly runs more tokens, it will be faster? And if the total length of the one seq is bigger than `max_num_batched_tokens `, will it be stopped by this argument? Also another question: I find that docs notion it only for prefills, will it have the same treading for prefix-caching? These questions really matter me for setting the argument. Wish for your kindness support~ ### Before submitting a new issue... - [X] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: [Usage]: Why Smaller max_num_batched_tokens achieves better ITL usage I have carefully read many issues/docs/webpages about `max_num_batched_tokens `, but I am confused about why smaller `max_num_batched_tokens` achieve...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: ler `max_num_batched_tokens` achieves better ITL because there are fewer prefills interrupting decodes. In my point of view, if the model parallelly runs more tokens, it will be faster? And if the total length of the on...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: ere are fewer prefills interrupting decodes. In my point of view, if the model parallelly runs more tokens, it will be faster? And if the total length of the one seq is bigger than `max_num_batched_tokens `, will it be...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
