# vllm-project/vllm#18988: [Usage]: Controll Deepseek R1 think or not

| 字段 | 值 |
| --- | --- |
| Issue | [#18988](https://github.com/vllm-project/vllm/issues/18988) |
| 状态 | closed |
| 标签 | usage;stale |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Usage]: Controll Deepseek R1 think or not

### Issue 正文摘录

### Your current environment ```text vLLM 0.9.0 ``` ### How would you like to use vllm I'd like to ask if there's any way to control whether DeepSeek R1 engages in "thinking" (i.e., its chain of thought process). Ollama, in a recent update (https://github.com/ollama/ollama/pull/10584), added a parameter to control this for DeepSeek R1. It seems vLLM doesn't have a similar implementation. I believe being able to control the "thinking" process could significantly reduce deployment costs, as deploying one DeepSeek R1 would essentially give us both DeepSeek R1 and V3 capabilities. ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: es. ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: DeepSeek R1 engages in "thinking" (i.e., its chain of thought process). Ollama, in a recent update (https://github.com/ollama/ollama/pull/10584), added a parameter to control this for DeepSeek R1. It seems vLLM doesn't...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: [Usage]: Controll Deepseek R1 think or not usage;stale ### Your current environment ```text vLLM 0.9.0 ``` ### How would you like to use vllm I'd like to ask if there's any way to control whether DeepSeek R1 engages in...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
