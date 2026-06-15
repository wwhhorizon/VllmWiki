# vllm-project/vllm#7301: [Usage]: Acceptance rate for Speculative Decoding

| 字段 | 值 |
| --- | --- |
| Issue | [#7301](https://github.com/vllm-project/vllm/issues/7301) |
| 状态 | closed |
| 标签 | usage;stale |
| 评论 | 13; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Usage]: Acceptance rate for Speculative Decoding

### Issue 正文摘录

I have been running the scripts from [https://docs.vllm.ai/en/latest/models/spec_decode.html](https://docs.vllm.ai/en/latest/models/spec_decode.html ) on how to do speculative decoding with vLLM. However, it seems that the acceptance rate is not shown/outputted anywhere. Is there any way of computing it/accessing it?

## 候选优化模式

- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 3: [Usage]: Acceptance rate for Speculative Decoding usage;stale I have been running the scripts from [https://docs.vllm.ai/en/latest/models/spec_decode.html](https://docs.vllm.ai/en/latest/models/spec_decode.html ) on how...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: ale I have been running the scripts from [https://docs.vllm.ai/en/latest/models/spec_decode.html](https://docs.vllm.ai/en/latest/models/spec_decode.html ) on how to do speculative decoding with vLLM. However, it seems t...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ge;stale I have been running the scripts from [https://docs.vllm.ai/en/latest/models/spec_decode.html](https://docs.vllm.ai/en/latest/models/spec_decode.html ) on how to do speculative decoding with vLLM. However, it se...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
