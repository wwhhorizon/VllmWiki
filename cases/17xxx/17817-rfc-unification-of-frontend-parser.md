# vllm-project/vllm#17817: [RFC]: Unification of frontend parser

| 字段 | 值 |
| --- | --- |
| Issue | [#17817](https://github.com/vllm-project/vllm/issues/17817) |
| 状态 | closed |
| 标签 | structured-output;RFC;unstale;tool-calling |
| 评论 | 6; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [RFC]: Unification of frontend parser

### Issue 正文摘录

## motivation https://github.com/vllm-project/vllm/issues/11522 (with draft implementation at https://github.com/vllm-project/vllm/pull/11554) aims to simplify the logics of the tool parser interface. However, this doesn't cover the cases for reasoning models (where we want to parse tokens generated within the thinking budgets, etc. Our current solutions involves a reasoning parser, which will soon be running into the same issue mentioned in #11522 when dealing with very long thinking budget). Additionally, the current implementations of tool calling are relatively fragile, and not scalable when adding more tool format. This RFC aims to build on top of some similar ideas from the RFC and unify both tool calling and reasoning parser logic for a more robust way for us to move forward, especially with v0.10.x. ## proposed change The workflow can be seen as follows: - function/tool calling format for supported models (defined by the LLMEngine) - Construct structural tags structured objects From vLLM perspective: ```bash ┌───────┐ │Prompt │ └───┬───┘ │ ▼ ┌────────────────────────────────┐ │ vLLM (OpenAI‑compatible FE) │ └───┬───────────────────┬────────┘ │ [tool / func‑call │ reasoning...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: ol parser interface. However, this doesn't cover the cases for reasoning models (where we want to parse tokens generated within the thinking budgets, etc. Our current solutions involves a reasoning parser, which will so...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: ragile, and not scalable when adding more tool format. This RFC aims to build on top of some similar ideas from the RFC and unify both tool calling and reasoning parser logic for a more robust way for us to move forward...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: [RFC]: Unification of frontend parser structured-output;RFC;unstale;tool-calling ## motivation https://github.com/vllm-project/vllm/issues/11522 (with draft implementation at https://github.com/vllm-project/vllm/pull/11...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 1: ntation of the parser would be ```python class Parser: tool: bool = False reasoning: bool = False def parse_tool_call(self, structural_tag: StructuralTagResult) -> ToolCallResult: ... def parse_tool_call_stream(self, st...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
