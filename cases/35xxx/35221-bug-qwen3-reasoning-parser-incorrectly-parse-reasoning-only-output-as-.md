# vllm-project/vllm#35221: [Bug]: `qwen3` reasoning parser incorrectly parse reasoning-only output as `content`

| 字段 | 值 |
| --- | --- |
| Issue | [#35221](https://github.com/vllm-project/vllm/issues/35221) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 0; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: `qwen3` reasoning parser incorrectly parse reasoning-only output as `content`

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug Using `--reasoning-parser qwen3`, Qwen3 model server that stops token generation in the reasoning phase (i.e. stops before generating ` ` token) sends the model output in the `content` field of the response body, contrary to the other reasoning parsers like `deepseek_v3` or `openai_gptoss`. # Reproducer This bug is only applicable to block-type chat completion requests: ```shell # launch script vllm serve Qwen/Qwen3-4B-Thinking-2507 \ --host 0.0.0.0 \ --port 8080 \ --reasoning-parser qwen3 # client request curl -s http://localhost:8080/v1/chat/completions \ -H 'Content-Type: application/json' \ -d '{"messages":[{"role":"user","content":"안녕?"}],"max_completion_tokens":5,"stream":false}' \ | jq '.choices[0]' ``` A sample model response is like: ```json { "index": 0, "message": { "role": "assistant", "content": "Thinking Process:\n\n1", "refusal": null, "annotations": null, "audio": null, "function_call": null, "tool_calls": [], "reasoning": null }, "logprobs": null, "finish_reason": "length", "stop_reason": null, "token_ids": null } ``` The model reasoning tokens are sent as `content` field. # Root Cause Analysis In https://github....

## 候选优化模式

- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 2: ek_v3` or `openai_gptoss`. # Reproducer This bug is only applicable to block-type chat completion requests: ```shell # launch script vllm serve Qwen/Qwen3-4B-Thinking-2507 \ --host 0.0.0.0 \ --port 8080 \ --reasoning-pa...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: [Bug]: `qwen3` reasoning parser incorrectly parse reasoning-only output as `content` bug ### Your current environment ### 🐛 Describe the bug Using `--reasoning-parser qwen3`, Qwen3 model server that stops token generati...
- [Bitwise 确定性与数值等价](../patterns/bitwise_determinism_equivalence.md) - 分数 1: to the other reasoning parsers like `deepseek_v3` or `openai_gptoss`. # Reproducer This bug is only applicable to block-type chat completion requests: ```shell # launch script vllm serve Qwen/Qwen3-4B-Thinking-2507 \ --...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: ue. ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: # Reproducer This bug is only applicable to block-type chat completion requests: ```shell # launch script vllm serve Qwen/Qwen3-4B-Thinking-2507 \ --host 0.0.0.0 \ --port 8080 \ --reasoning-parser qwen3 # client request...

## Wiki 抽取状态

- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
