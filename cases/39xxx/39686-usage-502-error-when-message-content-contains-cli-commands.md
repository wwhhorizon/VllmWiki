# vllm-project/vllm#39686: [Usage]: 502 Error When Message Content Contains CLI Commands

| 字段 | 值 |
| --- | --- |
| Issue | [#39686](https://github.com/vllm-project/vllm/issues/39686) |
| 状态 | closed |
| 标签 | usage |
| 评论 | 0; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Usage]: 502 Error When Message Content Contains CLI Commands

### Issue 正文摘录

### Your current environment I encountered an issue where the service returns a 502 error whenever the content field in the request includes certain CLI commands. The model service is deployed using the Docker image vllm/vllm-openai:v0.11.2 ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: includes certain CLI commands. The model service is deployed using the Docker image vllm/vllm-openai:v0.11.2 ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the c...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: 1.2 ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: ver the content field in the request includes certain CLI commands. The model service is deployed using the Docker image vllm/vllm-openai:v0.11.2 ### Before submitting a new issue... - [x] Make sure you already searched...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: where the service returns a 502 error whenever the content field in the request includes certain CLI commands. The model service is deployed using the Docker image vllm/vllm-openai:v0.11.2 ### Before submitting a new is...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
