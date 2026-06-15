# vllm-project/vllm#2465: Problems in inference Qwen-14B with vLLMv0.1.7

| 字段 | 值 |
| --- | --- |
| Issue | [#2465](https://github.com/vllm-project/vllm/issues/2465) |
| 状态 | closed |
| 标签 |  |
| 评论 | 0; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> Problems in inference Qwen-14B with vLLMv0.1.7

### Issue 正文摘录

I used vLLM in deploy Qwen-14b-Chat, but I found there were problems in generation. Some letters like l, n, m can't be generated. Meanwhile the the word followed by "//" can't be decoded as well. If I update vLLM to the newest version ,will this problem be solved? Hope there is any suggestion .

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: lowed by "//" can't be decoded as well. If I update vLLM to the newest version ,will this problem be solved? Hope there is any suggestion .
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: Problems in inference Qwen-14B with vLLMv0.1.7 I used vLLM in deploy Qwen-14b-Chat, but I found there were problems in generation. Some letters like l, n, m can't be generated. Meanwhile the the word followed by "//" ca...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: , m can't be generated. Meanwhile the the word followed by "//" can't be decoded as well. If I update vLLM to the newest version ,will this problem be solved? Hope there is any suggestion .

## Wiki 抽取状态

- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
