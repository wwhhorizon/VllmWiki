# vllm-project/vllm#39769: [Feature]: vllm 的 api 添加支持 ollama 的风格

| 字段 | 值 |
| --- | --- |
| Issue | [#39769](https://github.com/vllm-project/vllm/issues/39769) |
| 状态 | open |
| 标签 | feature request |
| 评论 | 0; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Feature]: vllm 的 api 添加支持 ollama 的风格

### Issue 正文摘录

### 🚀 The feature, motivation and pitch 在vscode 中使用github copilot,自定义模型,只能选择ollama,如何可以使vllm 的 api 接口支持ollama 风格,以便某些ide 只支持ollama的使用 github copilot中因为openai的 api 接口无法修改baseurl,所以无法以openai的方式调用 ### Alternatives _No response_ ### Additional context _No response_ ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: se_ ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: [Feature]: vllm 的 api 添加支持 ollama 的风格 feature request ### 🚀 The feature, motivation and pitch 在vscode 中使用github copilot,自定义模型,只能选择ollama,如何可以使vllm 的 api 接口支持ollama 风格,以便某些ide 只支持ollama的使用 github copilot中因为openai的 api 接口...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: [Feature]: vllm 的 api 添加支持 ollama 的风格 feature request ### 🚀 The feature, motivation and pitch 在vscode 中使用github copilot,自定义模型,只能选择ollama,如何可以使vllm 的 api 接口支持ollama 风格,以便某些ide 只支持ollama的使用 github copilot中因为openai的 api 接口...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
