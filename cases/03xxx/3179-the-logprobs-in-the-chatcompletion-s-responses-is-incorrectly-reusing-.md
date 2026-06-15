# vllm-project/vllm#3179: The logprobs in the ChatCompletion's responses is incorrectly reusing the Completions's schema; not following the OpenAI API's spec

| 字段 | 值 |
| --- | --- |
| Issue | [#3179](https://github.com/vllm-project/vllm/issues/3179) |
| 状态 | closed |
| 标签 |  |
| 评论 | 8; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> The logprobs in the ChatCompletion's responses is incorrectly reusing the Completions's schema; not following the OpenAI API's spec

### Issue 正文摘录

According to the OpenAI's documentation, the logprobs are returned in a different format when using the Chat Completion API, which is different from the format used in the old Completions one: https://platform.openai.com/docs/api-reference/chat/create ![image1](https://github.com/vllm-project/vllm/assets/131767832/1a2e48f1-4031-4dcf-8217-885d45c62958) But vLLM uses the Completion API's way to return the logprobs for the ChatCompletion's responses too. This is the example chat completion output from the OpenAI API's documentation: ``` json { "id": "chatcmpl-123", "object": "chat.completion", "created": 1702685778, "model": "gpt-3.5-turbo-0125", "choices": [ { "index": 0, "message": { "role": "assistant", "content": "Hello" }, "logprobs": { "content": [ { "token": "Hello", "logprob": -0.31725305, "bytes": [72, 101, 108, 108, 111], "top_logprobs": [ { "token": "Hello", "logprob": -0.31725305, "bytes": [72, 101, 108, 108, 111] }, { "token": "Hi", "logprob": -1.3190403, "bytes": [72, 105] } ] } ] }, "finish_reason": "length" } ], "usage": { "prompt_tokens": 10, "completion_tokens": 1, "total_tokens": 11 }, "system_fingerprint": null } ``` And this is what vLLM is returning with commit...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: to the OpenAI's documentation, the logprobs are returned in a different format when using the Chat Completion API, which is different from the format used in the old Completions one: https://platform.openai.com/docs/api...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 1: completion", "created": 997761, "model": "Qwen/Qwen1.5-72B-Chat-GPTQ-Int4", "choices": [ { "index": 0, "message": { "role": "assistant", "content": "Hello" }, "logprobs": { "text_offset": [ 0 ], "token_logprob

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
