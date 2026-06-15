# vllm-project/vllm#19594: [Bug]: 通过openai兼容接口调用qwen2.5-vl模型解析mp4，一直没返回，也没出错

| 字段 | 值 |
| --- | --- |
| Issue | [#19594](https://github.com/vllm-project/vllm/issues/19594) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: 通过openai兼容接口调用qwen2.5-vl模型解析mp4，一直没返回，也没出错

### Issue 正文摘录

### Your current environment 使用的vllm是0.9.0.1 ### 🐛 Describe the bug messages = [ { "role": "user", "content": [ { "type": "video_url", "video_url": {"url": f"data:video/mp4;base64,{base64_video}"}, }, {"type": "text", "text": "What's in this video?"}, ], } ] 用的就是文档中的例子 https://docs.vllm.ai/en/v0.8.0/getting_started/examples/openai_chat_completion_client_for_multimodal.html 但发出请求后，一直等待，也没出错。 ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: [Bug]: 通过openai兼容接口调用qwen2.5-vl模型解析mp4，一直没返回，也没出错 bug ### Your current environment 使用的vllm是0.9.0.1 ### 🐛 Describe the bug messages = [ { "role": "user", "content": [ { "t
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: 出错。 ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
