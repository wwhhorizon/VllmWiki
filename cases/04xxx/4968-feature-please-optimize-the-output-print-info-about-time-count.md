# vllm-project/vllm#4968: [Feature]: Please optimize the output print info about time count.

| 字段 | 值 |
| --- | --- |
| Issue | [#4968](https://github.com/vllm-project/vllm/issues/4968) |
| 状态 | closed |
| 标签 | feature request |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Feature]: Please optimize the output print info about time count.

### Issue 正文摘录

### 🚀 The feature, motivation and pitch ```text optimized outputs = [RequestOutput(request_id=0, prompt='Once upone a time, Once upone a time, Once upone a time, Once upone a time, Once upone a time, time', prompt_token_ids=[1, 9038, 701, 650, 263, 931, 29892, 9038, 701, 650, 263, 931, 29892, 9038, 701, 650, 263, 931, 29892, 9038, 701, 650, 263, 931, 29892, 9038, 701, 650, 263, 931, 29892, 931], prompt_logprobs=None, outputs=[CompletionOutput(index=0, text=', time, time, time, time, And little matching socks\n порвулира worst and best. 👣 You finallybfree', token_ids=[29892, 931, 29892, 931, 29892, 931, 29892, 931, 29892, 1126, 2217, 9686, 577, 4684, 13, 21463, 5944, 644, 494, 17322, 322, 1900, 29889, 29871, 243, 162, 148, 166, 887, 7146, 1635, 929], cumulative_logprob=-113.95129056274891, logprobs=None, finish_reason=length, stop_reason=None)], finished=True, metrics=RequestMetrics(arrival_time=1716350294.3862529, last_token_time=1716350294.3862529, first_scheduled_time=1716350294.3872488, first_token_time=1716350294.6243978, time_in_queue=0.0009958744049072266, finished_time=1716350296.0638247), lora_request=None)] ``` Please optimize the output print info about time count. Don't...

## 候选优化模式

- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: eature]: Please optimize the output print info about time count. feature request ### 🚀 The feature, motivation and pitch ```text optimized outputs = [RequestOutput(request_id=0, prompt='Once upone a time, Once upone a t...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
