# vllm-project/vllm#35999: [New Model]: MetaCLIP-2 variants

| 字段 | 值 |
| --- | --- |
| Issue | [#35999](https://github.com/vllm-project/vllm/issues/35999) |
| 状态 | open |
| 标签 | new-model;stale;multi-modality |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [New Model]: MetaCLIP-2 variants

### Issue 正文摘录

### The model to consider. Model Collections: https://huggingface.co/collections/facebook/meta-clip-2 ### The closest model vllm already supports. CLIP ### What's your difficulty of supporting the model you want? Hello, I checked supported models docs but couldn't see MetaCLIP-2 models. There is CLIPModel class but MetaCLIP uses different class it seems: `Usage of the MetaCLIP 2 models is identical to the CLIP models, you just need the MetaClip2Model class instead of CLIPModel.` (https://huggingface.co/docs/transformers/main/model_doc/metaclip_2) Can you add MetaCLIP-2 support on vLLM? Model Collections: https://huggingface.co/collections/facebook/meta-clip-2 ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: [New Model]: MetaCLIP-2 variants new-model;stale;multi-modality ### The model to consider. Model Collections: https://huggingface.co/collections/facebook/meta-clip-2 ### The closest model vllm already supports. CLIP ###...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: p-2 ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: [New Model]: MetaCLIP-2 variants new-model;stale;multi-modality ### The model to consider. Model Collections: https://huggingface.co/collections/facebook/meta-clip-2 ### The closest model vllm already supports. CLIP ###...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
