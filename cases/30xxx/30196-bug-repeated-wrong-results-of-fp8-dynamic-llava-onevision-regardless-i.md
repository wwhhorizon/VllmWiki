# vllm-project/vllm#30196: [Bug]: Repeated, wrong results of FP8-Dynamic Llava-OneVision regardless input images

| 字段 | 值 |
| --- | --- |
| Issue | [#30196](https://github.com/vllm-project/vllm/issues/30196) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | development |
| 工作域 | model_support;multimodal_vlm;quantization;sampling_logits |
| 子分类 | env_compat |
| Operator 关键词 | cuda;fp8;quantization |
| 症状 | crash |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Repeated, wrong results of FP8-Dynamic Llava-OneVision regardless input images

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug I encounter an issue that [FP8-quantized Llava-Onevision ](https://huggingface.co/nm-testing/llava-onevision-qwen2-7b-ov-hf-FP8-dynamic) model produces (mostly) identical, wrong outputs for all input images (e.g., "blue" for red/blue/green images, wrong/repeated descriptions for natural images), while the [non-quantized model ](https://huggingface.co/llava-hf/llava-onevision-qwen2-7b-ov-hf) works correctly. Could you please help to take a look? ### 🛠️ Steps to reproduce - **Reproduction:** - Load `nm-testing/llava-onevision-qwen2-7b-ov-hf-FP8-dynamic` with vLLM, test with different mono-colored images (red/blue/green) - all produce identical outputs: ``` Testing with 3 different colored images: -------------------------------------------------------------------------------- RED image -> blue BLUE image -> blue GREEN image -> blue ``` , with different natural images - producing repeated, mostly identical descriptions: ``` Testing with 7 random real images from data -------------------------------------------------------------------------------- 1. image6_wide_1200x800.jpg -> The image 2. image1_landscape_800x600.jpg -> The image s...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 7: bug I encounter an issue that [FP8-quantized Llava-Onevision ](https://huggingface.co/nm-testing/llava-onevision-qwen2-7b-ov-hf-FP8-dynamic) model produces (mostly) identical, wrong outputs for all input images (e.g., "...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 5: lue GREEN image -> blue ``` , with different natural images - producing repeated, mostly identical descriptions: ``` Testing with 7 random real images from data ----------------------------------------------------------...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 3: [Bug]: Repeated, wrong results of FP8-Dynamic Llava-OneVision regardless input images bug;stale ### Your current environment ### 🐛 Describe the bug I encounter an issue that [FP8-quantized Llava-Onevision ](https://hugg...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: > The image shows a person standing in front of a building. 5. image5_small_400x300.jpg -> The image shows a scene with a person standing in front of a... 6. image3_square_500x500.jpg -> The image shows a person standin...
- [Bitwise 确定性与数值等价](../patterns/bitwise_determinism_equivalence.md) - 分数 2: works correctly. Could you please help to take a look? ### 🛠️ Steps to reproduce - **Reproduction:** - Load `nm-testing/llava-onevision-qwen2-7b-ov-hf-FP8-dynamic` with vLLM, test with different mono-colored images (red...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
