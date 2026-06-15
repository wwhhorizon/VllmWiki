# vllm-project/vllm#11964: [Feature]: 【support tts llm like cosyvoice2.0】

| 字段 | 值 |
| --- | --- |
| Issue | [#11964](https://github.com/vllm-project/vllm/issues/11964) |
| 状态 | closed |
| 标签 | feature request;stale |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Feature]: 【support tts llm like cosyvoice2.0】

### Issue 正文摘录

### 🚀 The feature, motivation and pitch Do we have a plan to support voice models like cosyVoice? vllm does not currently support embedding input. cosyvoice2.0 repo: https://github.com/FunAudioLLM/CosyVoice/tree/main ![image](https://github.com/user-attachments/assets/0fd211b6-ce6e-44dd-beff-a08f4c232e86) ![image](https://github.com/user-attachments/assets/4cd8b412-b0ed-4e57-a7fc-0046765b185e) - [X] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: [Feature]: 【support tts llm like cosyvoice2.0】 feature request;stale ### 🚀 The feature, motivation and pitch Do we have a plan to support voice models like cosyVoice? vllm does not currently support embedding input. cos...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: ets/4cd8b412-b0ed-4e57-a7fc-0046765b185e) - [X] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), w...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: 🚀 The feature, motivation and pitch Do we have a plan to support voice models like cosyVoice? vllm does not currently support embedding input. cosyvoice2.0 repo: https://github.com/FunAudioLLM/CosyVoice/tree/main ![imag...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
