# vllm-project/vllm#8854: [Feature]: Support system messages for Multi Modal models

| 字段 | 值 |
| --- | --- |
| Issue | [#8854](https://github.com/vllm-project/vllm/issues/8854) |
| 状态 | closed |
| 标签 | feature request |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Feature]: Support system messages for Multi Modal models

### Issue 正文摘录

### 🚀 The feature, motivation and pitch When running **vllm serve meta-llama/Llama-3.2-11B-Vision-Instruct** and using the Open AI Vision API, I get a message ERROR 09-26 07:37:07 serving_chat.py:155] Error in applying chat template from request: Prompting with images is incompatible with system messages. INFO: 10.0.0.75:50436 - "POST /v1/chat/completions HTTP/1.1" 400 Bad Request Could you remove these restrictions for multi-modal models since the user wants to use them for both text queries and/or images. I have a COT prompt in the system message that I would like to keep. ### Alternatives Open to suggestions as I have a COT prompt in the system message that I would like to keep. ### Additional context _No response_ ### Before submitting a new issue... - [X] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: [Feature]: Support system messages for Multi Modal models feature request ### 🚀 The feature, motivation and pitch When running **vllm serve meta-llama/Llama-3.2-11B-Vision-Instruct** and using the Open AI Vision API, I...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: se_ ### Before submitting a new issue... - [X] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: [Feature]: Support system messages for Multi Modal models feature request ### 🚀 The feature, motivation and pitch When running **vllm serve meta-llama/Llama-3.2-11B-Vision-Instruct** and using the Open AI Vision API, I...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
