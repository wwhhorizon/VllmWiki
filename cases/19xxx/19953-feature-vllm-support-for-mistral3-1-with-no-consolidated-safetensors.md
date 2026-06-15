# vllm-project/vllm#19953: [Feature]: vllm support for mistral3.1 with no consolidated.safetensors

| 字段 | 值 |
| --- | --- |
| Issue | [#19953](https://github.com/vllm-project/vllm/issues/19953) |
| 状态 | closed |
| 标签 | feature request;stale |
| 评论 | 5; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Feature]: vllm support for mistral3.1 with no consolidated.safetensors

### Issue 正文摘录

### 🚀 The feature, motivation and pitch when load format mistrall , vllm searches for the consolidated shard in the directory which maybe missing after finetuning , so add the support to check whether it exists or not , if not load normally from the model shards ### Alternatives _No response_ ### Additional context _No response_ ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: feature request;stale ### 🚀 The feature, motivation and pitch when load format mistrall , vllm searches for the consolidated shard in the directory which maybe missing after finetuning , so add the support to check whet...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: e]: vllm support for mistral3.1 with no consolidated.safetensors feature request;stale ### 🚀 The feature, motivation and pitch when load format mistrall , vllm searches for the consolidated shard in the directory which...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: 🚀 The feature, motivation and pitch when load format mistrall , vllm searches for the consolidated shard in the directory which maybe missing after finetuning , so add the support to check whether it exists or not , if...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
