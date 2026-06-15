# vllm-project/vllm#43431: [New Model]: OpenMOSS-Team/MOSS-Audio (audio understanding)

| 字段 | 值 |
| --- | --- |
| Issue | [#43431](https://github.com/vllm-project/vllm/issues/43431) |
| 状态 | open |
| 标签 |  |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [New Model]: OpenMOSS-Team/MOSS-Audio (audio understanding)

### Issue 正文摘录

### The model to consider. https://huggingface.co/OpenMOSS-Team/MOSS-Audio-8B-Instruct https://huggingface.co/OpenMOSS-Team/MOSS-Audio-4B-Instruct https://huggingface.co/OpenMOSS-Team/MOSS-Audio-8B-Thinking https://huggingface.co/OpenMOSS-Team/MOSS-Audio-4B-Thinking GitHub: https://github.com/OpenMOSS/MOSS-Audio ### The closest model vllm already supports. Qwen2.5-Omni Qwen3-Omni MiMo-Audio ### What's your difficulty of supporting the model you want? 1. DeepStack Cross-Layer Injection 2. Custom audio encoder (MOSS-Audio-Encoder) 3. Time-aware tokens A reference implementation exists in the OpenMOSS SGLang fork (https://github.com/OpenMOSS/sglang/tree/moss-audio) ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: [New Model]: OpenMOSS-Team/MOSS-Audio (audio understanding) ### The model to consider. https://huggingface.co/OpenMOSS-Team/MOSS-Audio-8B-Instruct https://huggingface.co/OpenMOSS-Team/MOSS-Audio-4B-Instruct https://hugg...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: io) ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
