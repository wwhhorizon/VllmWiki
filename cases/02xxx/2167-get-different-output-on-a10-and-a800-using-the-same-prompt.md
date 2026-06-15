# vllm-project/vllm#2167: Get different output on A10 and A800 using the same prompt

| 字段 | 值 |
| --- | --- |
| Issue | [#2167](https://github.com/vllm-project/vllm/issues/2167) |
| 状态 | closed |
| 标签 |  |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> Get different output on A10 and A800 using the same prompt

### Issue 正文摘录

I have deployed Qwen using vllm 0.2.3 on A800 and A10(2 A10 card) . I find out that I will get different output using the same prompt，but get same output on same gpu type. What should I do to get same output on different type of gpu? ### request ```json { "model": "Qwen", "messages": [ {"role": "system", "content": "You are a helpful assistant."}, {"role": "user", "content": "Hello, what is Apple"} ], "temperature": 0, "do_sample": false, "max_tokens": 512, "stop": [" ", " ", " "] } ``` **output on A800** ```json { "id": "cmpl-78a74b93e2124cd1b045f1cef84c3926", "object": "chat.completion", "created": 6997154, "model": "Qwen", "choices": [ { "index": 0, "message": { "role": "assistant", "content": "Apple is a technology company that designs, develops, and sells consumer electronics, computer software, and online services. It is headquartered in Cupertino, California, and was founded in 1976 by Steve Jobs, Steve Wozniak, and Ronald Wayne. Apple is known for its popular products such as the iPhone, iPad, Mac computer, and Apple Watch, as well as its operating systems, such as iOS and macOS. The company also offers a range of online services, including the App Store, Apple Music, and...

## 候选优化模式

- [Bitwise 确定性与数值等价](../patterns/bitwise_determinism_equivalence.md) - 分数 2: Get different output on A10 and A800 using the same prompt I have deployed Qwen using vllm 0.2.3 on A800 and A10(2 A10 card) . I find out that I will get different output using the same prompt，but get same output on sam...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: t different output on A10 and A800 using the same prompt I have deployed Qwen using vllm 0.2.3 on A800 and A10(2 A10 card) . I find out that I will get different output using the same prompt，but get same output on same...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 1: "Hello, what is Apple"} ], "temperature": 0, "do_sample": false, "max_tokens": 512, "stop": [" ", " ", " "] } ``` **output on A800** ```json { "id": "cmpl-78a74b93e2124cd1b045f1cef84c3926", "object": "chat.completion",...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: type. What should I do to get same output on different type of gpu? ### request ```json { "model": "Qwen", "messages": [ {"role": "system", "content": "You are a helpful assistant."}, {"role": "user", "content": "Hello,...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
