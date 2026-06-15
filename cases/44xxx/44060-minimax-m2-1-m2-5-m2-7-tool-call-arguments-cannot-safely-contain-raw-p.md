# vllm-project/vllm#44060: MiniMax-M2.1/M2.5/M2.7 tool-call arguments cannot safely contain raw </parameter> delimiters

| 字段 | 值 |
| --- | --- |
| Issue | [#44060](https://github.com/vllm-project/vllm/issues/44060) |
| 状态 | open |
| 标签 |  |
| 评论 | 0; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> MiniMax-M2.1/M2.5/M2.7 tool-call arguments cannot safely contain raw </parameter> delimiters

### Issue 正文摘录

## Problem MiniMax-M2-series models use an XML-style tool-call format internally, with parameters encoded like: ```xml ... ``` When a string argument itself contains the raw delimiter text ` `, the argument becomes ambiguous. A common example is a file-writing tool asked to write XML content: ```xml ``` The parser cannot reliably distinguish a literal ` ` inside the argument value from the protocol delimiter closing the tool parameter. This can truncate tool-call arguments, especially for `write_file`-style tools. ## Official MiniMax API behavior I tested the official MiniMax API at `https://api.minimaxi.com/v1`, forcing a single `write_file(path: string, content: string)` tool call. Expected `content`: ```xml ``` Observed behavior by model: | Model | Non-streaming | Streaming | Notes | | --- | --- | --- | --- | | `MiniMax-M2` | Preserves the full raw XML content | Preserves the full raw XML content | Surprisingly not affected in this test | | `MiniMax-M2.1` | Truncates at the raw ` ` delimiter | Truncates at the raw ` ` delimiter | Affected | | `MiniMax-M2.5` | Truncates at the raw ` ` delimiter | Truncates at the raw ` ` delimiter | Affected | | `MiniMax-M2.7` | Truncates at the...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: safely contain raw </parameter> delimiters ## Problem MiniMax-M2-series models use an XML-style tool-call format internally, with parameters encoded like: ```xml ... ``` When a string argument itself contains the raw de...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: xml"} ``` Both official API paths lose the literal closing ` ` from the requested file content for the affected models. I also tested XML-escaped content with `MiniMax-M2.7`: ```text &lt;parameter&gt; &lt;hello&gt;&lt;/...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: r closing the tool parameter. This can truncate tool-call arguments, especially for `write_file`-style tools. ## Official MiniMax API behavior I tested the official MiniMax API at `https://api.minimaxi.com/v1`, forcing...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 1: nt vLLM MiniMax-M2 parser also uses XML-style delimiters for ` ` and ` ` blocks, so it has the same class of ambiguity when raw argument values contain protocol delimiter strings.
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ially for `write_file`-style tools. ## Official MiniMax API behavior I tested the official MiniMax API at `https://api.minimaxi.com/v1`, forcing a single `write_file(path: string, content: string)` tool call. Expected `...

## Wiki 抽取状态

- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
