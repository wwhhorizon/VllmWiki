# vllm-project/vllm#2212: PowerInfer : using a combination of cpu and gpu for faster Inference

| 字段 | 值 |
| --- | --- |
| Issue | [#2212](https://github.com/vllm-project/vllm/issues/2212) |
| 状态 | closed |
| 标签 | feature request;stale |
| 评论 | 5; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> PowerInfer : using a combination of cpu and gpu for faster Inference

### Issue 正文摘录

Splitting hot and cold neurons across cpu and gpu allows faster Inference when using larger models/higher quantisations. Demo shows 11x speedup over llama.cpp when using a 40b on a single 24gb GPU. Demo https://twitter.com/omarsar0/status/1737168751668187229?t=blU8xZMb7JMJTtAHra7zvQ&s=19 GitHub https://github.com/SJTU-IPADS/PowerInfer Wondering if this is something that can also be integrated into vllm.

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: old neurons across cpu and gpu allows faster Inference when using larger models/higher quantisations. Demo shows 11x speedup over llama.cpp when using a 40b on a single 24gb GPU. Demo https://twitter.com/omarsar0/status...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: rInfer : using a combination of cpu and gpu for faster Inference feature request;stale Splitting hot and cold neurons across cpu and gpu allows faster Inference when using larger models/higher quantisations. Demo shows...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 1: ross cpu and gpu allows faster Inference when using larger models/higher quantisations. Demo shows 11x speedup over llama.cpp when using a 40b on a single 24gb GPU. Demo https://twitter.com/omarsar0/status/1737168751668...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
