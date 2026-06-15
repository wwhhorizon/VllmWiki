# vllm-project/vllm#31479: [Feature]: Enable LoRA support for tower and connector in more MM models

| 字段 | 值 |
| --- | --- |
| Issue | [#31479](https://github.com/vllm-project/vllm/issues/31479) |
| 状态 | open |
| 标签 | help wanted;feature request;multi-modality |
| 评论 | 10; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Feature]: Enable LoRA support for tower and connector in more MM models

### Issue 正文摘录

### 🚀 The feature, motivation and pitch Regarding multi-modal models, we have supported adding LoRA to the tower encoder and connector,see: #26674, but have only implemented it for a few models (`Qwen VL series` and `idefics3`). There is no reason not to support other multi-modal models. ### Solution For the remaining models we want to support adding LoRA to the tower encoder and connector, we need to implement the following 2 functions: `get_num_mm_encoder_tokens` `get_num_mm_connector_tokens` **The root cause we need to implement these two functions is:** the number of multi-modal tokens represented in the language model does not necessarily match the input length required by the linear layers in the vision tower or connector. Since the lora_mapping requires the precise input token length prior to activation, these helper functions are necessary to bridge the discrepancy and calculate the correct lengths. ### List of models that are completed or WIP - Qwen VL series: #26674 - idefics3: #26674 - LLaVA: https://github.com/vllm-project/vllm/pull/31513 - BLIP2: https://github.com/vllm-project/vllm/pull/31620 - GLM4 : https://github.com/vllm-project/vllm/pull/31652 - PaliGemma https:...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 5: [Feature]: Enable LoRA support for tower and connector in more MM models help wanted;feature request;multi-modality ### 🚀 The feature, motivation and pitch Regarding multi-modal models, we have supported adding LoRA to...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: in the vision tower or connector. Since the lora_mapping requires the precise input token length prior to activation, these helper functions are necessary to bridge the discrepancy and calculate the correct lengths. ###...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: 9291 ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), w...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 1: ed by the linear layers in the vision tower or connector. Since the lora_mapping requires the precise input token length prior to activation, these helper functions are necessary to bridge the discrepancy and calculate...
- [MoE、GEMM 与 Expert Routing](../patterns/moe_gemm_routing.md) - 分数 1: ull/31620 - GLM4 : https://github.com/vllm-project/vllm/pull/31652 - PaliGemma https://github.com/vllm-project/vllm/pull/31656 - H2OVL https://github.com/vllm-project/vllm/pull/31696 - Pixtral https://github.com/vllm-pr...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
