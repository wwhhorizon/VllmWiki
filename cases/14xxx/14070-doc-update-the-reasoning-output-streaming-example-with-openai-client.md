# vllm-project/vllm#14070: [Doc]: Update the reasoning output streaming example with OpenAI client

| 字段 | 值 |
| --- | --- |
| Issue | [#14070](https://github.com/vllm-project/vllm/issues/14070) |
| 状态 | closed |
| 标签 | documentation |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Doc]: Update the reasoning output streaming example with OpenAI client

### Issue 正文摘录

### 📚 The doc issue We are using requests in the reasoning output streaming example because at that time DeltaMessage does not support custom fields. https://github.com/vllm-project/vllm/blob/main/examples/online_serving/openai_chat_completion_with_reasoning_streaming.py Here is a contributor in SGLang community verified that OpenAI python client should work now. https://github.com/sgl-project/sglang/pull/3859#discussion_r1975199498 ### Suggest a potential alternative/fix _No response_ ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: se_ ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: ample with OpenAI client documentation ### 📚 The doc issue We are using requests in the reasoning output streaming example because at that time DeltaMessage does not support custom fields. https://github.com/vllm-projec...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
