# vllm-project/vllm#4995: [Feature]: Chunked prefill + lora

| 字段 | 值 |
| --- | --- |
| Issue | [#4995](https://github.com/vllm-project/vllm/issues/4995) |
| 状态 | closed |
| 标签 | feature request;stale |
| 评论 | 13; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Feature]: Chunked prefill + lora

### Issue 正文摘录

### 🚀 The feature, motivation and pitch Currently lora doesn't work with chunked prefill because some of lora index logic doesn't cover the case where sampling is not required. This also means lora is not working with sampling_params do_sample=True. We need to add test cases for these. WIP https://github.com/vllm-project/vllm/pull/4994 ### Alternatives _No response_ ### Additional context _No response_

## 候选优化模式

- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 3: [Feature]: Chunked prefill + lora feature request;stale ### 🚀 The feature, motivation and pitch Currently lora doesn't work with chunked prefill because some of lora index logic doesn't cover the case where sampling is...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ora is not working with sampling_params do_sample=True. We need to add test cases for these. WIP https://github.com/vllm-project/vllm/pull/4994 ### Alternatives _No response_ ### Additional context _No response_

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
