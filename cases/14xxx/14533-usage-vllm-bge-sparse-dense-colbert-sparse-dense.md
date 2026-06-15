# vllm-project/vllm#14533: [Usage]: vllm 启动bge 怎么支持sparse+dense  colbert+sparse+dense 这些返回呢

| 字段 | 值 |
| --- | --- |
| Issue | [#14533](https://github.com/vllm-project/vllm/issues/14533) |
| 状态 | closed |
| 标签 | usage;stale |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Usage]: vllm 启动bge 怎么支持sparse+dense  colbert+sparse+dense 这些返回呢

### Issue 正文摘录

### Your current environment ![Image](https://github.com/user-attachments/assets/5af2ad38-7bfe-4de2-b3f0-4b58868ec380) 怎么支持返回 ![Image](https://github.com/user-attachments/assets/30a3788a-7981-4c5b-89eb-2c2d97518a77) ### How would you like to use vllm I want to run inference of a [specific model](put link here). I don't know how to integrate it with vllm. ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: 7) ### How would you like to use vllm I want to run inference of a [specific model](put link here). I don't know how to integrate it with vllm. ### Before submitting a new issue... - [x] Make sure you already searched f...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: lm. ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: # How would you like to use vllm I want to run inference of a [specific model](put link here). I don't know how to integrate it with vllm. ### Before submitting a new issue... - [x] Make sure you already searched for re...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: [Usage]: vllm 启动bge 怎么支持sparse+dense colbert+sparse+dense 这些返回呢 usage;stale ### Your current environment ![Image](https://github.com/user-attachments/assets/5af2ad38-7bfe-4de2-b3f0-4b58868ec380) 怎么支持返回 ![Image](https://...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
