# vllm-project/vllm#6601: [Usage]:Can vllm use a method similar to device_map in transformers ?

| 字段 | 值 |
| --- | --- |
| Issue | [#6601](https://github.com/vllm-project/vllm/issues/6601) |
| 状态 | closed |
| 标签 | usage;stale |
| 评论 | 11; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Usage]:Can vllm use a method similar to device_map in transformers ?

### Issue 正文摘录

### Your current environment ```text ``` ### How would you like to use vllm I have three 4090 GPUs with a total of 24*3 GB of memory, and the model I need to deploy requires at least 52 GB. The issue is that parallel deployment requires the number of GPUs to be divisible by 32, which is clearly not feasible. Can vllm use a method similar to device_map in transformers to specify how each layer is deployed to solve this problem?

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: sible. Can vllm use a method similar to device_map in transformers to specify how each layer is deployed to solve this problem?
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: vllm I have three 4090 GPUs with a total of 24*3 GB of memory, and the model I need to deploy requires at least 52 GB. The issue is that parallel deployment requires the number of GPUs to be divisible by 32, which is cl...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: age]:Can vllm use a method similar to device_map in transformers ? usage;stale ### Your current environment ```text ``` ### How would you like to use vllm I have three 4090 GPUs with a total of 24*3 GB of memory, and th...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
