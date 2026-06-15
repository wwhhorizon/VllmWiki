# vllm-project/vllm#23546: [Feature]: FlexProcessing support

| 字段 | 值 |
| --- | --- |
| Issue | [#23546](https://github.com/vllm-project/vllm/issues/23546) |
| 状态 | closed |
| 标签 | feature request |
| 评论 | 4; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Feature]: FlexProcessing support

### Issue 正文摘录

### 🚀 The feature, motivation and pitch openai has recently added the [flex processing](https://platform.openai.com/docs/guides/flex-processing?api-mode=responses) feature, it is a replacment for the Batch Processing, where the sent request will wait for the API to respond do we have any plan for implementing this? ### Alternatives an alternative method would be a way for the user, to prioritize the request's to let the model know that this request is more important, and this other one is not that important somthing like this example: ```python from openai import OpenAI client = OpenAI() # Example: adding a "priority" parameter to requests # Higher numbers = more important, lower numbers = background or less critical # A high-priority request (critical, must respond quickly) urgent_response = client.chat.completions.create( model="gpt-5", priority=10, # 👈 imaginary new feature messages=[ {"role": "system", "content": "You are a helpful assistant."}, {"role": "user", "content": "Summarize the top 3 breaking news headlines today."} ] ) print("URGENT:", urgent_response.choices[0].message.content) # A lower-priority request (nice to have, can wait longer) background_response = client....

## 候选优化模式

- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: [Feature]: FlexProcessing support feature request ### 🚀 The feature, motivation and pitch openai has recently added the [flex processing](https://platform.openai.com/docs/guides/flex-processing?api-mode=responses) featu...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: prioritize the request's to let the model know that this request is more important, and this other one is not that important somthing like this example: ```python from openai import OpenAI client = OpenAI() # Example: a...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: se_ ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: thod would be a way for the user, to prioritize the request's to let the model know that this request is more important, and this other one is not that important somthing like this example: ```python from openai import...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
