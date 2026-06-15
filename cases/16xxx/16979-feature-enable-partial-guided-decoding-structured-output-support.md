# vllm-project/vllm#16979: [Feature]: Enable Partial Guided Decoding / Structured Output Support

| 字段 | 值 |
| --- | --- |
| Issue | [#16979](https://github.com/vllm-project/vllm/issues/16979) |
| 状态 | closed |
| 标签 | feature request;stale |
| 评论 | 4; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Feature]: Enable Partial Guided Decoding / Structured Output Support

### Issue 正文摘录

### 🚀 The feature, motivation and pitch In some use cases, we don’t need the entire output to strictly follow a defined grammar, but only a specific segment of the generation. It would be great to support partial guided decoding, where structured output is enforced only within defined token boundaries. For example: - Guided decoding begins at ` ` and ends at ` ` - Or for markdown, it starts at \```json and ends at \``` This would make guided decoding more flexible and broadly applicable to tasks where only a partial defined structure is needed (e.g., code generation or agent tool). ### Alternatives Currently, vLLM supports a `guided_grammar` option that allows context-free grammar-based customization. However, using it for partial guided decoding introduces additional complexity and isn’t as intuitive for cases where a pre-defined structure (such as JSON) is only required in segments of the output. ### Additional context _No response_ ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently a...

## 候选优化模式

- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: ure]: Enable Partial Guided Decoding / Structured Output Support feature request;stale ### 🚀 The feature, motivation and pitch In some use cases, we don’t need the entire output to strictly follow a defined grammar, but...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: ed the entire output to strictly follow a defined grammar, but only a specific segment of the generation. It would be great to support partial guided decoding, where structured output is enforced only within defined tok...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: se_ ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
