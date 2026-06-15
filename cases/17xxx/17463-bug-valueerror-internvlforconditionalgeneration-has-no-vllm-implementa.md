# vllm-project/vllm#17463: [Bug]: ValueError: InternVLForConditionalGeneration has no vLLM implementation and the Transformers implementation is not compatible with vLLM.

| 字段 | 值 |
| --- | --- |
| Issue | [#17463](https://github.com/vllm-project/vllm/issues/17463) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: ValueError: InternVLForConditionalGeneration has no vLLM implementation and the Transformers implementation is not compatible with vLLM.

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug model = models.vllm( model_name= model_path, trust_remote_code=True, tokenizer=model_path, guided_decoding_backend="outlines", quantization="fp8" ) when I use vllm to infer mllm OpenGVLab/InternVL2_5-8B-MPO-hf(https://huggingface.co/OpenGVLab/InternVL2_5-8B-MPO-hf), I got this error: ValueError: InternVLForConditionalGeneration has no vLLM implementation and the Transformers implementation is not compatible with vLLM. I find that the architectures of hf version is different from base version like [OpenGVLab/InternVL2_5-8B-MPO]. the base version architectures in config.json of is InternVLChatModel. how to solve this? model:OpenGVLab/InternVL2_5-8B-MPO-hf vllm: 0.7.2 torch: 2.5.1 I also try below version, it does not work either vllm: 0.8.5 torch: 2.6.0 ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 5: [Bug]: ValueError: InternVLForConditionalGeneration has no vLLM implementation and the Transformers implementation is not compatible with vLLM. bug;stale ### Your current environment ### 🐛 Describe the bug model = model...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 2: True, tokenizer=model_path, guided_decoding_backend="outlines", quantization="fp8" ) when I use vllm to infer mllm OpenGVLab/InternVL2_5-8B-MPO-hf(https://huggingface.co/OpenGVLab/InternVL2_5-8B-MPO-hf), I got this erro...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: trust_remote_code=True, tokenizer=model_path, guided_decoding_backend="outlines", quantization="fp8" ) when I use vllm to infer mllm OpenGVLab/InternVL2_5-8B-MPO-hf(https://huggingface.co/OpenGVLab/InternVL2_5-8B-MPO-hf...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: tation is not compatible with vLLM. I find that the architectures of hf version is different from base version like [OpenGVLab/InternVL2_5-8B-MPO]. the base version architectures in config.json of is InternVLChatModel....
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: ransformers implementation is not compatible with vLLM. I find that the architectures of hf version is different from base version like [OpenGVLab/InternVL2_5-8B-MPO]. the base version architectures in config.json of is...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
