# vllm-project/vllm#15144: [Bug] Mismatch between `get_multimodal_embedding` output and `PlaceholderRange`

| 字段 | 值 |
| --- | --- |
| Issue | [#15144](https://github.com/vllm-project/vllm/issues/15144) |
| 状态 | closed |
| 标签 | bug;help wanted;v1;multi-modality |
| 评论 | 4; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug] Mismatch between `get_multimodal_embedding` output and `PlaceholderRange`

### Issue 正文摘录

In V1, we expect the output of `get_multimodal_embedding` to correspond to the `PlaceholderRange`, which is in turn constructed based on `PromptUpdateDetails.features`. However, the current V1 code doesn't validate this, causing the model to crash during inference when under high load (e.g. #14897, #14963). From a quick look at the code, these models output embedding sizes which are inconsistent with the placeholder range: - [x] Fuyu (fixed by #15731) - [x] Gemma3 (fixed by #14980) - [x] Idefics3 (fixed by #15696) - [x] InternVL-based models (fixed by #15086) - [x] MiniCPM-V (fixed by #15487) (Basically, any model that has image newline/column tokens after applying HF processor needs a mask to map image patch features to image embeddings, as described below.) To fix this, we can follow these steps: 1. Update the multi-modal processor to output a mask to indicate which positions in the `PlaceholderRange`-aligned embeddings should the patch features (outputted by vision encoder) be assigned to. This mask can be called `embed_is_patch`. 2. Use `scatter_patch_features` to scatter the patch features into the image embedding tensor. 3. When merging multimodal embeddings, use `select_pat...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 5: [Bug] Mismatch between `get_multimodal_embedding` output and `PlaceholderRange` bug;help wanted;v1;multi-modality In V1, we expect the output of `get_multimodal_embedding` to correspond to the `PlaceholderRange`, which...
- [Bitwise 确定性与数值等价](../patterns/bitwise_determinism_equivalence.md) - 分数 1: [Bug] Mismatch between `get_multimodal_embedding` output and `PlaceholderRange` bug;help wanted;v1;multi-modality In V1, we expect the output of `get_multimodal_embedding` to correspond to the `PlaceholderRange`, which...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: [Bug] Mismatch between `get_multimodal_embedding` output and `PlaceholderRange` bug;help wanted;v1;multi-modality In V1, we expect the output of `get_multimodal_embedding` to correspond to the `PlaceholderRange`, which...
- [MoE、GEMM 与 Expert Routing](../patterns/moe_gemm_routing.md) - 分数 1: nsistent with the placeholder range: - [x] Fuyu (fixed by #15731) - [x] Gemma3 (fixed by #14980) - [x] Idefics3 (fixed by #15696) - [x] InternVL-based models (fixed by #15086) - [x] MiniCPM-V (fixed by #15487) (Basicall...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
