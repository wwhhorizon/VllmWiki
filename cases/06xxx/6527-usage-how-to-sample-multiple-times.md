# vllm-project/vllm#6527: [Usage]: How to sample multiple times?

| 字段 | 值 |
| --- | --- |
| Issue | [#6527](https://github.com/vllm-project/vllm/issues/6527) |
| 状态 | closed |
| 标签 | usage;stale |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Usage]: How to sample multiple times?

### Issue 正文摘录

I am running inference as in [this](https://github.com/marcelbra/sft/blob/main/inference.py) script. I set `n=10` in the sampling parameters but for each request I only get one output. Could someone point me to the error? Or is it a bug with LoRA? I built my script on top of [this](github.com/vllm-project/vllm/blob/main/examples/multilora_inference.py) script.

## 候选优化模式

- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: [Usage]: How to sample multiple times? usage;stale I am running inference as in [this](https://github.com/marcelbra/sft/blob/main/inference.py) script. I set `n=10` in the sampling parameters but for each request I only...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
