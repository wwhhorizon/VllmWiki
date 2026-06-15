# vllm-project/vllm#39981: [Bug]: Mismatch between batch queue size and max-num-seqs

| 字段 | 值 |
| --- | --- |
| Issue | [#39981](https://github.com/vllm-project/vllm/issues/39981) |
| 状态 | open |
| 标签 | bug |
| 评论 | 0; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: Mismatch between batch queue size and max-num-seqs

### Issue 正文摘录

### Your current environment Phython3.12.12, vllm=0.11.2, model- GPT-OSS-120b ### 🐛 Describe the bug I think batch Queue size and max-num-sequences should have same value based on documentation below. But please find the vllm logs attached along with official vllm definition ### **OFFICIAL DOCUMENTATION** ### **ACTUAL LOGS:-** ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: [Bug]: Mismatch between batch queue size and max-num-seqs bug ### Your current environment Phython3.12.12, vllm=0.11.2, model- GPT-OSS-120b ### 🐛 Describe the bug I think batch Queue size and max-num-sequences should ha...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: -num-seqs bug ### Your current environment Phython3.12.12, vllm=0.11.2, model- GPT-OSS-120b ### 🐛 Describe the bug I think batch Queue size and max-num-sequences should have same value based on documentation below. But...
- [Bitwise 确定性与数值等价](../patterns/bitwise_determinism_equivalence.md) - 分数 1: [Bug]: Mismatch between batch queue size and max-num-seqs bug ### Your current environment Phython3.12.12, vllm=0.11.2, model- GPT-OSS-120b ### 🐛 Describe the bug I think batch Queue size and max-num-sequences should ha...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: cumentation below. But please find the vllm logs attached along with official vllm definition ### **OFFICIAL DOCUMENTATION** ### **ACTUAL LOGS:-** ### Before submitting a new issue... - [x] Make sure you already searche...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: [Bug]: Mismatch between batch queue size and max-num-seqs bug ### Your current environment Phython3.12.12, vllm=0.11.2, model- GPT-OSS-120b ### 🐛 Describe the bug I think batch Queue size and max-num-sequences should ha...

## Wiki 抽取状态

- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
