# vllm-project/vllm#4266: [Usage]: speculative model 

| 字段 | 值 |
| --- | --- |
| Issue | [#4266](https://github.com/vllm-project/vllm/issues/4266) |
| 状态 | closed |
| 标签 | usage |
| 评论 | 10; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Usage]: speculative model 

### Issue 正文摘录

### How would you like to use vllm I am curious about the speculative model support in VLLM. I could not find much about speculation in docs, except the following flags: --speculative-model The name of the draft model to be used in speculative decoding. --num-speculative-tokens The number of speculative tokens to sample from the draft model in speculative decoding. I am curious if this is supported now. And possibly how to use. (If possible, prompt based decoding like in tranformers) thanks

## 候选优化模式

- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: [Usage]: speculative model usage ### How would you like to use vllm I am curious about the speculative model support in VLLM. I could not find much about speculation in docs, except the following flags: --speculative-mo...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: [Usage]: speculative model usage ### How would you like to use vllm I am curious about the speculative model support in VLLM. I could not find much about speculation in docs, except the following flags: --speculative-mo...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
