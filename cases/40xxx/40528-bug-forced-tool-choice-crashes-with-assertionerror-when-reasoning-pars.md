# vllm-project/vllm#40528: [Bug]: Forced tool_choice crashes with AssertionError when reasoning_parser consumes all content

| 字段 | 值 |
| --- | --- |
| Issue | [#40528](https://github.com/vllm-project/vllm/issues/40528) |
| 状态 | open |
| 标签 |  |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: Forced tool_choice crashes with AssertionError when reasoning_parser consumes all content

### Issue 正文摘录

## Your current environment ``` vllm main branch (upstream/main commit 0008729ab) ``` ## Bug Description When using `--reasoning-parser` (e.g., `glm45`, `deepseek_r1`) with forced `tool_choice`, the server crashes with an `AssertionError` if the reasoning parser consumes the entire model output into ` ... ` tags, leaving `content` as `None` or empty string. This affects two `tool_choice` modes: 1. **`tool_choice: {type: "function", function: {name: "xxx"}}`** — `ToolChoiceFunction` path 2. **`tool_choice: {function: {name: "xxx"}}`** — `ChatCompletionNamedToolChoiceParam` path The `"required"` mode was partially fixed in a recent commit but the named function modes still crash. ## How to reproduce 1. Start vllm with a reasoning model and tool_choice support: ```bash vllm serve --reasoning-parser glm45 --enable-auto-tool-choice --tool-call-parser hermes ``` 2. Send a request with forced tool_choice where the model wraps all output in ` ` tags: ```python import openai client = openai.OpenAI(base_url="http://localhost:8000/v1") response = client.chat.completions.create( model=" ", messages=[{"role": "user", "content": "What's the weather in Beijing?"}], tools=[{ "type": "function", "...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: rced tool_choice where the model wraps all output in ` ` tags: ```python import openai client = openai.OpenAI(base_url="http://localhost:8000/v1") response = client.chat.completions.create( model=" ", messages=[{"role":...
- [Bitwise 确定性与数值等价](../patterns/bitwise_determinism_equivalence.md) - 分数 1: in a recent commit but the named function modes still crash. ## How to reproduce 1. Start vllm with a reasoning model and tool_choice support: ```bash vllm serve --reasoning-parser glm45 --enable-auto-tool-choice --tool...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: ne # 0 # 0` | ## Before submitting a new issue... - [x] I have searched for similar issues and couldn't find anything relevant. - [x] I have read the documentation.
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: hes with an `AssertionError` if the reasoning parser consumes the entire model output into ` ... ` tags, leaving `content` as `None` or empty string. This affects two `tool_choice` modes: 1. **`tool_choice: {type: "func...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: glm45 --enable-auto-tool-choice --tool-call-parser hermes ``` 2. Send a request with forced tool_choice where the model wraps all output in ` ` tags: ```python import openai client = openai.OpenAI(base_url="http://local...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
