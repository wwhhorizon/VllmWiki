# vllm-project/vllm#1452: Questions on High Throughput Support and Parameter Tuning

| 字段 | 值 |
| --- | --- |
| Issue | [#1452](https://github.com/vllm-project/vllm/issues/1452) |
| 状态 | closed |
| 标签 |  |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> Questions on High Throughput Support and Parameter Tuning

### Issue 正文摘录

Hey vllm Team, I’ve been diving into vllm and saw that it’s designed to support high throughput, which is awesome! Got a few questions and was hoping to get some guidance to make the most out of it. 1. **Parameter Settings for High User Load**: I was wondering if you guys have any recommended settings or a formula for determining the best parameters when dealing with a lot of users. Any tips or best practices on this? 2. **Example with a Specific Model**: If you could provide an example, especially using a specific model, on how to set this up for optimal performance, that would be super helpful. 3. **Handling More Concurrent Requests**: Also, is there a way to reduce the token/s but still handle more concurrent requests? Looking for some strategies or tweaks here. Thanks a ton for your help!

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: lot of users. Any tips or best practices on this? 2. **Example with a Specific Model**: If you could provide an example, especially using a specific model, on how to set this up for optimal performance, that would be su...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: users. Any tips or best practices on this? 2. **Example with a Specific Model**: If you could provide an example, especially using a specific model, on how to set this up for optimal performance, that would be super hel...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: performance, that would be super helpful. 3. **Handling More Concurrent Requests**: Also, is there a way to reduce the token/s but still handle more concurrent requests? Looking for some strategies or tweaks here. Thank...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: Questions on High Throughput Support and Parameter Tuning Hey vllm Team, I’ve been diving into vllm and saw that it’s designed to support high throughput, which is awesome! Got a few questions and was hoping to get some...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
