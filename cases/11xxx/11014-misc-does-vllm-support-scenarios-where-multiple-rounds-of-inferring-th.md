# vllm-project/vllm#11014: [Misc]: Does vllm support scenarios where multiple rounds of inferring the same model require loading the weights of that model only once?

| 字段 | 值 |
| --- | --- |
| Issue | [#11014](https://github.com/vllm-project/vllm/issues/11014) |
| 状态 | closed |
| 标签 | stale |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Misc]: Does vllm support scenarios where multiple rounds of inferring the same model require loading the weights of that model only once?

### Issue 正文摘录

### Anything you want to discuss about vllm. As the title write: Sometimes i need to run the same model multiple times, but reloading the weights for that model each time is too time consuming. So i want to know if vllm can just load weight one time? ### Before submitting a new issue... - [X] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: me? ### Before submitting a new issue... - [X] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: Does vllm support scenarios where multiple rounds of inferring the same model require loading the weights of that model only once? stale ### Anything you want to discuss about vllm. As the title write: Sometimes i need...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: ring the same model require loading the weights of that model only once? stale ### Anything you want to discuss about vllm. As the title write: Sometimes i need to run the same model multiple times, but reloading the we...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
