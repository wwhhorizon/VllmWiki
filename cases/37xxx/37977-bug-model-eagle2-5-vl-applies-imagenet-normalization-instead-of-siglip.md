# vllm-project/vllm#37977: [Bug][Model] Eagle2.5-VL applies ImageNet normalization instead of SigLIP2

| 字段 | 值 |
| --- | --- |
| Issue | [#37977](https://github.com/vllm-project/vllm/issues/37977) |
| 状态 | open |
| 标签 |  |
| 评论 | 0; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug][Model] Eagle2.5-VL applies ImageNet normalization instead of SigLIP2

### Issue 正文摘录

### Your current environment vLLM main branch (commit 5bf3c42d4) ### Model nvidia/Eagle2.5-8B, nvidia/Eagle2-1B (all Eagle2.5-VL variants) ### 🐛 Describe the bug Eagle2.5-VL in vLLM applies **ImageNet normalization** (`mean=[0.485, 0.456, 0.406]`, `std=[0.229, 0.224, 0.225]`) instead of **SigLIP2 normalization** (`mean=[0.5, 0.5, 0.5]`, `std=[0.5, 0.5, 0.5]`). Eagle2.5-VL uses SigLIP2 as its vision encoder, but inherits InternVL's `InternVLImageProcessor` which hardcodes ImageNet normalization. The model's official HuggingFace `preprocessor_config.json` specifies `image_mean=[0.5, 0.5, 0.5]` and `image_std=[0.5, 0.5, 0.5]`. **Call chain:** ``` Eagle2_5_VLProcessingInfo.get_image_processor() [eagle2_5_vl.py:87] └─► InternVLImageProcessor(**kwargs) └─► _images_to_pixel_values_lst() [internvl.py:257] └─► image_to_pixel_values_internvl() [internvl.py:169] └─► build_transform(input_size) [internvl.py:27] └─► T.Normalize(IMAGENET_MEAN, IMAGENET_STD) ← wrong for Eagle2.5 ``` **Evidence:** - [nvidia/Eagle2-1B preprocessor_config.json](https://huggingface.co/nvidia/Eagle2-1B/raw/main/preprocessor_config.json): `image_mean=[0.5, 0.5, 0.5]`, `image_std=[0.5, 0.5, 0.5]` - Eagle2.5 uses SigLIP...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: [Bug][Model] Eagle2.5-VL applies ImageNet normalization instead of SigLIP2 ### Your current environment vLLM main branch (commit 5bf3c42d4) ### Model nvidia/Eagle2.5-8B, nvidia/Eagle2-1B (all Eagle2.5-VL variants) ### 🐛...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: LImageProcessor` which hardcodes ImageNet normalization. The model's official HuggingFace `preprocessor_config.json` specifies `image_mean=[0.5, 0.5, 0.5]` and `image_std=[0.5, 0.5, 0.5]`. **Call chain:** ``` Eagle2_5_V...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: on. ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
