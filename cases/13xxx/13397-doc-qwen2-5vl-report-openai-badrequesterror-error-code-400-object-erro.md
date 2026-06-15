# vllm-project/vllm#13397: [Doc]: Qwen2.5vl  report: openai.BadRequestError: Error code: 400 - {'object': 'error', 'message': 'At most 1 image(s) may be provided in one request.', 'type': 'BadRequestError', 'param': None, 'code': 400}

| 字段 | 值 |
| --- | --- |
| Issue | [#13397](https://github.com/vllm-project/vllm/issues/13397) |
| 状态 | closed |
| 标签 | documentation |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Doc]: Qwen2.5vl  report: openai.BadRequestError: Error code: 400 - {'object': 'error', 'message': 'At most 1 image(s) may be provided in one request.', 'type': 'BadRequestError', 'param': None, 'code': 400}

### Issue 正文摘录

### 📚 The doc issue Seems qwenvl2.5 now can only support 1 images. Not support for multi-images. single images, it works my code `chat_response = client.chat.completions.create( model="/Qwen2.5-VL-7B-Instruct", messages=[ {"role": "system", "content": "You are a helpful assistant."}, { "role": "user", "content": [ # { # "type": "image_url", # "image_url": { # "url": "https://modelscope.oss-cn-beijing.aliyuncs.com/resource/qwen.png" # }, # }, { "type": "image_url", "image_url": { "url": base64_qwen }, }, { "type": "image_url", "image_url": { "url": base64_qwen }, }, {"type": "text", "text": "What is the similarity between images?"}, ], }, ], ) print(chat_response.choices[0].message.content)` ### Suggest a potential alternative/fix _No response_ ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: [Doc]: Qwen2.5vl report: openai.BadRequestError: Error code: 400 - {'object': 'error', 'message': 'At most 1 image(s) may be provided in one request.', 'type': 'BadRequestError', 'param': None, 'code': 400} documentatio...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: se_ ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: [Doc]: Qwen2.5vl report: openai.BadRequestError: Error code: 400 - {'object': 'error', 'message': 'At most 1 image(s) may be provided in one request.', 'type': 'BadRequestError', 'param': None, 'code': 400} documentatio...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
