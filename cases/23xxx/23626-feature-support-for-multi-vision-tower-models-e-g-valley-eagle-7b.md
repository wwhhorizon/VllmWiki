# vllm-project/vllm#23626: [Feature]: Support for Multi-Vision Tower Models (e.g., Valley-Eagle-7B)

| 字段 | 值 |
| --- | --- |
| Issue | [#23626](https://github.com/vllm-project/vllm/issues/23626) |
| 状态 | closed |
| 标签 | feature request;stale;multi-modality |
| 评论 | 6; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Feature]: Support for Multi-Vision Tower Models (e.g., Valley-Eagle-7B)

### Issue 正文摘录

### 🚀 The feature, motivation and pitch ### **Problem** vLLM excels in multimodal inference but lacks built-in support for models with multiple vision towers, like Valley-Eagle-7B (SigLIP + Qwen2-VL). Custom adaptations work but require extensive modifications for feature fusion, token handling, and weight loading. **### Proposed Solution** Extend BaseMultiModalProcessor to support multiple vision encoders with fusion (e.g., concatenation). Update SupportsMultiModal for multi-tower embeddings. Add config/weight mappers for multi-tower architectures. Include an example adapter for Valley-Eagle-7B. ### Alternatives Custom processor: Functional but not scalable. External fusion: Less efficient. ### Additional context This would enhance vLLM for advanced VLMs with multi-tower designs. ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 5: [Feature]: Support for Multi-Vision Tower Models (e.g., Valley-Eagle-7B) feature request;stale;multi-modality ### 🚀 The feature, motivation and pitch ### **Problem** vLLM excels in multimodal inference but lacks built-i...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: ultiple vision encoders with fusion (e.g., concatenation). Update SupportsMultiModal for multi-tower embeddings. Add config/weight mappers for multi-tower architectures. Include an example adapter for Valley-Eagle-7B. #...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: ]: Support for Multi-Vision Tower Models (e.g., Valley-Eagle-7B) feature request;stale;multi-modality ### 🚀 The feature, motivation and pitch ### **Problem** vLLM excels in multimodal inference but lacks built-in suppor...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: Custom processor: Functional but not scalable. External fusion: Less efficient. ### Additional context This would enhance vLLM for advanced VLMs with multi-tower designs. ### Before submitting a new issue... - [x] Make...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
