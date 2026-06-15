# vllm-project/vllm#13179: [Doc]: Clarify QLoRA (Quantized Model + LoRA) Support in Documentation

| 字段 | 值 |
| --- | --- |
| Issue | [#13179](https://github.com/vllm-project/vllm/issues/13179) |
| 状态 | closed |
| 标签 | documentation |
| 评论 | 11; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Doc]: Clarify QLoRA (Quantized Model + LoRA) Support in Documentation

### Issue 正文摘录

### 📚 The doc issue Two parts of the documentation appear to contradict each other, especially at first glance. Here, it is explicitly stated that LoRA inference with a quantized model is **not supported**: https://github.com/vllm-project/vllm/blob/4c0d93f4b2de241336f4732cb5799cee8fedcb52/docs/source/models/supported_models.md?plain=1#L59-L61 However, here, an example is provided for running offline inference with a quantized model and a LoRA adapter: https://github.com/vllm-project/vllm/blob/4c0d93f4b2de241336f4732cb5799cee8fedcb52/examples/offline_inference/lora_with_quantization_inference.py#L3-L4 To resolve this confusion, it would be very helpful to clarify the following points directly (please correct me if I am mistaken): 1. **QLoRA *is* supported**, but **only for offline inference**. This means you cannot dynamically load LoRA adapters after loading the quantized base model. 2. **QLoRA *is not* supported** with the OpenAI-compatible server, even for a single LoRA-base model pair. **Edit:** It's easy to miss on the docs site, that `##### LORA and quantization` is a subsection of `### Transformers fallback`, that's why I was confused. https://github.com/vllm-project/vllm/bl...

## 候选优化模式

- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: that `##### LORA and quantization` is a subsection of `### Transformers fallback`, that's why I was confused. https://github.com/vllm-project/vllm/blob/4c0d93f4b2de241336f4732cb5799cee8fedcb52/docs/source/models/support...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: sue Two parts of the documentation appear to contradict each other, especially at first glance. Here, it is explicitly stated that LoRA inference with a quantized model is **not supported**: https://github.com/vllm-proj...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 1: [Doc]: Clarify QLoRA (Quantized Model + LoRA) Support in Documentation documentation ### 📚 The doc issue Two parts of the documentation appear to contradict each other, especially at first glance. Here, it is explicitly...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: [Doc]: Clarify QLoRA (Quantized Model + LoRA) Support in Documentation documentation ### 📚 The doc issue Two parts of the documentation appear to contradict each other, especially at first glance. Here, it is explicitly...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
