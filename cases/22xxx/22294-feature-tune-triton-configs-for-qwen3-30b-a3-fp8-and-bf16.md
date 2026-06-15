# vllm-project/vllm#22294: [Feature]: Tune Triton Configs for Qwen3-30B-A3-Fp8 and Bf16

| 字段 | 值 |
| --- | --- |
| Issue | [#22294](https://github.com/vllm-project/vllm/issues/22294) |
| 状态 | closed |
| 标签 | good first issue;feature request |
| 评论 | 9; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Feature]: Tune Triton Configs for Qwen3-30B-A3-Fp8 and Bf16

### Issue 正文摘录

### 🚀 The feature, motivation and pitch Hardware Cases: - H100, H200, B200 Configurations: - TP=1 - TP=2 - TP=4 - TP=8 - EP=1 - EP=2 - EP=4 - EP=8 Precisions - Fp8 - Bf16 ### Alternatives _No response_ ### Additional context _No response_ ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: ature request ### 🚀 The feature, motivation and pitch Hardware Cases: - H100, H200, B200 Configurations: - TP=1 - TP=2 - TP=4 - TP=8 - EP=1 - EP=2 - EP=4 - EP=8 Precisions - Fp8 - Bf16 ### Alternatives _No response_ ###...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 2: [Feature]: Tune Triton Configs for Qwen3-30B-A3-Fp8 and Bf16 good first issue;feature request ### 🚀 The feature, motivation and pitch Hardware Cases: - H100, H200, B200 Configurations: - TP=1 - TP=2 - TP=4 - TP=8 - EP=1...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: [Feature]: Tune Triton Configs for Qwen3-30B-A3-Fp8 and Bf16 good first issue;feature request ### 🚀 The feature, motivation and pitch Hardware Cases: - H100, H200, B200 Configurations: - TP=1 - TP=2 - TP=4 - TP=8 - EP=1...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: [Feature]: Tune Triton Configs for Qwen3-30B-A3-Fp8 and Bf16 good first issue;feature request ### 🚀 The feature, motivation and pitch Hardware Cases: - H100, H200, B200 Configurations: - TP=1 - TP=2 - TP=4 - TP=8 - EP=1...
- [Bitwise 确定性与数值等价](../patterns/bitwise_determinism_equivalence.md) - 分数 1: Configurations: - TP=1 - TP=2 - TP=4 - TP=8 - EP=1 - EP=2 - EP=4 - EP=8 Precisions - Fp8 - Bf16 ### Alternatives _No response_ ### Additional context _No response_ ### Before submitting a new issue... - [x] Make sure yo...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
