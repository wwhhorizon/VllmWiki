# vllm-project/vllm#30378: [Feature]: Automatically infer Qwen3 reranker settings (remove need for hf_overrides)

| 字段 | 值 |
| --- | --- |
| Issue | [#30378](https://github.com/vllm-project/vllm/issues/30378) |
| 状态 | open |
| 标签 | feature request;stale |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Feature]: Automatically infer Qwen3 reranker settings (remove need for hf_overrides)

### Issue 正文摘录

### 🚀 The feature, motivation and pitch When running **Qwen3 reranker models** in vLLM, users must manually specify several hf_overrides parameters to make the model load correctly: ``` --hf_overrides '{ "architectures": ["Qwen3ForSequenceClassification"], "classifier_from_token": ["no", "yes"], "is_original_qwen3_reranker": true }' ``` It seems that vLLM cannot currently infer these settings directly from the model config. Other inference engines (e.g., **llama.cpp**) load Qwen3 rerankers without needing additional parameters. This issue requests that vLLM automatically detect and apply these required settings when loading Qwen3 rerankers. **Problem Description** Without overrides, vLLM fails to instantiate the reranker correctly. The user must manually supply parameters that: - Override the architecture name - Specify classifier-from-token behavior - Mark it as an "original" Qwen3 reranker model This adds friction and makes Qwen3 reranker support feel incomplete or non-automatic. Example command requiring overrides: ``` vllm serve qwen/Qwen3-xxx-reranker \ --hf_overrides '{"architectures":["Qwen3ForSequenceClassification"], ... }' ``` **Expected behavior:** vLLM should infer the...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 5: [Feature]: Automatically infer Qwen3 reranker settings (remove need for hf_overrides) feature request;stale ### 🚀 The feature, motivation and pitch When running **Qwen3 reranker models** in vLLM, users must manually spe...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: lly infer Qwen3 reranker settings (remove need for hf_overrides) feature request;stale ### 🚀 The feature, motivation and pitch When running **Qwen3 reranker models** in vLLM, users must manually specify several hf_overr...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: When running **Qwen3 reranker models** in vLLM, users must manually specify several hf_overrides parameters to make the model load correctly: ``` --hf_overrides '{ "architectures": ["Qwen3ForSequenceClassification"], "c...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: s parameters to make the model load correctly: ``` --hf_overrides '{ "architectures": ["Qwen3ForSequenceClassification"], "classifier_from_token": ["no", "yes"], "is_original_qwen3_reranker": true }' ``` It seems that v...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 1: tecture and classifier behavior based solely on the model’s Hugging Face metadata, without requiring explicit overrides. **Why This Matters** - Reduces user setup errors - Makes Qwen3 reranker support seamless and consi...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
