# vllm-project/vllm#15526: [Bug]: FunctionDefinition missing optional param strict

| 字段 | 值 |
| --- | --- |
| Issue | [#15526](https://github.com/vllm-project/vllm/issues/15526) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 7; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: FunctionDefinition missing optional param strict

### Issue 正文摘录

### Your current environment class FunctionDefinition(OpenAIBaseModel): name: str description: Optional[str] = None parameters: Optional[dict[str, Any]] = None but openapi need strict https://platform.openai.com/docs/guides/function-calling?api-mode=chat#strict-mode and ### 🐛 Describe the bug and when request carry strict , then vllm will return this error. [{'type': 'extra_forbidden', 'loc': ('body', 'tools', 0, 'function', 'strict'), 'msg': 'Extra inputs are not permitted' ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: [Bug]: FunctionDefinition missing optional param strict bug;stale ### Your current environment class FunctionDefinition(OpenAIBaseModel): name: str description: Optional[str] = None parameters: Optional[dict[str, Any]]...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: ed' ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: g;stale ### Your current environment class FunctionDefinition(OpenAIBaseModel): name: str description: Optional[str] = None parameters: Optional[dict[str, Any]] = None but openapi need strict https://platform.openai.com...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
