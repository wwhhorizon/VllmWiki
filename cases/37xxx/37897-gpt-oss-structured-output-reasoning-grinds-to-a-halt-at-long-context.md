# vllm-project/vllm#37897: GPT-OSS structured output + reasoning grinds to a halt at long context

| 字段 | 值 |
| --- | --- |
| Issue | [#37897](https://github.com/vllm-project/vllm/issues/37897) |
| 状态 | closed |
| 标签 |  |
| 评论 | 0; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> GPT-OSS structured output + reasoning grinds to a halt at long context

### Issue 正文摘录

## Problem When using a GPT-OSS reasoning model with structured output (`guided_decoding` / `response_format`), generation speed degrades severely as output length increases. Long reasoning traces cause decoding to stall — and since this blocks the decode step, a single long-context request stalls the entire engine. I think it affects any GPT-OSS deployment using structured output with a reasoning model. The longer the reasoning trace, the worse it gets. ## Root cause `GptOssReasoningParser.is_reasoning_end()` scans backward through the entire accumulated token sequence on every decode step to detect the end of the reasoning phase. As the response grows, each step takes progressively longer. PR #30056 introduced `is_reasoning_end_streaming()` to solve this for single-token reasoning parsers (DeepSeek, BaseThinking, Step3). GPT-OSS was explicitly left unfixed because its end pattern (` final ... `) spans multiple tokens with a variable gap and couldn't use the same single-token optimization. ## Suggested fix Window the backward scan to just the tokens that could contain the end pattern (~23 + delta size), making per-step cost constant regardless of output length. See #35745.

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: GPT-OSS structured output + reasoning grinds to a halt at long context ## Problem When using a GPT-OSS reasoning model with structured output (`guided_decoding` / `response_format`), generation speed degrades severely a
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: ong reasoning traces cause decoding to stall — and since this blocks the decode step, a single long-context request stalls the entire engine. I think it affects any GPT-OSS deployment using structured output with a reas...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: oken reasoning parsers (DeepSeek, BaseThinking, Step3). GPT-OSS was explicitly left unfixed because its end pattern (` final ... `) spans multiple tokens with a variable gap and couldn't use the same single-token optimi...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 1: ncreases. Long reasoning traces cause decoding to stall — and since this blocks the decode step, a single long-context request stalls the entire engine. I think it affects any GPT-OSS deployment using structured output...

## Wiki 抽取状态

- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
