# vllm-project/vllm#12705: [RFC]: Scale the API server across multiple CPUs

| 字段 | 值 |
| --- | --- |
| Issue | [#12705](https://github.com/vllm-project/vllm/issues/12705) |
| 状态 | closed |
| 标签 | RFC |
| 评论 | 12; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [RFC]: Scale the API server across multiple CPUs

### Issue 正文摘录

### Motivation. Currently, the API server runs in a single process, utilizing a single CPU for its work. As GPUs continue to get faster, it is important that we scale the API server to ensure that it is able to process requests fast enough to keep GPU resources fully utilized. ### Proposed Change. From a high level, this proposal is to move from the API server being a single process to being a configurable pool of processes to ensure that a single CPU for the apiserver will not become a bottleneck in server utilization. Design notes: https://docs.google.com/document/d/1Y2S011RKYkFKtrcz_MuEqEf3cRXORNGsVvMHCaqqc-k/edit?tab=t.0 ### Feedback Period. _No response_ ### CC List. @robertgshaw2-redhat @njhill ### Any Other Things. _No response_ ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: ilizing a single CPU for its work. As GPUs continue to get faster, it is important that we scale the API server to ensure that it is able to process requests fast enough to keep GPU resources fully utilized. ### Propose...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 1: [RFC]: Scale the API server across multiple CPUs RFC ### Motivation. Currently, the API server runs in a single process, utilizing a single CPU for its work. As GPUs continue to get faster, it is important that we scale...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: se_ ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: roposal is to move from the API server being a single process to being a configurable pool of processes to ensure that a single CPU for the apiserver will not become a bottleneck in server utilization. Design notes: htt...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: ortant that we scale the API server to ensure that it is able to process requests fast enough to keep GPU resources fully utilized. ### Proposed Change. From a high level, this proposal is to move from the API server be...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
