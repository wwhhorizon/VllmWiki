# vllm-project/vllm#25390: [Usage]: vLLM doesn't properly handle 'tie_word_embeddings:true' for Idefics3 models

| 字段 | 值 |
| --- | --- |
| Issue | [#25390](https://github.com/vllm-project/vllm/issues/25390) |
| 状态 | closed |
| 标签 | usage |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Usage]: vLLM doesn't properly handle 'tie_word_embeddings:true' for Idefics3 models

### Issue 正文摘录

### Your current environment vLLM version: 0.10.1.1 Model: https://huggingface.co/ibm-granite/granite-docling-258M Discussion: https://huggingface.co/ibm-granite/granite-docling-258M/discussions/20 ### How would you like to use vllm I want to serve the granite-docling (https://huggingface.co/ibm-granite/granite-docling-258M) with vLLM. We're running into some issues in trying to do this, specifically: When the 'tie_word_embeddings' param is set in the config.json for the model, it is not inherited correctly at inference/model loading time for the granite-docling model (which is a Idefics3 model). We are encountering errors related to missing wte.weight parameters. Current placeholder fix: the docling team has provided a different set of weights for vllm, in a different branch, which has the parameters replicated ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: e]: vLLM doesn't properly handle 'tie_word_embeddings:true' for Idefics3 models usage ### Your current environment vLLM version: 0.10.1.1 Model: https://huggingface.co/ibm-granite/granite-docling-258M Discussion: https:...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: dings:true' for Idefics3 models usage ### Your current environment vLLM version: 0.10.1.1 Model: https://huggingface.co/ibm-granite/granite-docling-258M Discussion: https://huggingface.co/ibm-granite/granite-docling-258...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: ted ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
