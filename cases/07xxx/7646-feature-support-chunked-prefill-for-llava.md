# vllm-project/vllm#7646: [Feature]: support chunked_prefill for llava

| 字段 | 值 |
| --- | --- |
| Issue | [#7646](https://github.com/vllm-project/vllm/issues/7646) |
| 状态 | closed |
| 标签 | feature request;stale |
| 评论 | 4; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Feature]: support chunked_prefill for llava

### Issue 正文摘录

### 🚀 The feature, motivation and pitch I want to use this feature to speed up the throughput in generation step under RLHF. ### Alternatives _No response_ ### Additional context also there is [a related comment](https://github.com/vllm-project/vllm/issues/6362#issuecomment-2228619748).

## 候选优化模式

- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 3: [Feature]: support chunked_prefill for llava feature request;stale ### 🚀 The feature, motivation and pitch I want to use this feature to speed up the throughput in generation step under RLHF. ### Alternatives _No respon...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: o use this feature to speed up the throughput in generation step under RLHF. ### Alternatives _No response_ ### Additional context also there is [a related comment](https://github.com/vllm-project/vllm/issues/6362#issue...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ure, motivation and pitch I want to use this feature to speed up the throughput in generation step under RLHF. ### Alternatives _No response_ ### Additional context also there is [a related comment](https://github.com/v...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
