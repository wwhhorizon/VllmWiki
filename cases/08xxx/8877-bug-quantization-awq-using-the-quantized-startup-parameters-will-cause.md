# vllm-project/vllm#8877: [Bug]: --quantization=awq Using the quantized startup parameters will cause a restart

| 字段 | 值 |
| --- | --- |
| Issue | [#8877](https://github.com/vllm-project/vllm/issues/8877) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: --quantization=awq Using the quantized startup parameters will cause a restart

### Issue 正文摘录

### Your current environment ### Model Input Dumps ![微信截图_20240927082228](https://github.com/user-attachments/assets/a08cba85-f8ea-44ed-85b0-c1df6a521f17) Adding --quantization=awq or --quantization=gptq to the startup code will cause the system to restart if there are too many concurrent connections. ### 🐛 Describe the bug ![微信截图_20240927082228](https://github.com/user-attachments/assets/86ea40a7-b63e-46d9-a10c-f47f5f3ab85d) ### Before submitting a new issue... - [X] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 1: [Bug]: --quantization=awq Using the quantized startup parameters will cause a restart bug;stale ### Your current environment ### Model Input Dumps ![微信截图_20240927082228](https://github.com/user-attachments/assets/a08cba...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: 5d) ### Before submitting a new issue... - [X] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: ters will cause a restart bug;stale ### Your current environment ### Model Input Dumps ![微信截图_20240927082228](https://github.com/user-attachments/assets/a08cba85-f8ea-44ed-85b0-c1df6a521f17) Adding --quantization=awq or...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: tion=awq Using the quantized startup parameters will cause a restart bug;stale ### Your current environment ### Model Input Dumps ![微信截图_20240927082228](https://github.com/user-attachments/assets/a08cba85-f8ea-44ed-85b0...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
