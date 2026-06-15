# vllm-project/vllm#32926: [Feature]: Add dedicated tool parser for Qwen2.5-Coder models

| 字段 | 值 |
| --- | --- |
| Issue | [#32926](https://github.com/vllm-project/vllm/issues/32926) |
| 状态 | open |
| 标签 | feature request;unstale |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Feature]: Add dedicated tool parser for Qwen2.5-Coder models

### Issue 正文摘录

### 🚀 The feature, motivation and pitch Qwen2.5-Coder models have no working tool call parser in vLLM. The [vLLM documentation](https://docs.vllm.ai/en/latest/features/tool_calling.html) recommend `--tool-call-parser hermes` for Qwen2.5, but Qwen2.5-Coder does not follow hermes format — it outputs ` ```json``` ` code blocks or plain JSON instead of ` ` tags. **Output format analysis (Qwen2.5-Coder-7B-Instruct, `temperature=0`):** | System prompt strategy | Model output format | vLLM parseable? | |------------------------|---------------------|:---------------:| | No format instruction | 100% ` ```json``` ` code blocks | No | | Hermes ` ` few-shot examples | 60% code blocks + 40% plain JSON | No | | ` ` tag few-shot examples | **100% ` ` tags** | **Yes** | The model outputs code blocks regardless of hermes prompting, but follows ` ` tag format with 100% compliance when given few-shot examples. **Why not reuse existing parsers?** - `hermes`: Model outputs code blocks/plain JSON, not ` ` tags - `qwen3_coder`: Expects XML (` `), not what Qwen2.5-Coder outputs **Proposal:** Add a dedicated `qwen2_5_coder` parser that extracts JSON tool calls from ` ` tags. Qwen2.5-Coder has no native t...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: [Feature]: Add dedicated tool parser for Qwen2.5-Coder models feature request;unstale ### 🚀 The feature, motivation and pitch Qwen2.5-Coder models have no working tool call parser in vLLM. The [vLLM documentation](https...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: [Feature]: Add dedicated tool parser for Qwen2.5-Coder models feature request;unstale ### 🚀 The feature, motivation and pitch Qwen2.5-Coder models have no working tool call parser in vLLM. The [vLLM documentation](https...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: escaping (known model limitation). ### Alternatives A server-side text fallback parser could extract tool calls from ` ```json``` ` code blocks, but this is fragile: - No clear boundary between tool call JSON and other...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: 192 ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 1: 2.5-Coder does not follow hermes format — it outputs ` ```json``` ` code blocks or plain JSON instead of ` ` tags. **Output format analysis (Qwen2.5-Coder-7B-Instruct, `temperature=0`):** | System prompt strategy | Mode...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
