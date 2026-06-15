# vllm-project/vllm#16914: [Bug]:  vllm can' t  serve  for Multi-audio input inference

| 字段 | 值 |
| --- | --- |
| Issue | [#16914](https://github.com/vllm-project/vllm/issues/16914) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 8; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]:  vllm can' t  serve  for Multi-audio input inference

### Issue 正文摘录

### Your current environment In the example at https://github.com/vllm-project/vllm/blob/main/examples/online_serving/openai_chat_completion_client_for_multimodal.py, there's a demo showing multi-image input inference. I want to refer to that example and use multi-audio input inference instead, but currently, only one audio from the batch is being processed. Does this mean that batch inference for audio is not supported at the moment? ### 🐛 Describe the bug my codes： data = { "model": "qwen2-audio-7b-instruct", "messages": [ { "role": "user", "content": [ {"type": "audio_url", "audio_url": {"url": data_uri1}}, {"type": "audio_url", "audio_url": {"url": data_uri2}}, {"type": "text", "text": "xxxx？"} ] } ], "temperature": 0.2, "top_p": 0.8, "max_tokens": 4096 } ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: vllm/blob/main/examples/online_serving/openai_chat_completion_client_for_multimodal.py, there's a demo showing multi-image input inference. I want to refer to that example and use multi-audio input inference instead, bu...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: 6 } ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: [Bug]: vllm can' t serve for Multi-audio input inference bug;stale ### Your current environment In the example at https://github.com/vllm-project/vllm/blob/main/examples/online_serving/openai_chat_completion_client_for_...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
