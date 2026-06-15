# vllm-project/vllm#15814: [Bug]: Command-A model returns responses with unintended

| 字段 | 值 |
| --- | --- |
| Issue | [#15814](https://github.com/vllm-project/vllm/issues/15814) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 15; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: Command-A model returns responses with unintended

### Issue 正文摘录

### 🐛 Describe the bug 1. I used the latest vllm Docker with 0.8.2 version to run the CohereForAI/c4ai-command-a-03-2025 model in HuggingFace. 2. When I requested a message using the OpenAI Library, the response returned with an additional message appended at the end. The example of the bug is followings. ```python from openai import OpenAI openai_api_key= "EMPTY" openai_api_base= "http://localhost:8000/v1" client = OpenAI(api_key=openai_api_key, base_url=openai_api_base) completion = client.chat.completions.create( model="CohereForAI/c4ai-command-a-03-2025", messages=[ { "role": "user", "content": "Hello.", }, ], ) print("Chat completion results:") print(completion.choices[0].message.content) ``` ------------- Chat completion results: Hello! How can I assist you today? ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: th unintended bug;stale ### 🐛 Describe the bug 1. I used the latest vllm Docker with 0.8.2 version to run the CohereForAI/c4ai-command-a-03-2025 model in HuggingFace. 2. When I requested a message using the OpenAI Libra...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: [Bug]: Command-A model returns responses with unintended bug;stale ### 🐛 Describe the bug 1. I used the latest vllm Docker with 0.8.2 version to run the CohereForAI/c4ai-command-a-03-2025 model in HuggingFace. 2. When I...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: [Bug]: Command-A model returns responses with unintended bug;stale ### 🐛 Describe the bug 1. I used the latest vllm Docker with 0.8.2 version to run the CohereForAI/c4ai-command-a-03-2025 model in HuggingFace. 2. When I...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: y? ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), whi...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: sponses with unintended bug;stale ### 🐛 Describe the bug 1. I used the latest vllm Docker with 0.8.2 version to run the CohereForAI/c4ai-command-a-03-2025 model in HuggingFace. 2. When I requested a message using the Op...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
