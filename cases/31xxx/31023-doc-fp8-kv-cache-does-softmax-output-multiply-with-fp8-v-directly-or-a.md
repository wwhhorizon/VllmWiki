# vllm-project/vllm#31023: [Doc]: FP8 KV Cache: Does softmax output multiply with FP8 V directly or after dequantization?

| 字段 | 值 |
| --- | --- |
| Issue | [#31023](https://github.com/vllm-project/vllm/issues/31023) |
| 状态 | closed |
| 标签 | documentation |
| 评论 | 0; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Doc]: FP8 KV Cache: Does softmax output multiply with FP8 V directly or after dequantization?

### Issue 正文摘录

### 📚 The doc issue https://docs.vllm.ai/en/v0.8.5.post1/features/quantization/quantized_kvcache.html Question: In the FP8 KV Cache implementation, after computing attention scores and softmax at higher precision (FP16/BF16), is the resulting attention weight matrix: Quantized to FP8 and multiplied directly with FP8 V cache, or Multiplied with V cache after dequantizing V to higher precision? The documentation mentions "no fused dequantization and attention operations yet" but doesn't specify the precision of this final multiplication. Clarifying this detail would help understand the accuracy-performance tradeoff. Thanks! ### Suggest a potential alternative/fix _No response_ ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 4: [Doc]: FP8 KV Cache: Does softmax output multiply with FP8 V directly or after dequantization? documentation ### 📚 The doc issue https://docs.vllm.ai/en/v0.8.5.post1/features/quantization/quantized_kvcache.html Question...
- [Bitwise 确定性与数值等价](../patterns/bitwise_determinism_equivalence.md) - 分数 2: e implementation, after computing attention scores and softmax at higher precision (FP16/BF16), is the resulting attention weight matrix: Quantized to FP8 and multiplied directly with FP8 V cache, or Multiplied with V c...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 2: s final multiplication. Clarifying this detail would help understand the accuracy-performance tradeoff. Thanks! ### Suggest a potential alternative/fix _No response_ ### Before submitting a new issue... - [x] Make sure...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: mplementation, after computing attention scores and softmax at higher precision (FP16/BF16), is the resulting attention weight matrix: Quantized to FP8 and multiplied directly with FP8 V cache, or Multiplied with V cach...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: se_ ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...

## Wiki 抽取状态

- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
