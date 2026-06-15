# vllm-project/vllm#19381: [New Model]: Support ColQwen2VL

| 字段 | 值 |
| --- | --- |
| Issue | [#19381](https://github.com/vllm-project/vllm/issues/19381) |
| 状态 | closed |
| 标签 | new-model;stale;multi-modality |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [New Model]: Support ColQwen2VL

### Issue 正文摘录

### The model to consider. ColQwen2VL is an efficient document retrieval vision language model based on Qwen2VL, as described in the paper "ColPali: Efficient Document Retrieval with Vision Language Models". The model is designed to generate embeddings rather than text outputs, making it suitable for document retrieval applications. This was supported in HF Transformers as of https://github.com/huggingface/transformers/pull/35778 An initial attempt to support the model was posted in https://github.com/vllm-project/vllm/pull/14291 but it was made before the HF definition was finalized so it grew out-of-date. ### The closest model vllm already supports. Qwen2VL is used as a base, so mostly it is wrapping that backbone ### What's your difficulty of supporting the model you want? See previous attempt https://github.com/vllm-project/vllm/pull/14291 ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: [New Model]: Support ColQwen2VL new-model;stale;multi-modality ### The model to consider. ColQwen2VL is an efficient document retrieval vision language model based on Qwen2VL, as described in the paper "ColPali: Efficie...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 2: ity ### The model to consider. ColQwen2VL is an efficient document retrieval vision language model based on Qwen2VL, as described in the paper "ColPali: Efficient Document Retrieval with Vision Language Models". The mod...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: el;stale;multi-modality ### The model to consider. ColQwen2VL is an efficient document retrieval vision language model based on Qwen2VL, as described in the paper "ColPali: Efficient Document Retrieval with Vision Langu...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: 291 ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: [New Model]: Support ColQwen2VL new-model;stale;multi-modality ### The model to consider. ColQwen2VL is an efficient document retrieval vision language model based on Qwen2VL, as described in the paper "ColPali: Efficie...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
