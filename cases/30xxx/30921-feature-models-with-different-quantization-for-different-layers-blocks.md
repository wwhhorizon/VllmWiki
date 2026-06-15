# vllm-project/vllm#30921: [Feature]: Models with different quantization for different layers/blocks

| 字段 | 值 |
| --- | --- |
| Issue | [#30921](https://github.com/vllm-project/vllm/issues/30921) |
| 状态 | open |
| 标签 | feature request;unstale |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | attention_kv_cache;distributed_parallel;frontend_api;gemm_linear;model_support;moe;quantization;scheduler_memory |
| 子分类 | precision |
| Operator 关键词 | attention;cuda;operator;quantization |
| 症状 | crash |
| 根因提示 | dtype;env_dependency;shape |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Feature]: Models with different quantization for different layers/blocks

### Issue 正文摘录

### 🚀 The feature, motivation and pitch We at [Unsloth](https://unsloth.ai/) have dynamically quantized bnb 4bit models which we ideally do to preserve accuracy, keeping in mind the important layers. We let them be in 16-bit while quantizing the rest to 4-bit. For example, if you see [unsloth/Qwen3-VL-2B-Instruct-unsloth-bnb-4bit](https://huggingface.co/unsloth/Qwen3-VL-2B-Instruct-unsloth-bnb-4bit/tree/main), all of the vision layers are left unquantized, while having only a [few language layers](https://huggingface.co/unsloth/Qwen3-VL-2B-Instruct-unsloth-bnb-4bit/blob/main/config.json#L31) in half precision and the rest in 4bit. Do note that we noticed, in cases where all the image layers are 16bit and all the text layers are 4bit, vllm has no problems running/serving the model. It'd be great if vLLM can support this kind of mixture of layers/blocks where within a layer (say language.0 in this case) or within a module (language vs vision) there can be mixture of quantizations ### Additional context This is what happens when I try to serve the said model ```bash ❯ vllm serve unsloth/Qwen3-VL-2B-Instruct-unsloth-bnb-4bit Skipping import of cpp extensions due to incompatible torch...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 6: bit models which we ideally do to preserve accuracy, keeping in mind the important layers. We let them be in 16-bit while quantizing the rest to 4-bit. For example, if you see [unsloth/Qwen3-VL-2B-Instruct-unsloth-bnb-4...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 5: [Feature]: Models with different quantization for different layers/blocks feature request;unstale ### 🚀 The feature, motivation and pitch We at [Unsloth](https://unsloth.ai/) have dynamically quantized bnb 4bit models w...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 3: [Feature]: Models with different quantization for different layers/blocks feature request;unstale ### 🚀 The feature, motivation and pitch We at [Unsloth](https://unsloth.ai/) have dynamically quantized bnb 4bit models w...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 3: : Models with different quantization for different layers/blocks feature request;unstale ### 🚀 The feature, motivation and pitch We at [Unsloth](https://unsloth.ai/) have dynamically quantized bnb 4bit models which we i...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 3: ve dynamically quantized bnb 4bit models which we ideally do to preserve accuracy, keeping in mind the important layers. We let them be in 16-bit while quantizing the rest to 4-bit. For example, if you see [unsloth/Qwen...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
