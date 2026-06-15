# vllm-project/vllm#15680: [Bug]: Qwen-2-vl inference question about max_seq_length

| 字段 | 值 |
| --- | --- |
| Issue | [#15680](https://github.com/vllm-project/vllm/issues/15680) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 5; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: Qwen-2-vl inference question about max_seq_length

### Issue 正文摘录

### Your current environment ![Image](https://github.com/user-attachments/assets/a7af3a14-1dea-4378-aebc-6dfdf74f04ca) ![Image](https://github.com/user-attachments/assets/51ab2519-076e-4f3c-866b-cde02b231029) ### 🐛 Describe the bug My model is a fine-tuned qwen2-vl In fine-tuning I set max_seq_length but it seems that vllm defaults to this parameter, does this have an effect on the... There are also some warnings about api calls, the model is reasoning slower, the I'm wondering if it's because when max_seq_length exceeds my model settings, it causes the optimization to fail, the ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: [Bug]: Qwen-2-vl inference question about max_seq_length bug;stale ### Your current environment ![Image](https://github.com/user-attachments/assets/a7af3a14-1dea-4378-aebc-6dfdf74f04ca) ![Image](https://github.com/user-...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: the ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: [Bug]: Qwen-2-vl inference question about max_seq_length bug;stale ### Your current environment ![Image](https://github.com/user-attachments/assets/a7af3a14-1dea-4378-aebc-6dfdf74f04ca) ![Image](https://github.com/user-...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
