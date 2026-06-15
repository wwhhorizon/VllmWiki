# vllm-project/vllm#28560: [Feature]: Allow custom prompts for Random-MM with vllm bench serve

| 字段 | 值 |
| --- | --- |
| Issue | [#28560](https://github.com/vllm-project/vllm/issues/28560) |
| 状态 | closed |
| 标签 | feature request;stale |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Feature]: Allow custom prompts for Random-MM with vllm bench serve

### Issue 正文摘录

### 🚀 The feature, motivation and pitch https://docs.vllm.ai/en/latest/cli/bench/serve.html Currently, when benchmarking with random-MM dataset, input tokens are randomly generated. Could there be an option where we use custom prompts, with randomly generated images, and output tokens from the Multimodal Model itself, for what's reported in vllm bench serve metrics? This is so that for a given custom prompt and model configuration, I can obtain throughput stats of 1. Number of input tokens for the custom prompt + image tokens 2. Throughput of this custom prompt + image tokens ### Alternatives Thinking if a custom prompt can be added to an --extra-body flag in a json format. ### Additional context There's another issue closed that suggested using --extra-body to disable thinking for models. ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: stom prompts, with randomly generated images, and output tokens from the Multimodal Model itself, for what's reported in vllm bench serve metrics? This is so that for a given custom prompt and model configuration, I can...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 3: ;stale ### 🚀 The feature, motivation and pitch https://docs.vllm.ai/en/latest/cli/bench/serve.html Currently, when benchmarking with random-MM dataset, input tokens are randomly generated. Could there be an option where...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: ature]: Allow custom prompts for Random-MM with vllm bench serve feature request;stale ### 🚀 The feature, motivation and pitch https://docs.vllm.ai/en/latest/cli/bench/serve.html Currently, when benchmarking with random...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: ls. ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
