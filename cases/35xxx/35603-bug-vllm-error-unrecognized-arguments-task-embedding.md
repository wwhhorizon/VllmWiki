# vllm-project/vllm#35603: [Bug]: vllm: error: unrecognized arguments: --task embedding

| 字段 | 值 |
| --- | --- |
| Issue | [#35603](https://github.com/vllm-project/vllm/issues/35603) |
| 状态 | open |
| 标签 | bug |
| 评论 | 12; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: vllm: error: unrecognized arguments: --task embedding

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug when I deploy Qwen3-VL-Embedding-8B,there is error vllm: error: unrecognized arguments: --task embedding ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: ing ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: g ### Your current environment ### 🐛 Describe the bug when I deploy Qwen3-VL-Embedding-8B,there is error vllm: error: unrecognized arguments: --task embedding ### Before submitting a new issue... - [x] Make sure you alr...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
