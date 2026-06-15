# vllm-project/vllm#2308: performance and concurrency questions

| 字段 | 值 |
| --- | --- |
| Issue | [#2308](https://github.com/vllm-project/vllm/issues/2308) |
| 状态 | closed |
| 标签 |  |
| 评论 | 7; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> performance and concurrency questions

### Issue 正文摘录

I've done some experiments with vllm and read through the docs, but have not been able to get higher performing systems. I have a couple of questions. 1) Will using vllm on linux with a 4090 get faster results? I have been comparing with ollama and the speed is the same. 2) will I get automatic speed ups if I use the api web server vs offline batch inference? I did my initial experiments with offline batch inference doing only a single prompt at a time, and saw no speed difference. My current code does single llm requests at a time, not in batches. 3) to properly properly use vllm , do I need to convert my code to be concurrent/send batch requests?

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: llm on linux with a 4090 get faster results? I have been comparing with ollama and the speed is the same. 2) will I get automatic speed ups if I use the api web server vs offline batch inference? I did my initial experi...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: at a time, and saw no speed difference. My current code does single llm requests at a time, not in batches. 3) to properly properly use vllm , do I need to convert my code to be concurrent/send batch requests?

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
