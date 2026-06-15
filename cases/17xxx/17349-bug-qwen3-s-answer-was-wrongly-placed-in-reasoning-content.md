# vllm-project/vllm#17349: [Bug]: Qwen3's answer was wrongly placed in `reasoning_content`

| 字段 | 值 |
| --- | --- |
| Issue | [#17349](https://github.com/vllm-project/vllm/issues/17349) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 13; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: Qwen3's answer was wrongly placed in `reasoning_content`

### Issue 正文摘录

### Your current environment VLLM version: 0.85 ### 🐛 Describe the bug The command to serve Qwen3-32b: ``` VLLM_USE_V1=0 vllm serve Qwen/Qwen3-32B --served-model-name qwen3-32b -tp 4 --trust-remote-code --enable-reasoning --reasoning-parser deepseek_r1 ``` Here I use `VLLM_USE_V1=0` to enable guided output. The query command: ``` curl http://localhost:8000/v1/chat/completions \ -H "Content-Type: application/json" \ -d '{ "model": "qwen3-32b", "messages": [ {"role": "system", "content": "You are a helpful assistant."}, {"role": "user", "content": "你好"} ], "chat_template_kwargs": {"enable_thinking": false} }' ``` Here, I want to disable thinking temporarily. And I got: ```json ... "choices": [ { "finish_reason": "stop", "index": 0, "message": { "content": null, "role": "assistant", "tool_calls": null, "function_call": null, "refusal": null, "reasoning_content": "你好！有什么我可以帮你的吗？" } } ], ... ``` I think the reply should be in the `content` field instead of the `reasoning_content` field. ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: [Bug]: Qwen3's answer was wrongly placed in `reasoning_content` bug;stale ### Your current environment VLLM version: 0.85 ### 🐛 Describe the bug The command to serve Qwen3-32b: ``` VLLM_USE_V1=0 vllm serve Qwen/Qwen3-32...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: aced in `reasoning_content` bug;stale ### Your current environment VLLM version: 0.85 ### 🐛 Describe the bug The command to serve Qwen3-32b: ``` VLLM_USE_V1=0 vllm serve Qwen/Qwen3-32B --served-model-name qwen3-32b -tp...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: ld. ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 1: : "你好"} ], "chat_template_kwargs": {"enable_thinking": false} }' ``` Here, I want to disable thinking temporarily. And I got: ```json ... "choices": [ { "finish_reason": "stop", "index": 0, "message": { "content": null,...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: [Bug]: Qwen3's answer was wrongly placed in `reasoning_content` bug;stale ### Your current environment VLLM version: 0.85 ### 🐛 Describe the bug The command to serve Qwen3-32b: ``` VLLM_USE_V1=0 vllm serve Qwen/Qwen3-32...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
