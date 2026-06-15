# vllm-project/vllm#2960: Add support for Gemma models

| 字段 | 值 |
| --- | --- |
| Issue | [#2960](https://github.com/vllm-project/vllm/issues/2960) |
| 状态 | closed |
| 标签 |  |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> Add support for Gemma models

### Issue 正文摘录

Architecture difference (what I could find): - [Normalizes embeddings](https://github.com/huggingface/transformers/blob/ae49b218c3d718df90d8e4a109016450fb8f0632/src/transformers/models/gemma/modeling_gemma.py#L881) Links: - Gemma 7B: https://huggingface.co/google/gemma-7b - Gemma 2B: https://huggingface.co/google/gemma-2b - Blog: https://blog.google/technology/developers/gemma-open-models/ - Paper: https://storage.googleapis.com/deepmind-media/gemma/gemma-report.pdf

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: Add support for Gemma models Architecture difference (what I could find): - [Normalizes embeddings](https://github.com/huggingface/transformers/blob/ae49b218c3d718df90d8e4a109016450fb8f0632/src/transformers/models/gemma...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: 109016450fb8f0632/src/transformers/models/gemma/modeling_gemma.py#L881) Links: - Gemma 7B: https://huggingface.co/google/gemma-7b - Gemma 2B: https://huggingface.co/google/gemma-2b - Blog: https://blog.google/technology...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: Add support for Gemma models Architecture difference (what I could find): - [Normalizes embeddings](https://github.com/huggingface/transformers/blob/ae49b218c3d718df90d8e4a109016450fb8f0632/src/transformers/models/gemma...
- [MoE、GEMM 与 Expert Routing](../patterns/moe_gemm_routing.md) - 分数 1: Add support for Gemma models Architecture difference (what I could find): - [Normalizes embeddings](https://github.com/huggingface/transformers/blob/ae49b218c3d718df90d8e4a109016450fb8f0632/src/transformers/models/gemma...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
