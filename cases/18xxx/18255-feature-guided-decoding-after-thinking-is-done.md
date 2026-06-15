# vllm-project/vllm#18255: [Feature]: Guided decoding after thinking is done

| 字段 | 值 |
| --- | --- |
| Issue | [#18255](https://github.com/vllm-project/vllm/issues/18255) |
| 状态 | closed |
| 标签 | feature request |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Feature]: Guided decoding after thinking is done

### Issue 正文摘录

### 🚀 The feature, motivation and pitch I want to activate Guided Decoding while performing thinking, which is an advantage of the CoT model. I tried to use the guided decoding function to get a response in json format using Deepseek-R1. However, when the Guided Decoding function is turned on, the token that breaks the json format is masked, so the token is not generated, and the thinking process is not performed. The quality of the answer decreases due to the inability to think about the strength of the CoT model. Another problem is that when you want to receive a json response using the with_structure_output method in langchain, when you activate --enable-reasoning in vllm, the json response is filled the reasoning_content field rather than the content field after parsing, causing an exception. ### Alternatives To solve this problem, we request the function of deactivating guided decoding in the thinking process and activating guided decoding only when thinking is terminated and actual answers are generated. ### Additional context _No response_ ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the botto...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: ded Decoding while performing thinking, which is an advantage of the CoT model. I tried to use the guided decoding function to get a response in json format using Deepseek-R1. However, when the Guided Decoding function...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: se_ ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: [Feature]: Guided decoding after thinking is done feature request ### 🚀 The feature, motivation and pitch I want to activate Guided Decoding while performing thinking, which is an advantage of the CoT model. I tried to...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
