# vllm-project/vllm#11410: [RFC]: The two features i wish vllm has

| 字段 | 值 |
| --- | --- |
| Issue | [#11410](https://github.com/vllm-project/vllm/issues/11410) |
| 状态 | closed |
| 标签 | RFC;stale |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [RFC]: The two features i wish vllm has

### Issue 正文摘录

### Motivation. There are two features i wish vllm support: 1. `vllm auto-serve` this command takes a model and it tries different engine arguments for the hardware avialable to serve this model at the highest throughput possible for this model in the hardware avialable. 2. `vllm multiple-models-serve` this command takes multiple models and serve all of them on the hardware available (they get accessed through the model_name in openai library without have to make different servers with different ports just to host a couple of models) ### Proposed Change. - `vllm auto-serve` - `vllm multiple-models-serve` ### Feedback Period. okay ### CC List. Anyone who thinks this a good idea ### Any Other Things. You are doing great work guys ### Before submitting a new issue... - [X] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 2: arguments for the hardware avialable to serve this model at the highest throughput possible for this model in the hardware avialable. 2. `vllm multiple-models-serve` this command takes multiple models and serve all of t...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: uys ### Before submitting a new issue... - [X] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: features i wish vllm support: 1. `vllm auto-serve` this command takes a model and it tries different engine arguments for the hardware avialable to serve this model at the highest throughput possible for this model in t...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: [RFC]: The two features i wish vllm has RFC;stale ### Motivation. There are two features i wish vllm support: 1. `vllm auto-serve` this command takes a model and it tries different engine arguments for the hardware avia...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
