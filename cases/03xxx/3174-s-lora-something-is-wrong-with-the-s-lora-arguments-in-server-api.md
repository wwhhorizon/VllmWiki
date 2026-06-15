# vllm-project/vllm#3174: [S-LoRA] Something is wrong with the s-lora arguments in server_api

| 字段 | 值 |
| --- | --- |
| Issue | [#3174](https://github.com/vllm-project/vllm/issues/3174) |
| 状态 | closed |
| 标签 | stale |
| 评论 | 6; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [S-LoRA] Something is wrong with the s-lora arguments in server_api

### Issue 正文摘录

I notice that there is no --lora-modules argument in the `vllm.entrypoints.api_server`, which means I must add the lora local path when sending request. That's unrealistic. Because the client doesn't know the lora path. Any plan to fix it ?

## 候选优化模式

- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: [S-LoRA] Something is wrong with the s-lora arguments in server_api stale I notice that there is no --lora-modules argument in the `vllm.entrypoints.api_server`, which means I must add the lora local path when sending r...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
