# vllm-project/vllm#5777: [Bug]: vllm deploy internLM2 not stop until out of max model length

| 字段 | 值 |
| --- | --- |
| Issue | [#5777](https://github.com/vllm-project/vllm/issues/5777) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: vllm deploy internLM2 not stop until out of max model length

### Issue 正文摘录

### Your current environment vllm 0.5.0 pytroch 2.3.0 ### 🐛 Describe the bug python -m vllm.entrypoints.openai.api_server --model /data/resources/internlm2-chat-7b --served-model-name internlm2-chat-7b --trust-remote-code curl http://localhost:8000/v1/chat/completions \ > -H "Content-Type: application/json" \ > -d '{ > "model": "internlm2-chat-7b", > "messages": [ > {"role": "system", "content": "You are a helpful assistant."}, > {"role": "user", "content": "Introduce deep learning to me."} > ] > }' the response would be very long, it will not stop until max_model_length out of memory ![image](https://github.com/vllm-project/vllm/assets/55178251/836b5539-1c46-445f-922e-61ab72a8498b)

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: [Bug]: vllm deploy internLM2 not stop until out of max model length bug;stale ### Your current environment vllm 0.5.0 pytroch 2.3.0 ### 🐛 Describe the bug python -m vllm.entrypoints.openai.api_server --model /data/resou...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: [Bug]: vllm deploy internLM2 not stop until out of max model length bug;stale ### Your current environment vllm 0.5.0 pytroch 2.3.0 ### 🐛 Describe the bug python -m vllm.entrypoints.openai.api_server --model /data/resou...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
