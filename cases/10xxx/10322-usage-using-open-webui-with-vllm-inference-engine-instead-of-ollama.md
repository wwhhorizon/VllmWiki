# vllm-project/vllm#10322: [Usage]: using open-webui with vLLM inference engine instead of ollama

| 字段 | 值 |
| --- | --- |
| Issue | [#10322](https://github.com/vllm-project/vllm/issues/10322) |
| 状态 | closed |
| 标签 | usage |
| 评论 | 18; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Usage]: using open-webui with vLLM inference engine instead of ollama

### Issue 正文摘录

### Your current environment No need for the environment ### How would you like to use vllm I want to run inference using openwebui (or something similar) using vLLM as a backend instead of ollama. I already launched the vLLM openai server api and open-webai. However, it is not working. ### Before submitting a new issue... - [X] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: to run inference using openwebui (or something similar) using vLLM as a backend instead of ollama. I already launched the vLLM openai server api and open-webai. However, it is not working. ### Before submitting a new is...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: ng. ### Before submitting a new issue... - [X] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: [Usage]: using open-webui with vLLM inference engine instead of ollama usage ### Your current environment No need for the environment ### How would you like to use vllm I want to run inference using openwebui (or someth...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
