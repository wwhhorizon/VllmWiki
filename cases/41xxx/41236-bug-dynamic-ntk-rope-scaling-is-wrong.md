# vllm-project/vllm#41236: [Bug]: Dynamic NTK RoPE scaling is wrong

| 字段 | 值 |
| --- | --- |
| Issue | [#41236](https://github.com/vllm-project/vllm/issues/41236) |
| 状态 | open |
| 标签 | bug |
| 评论 | 7; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: Dynamic NTK RoPE scaling is wrong

### Issue 正文摘录

### Your current environment Irrelevant ### 🐛 Describe the bug The original formula for NTK Dynamic scaling is: `(α * current sequence length / original model context length) - (α - 1)` References [1](https://www.reddit.com/r/LocalLLaMA/comments/14mrgpr/dynamically_scaled_rope_further_increases/), [2](https://arxiv.org/pdf/2402.01613). However in `vllm/model_executor/layers/rotary_embedding/dynamic_ntk_scaling_rope.py` we see the following: ``` max_len = self.max_position_embeddings * self.scaling_factor base = self.base * ( (self.scaling_factor * max_len / self.max_position_embeddings) - (self.scaling_factor - 1) ``` Where `α = self.scaling_factor`. If we substitute `max_len`, the formula becomes `(α * α) - (α - 1)`, which is a constant that is completely independent of the sequence length. Affected models are the Nomic embedding models such as `nomic-ai/nomic-embed-text-v1` cc: @noooop ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: ula for NTK Dynamic scaling is: `(α * current sequence length / original model context length) - (α - 1)` References [1](https://www.reddit.com/r/LocalLLaMA/comments/14mrgpr/dynamically_scaled_rope_further_increases/),...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 1: ces [1](https://www.reddit.com/r/LocalLLaMA/comments/14mrgpr/dynamically_scaled_rope_further_increases/), [2](https://arxiv.org/pdf/2402.01613). However in `vllm/model_executor/layers/rotary_embedding/dynamic_ntk_scalin...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: op ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), whi...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
