# vllm-project/vllm#37525: [Bug]: 启动qwen3.5-35B后反复kill进程：vllm.v1.engine exceptions enginedeaderror enginecore encountered an issue

| 字段 | 值 |
| --- | --- |
| Issue | [#37525](https://github.com/vllm-project/vllm/issues/37525) |
| 状态 | open |
| 标签 | bug |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: 启动qwen3.5-35B后反复kill进程：vllm.v1.engine exceptions enginedeaderror enginecore encountered an issue

### Issue 正文摘录

### Your current environment ![Image](https://github.com/user-attachments/assets/33b19f8a-96c6-4fda-8112-f775a444eda5) vllm版本为0.17.1 环境为4卡*80G（A800） ### 🐛 Describe the bug 无 ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: [Bug]: 启动qwen3.5-35B后反复kill进程：vllm.v1.engine exceptions enginedeaderror enginecore encountered an issue bug ### Your current environment ![Image](https://github.com/user-attachments/assets/33b19f8a-96c6-4fda-8112-f775a4...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
