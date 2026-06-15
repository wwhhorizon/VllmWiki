# vllm-project/vllm#2266: openai v1/completions api completion_stream_generator return two stops

| 字段 | 值 |
| --- | --- |
| Issue | [#2266](https://github.com/vllm-project/vllm/issues/2266) |
| 状态 | closed |
| 标签 |  |
| 评论 | 0; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> openai v1/completions api completion_stream_generator return two stops

### Issue 正文摘录

When I use the completion api, set stream to true two stops are returned ``` ... { "id": "cmpl-3a688b392f324adcb369c11d97d304c7", "created": 2421200, "model": "qwen-14b-chat-int4", "choices": [ { "index": 0, "text": "0", "logprobs": null, "finish_reason": null } ] } { "id": "cmpl-3a688b392f324adcb369c11d97d304c7", "created": 2421200, "model": "qwen-14b-chat-int4", "choices": [ { "index": 0, "text": "", "logprobs": null, "finish_reason": "stop". # first } ] } { "id": "cmpl-3a688b392f324adcb369c11d97d304c7", "created": 2421200, "model": "qwen-14b-chat-int4", "choices": [ { "index": 0, "text": "", "logprobs": null, "finish_reason": "stop" # second } ], "usage": { "prompt_tokens": 27, "total_tokens": 319, "completion_tokens": 292 } } ```

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: "id": "cmpl-3a688b392f324adcb369c11d97d304c7", "created": 2421200, "model": "qwen-14b-chat-int4", "choices": [ { "index": 0, "text": "0", "logprobs": null, "finish_reason": null } ] } { "id": "cmpl-3a688b392f324adcb369c...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 1: 324adcb369c11d97d304c7", "created": 2421200, "model": "qwen-14b-chat-int4", "choices": [ { "index": 0, "text": "0", "logprobs": null, "finish_reason": null } ] } { "id": "cmpl-3a688b392f324adcb369c11d97d304c7", "created...

## Wiki 抽取状态

- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
