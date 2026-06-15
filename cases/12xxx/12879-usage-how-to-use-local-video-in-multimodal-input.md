# vllm-project/vllm#12879: [Usage]: How to use local video in multimodal input?

| 字段 | 值 |
| --- | --- |
| Issue | [#12879](https://github.com/vllm-project/vllm/issues/12879) |
| 状态 | closed |
| 标签 | usage |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Usage]: How to use local video in multimodal input?

### Issue 正文摘录

### Your current environment `from openai import OpenAI openai_api_key = "EMPTY" openai_api_base = "http://localhost:8000/v1" client = OpenAI( api_key=openai_api_key, base_url=openai_api_base, ) video_url = "http://commondatastorage.googleapis.com/gtv-videos-bucket/sample/ForBiggerFun.mp4" ## Use video url in the payload chat_completion_from_url = client.chat.completions.create( messages=[{ "role": "user", "content": [ { "type": "text", "text": "What's in this video?" }, { "type": "video_url", "video_url": { "url": video_url }, }, ], }], model=model, max_completion_tokens=64, ) result = chat_completion_from_url.choices[0].message.content print("Chat completion output from image url:", result)` ### How would you like to use vllm _No response_ ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: [Usage]: How to use local video in multimodal input? usage ### Your current environment `from openai import OpenAI openai_api_key = "EMPTY" openai_api_base = "http://localhost:8000/v1" client = OpenAI( api_key=openai_ap...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: eo in multimodal input? usage ### Your current environment `from openai import OpenAI openai_api_key = "EMPTY" openai_api_base = "http://localhost:8000/v1" client = OpenAI( api_key=openai_api_key, base_url=openai_api_ba...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: se_ ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
