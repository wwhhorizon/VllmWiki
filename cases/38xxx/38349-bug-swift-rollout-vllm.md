# vllm-project/vllm#38349: [Bug]: 使用swift rollout启动vllm，推理结果乱码

| 字段 | 值 |
| --- | --- |
| Issue | [#38349](https://github.com/vllm-project/vllm/issues/38349) |
| 状态 | open |
| 标签 | bug |
| 评论 | 0; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: 使用swift rollout启动vllm，推理结果乱码

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug 1、启动脚本 swift rollout \ --model $MODEL_PATH \ --model_type qwen3_vl \ --host 127.0.0.1 \ --port 8001 \ --vllm_tensor_parallel_size 1 \ --vllm_data_parallel_size 1 2、http请求返回结果乱码 [ { "response": { "model": "checkpoint-56", "choices": [ { "index": 0, "message": { "role": "assistant", "content": " inmates Ctrl\")] Ctrl\")] Ctrl\")] Ctrl\")] Ctrl\")] Ctrl\")] Ctrl\")] Ctrl\")] Ctrl\")] Ctrl\")] Ctrl\")] Ctrl\")] Ctrl\")] Ctrl\")] Ctrl\")] Ctrl\")] Ctrl\")] Ctrl\")] Ctrl\")] Ctrl\")] Ctrl\")] Ctrl\")] Ctrl\")] Ctrl\")] Ctrl\")] Ctrl\")] Ctrl\")] Ctrl\")] Ctrl\")] Ctrl\")] Ctrl\")] Ctrl", "tool_calls": null, "reasoning_content": null }, "finish_reason": "length", "logprobs": null, "token_ids": null } ], "usage": { "prompt_tokens": 40, "completion_tokens": 64, "total_tokens": 104 }, "id": "1", "object": "chat.completion", "created": 1774597539, "prompt_token_ids": null, "images_size": null }, "messages": null, "response_token_ids": [], "response_loss_mask": [], "rollout_infos": {}, "rollout_logprobs": [] } ] 3、疑问 使用vllm serve启动服务，http请求结果正常 ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: rrent environment ### 🐛 Describe the bug 1、启动脚本 swift rollout \ --model $MODEL_PATH \ --model_type qwen3_vl \ --host 127.0.0.1 \ --port 8001 \ --vllm_tensor_parallel_size 1 \ --vllm_data_parallel_size 1 2、http请求返回结果乱码 [...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: 果正常 ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
