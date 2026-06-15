# vllm-project/vllm#27263: [Responses API] Support tool calling and ouput token streaming

| 字段 | 值 |
| --- | --- |
| Issue | [#27263](https://github.com/vllm-project/vllm/issues/27263) |
| 状态 | open |
| 标签 | unstale |
| 评论 | 10; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Responses API] Support tool calling and ouput token streaming

### Issue 正文摘录

Splitting off from #14721 > FYI a start has been made here https://github.com/vllm-project/vllm/pull/20504 > > That PR (which was merged to `main` on [7/9/2025](https://github.com/vllm-project/vllm/pull/20504#event-18495144925)) explicitly has an unchecked boxes for > > * [ ] Tool/functional calling support > * [ ] Output token streaming > > Any plans to implement those features? I think that is what is needed to support agentic coding tools like codex. See: > > * https://docs.vllm.ai/projects/recipes/en/latest/OpenAI/GPT-OSS.html#harmony-format-support _Originally posted by @bartlettroscoe in [#14721](https://github.com/vllm-project/vllm/issues/14721#issuecomment-3321963360)_

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: dex. See: > > * https://docs.vllm.ai/projects/recipes/en/latest/OpenAI/GPT-OSS.html#harmony-format-support _Originally posted by @bartlettroscoe in [#14721](https://github.com/vllm-project/vllm/issues/14721#issuecomment...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: https://github.com/vllm-project/vllm/pull/20504#event-18495144925)) explicitly has an unchecked boxes for > > * [ ] Tool/functional calling support > * [ ] Output token streaming > > Any plans to implement those feature...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: [Responses API] Support tool calling and ouput token streaming unstale Splitting off from #14721 > FYI a start has been made here https://github.com/vllm-project/vllm/pull/20504 > > That PR (which was merged to `main` o...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ools like codex. See: > > * https://docs.vllm.ai/projects/recipes/en/latest/OpenAI/GPT-OSS.html#harmony-format-support _Originally posted by @bartlettroscoe in [#14721](https://github.com/vllm-project/vllm/issues/14721#...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
