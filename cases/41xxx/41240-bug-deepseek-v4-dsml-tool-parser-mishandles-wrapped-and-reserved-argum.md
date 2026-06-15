# vllm-project/vllm#41240: [Bug]: DeepSeek V4 DSML tool parser mishandles wrapped and reserved arguments

| 字段 | 值 |
| --- | --- |
| Issue | [#41240](https://github.com/vllm-project/vllm/issues/41240) |
| 状态 | closed |
| 标签 |  |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: DeepSeek V4 DSML tool parser mishandles wrapped and reserved arguments

### Issue 正文摘录

### Current behavior vLLM already has registered `deepseek_v4` tokenizer, tool-call parser, and reasoning parser support. Recent upstream work also added structural-tag support and generic DSV3.2/V4 non-streaming type conversion. There are still DeepSeek V4 DSML tool-call edge cases that do not round-trip OpenAI-compatible tool arguments correctly with the serving flag combination: ```bash --tokenizer-mode deepseek_v4 \ --tool-call-parser deepseek_v4 \ --enable-auto-tool-choice \ --reasoning-parser deepseek_v4 ``` ### Problems The remaining parser/tokenizer gaps are: - DSML parameter parsing should respect the `string="true|false"` attribute and use the request tool schema / JSON fallback for non-string values - model-emitted single `arguments` or `input` wrapper parameters should be unwrapped when those names are not actual fields in the requested tool schema - real tool schema parameters named `arguments` should not be confused with OpenAI tool-call wrapper semantics - streaming responses that end while plain text is being held because it looks like the start of a DSML marker, for example `2 <`, should flush that text ### Expected behavior The DeepSeek V4 tokenizer/parser path s...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: added structural-tag support and generic DSV3.2/V4 non-streaming type conversion. There are still DeepSeek V4 DSML tool-call edge cases that do not round-trip OpenAI-compatible tool arguments correctly with the serving...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: e `string="true|false"` attribute and use the request tool schema / JSON fallback for non-string values - model-emitted single `arguments` or `input` wrapper parameters should be unwrapped when those names are not actua...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: [Bug]: DeepSeek V4 DSML tool parser mishandles wrapped and reserved arguments ### Current behavior vLLM already has registered `deepseek_v4` tokenizer, tool-call parser, and reasoning parser support. Recent upstream wor...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 1: r gaps are: - DSML parameter parsing should respect the `string="true|false"` attribute and use the request tool schema / JSON fallback for non-string values - model-emitted single `arguments` or `input` wrapper paramet...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: and use the request tool schema / JSON fallback for non-string values - model-emitted single `arguments` or `input` wrapper parameters should be unwrapped when those names are not actual fields in the requested tool sch...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
