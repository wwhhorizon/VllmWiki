# vllm-project/vllm#13766: [Usage]: Cannot use FA version 2 is not supported due to FA3 is only supported on devices with compute capability >= 8 excluding 8.6 and 8.9

| 字段 | 值 |
| --- | --- |
| Issue | [#13766](https://github.com/vllm-project/vllm/issues/13766) |
| 状态 | closed |
| 标签 | usage;stale |
| 评论 | 5; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Usage]: Cannot use FA version 2 is not supported due to FA3 is only supported on devices with compute capability >= 8 excluding 8.6 and 8.9

### Issue 正文摘录

### Your current environment ```text how to ban Flash Attention？ ``` ### How would you like to use vllm I want to run inference of a [specific model](put link here). I don't know how to integrate it with vllm. ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: [Usage]: Cannot use FA version 2 is not supported due to FA3 is only supported on devices with compute capability >= 8 excluding 8.6 and 8.9 usage;stale ### Your current environment ```text how to ban Flash Attention？ `...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 2: [Usage]: Cannot use FA version 2 is not supported due to FA3 is only supported on devices with compute capability >= 8 excluding 8.6 and 8.9 usage;stale ### Your current environment ```text how to ban Flash Attention？ `...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: 2 is not supported due to FA3 is only supported on devices with compute capability >= 8 excluding 8.6 and 8.9 usage;stale ### Your current environment ```text how to ban Flash Attention？ ``` ### How would you like to us...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: # How would you like to use vllm I want to run inference of a [specific model](put link here). I don't know how to integrate it with vllm. ### Before submitting a new issue... - [x] Make sure you already searched for re...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: rted on devices with compute capability >= 8 excluding 8.6 and 8.9 usage;stale ### Your current environment ```text how to ban Flash Attention？ ``` ### How would you like to use vllm I want to run inference of a [specif...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
