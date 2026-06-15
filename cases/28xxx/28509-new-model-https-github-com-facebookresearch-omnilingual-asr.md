# vllm-project/vllm#28509: [New Model]: https://github.com/facebookresearch/omnilingual-asr

| 字段 | 值 |
| --- | --- |
| Issue | [#28509](https://github.com/vllm-project/vllm/issues/28509) |
| 状态 | open |
| 标签 | new-model;multi-modality |
| 评论 | 7; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [New Model]: https://github.com/facebookresearch/omnilingual-asr

### Issue 正文摘录

### The model to consider. OmniLingual ASR LLM model supports more than 1600 languages and achieves SOTA performance in few resources language tasks. However the official inference pipeline is not efficient, which needs VLLM help. ### The closest model vllm already supports. Like Voxtral, LlaMa. ### What's your difficulty of supporting the model you want? wav2vec2 encoder ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: [New Model]: https://github.com/facebookresearch/omnilingual-asr new-model;multi-modality ### The model to consider. OmniLingual ASR LLM model supports more than 1600 languages and achieves SOTA performance in few resou...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: hieves SOTA performance in few resources language tasks. However the official inference pipeline is not efficient, which needs VLLM help. ### The closest model vllm already supports. Like Voxtral, LlaMa. ### What's your...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: [New Model]: https://github.com/facebookresearch/omnilingual-asr new-model;multi-modality ### The model to consider. OmniLingual ASR LLM model supports more than 1600 languages and achieves SOTA performance in few resou...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
