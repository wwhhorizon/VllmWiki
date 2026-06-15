# vllm-project/vllm#12492: [New Model]: deepseek-ai/Janus-Pro-7B

| 字段 | 值 |
| --- | --- |
| Issue | [#12492](https://github.com/vllm-project/vllm/issues/12492) |
| 状态 | closed |
| 标签 | new-model |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [New Model]: deepseek-ai/Janus-Pro-7B

### Issue 正文摘录

### The model to consider. deepseek-ai/Janus-Pro-7B Running vllm results in the following error with this model: _ValueError: The checkpoint you are trying to load has model type `multi_modality` but Transformers does not recognize this architecture. This could be because of an issue with the checkpoint, or because your version of Transformers is out of date._ This is with the latest vllm and latest transformers version ### The closest model vllm already supports. _No response_ ### What's your difficulty of supporting the model you want? _No response_ ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: . This could be because of an issue with the checkpoint, or because your version of Transformers is out of date._ This is with the latest vllm and latest transformers version ### The closest model vllm already supports....
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: has model type `multi_modality` but Transformers does not recognize this architecture. This could be because of an issue with the checkpoint, or because your version of Transformers is out of date._ This is with the lat...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: [New Model]: deepseek-ai/Janus-Pro-7B new-model ### The model to consider. deepseek-ai/Janus-Pro-7B Running vllm results in the following error with this model: _ValueError: The checkpoint you are trying to load has mod...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ecause your version of Transformers is out of date._ This is with the latest vllm and latest transformers version ### The closest model vllm already supports. _No response_ ### What's your difficulty of supporting the m...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
