# vllm-project/vllm#32380: [Feature]: Benchmak Scalability Optimization

| 字段 | 值 |
| --- | --- |
| Issue | [#32380](https://github.com/vllm-project/vllm/issues/32380) |
| 状态 | closed |
| 标签 | feature request;stale |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Feature]: Benchmak Scalability Optimization

### Issue 正文摘录

### 🚀 The feature, motivation and pitch The current vLLM benchmark does not easily to extend to support the addition of new performance metrics or datasets for other case, e.g., vllm omni. Our aim is: For new request: just add new ASYNC_REQUEST_FUNCS, and metric calculate metrics function For new dataset: provide interface to add new dataset support. ### Alternatives _No response_ ### Additional context _No response_ ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: [Feature]: Benchmak Scalability Optimization feature request;stale ### 🚀 The feature, motivation and pitch The current vLLM benchmark does not easily to extend to support the addition of new performance metrics or datas...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 2: request;stale ### 🚀 The feature, motivation and pitch The current vLLM benchmark does not easily to extend to support the addition of new performance metrics or datasets for other case, e.g., vllm omni. Our aim is: For...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: se_ ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
