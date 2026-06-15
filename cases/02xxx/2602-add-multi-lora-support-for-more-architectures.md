# vllm-project/vllm#2602: Add multi-LoRA support for more architectures

| 字段 | 值 |
| --- | --- |
| Issue | [#2602](https://github.com/vllm-project/vllm/issues/2602) |
| 状态 | closed |
| 标签 | feature request;stale |
| 评论 | 8; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> Add multi-LoRA support for more architectures

### Issue 正文摘录

Currently, multi-LoRA supports only Llama and Mistral architectures. We should extend this functionality to all architectures. Yi, Qwen, Phi and Mixtral architectures seem to be the most demanded right now. One challenge will be ensuring that all allowed weight shapes are supported by punica kernels. We may need to investigate some sort of padding there. _Originally posted by @Yard1 in https://github.com/vllm-project/vllm/issues/1804#issuecomment-1882913208_

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: architectures feature request;stale Currently, multi-LoRA supports only Llama and Mistral architectures. We should extend this functionality to all architectures. Yi, Qwen, Phi and Mixtral architectures seem to be the m...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: Add multi-LoRA support for more architectures feature request;stale Currently, multi-LoRA supports only Llama and Mistral architectures. We should extend this functionality to all architectures. Yi, Qwen, Phi and Mixtra...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: Add multi-LoRA support for more architectures feature request;stale Currently, multi-LoRA supports only Llama and Mistral architectures. We should extend this functionality to all architectures. Yi, Qwen, Phi and Mixtra...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
