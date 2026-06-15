# vllm-project/vllm#43771: [Bug]: Why does the video file uploaded to the LLM node parse out as files:[] during the data processing step?

| 字段 | 值 |
| --- | --- |
| Issue | [#43771](https://github.com/vllm-project/vllm/issues/43771) |
| 状态 | open |
| 标签 | bug |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: Why does the video file uploaded to the LLM node parse out as files:[] during the data processing step?

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug * LLM input: { "#files#": [ { "dify_model_identity": "__dify__file__", "extension": ".mp4", "filename": "normal_640_360.mp4", "id": null, "mime_type": "video/mp4", "reference": "dify-file-ref:eyJyZWNvcmRfaWQiOiI2MDI3OTVhMi1mNzU5LTRmZmMtOTA4Mi03ZWQ1OTZhMDljMjYifQ==", "related_id": "602795a2-f759-4ffc-9082-7ed596a09c26", "remote_url": "", "size": 1440220, "transfer_method": "local_file", "type": "video", "url": "/files/602795a2-f759-4ffc-9082-7ed596a09c26/file-preview?timestamp=1779875564&nonce=7c73e1449854f45ce47bf21263df4e89&sign=Z4dSC2H91eax5mEQislE1BQY1KKcHxiDWMLgNrzfbBc%3D" } ], "model_provider": "yangyaofei/vllm/vllm", "model_name": "qwen3.6-35b" } * process step: { "model_mode": "chat", "prompts": [ { "files": [], "role": "user", "text": "视频中是什么\n\n" } ], "usage": { "completion_price": "0", "completion_price_unit": "0", "completion_tokens": 755, "completion_unit_price": "0", "currency": "USD", "latency": 1.377, "prompt_price": "0", "prompt_price_unit": "0", "prompt_tokens": 13, "prompt_unit_price": "0", "time_to_first_token": 1.144, "time_to_generate": 0.233, "total_price": "0", "total_tokens": 768 }, "finish_reason": "stop"...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: 🐛 Describe the bug * LLM input: { "#files#": [ { "dify_model_identity": "__dify__file__", "extension": ".mp4", "filename": "normal_640_360.mp4", "id": null, "mime_type": "video/mp4", "reference": "dify-file-ref:eyJyZWNv...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 2: ens": 755, "completion_unit_price": "0", "currency": "USD", "latency": 1.377, "prompt_price": "0", "prompt_price_unit": "0", "prompt_tokens": 13, "prompt_unit_price": "0", "time_to_first_token": 1.144, "time_to_generate...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: " } ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
