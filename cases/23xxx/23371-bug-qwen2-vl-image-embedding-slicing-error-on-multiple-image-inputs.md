# vllm-project/vllm#23371: [Bug]: Qwen2_VL image embedding slicing error on multiple image inputs

| 字段 | 值 |
| --- | --- |
| Issue | [#23371](https://github.com/vllm-project/vllm/issues/23371) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | development |
| 工作域 | ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;multimodal_vlm;sampling_logits |
| 子分类 | env_compat |
| Operator 关键词 | cuda;sampling;triton |
| 症状 | build_error;crash |
| 根因提示 | dtype;env_dependency;shape |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Qwen2_VL image embedding slicing error on multiple image inputs

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug Batched Image embeddings were incorrectly split by `image_grid_thw`'s product when `image_embeds` are provided directly. They should be divided by the `spatial_merge_size` parameter on `image_grid_thw`'s product in the Qwen2_VL and Qwen2_5_Omni MultiModalDataParsers. It's already present in Qwen2_VL's model's input embedding processing procedure, which may not be considered carefully in the scenario when user provide `image_embed` and `image_grid_thw`, then `image_embed` are split across `image_grid_thw`'s product, which will cause a slice error(out of range without merging). There is similar problem on video processing. ```python import torch import requests from PIL import Image from io import BytesIO from vllm import LLM, SamplingParams from transformers import AutoProcessor model_name = "Qwen/Qwen2-VL-7B-Instruct" llm = LLM( model=model_name, tensor_parallel_size=1, dtype="float16", trust_remote_code=True ) processor = AutoProcessor.from_pretrained(model_name) image_urls = [ "https://example.com/image1.jpg", "https://example.com/image2.jpg", "https://example.com/image3.jpg", "https://example.com/image4.jpg", "https://example....

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: [Bug]: Qwen2_VL image embedding slicing error on multiple image inputs bug ### Your current environment ### 🐛 Describe the bug Batched Image embeddings were incorrectly split by `image_grid_thw`'s product when `image_em...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: [Bug]: Qwen2_VL image embedding slicing error on multiple image inputs bug ### Your current environment ### 🐛 Describe the bug Batched Image embeddings were incorrectly split by `image_grid_thw`'s product when `image_em...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 2: truct" llm = LLM( model=model_name, tensor_parallel_size=1, dtype="float16", trust_remote_code=True ) processor = AutoProcessor.from_pretrained(model_name) image_urls = [ "https://example.com/image1.jpg", "https://examp...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: ler_Encoder_inputs: {'1': [10]} grid_thw: tensor([[ 1, 14, 16]], device='cuda:0'), image_input type: image_embeds image_embeds shape: torch.Size([0, 2048]) merge_size: 2 sizes: tensor([56], device='cuda:0') ERROR 08-22...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: e is similar problem on video processing. ```python import torch import requests from PIL import Image from io import BytesIO from vllm import LLM, SamplingParams from transformers import AutoProcessor model_name = "Qwe...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
