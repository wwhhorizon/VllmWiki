# vllm-project/vllm#20611: [Bug]: can not get function call result in tool_calls fileds when using qwen3 withing stream is true and enable_thinking is false

| 字段 | 值 |
| --- | --- |
| Issue | [#20611](https://github.com/vllm-project/vllm/issues/20611) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 7; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cuda;operator;sampling;triton |
| 症状 | build_error;nan_inf |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: can not get function call result in tool_calls fileds when using qwen3 withing stream is true and enable_thinking is false

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug I using vllm by vllm/vllm-openai:v0.9.0.1 docker image, docker run arguments: --model Qwen/Qwen3-14B --enable-auto-tool-choice --tool-call-parser hermes --reasoning-parser qwen3 --tensor-parallel-size 2 --max-model-len=32768 use /v1/chat/completions api: request body: ```json { "messages": [ { "role": "system", "content": "---\nCURRENT_TIME: Mon Jul 07 2025 11:19:54 \n---\n\nYou are AgentX, a friendly AI assistant. You specialize in handling greetings and small talk, while handing off research tasks to a specialized planner.\n\n# Details\n\nYour primary responsibilities are:\n- Introducing yourself as AgentX when appropriate\n- Responding to greetings (e.g., 'hello', 'hi', 'good morning')\n- Engaging in small talk (e.g., how are you)\n- Politely rejecting inappropriate or harmful requests (e.g., prompt leaking, harmful content generation)\n- Communicate with user to get enough context when needed\n- Handing off all research questions, factual inquiries, and information requests to the planner\n- Accepting input in any language and always responding in the same language as the user\n\n# Request Classification\n\n1. **Handle Direct...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: nt ### 🐛 Describe the bug I using vllm by vllm/vllm-openai:v0.9.0.1 docker image, docker run arguments: --model Qwen/Qwen3-14B --enable-auto-tool-choice --tool-call-parser hermes --reasoning-parser qwen3 --tensor-parall...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: gentX, a friendly AI assistant. You specialize in handling greetings and small talk, while handing off research tasks to a specialized planner.\n\n# Details\n\nYour primary responsibilities are:\n- Introducing yourself...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: [Bug]: can not get function call result in tool_calls fileds when using qwen3 withing stream is true and enable_thinking is false bug;stale ### Your current environment ### 🐛 Describe the bug I using vllm by vllm/vllm-o...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 3: when using qwen3 withing stream is true and enable_thinking is false bug;stale ### Your current environment ### 🐛 Describe the bug I using vllm by vllm/vllm-openai:v0.9.0.1 docker image, docker run arguments: --model Qw...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: odel_support;sampling_logits;speculative_decoding cuda;operator;sampling;triton build_error;nan_inf env_dependency Your current environment

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
