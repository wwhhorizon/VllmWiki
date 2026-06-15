# vllm-project/vllm#21545: [Feature]: Zero copy for direct GPU model loading

| 字段 | 值 |
| --- | --- |
| Issue | [#21545](https://github.com/vllm-project/vllm/issues/21545) |
| 状态 | closed |
| 标签 | feature request;stale |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Feature]: Zero copy for direct GPU model loading

### Issue 正文摘录

### 🚀 The feature, motivation and pitch Not sure if this has been discussed before but I wanted to propose implementing a new feature (or polish existing) that allows to load weights on the fly, similarly to what is described [here](https://www.bentoml.com/blog/25x-faster-cold-starts-for-llms-on-kubernetes#step%203%3A%20load%20models%20directly%20into%20gpu%20memory). This is more inspired by zero copy techniques used elsewhere and how Ray shares data in memory via its object storage layer. I think it would be ideal for fast loading and fast inference. ### Alternatives I have seen that this is supported with fastsafetensors to some extend but I think it should be part of the core even though there are some downsides when environments are not fast enough e.g. gpus, net etc. ### Additional context _No response_ ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: [Feature]: Zero copy for direct GPU model loading feature request;stale ### 🚀 The feature, motivation and pitch Not sure if this has been discussed before but I wanted to propose implementing a new feature (or polish ex...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: se_ ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 1: nto%20gpu%20memory). This is more inspired by zero copy techniques used elsewhere and how Ray shares data in memory via its object storage layer. I think it would be ideal for fast loading and fast inference. ### Altern...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: [Feature]: Zero copy for direct GPU model loading feature request;stale ### 🚀 The feature, motivation and pitch Not sure if this has been discussed before but I wanted to propose implementing a new feature (or polish ex...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
