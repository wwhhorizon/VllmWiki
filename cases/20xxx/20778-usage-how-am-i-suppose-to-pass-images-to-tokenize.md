# vllm-project/vllm#20778: [Usage]: How am I suppose to pass images to /tokenize?

| 字段 | 值 |
| --- | --- |
| Issue | [#20778](https://github.com/vllm-project/vllm/issues/20778) |
| 状态 | closed |
| 标签 | good first issue;usage;stale |
| 评论 | 10; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Usage]: How am I suppose to pass images to /tokenize?

### Issue 正文摘录

### Your current environment I believe this is env-independent. ### How would you like to use vllm I'm trying to figure out how I successfully get the token-counts for an image when working with a VLM. Every time I try to pass a messages array like: ``` "messages": [ { "role": "user", "content": [ { "type": "text", "text": "What is in this image?" }, { "type": "image_url", "image_url": { "url": "https://upload.wikimedia.org/wikipedia/commons/thumb/d/dd/Gfp-wisconsin-madison-the-nature-boardwalk.jpg/2560px-Gfp-wisconsin-madison-the-nature-boardwalk.jpg" } } ] ``` I just get the tokens of the string-literal text inside `content`. Same with like: ``` "content": [ { "type": "input_text", "text": "what's in this image?" }, { "type": "input_image", "image_url": f"data:image/jpeg;base64, ", }, ] ``` What's the correct way to pass a `messages` array to vLLM such that I get back the post-tokenizer, pre-model inputs? ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: how I successfully get the token-counts for an image when working with a VLM. Every time I try to pass a messages array like: ``` "messages": [ { "role": "user", "content": [ { "type": "text", "text": "What is in this i...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: ts? ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: e]: How am I suppose to pass images to /tokenize? good first issue;usage;stale ### Your current environment I believe this is env-independent. ### How would you like to use vllm I'm trying to figure out how I successful...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
