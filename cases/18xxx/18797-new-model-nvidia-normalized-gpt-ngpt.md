# vllm-project/vllm#18797: [New Model]: NVIDIA-Normalized-GPT (nGPT)

| 字段 | 值 |
| --- | --- |
| Issue | [#18797](https://github.com/vllm-project/vllm/issues/18797) |
| 状态 | closed |
| 标签 | new-model |
| 评论 | 0; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [New Model]: NVIDIA-Normalized-GPT (nGPT)

### Issue 正文摘录

### 🚀 The feature, motivation and pitch We are planning to release a model based on a new architecture called normalized transformer (nGPT) and would like to have vllm support for it. We have started the integration process of nGPT into transformers library via [this PR](https://github.com/huggingface/transformers/pull/38276). ### Model description Normalized Transformer (nGPT) is a novel architecture with representation learning on the hypersphere. In nGPT, all vectors forming the embeddings, MLP, attention matrices and hidden states are unit norm normalized. The input stream of tokens travels on the surface of a hypersphere, with each layer contributing a displacement towards the target output predictions. These displacements are defined by the MLP and attention blocks, whose vector components also reside on the same hypersphere. Paper: https://arxiv.org/abs/2410.01131 ### Alternatives _No response_ ### Additional context _No response_ ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequentl...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: [New Model]: NVIDIA-Normalized-GPT (nGPT) new-model ### 🚀 The feature, motivation and pitch We are planning to release a model based on a new architecture called normalized transformer (nGPT) and would like to have vllm...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: motivation and pitch We are planning to release a model based on a new architecture called normalized transformer (nGPT) and would like to have vllm support for it. We have started the integration process of nGPT into t...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 1: ut predictions. These displacements are defined by the MLP and attention blocks, whose vector components also reside on the same hypersphere. Paper: https://arxiv.org/abs/2410.01131 ### Alternatives _No response_ ### Ad...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
