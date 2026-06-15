# vllm-project/vllm#21111: [Bug]: vllm config.py报错selected_task=next(iter(supported_tasks_lst))

| 字段 | 值 |
| --- | --- |
| Issue | [#21111](https://github.com/vllm-project/vllm/issues/21111) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: vllm config.py报错selected_task=next(iter(supported_tasks_lst))

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug vllm 0.6.4.post1 使用cosyvoice2报错selected_task=next(iter(supported_tasks_lst)) StopIteration ![Image](https://github.com/user-attachments/assets/3961ca6f-780b-44c2-b920-9f7a30201f89) ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: 89) ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: [Bug]: vllm config.py报错selected_task=next(iter(supported_tasks_lst)) bug;stale ### Your current environment ### 🐛 Describe the bug vllm 0.6.4.post1 使用cosyvoice2报错selected_task=next(iter(supported_tasks_lst)) StopIterati...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: [Bug]: vllm config.py报错selected_task=next(iter(supported_tasks_lst)) bug;stale ### Your current environment ### 🐛 Describe the bug vllm 0.6.4.post1 使用cosyvoice2报错selected_task=next(iter(supported_tasks_lst)) StopIterati...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
