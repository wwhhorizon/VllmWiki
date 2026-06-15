# vllm-project/vllm#11522: [RFC]: Refactor tool parsers to eliminate coding errors and allow more efficient implementations.

| 字段 | 值 |
| --- | --- |
| Issue | [#11522](https://github.com/vllm-project/vllm/issues/11522) |
| 状态 | closed |
| 标签 | RFC;stale;tool-calling |
| 评论 | 13; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [RFC]: Refactor tool parsers to eliminate coding errors and allow more efficient implementations.

### Issue 正文摘录

### Motivation. Currently the tool parsers are buggy when used and are quite messy in terms of code, especially in the implementations of `extract_tool_calls_streaming`. Moreover, in the long term, maintaining the entire output string in the chat streaming server and parsing the entire output over and over again for each generated token will become very expensive. This will soon become a performance bottleneck in long tool calls. Many of the implemented tool parsers aren't carefully written either in terms of correctness nor in terms of efficiency causing a lot of issues in this repository. A complete refactor of this part of the frontend will be required sooner of later. So now is probably the best opportunity to refactor things before more tool calling support is added. From the architectural perspective, clearly it's should be the tool parser's job to maintain states that it needs, so if they need the complete output, they should maintain them with `delta_text` and `delta_token_ids` in their class instead of relying on the server. On the other hand, this encourages the tool parser to use custom, efficient alternative implementations to generate delta messages based on e.g. a in...

## 候选优化模式

- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: y to refactor things before more tool calling support is added. From the architectural perspective, clearly it's should be the tool parser's job to maintain states that it needs, so if they need the complete output, the...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: FC]: Refactor tool parsers to eliminate coding errors and allow more efficient implementations. RFC;stale;tool-calling ### Motivation. Currently the tool parsers are buggy when used and are quite messy in terms of code,...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: to eliminate coding errors and allow more efficient implementations. RFC;stale;tool-calling ### Motivation. Currently the tool parsers are buggy when used and are quite messy in terms of code, especially in the implemen...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: rts of the parsing logic in existing tool parsers. - [ ] Add appropriate tests for the tool parsers. ### Feedback Period. This shouldn't be hard so 1-2 weeks. ### CC List. @mgoin @simon-mo @cedonley @K-Mistele @DarkLigh...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
