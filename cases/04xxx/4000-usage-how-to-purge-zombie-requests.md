# vllm-project/vllm#4000: [Usage]: How to purge zombie requests

| 字段 | 值 |
| --- | --- |
| Issue | [#4000](https://github.com/vllm-project/vllm/issues/4000) |
| 状态 | closed |
| 标签 | bug;usage;stale |
| 评论 | 12; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Usage]: How to purge zombie requests

### Issue 正文摘录

### Your current environment When testing vLLM I noticed that sometimes when I have a client makes a request and the client terminates abnormally, the request still is shown as running on the vLLM server. Is there a way to send a signal to vLLM to purge the existing queue and reset? Of course, I can just kill the server and restart it, but because vLLM takes a long time to start-up (almost an hour) I want to find a way to avoid that. ### How would you like to use vllm I want to run inference of a [specific model](put link here). I don't know how to integrate it with vllm.

## 候选优化模式

- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 3: [Usage]: How to purge zombie requests bug;usage;stale ### Your current environment When testing vLLM I noticed that sometimes when I have a client makes a request and the client terminates abnormally, the request still...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: t. ### How would you like to use vllm I want to run inference of a [specific model](put link here). I don't know how to integrate it with vllm.
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: # How would you like to use vllm I want to run inference of a [specific model](put link here). I don't know how to integrate it with vllm.
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: purge zombie requests bug;usage;stale ### Your current environment When testing vLLM I noticed that sometimes when I have a client makes a request and the client terminates abnormally, the request still is shown as runn...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
