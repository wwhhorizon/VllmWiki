# vllm-project/vllm#9282: [Bug]: MiniCPM3-4B is support lora by --enable-lora ?

| 字段 | 值 |
| --- | --- |
| Issue | [#9282](https://github.com/vllm-project/vllm/issues/9282) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 5; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: MiniCPM3-4B is support lora by --enable-lora ?

### Issue 正文摘录

### Your current environment ### Model Input Dumps _No response_ ### 🐛 Describe the bug when i use this ![image](https://github.com/user-attachments/assets/9c8fe2fa-813b-42b6-97a8-e958e499ce73) then get the error ![image](https://github.com/user-attachments/assets/da6c06b5-22fb-4969-9833-708d0d000cf2) Does this model currently not support Lora but i read the describe ![image](https://github.com/user-attachments/assets/fe86b2e2-92f0-4c24-ba61-f49b9d26b659) it is supported ### Before submitting a new issue... - [X] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: ted ### Before submitting a new issue... - [X] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: support lora by --enable-lora ? bug ### Your current environment ### Model Input Dumps _No response_ ### 🐛 Describe the bug when i use this ![image](https://github.com/user-attachments/assets/9c8fe2fa-813b-42b6-97a8-e95...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
