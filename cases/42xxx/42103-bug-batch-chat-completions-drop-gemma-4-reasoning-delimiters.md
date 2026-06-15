# vllm-project/vllm#42103: [Bug]: Batch chat completions drop Gemma 4 reasoning delimiters

| 字段 | 值 |
| --- | --- |
| Issue | [#42103](https://github.com/vllm-project/vllm/issues/42103) |
| 状态 | open |
| 标签 |  |
| 评论 | 0; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: Batch chat completions drop Gemma 4 reasoning delimiters

### Issue 正文摘录

### Your current environment Observed in the current `vllm-project/vllm` development tree while inspecting the OpenAI chat completions batch endpoint. Relevant configuration: ```bash vllm serve google/gemma-4-... \ --reasoning-parser gemma4 ``` ### 🐛 Describe the bug `/v1/chat/completions/batch` does not preserve Gemma 4 reasoning delimiter tokens before reasoning parsing. Gemma 4 reasoning depends on special tokens such as ` ` and ` ` to delimit reasoning content. `Gemma4ReasoningParser.adjust_request()` sets `skip_special_tokens=False` so those delimiters remain in the generated text and can be parsed correctly. The regular `/v1/chat/completions` path calls the renderer with the reasoning parser, so `adjust_request()` runs before sampling params are built. The batch chat completions path did not pass the reasoning parser through preprocessing, so `Gemma4ReasoningParser.adjust_request()` was skipped. As a result, `skip_special_tokens` remained at the default `True`, the special delimiter tokens were dropped during detokenization, and the Gemma 4 reasoning parser could not reliably separate reasoning content from final answer content. This is related to the issue fixed for the reg...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: [Bug]: Batch chat completions drop Gemma 4 reasoning delimiters ### Your current environment Observed in the current `vllm-project/vllm` development tree while inspecting the OpenAI chat completions batch endpoint. Rele...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 2: rate(...)` - final `reasoning_parser.extract_reasoning(...)` 4. Add a regression test proving batch preprocessing invokes the reasoning parser adjustment and preserves the adjusted request objects. ### Before submitting...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: imiter tokens before reasoning parsing. Gemma 4 reasoning depends on special tokens such as ` ` and ` ` to delimit reasoning content. `Gemma4ReasoningParser.adjust_request()` sets `skip_special_tokens=False` so those de...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: justed request objects. ### Before submitting a new issue... - [x] I searched existing issues and PRs for Gemma 4 batch chat reasoning/parser reports. - [x] I found related regular-chat Gemma 4 parser work in #39081, bu...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 1: nt. `Gemma4ReasoningParser.adjust_request()` sets `skip_special_tokens=False` so those delimiters remain in the generated text and can be parsed correctly. The regular `/v1/chat/completions` path calls the renderer with...

## Wiki 抽取状态

- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
