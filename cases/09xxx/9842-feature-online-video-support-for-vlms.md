# vllm-project/vllm#9842: [Feature]: Online video support for VLMs

| 字段 | 值 |
| --- | --- |
| Issue | [#9842](https://github.com/vllm-project/vllm/issues/9842) |
| 状态 | closed |
| 标签 | feature request |
| 评论 | 5; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Feature]: Online video support for VLMs

### Issue 正文摘录

### 🚀 The feature, motivation and pitch ### Online video support for VLMs vLLM already supports a large number of MultiModal Machine Learning visual models, some of which support image and video input，such as [Qwen2-VL](https://huggingface.co/Qwen/Qwen2-VL-2B-Instruct), [LLaVA-Onevision](https://huggingface.co/llava-hf/llava-onevision-qwen2-7b-ov-hf), etc. Referring to the implementation of image, this proposal adds support for video. Refer to the visual interfaces of OpenAI [(vision](https://platform.openai.com/docs/guides/vision) and [video](https://cookbook.openai.com/examples/gpt_with_vision_for_video_understanding)) and Google Gemini, the visual interface should ideally support inputs from Video URLs and base64. #### Image ```python chat_response = client.chat.completions.create( model="llava", messages=[{ "role": "user", "content": [ {"type": "text", "text": "What’s in this image?"}, {"type": "image_url", "image_url": {"url": f"data:image/png;base64,{image}"}}, ], }], ) ``` #### Video ```python chat_response = client.chat.completions.create( model="llava", messages=[{ "role": "user", "content": [ {"type": "text", "text": "What’s in this video?"}, {"type": "video_url", "video...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 6: [Feature]: Online video support for VLMs feature request ### 🚀 The feature, motivation and pitch ### Online video support for VLMs vLLM already supports a large number of MultiModal Machine Learning visual models, some...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: se_ ### Before submitting a new issue... - [X] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: [Feature]: Online video support for VLMs feature request ### 🚀 The feature, motivation and pitch ### Online video support for VLMs vLLM already supports a large number of MultiModal Machine Learning visual models, some...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
