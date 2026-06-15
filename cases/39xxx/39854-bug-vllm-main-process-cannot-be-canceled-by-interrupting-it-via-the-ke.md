# vllm-project/vllm#39854: [Bug]: vllm main process cannot be canceled by interrupting it via the keyboard

| 字段 | 值 |
| --- | --- |
| Issue | [#39854](https://github.com/vllm-project/vllm/issues/39854) |
| 状态 | open |
| 标签 | bug |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: vllm main process cannot be canceled by interrupting it via the keyboard

### Issue 正文摘录

### Your current environment None ### 🐛 Describe the bug I'm using a version of vllm main + vllm-ascend. I'm starting the model service using `vllm serve ...`, but I'm finding that I can't cancel the process by interrupting it with a keyboard shortcut. I'd like to know if this was intentional, or if there's some other special usage. ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: ### Your current environment None ### 🐛 Describe the bug I'm using a version of vllm main + vllm-ascend. I'm starting the model service using `vllm serve ...`, but I'm finding that I can't cancel the process by interrup...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: ge. ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: he bug I'm using a version of vllm main + vllm-ascend. I'm starting the model service using `vllm serve ...`, but I'm finding that I can't cancel the process by interrupting it with a keyboard shortcut. I'd like to know...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
