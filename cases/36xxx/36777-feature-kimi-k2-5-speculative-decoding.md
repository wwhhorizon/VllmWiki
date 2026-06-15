# vllm-project/vllm#36777: [Feature]: Kimi K2.5 Speculative Decoding

| 字段 | 值 |
| --- | --- |
| Issue | [#36777](https://github.com/vllm-project/vllm/issues/36777) |
| 状态 | closed |
| 标签 | feature request |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Feature]: Kimi K2.5 Speculative Decoding

### Issue 正文摘录

### 🚀 The feature, motivation and pitch Kimi K2.5 is a 1T model which is heavy, but with speculative decoding, it's been shown that you can speed it up by 70% at batch size 1 with Eagle3. So this is a request to support it. I think much of what's already in other models like Qwen can be reused to support Kimi K2.5. Example from SGLang: https://huggingface.co/AQ-MedAI/Kimi-K25-eagle3 ### Alternatives _No response_ ### Additional context _No response_ ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: ature request ### 🚀 The feature, motivation and pitch Kimi K2.5 is a 1T model which is heavy, but with speculative decoding, it's been shown that you can speed it up by 70% at batch size 1 with Eagle3. So this is a requ...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: [Feature]: Kimi K2.5 Speculative Decoding feature request ### 🚀 The feature, motivation and pitch Kimi K2.5 is a 1T model which is heavy, but with speculative decoding, it's been shown that you can speed it up by 70% at...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: se_ ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
