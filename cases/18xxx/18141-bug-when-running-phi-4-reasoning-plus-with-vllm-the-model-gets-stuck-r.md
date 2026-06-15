# vllm-project/vllm#18141: [Bug]: When running phi-4-reasoning-plus with vLLM, the model gets stuck repeating reasoning phrases

| 字段 | 值 |
| --- | --- |
| Issue | [#18141](https://github.com/vllm-project/vllm/issues/18141) |
| 状态 | closed |
| 标签 | bug;usage;stale |
| 评论 | 21; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: When running phi-4-reasoning-plus with vLLM, the model gets stuck repeating reasoning phrases

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug Using vllm/vllm-openai:v0.8.5.post1 docker image version to serve huggingface Phi-4-reasoning-plus model but the model gets stuck repeating reasoning phrases/keeps on reasoning. Serving this model, using flags -enable-reasoning --reasoning-parser deepseek_r1. ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: ironment ### 🐛 Describe the bug Using vllm/vllm-openai:v0.8.5.post1 docker image version to serve huggingface Phi-4-reasoning-plus model but the model gets stuck repeating reasoning phrases/keeps on reasoning. Serving t...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: [Bug]: When running phi-4-reasoning-plus with vLLM, the model gets stuck repeating reasoning phrases bug;usage;stale ### Your current environment ### 🐛 Describe the bug Using vllm/vllm-openai:v0.8.5.post1 docker image v...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: 1. ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), whi...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: us with vLLM, the model gets stuck repeating reasoning phrases bug;usage;stale ### Your current environment ### 🐛 Describe the bug Using vllm/vllm-openai:v0.8.5.post1 docker image version to serve huggingface Phi-4-reas...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
