# vllm-project/vllm#17951: [Bug]: 为什么我使用qwen3 30b-a3b时明显慢于ollama部署的

| 字段 | 值 |
| --- | --- |
| Issue | [#17951](https://github.com/vllm-project/vllm/issues/17951) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: 为什么我使用qwen3 30b-a3b时明显慢于ollama部署的

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug ollama上运行qwen3 30b-a3b有130token/s 但是vllm上运行qwen3 30b-a3b的gguf时显示不支持 运行awq量化时也只有30多token/s 正确使用的设置是什么啊 ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: [Bug]: 为什么我使用qwen3 30b-a3b时明显慢于ollama部署的 bug;stale ### Your current environment ### 🐛 Describe the bug ollama上运行qwen3 30b-a3b有130token/s 但是vllm上运行qwen3 30b-a3b的gguf时显示不支持 运行awq量化时也只有30多token/s 正确使用的设置是什么啊 ### Before sub...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: 什么啊 ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: [Bug]: 为什么我使用qwen3 30b-a3b时明显慢于ollama部署的 bug;stale ### Your current environment ### 🐛 Describe the bug ollama上运行qwen3 30b-a3b有130token/s 但是vllm上运行qwen3 30b-a3b的gguf时显示不支持 运行awq量化时也只有30多token/s 正确使用的设置是什么啊 ### Before sub...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
