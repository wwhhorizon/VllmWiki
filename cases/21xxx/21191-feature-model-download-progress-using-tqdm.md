# vllm-project/vllm#21191: [Feature]: Model download progress using tqdm

| 字段 | 值 |
| --- | --- |
| Issue | [#21191](https://github.com/vllm-project/vllm/issues/21191) |
| 状态 | closed |
| 标签 | feature request;stale |
| 评论 | 13; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Feature]: Model download progress using tqdm

### Issue 正文摘录

### 🚀 The feature, motivation and pitch I use vllm via docker. However, when I download a model, I cannot tell how long I should wait. It will be nice to have an indicator using `tqdm`. ### Alternatives _No response_ ### Additional context _No response_ ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: [Feature]: Model download progress using tqdm feature request;stale ### 🚀 The feature, motivation and pitch I use vllm via docker. However, when I download a model, I cannot tell how long I should wait. It will be nice...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: request;stale ### 🚀 The feature, motivation and pitch I use vllm via docker. However, when I download a model, I cannot tell how long I should wait. It will be nice to have an indicator using `tqdm`. ### Alternatives _N...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: se_ ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: [Feature]: Model download progress using tqdm feature request;stale ### 🚀 The feature, motivation and pitch I use vllm via docker. However, when I download a model, I cannot tell how long I should wait. It will be nice...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
