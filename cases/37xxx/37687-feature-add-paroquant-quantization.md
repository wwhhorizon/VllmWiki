# vllm-project/vllm#37687: [Feature]: add ParoQuant quantization

| 字段 | 值 |
| --- | --- |
| Issue | [#37687](https://github.com/vllm-project/vllm/issues/37687) |
| 状态 | open |
| 标签 | feature request |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Feature]: add ParoQuant quantization

### Issue 正文摘录

### 🚀 The feature, motivation and pitch This quantization method is almost as fast as AWQ and it achieves higher accuracy, specially for reasoning models. ### Alternatives _No response_ ### Additional context ParoQuant: Pairwise Rotation Quantization for Efficient Reasoning LLM Inference https://z-lab.ai/projects/paroquant/ https://github.com/z-lab/paroquant https://arxiv.org/abs/2511.10645 ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 2: This quantization method is almost as fast as AWQ and it achieves higher accuracy, specially for reasoning models. ### Alternatives _No response_ ### Additional context ParoQuant: Pairwise Rotation Quantization for Effi...
- [Bitwise 确定性与数值等价](../patterns/bitwise_determinism_equivalence.md) - 分数 1: This quantization method is almost as fast as AWQ and it achieves higher accuracy, specially for reasoning models. ### Alternatives _No response_ ### Additional context ParoQuant: Pairwise Rotation Quantization for Effi...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: tion method is almost as fast as AWQ and it achieves higher accuracy, specially for reasoning models. ### Alternatives _No response_ ### Additional context ParoQuant: Pairwise Rotation Quantization for Efficient Reasoni...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 1: [Feature]: add ParoQuant quantization feature request ### 🚀 The feature, motivation and pitch This quantization method is almost as fast as AWQ and it achieves higher accuracy, specially for reasoning models. ### Altern...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: 645 ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
