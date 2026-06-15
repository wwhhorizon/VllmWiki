# vllm-project/vllm#24190: [Feature]: Model FLOPs Utilization Reporting

| 字段 | 值 |
| --- | --- |
| Issue | [#24190](https://github.com/vllm-project/vllm/issues/24190) |
| 状态 | closed |
| 标签 | feature request;stale |
| 评论 | 6; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Feature]: Model FLOPs Utilization Reporting

### Issue 正文摘录

### 🚀 The feature, motivation and pitch I'm working on inference optimization and would like Model FLOPs Utilization (MFU) to be more readily reported by vLLM. It knows the model and it knows the hardware -- that's all you need! I'd like to open this issue for discussion on the best way to report MFU. Some open questions include: - where does this get dumped? periodically printed like the speculative decoding metrics? - should it be always on or require something like "/start_profile"? - should care be taken to make FLOP counts exact (and unreported if the model isn't supported) or can simple approximations be used? (e.g. 2x # params) - for hardware peak should we compile + check in vendor metrics? should we use simple approximations (e.g. number of tensorcores * clock)? In general I would like to volunteer to help build out a calculator. ### Alternatives manual calculation ### Additional context _No response_ ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 3: [Feature]: Model FLOPs Utilization Reporting feature request;stale ### 🚀 The feature, motivation and pitch I'm working on inference optimization and would like Model FLOPs Utilization (MFU) to be more readily reported b...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: approximations be used? (e.g. 2x # params) - for hardware peak should we compile + check in vendor metrics? should we use simple approximations (e.g. number of tensorcores * clock)? In general I would like to volunteer...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 2: ding metrics? - should it be always on or require something like "/start_profile"? - should care be taken to make FLOP counts exact (and unreported if the model isn't supported) or can simple approximations be used? (e....
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: se_ ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: [Feature]: Model FLOPs Utilization Reporting feature request;stale ### 🚀 The feature, motivation and pitch I'm working on inference optimization and would like Model FLOPs Utilization (MFU) to be more readily reported b...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
