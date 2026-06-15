# vllm-project/vllm#5003: [Feature]: Tensor Parallelism with non divisble amount of attention heads

| 字段 | 值 |
| --- | --- |
| Issue | [#5003](https://github.com/vllm-project/vllm/issues/5003) |
| 状态 | closed |
| 标签 | feature request;stale |
| 评论 | 10; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Feature]: Tensor Parallelism with non divisble amount of attention heads

### Issue 正文摘录

### 🚀 The feature, motivation and pitch I am trying to run a 70B model on a node with 3XA100-80Gi. 2XA100-80Gi does not contain enough VRAM to run the model, and when I try to run vLLM with tensor parallelism of 3, it raises an error saying that the number of attention heads is not divisble by 3. I looked into changing the tensor parallelism feature so that it supports an uneven division of the tensors between GPUs. But I might be missing something here as there are a lot of validations in the codebase to avoid this scenario. Is it possible to implement tensor parallelism this way? ### Alternatives _No response_ ### Additional context _No response_

## 候选优化模式

- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: [Feature]: Tensor Parallelism with non divisble amount of attention heads feature request;stale ### 🚀 The feature, motivation and pitch I am trying to run a 70B model on a node with 3XA100-80Gi. 2XA100-80Gi does not con...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: : Tensor Parallelism with non divisble amount of attention heads feature request;stale ### 🚀 The feature, motivation and pitch I am trying to run a 70B model on a node with 3XA100-80Gi. 2XA100-80Gi does not contain enou...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: ;stale ### 🚀 The feature, motivation and pitch I am trying to run a 70B model on a node with 3XA100-80Gi. 2XA100-80Gi does not contain enough VRAM to run the model, and when I try to run vLLM with tensor parallelism of...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
