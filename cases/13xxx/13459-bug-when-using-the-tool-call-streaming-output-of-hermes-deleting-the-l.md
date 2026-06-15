# vllm-project/vllm#13459: [Bug]:  When using the tool call streaming output of hermes,deleting the last"}"of the parameter may result in missing information

| 字段 | 值 |
| --- | --- |
| Issue | [#13459](https://github.com/vllm-project/vllm/issues/13459) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]:  When using the tool call streaming output of hermes,deleting the last"}"of the parameter may result in missing information

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug ![Image](https://github.com/user-attachments/assets/85dff30b-cf61-46b9-8642-f93fd86adb12) This will result in missing"}"in the parameter ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: ter ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: t of hermes,deleting the last"}"of the parameter may result in missing information bug;stale ### Your current environment ### 🐛 Describe the bug ![Image](https://github.com/user-attachments/assets/85dff30b-cf61-46b9-864...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: leting the last"}"of the parameter may result in missing information bug;stale ### Your current environment ### 🐛 Describe the bug ![Image](https://github.com/user-attachments/assets/85dff30b-cf61-46b9-8642-f93fd86adb12...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
