# vllm-project/vllm#36916: [Feature]: W6A16 Support

| 字段 | 值 |
| --- | --- |
| Issue | [#36916](https://github.com/vllm-project/vllm/issues/36916) |
| 状态 | open |
| 标签 | feature request |
| 评论 | 0; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Feature]: W6A16 Support

### Issue 正文摘录

### 🚀 The feature, motivation and pitch Please consider adding W6A16 support for VLLM/LLM-Compressor. I'm aware it may be as slow as W8A16. My priority is VRAM and accuracy. W4A16 is good, but not accurate enough for me. I am VRAM constrained even with 4 GPU as I use high context. I have multiple 3090's. Last I checked, I cannot quant K,V cache on Ampere as VLLM does not support it. This makes it difficult for me. ### Alternatives None ### Additional context N/A ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: xt. I have multiple 3090's. Last I checked, I cannot quant K,V cache on Ampere as VLLM does not support it. This makes it difficult for me. ### Alternatives None ### Additional context N/A ### Before submitting a new is...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 2: mpressor. I'm aware it may be as slow as W8A16. My priority is VRAM and accuracy. W4A16 is good, but not accurate enough for me. I am VRAM constrained even with 4 GPU as I use high context. I have multiple 3090's. Last...
- [Bitwise 确定性与数值等价](../patterns/bitwise_determinism_equivalence.md) - 分数 1: mpressor. I'm aware it may be as slow as W8A16. My priority is VRAM and accuracy. W4A16 is good, but not accurate enough for me. I am VRAM constrained even with 4 GPU as I use high context. I have multiple 3090's. Last...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 1: as I use high context. I have multiple 3090's. Last I checked, I cannot quant K,V cache on Ampere as VLLM does not support it. This makes it difficult for me. ### Alternatives None ### Additional context N/A ### Before...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: [Feature]: W6A16 Support feature request ### 🚀 The feature, motivation and pitch Please consider adding W6A16 support for VLLM/LLM-Compressor. I'm aware it may be as slow as W8A16. My priority is VRAM and accuracy. W4A1...

## Wiki 抽取状态

- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
