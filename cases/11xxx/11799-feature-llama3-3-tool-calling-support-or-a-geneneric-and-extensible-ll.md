# vllm-project/vllm#11799: [Feature]: Llama3.3 Tool calling support or a Geneneric and extensible llama tool calling support

| 字段 | 值 |
| --- | --- |
| Issue | [#11799](https://github.com/vllm-project/vllm/issues/11799) |
| 状态 | closed |
| 标签 | feature request;stale;tool-calling |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Feature]: Llama3.3 Tool calling support or a Geneneric and extensible llama tool calling support

### Issue 正文摘录

### 🚀 The feature, motivation and pitch We have customer moving from llama3.1/3.2 to 3.3 and further when available ### Alternatives Not yet explored ### Additional context A generic way where we can use use tool calling support against llms instead of using specific params like --tool-call-parser llama3_json /instead of --tool-call-parser as an external reference via chat template or so ? ### Before submitting a new issue... - [X] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: support or a Geneneric and extensible llama tool calling support feature request;stale;tool-calling ### 🚀 The feature, motivation and pitch We have customer moving from llama3.1/3.2 to 3.3 and further when available ###...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: ere we can use use tool calling support against llms instead of using specific params like --tool-call-parser llama3_json /instead of --tool-call-parser as an external reference via chat template or so ? ### Before subm...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: o ? ### Before submitting a new issue... - [X] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: [Feature]: Llama3.3 Tool calling support or a Geneneric and extensible llama tool calling support feature request;stale;tool-calling ### 🚀 The feature, motivation and pitch We have customer moving from llama3.1/3.2 to 3...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
