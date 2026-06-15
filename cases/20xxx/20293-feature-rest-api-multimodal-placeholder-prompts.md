# vllm-project/vllm#20293: [Feature]: rest api multimodal placeholder prompts

| 字段 | 值 |
| --- | --- |
| Issue | [#20293](https://github.com/vllm-project/vllm/issues/20293) |
| 状态 | closed |
| 标签 | feature request;stale |
| 评论 | 5; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Feature]: rest api multimodal placeholder prompts

### Issue 正文摘录

### 🚀 The feature, motivation and pitch Dear vllm community, there is an interest at Spotify in vllm supporting a more flexible multi modal rest api. I am interested in being able to prompt vllm with a textual prompt templated with certain placeholders that are to be populated with embed vectors. Today this seems to be supported through [Multimodal inputs](https://docs.vllm.ai/en/latest/features/multimodal_inputs.html) at the vllm library level. However it is not accessible at the rest api level, at least this is how I'm understanding the code. Is such support something that is on the roadmap for vllm? ### Alternatives An alternative I tested out that could work is embed only prompts, which works only on the V0 engine. However ideally it would be good to support text and embeds together. ### Additional context _No response_ ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: [Feature]: rest api multimodal placeholder prompts feature request;stale ### 🚀 The feature, motivation and pitch Dear vllm community, there is an interest at Spotify in vllm supporting a more flexible multi modal rest a...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: se_ ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: [Feature]: rest api multimodal placeholder prompts feature request;stale ### 🚀 The feature, motivation and pitch Dear vllm community, there is an interest at Spotify in vllm supporting a more flexible multi modal rest a...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ms to be supported through [Multimodal inputs](https://docs.vllm.ai/en/latest/features/multimodal_inputs.html) at the vllm library level. However it is not accessible at the rest api level, at least this is how I'm unde...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
