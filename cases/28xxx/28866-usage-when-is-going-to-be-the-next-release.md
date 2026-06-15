# vllm-project/vllm#28866: [Usage]: When is going to be the next release?

| 字段 | 值 |
| --- | --- |
| Issue | [#28866](https://github.com/vllm-project/vllm/issues/28866) |
| 状态 | closed |
| 标签 | usage;stale |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Usage]: When is going to be the next release?

### Issue 正文摘录

Hi everyone, Thank you for developing such a great tool! I was wondering when the next release is scheduled. I’m interested in running Gemma3-text type architecture GGUF quantized models with VLLM. Are there any alternatives to do this with the latest release (v0.11.0)? I also noticed that you merged this PR with the working solution on October 9: https://github.com/vllm-project/vllm/pull/26189

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: wondering when the next release is scheduled. I’m interested in running Gemma3-text type architecture GGUF quantized models with VLLM. Are there any alternatives to do this with the latest release (v0.11.0)? I also noti...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 1: scheduled. I’m interested in running Gemma3-text type architecture GGUF quantized models with VLLM. Are there any alternatives to do this with the latest release (v0.11.0)? I also noticed that you merged this PR with th...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: he next release is scheduled. I’m interested in running Gemma3-text type architecture GGUF quantized models with VLLM. Are there any alternatives to do this with the latest release (v0.11.0)? I also noticed that you mer...
- [MoE、GEMM 与 Expert Routing](../patterns/moe_gemm_routing.md) - 分数 1: wondering when the next release is scheduled. I’m interested in running Gemma3-text type architecture GGUF quantized models with VLLM. Are there any alternatives to do this with the latest release (v0.11.0)? I also noti...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: [Usage]: When is going to be the next release? usage;stale Hi everyone, Thank you for developing such a great tool! I was wondering when the next release is scheduled. I’m interested in running Gemma3-text type architec...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
