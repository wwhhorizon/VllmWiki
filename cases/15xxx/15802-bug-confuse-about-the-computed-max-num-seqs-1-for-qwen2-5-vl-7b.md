# vllm-project/vllm#15802: [Bug]: Confuse about the `computed max_num_seqs < 1` for Qwen2.5-VL-7B

| 字段 | 值 |
| --- | --- |
| Issue | [#15802](https://github.com/vllm-project/vllm/issues/15802) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 16; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: Confuse about the `computed max_num_seqs < 1` for Qwen2.5-VL-7B

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug ```bash WARNING 03-31 16:53:06 [model_runner.py:1296] Computed max_num_seqs (min(64, 16384 // 32768)) to be less than 1. Setting it to the minimum value of 1. WARNING 03-31 16:53:11 [profiling.py:222] The sequence length used for profiling (max_num_batched_tokens / max_num_seqs = 16384) is too short to hold the multi-modal embeddings in the worst case (32768 tokens in total, out of which {'image': 16384, 'video': 16384} are reserved for multi-modal embeddings). This may cause certain multi-modal inputs to fail during inference, even when the input text is short. To avoid this, you should increase `max_model_len`, reduce `max_num_seqs`, and/or reduce `mm_counts`. ``` How can i reduce mm_counts? ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: [Bug]: Confuse about the `computed max_num_seqs < 1` for Qwen2.5-VL-7B bug ### Your current environment ### 🐛 Describe the bug ```bash WARNING 03-31 16:53:06 [model_runner.py:1296] Computed max_num_seqs (min(64, 16384 /...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 2: ss than 1. Setting it to the minimum value of 1. WARNING 03-31 16:53:11 [profiling.py:222] The sequence length used for profiling (max_num_batched_tokens / max_num_seqs = 16384) is too short to hold the multi-modal embe...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: ts? ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
