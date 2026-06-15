# vllm-project/vllm#16304: [Usage]: OpenAI client to vllm with lora

| 字段 | 值 |
| --- | --- |
| Issue | [#16304](https://github.com/vllm-project/vllm/issues/16304) |
| 状态 | closed |
| 标签 | usage;stale |
| 评论 | 4; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Usage]: OpenAI client to vllm with lora

### Issue 正文摘录

### Your current environment N/A ### How would you like to use vllm I want to connect to a model that is running online on a local GPU (running it with vllm serve). In the documentation, it shows how one can query the vllm server while providing the path to a lora module. The question that I now have is, how do I provide that path when using an OpenAI client to connect to the vllm instance? ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: ce? ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: ronment N/A ### How would you like to use vllm I want to connect to a model that is running online on a local GPU (running it with vllm serve). In the documentation, it shows how one can query the vllm server while prov...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: [Usage]: OpenAI client to vllm with lora usage;stale ### Your current environment N/A ### How would you like to use vllm I want to connect to a model that is running online on a local GPU (running it with vllm serve). I...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
