# vllm-project/vllm#14529: [Bug]: glm4v Is Broken

| 字段 | 值 |
| --- | --- |
| Issue | [#14529](https://github.com/vllm-project/vllm/issues/14529) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: glm4v Is Broken

### Issue 正文摘录

### Your current environment Per comment ### 🐛 Describe the bug - GLM4V is broken on V0 and V1 ```bash VLLM_USE_V1=0 pytest -v -x models/decoder_only/vision_language/test_models.py -k glm4v ``` ```bash def _validate_mm_placeholders( self, mm_placeholders: Mapping[str, list[PlaceholderFeaturesInfo]], mm_item_counts: Mapping[str, int], ) -> None: for modality, item_count in mm_item_counts.items(): placeholders = mm_placeholders.get(modality, []) if len(placeholders) != item_count: > raise RuntimeError( f"Expected there to be {item_count} prompt updates " f"corresponding to {item_count} {modality} items, but " f"instead found {len(placeholders)} prompt updates! " "Either the prompt text has missing/incorrect tokens for " "multi-modal inputs, or there is a problem with your " "implementation of merged multi-modal processor for this " "model (usually arising from an inconsistency between " "`_call_hf_processor` and `_get_prompt_updates`).") E RuntimeError: Expected there to be 1 prompt updates corresponding to 1 image items, but instead found 0 prompt updates! Either the prompt text has missing/incorrect tokens for multi-modal inputs, or there is a problem with your implementation of m...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: bug - GLM4V is broken on V0 and V1 ```bash VLLM_USE_V1=0 pytest -v -x models/decoder_only/vision_language/test_models.py -k glm4v ``` ```bash def _validate_mm_placeholders( self, mm_placeholders: Mapping[str, list[Place...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: ``` ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 1: sh def _validate_mm_placeholders( self, mm_placeholders: Mapping[str, list[PlaceholderFeaturesInfo]], mm_item_counts: Mapping[str, int], ) -> None: for modality, item_count in mm_item_counts.items(): placeholders = mm_p...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: GLM4V is broken on V0 and V1 ```bash VLLM_USE_V1=0 pytest -v -x models/decoder_only/vision_language/test_models.py -k glm4v ``` ```bash def _validate_mm_placeholders( self, mm_placeholders: Mapping[str, list[Placeholder...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: escribe the bug - GLM4V is broken on V0 and V1 ```bash VLLM_USE_V1=0 pytest -v -x models/decoder_only/vision_language/test_models.py -k glm4v ``` ```bash def _validate_mm_placeholders( self, mm_placeholders: Mapping[str...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
