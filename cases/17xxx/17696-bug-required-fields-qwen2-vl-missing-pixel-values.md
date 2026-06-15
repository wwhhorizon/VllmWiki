# vllm-project/vllm#17696: [Bug]: Required fields Qwen2-VL missing "pixel_values"

| 字段 | 值 |
| --- | --- |
| Issue | [#17696](https://github.com/vllm-project/vllm/issues/17696) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: Required fields Qwen2-VL missing "pixel_values"

### Issue 正文摘录

### Your current environment ** vllm 0.7.3** ### 🐛 Describe the bug The _parse_and_validate_image_input method implicitly requires pixel_values and image_grid_thw to construct the Qwen2VLImagePixelInputs dictionary. ` if pixel_values is not None: pixel_values = self._validate_and_reshape_mm_tensor( pixel_values, "image pixel values") image_grid_thw = self._validate_and_reshape_mm_tensor( image_grid_thw, "image grid_thw") if not isinstance(pixel_values, (torch.Tensor, list)): raise ValueError("Incorrect type of image pixel values. " f"Got type: {type(pixel_values)}") return Qwen2VLImagePixelInputs(type="pixel_values", pixel_values=pixel_values, image_grid_thw=image_grid_thw)` However, when this dictionary reaches Qwen2VLMultiModalDataParser._parse_image_data, the code incorrectly assumes any dictionary must represent pre-computed embeddings. ` if isinstance(data, dict): return DictEmbeddingItems( data, modality="image", required_fields={"image_embeds", "image_grid_thw"}, fields_factory=_qwen2vl_field_config, )` It immediately attempts to create DictEmbeddingItems, which has its own required_fields set to {"image_embeds", "image_grid_thw"}. Because the dictionary for the pixel_value...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: [Bug]: Required fields Qwen2-VL missing "pixel_values" bug;stale ### Your current environment ** vllm 0.7.3** ### 🐛 Describe the bug The _parse_and_validate_image_input method implicitly requires pixel_values and image_...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: ### 🐛 Describe the bug The _parse_and_validate_image_input method implicitly requires pixel_values and image_grid_thw to construct the Qwen2VLImagePixelInputs dictionary. ` if pixel_values is not None: pixel_values = se...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: [Bug]: Required fields Qwen2-VL missing "pixel_values" bug;stale ### Your current environment ** vllm 0.7.3** ### 🐛 Describe the bug The _parse_and_validate_image_input method implicitly requires pixel_values and image_...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
