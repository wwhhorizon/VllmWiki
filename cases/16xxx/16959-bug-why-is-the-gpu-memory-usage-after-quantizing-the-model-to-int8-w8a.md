# vllm-project/vllm#16959: [Bug]:Why is the GPU memory usage after quantizing the model to int8 W8A8 with llmcompressor almost the same as before quantization?

| 字段 | 值 |
| --- | --- |
| Issue | [#16959](https://github.com/vllm-project/vllm/issues/16959) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | ci_build;distributed_parallel;hardware_porting;model_support;multimodal_vlm;quantization;sampling_logits |
| 子分类 | memory |
| Operator 关键词 | cuda;operator;quantization;triton |
| 症状 | build_error |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]:Why is the GPU memory usage after quantizing the model to int8 W8A8 with llmcompressor almost the same as before quantization?

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug After using llmcompressor to quantize the fine-tuned QwenVL3B model VLM_R1 to an int8 W8A8 3B model, the expected GPU memory usage for the 3B int8 model should be around 3.6GB. However, during my testing (on an A10 GPU), the memory usage is 10GB, which seems abnormal. I'm not sure where the issue lies. Below is my test code: ``` import time import os from io import BytesIO import base64 from PIL import Image from transformers import AutoProcessor from vllm import LLM, SamplingParams from qwen_vl_utils import process_vision_info class VLLMTimestampRecognition: def __init__(self, model_path, device='cuda:0'): self.model = LLM( model=model_path, dtype="auto", max_model_len=4096, max_num_seqs=1, gpu_memory_utilization=0.5, device=device ) self.processor = AutoProcessor.from_pretrained(model_path,use_fast=True, min_pixels=256 * 28 * 28, max_pixels=1280 * 28 * 28, load_in_8bit=True ) def crop_and_concat_timestamp_regions(self, image, crop_size=(800, 150)): width, height = image.size top_left = image.crop((0, 0, crop_size[0], crop_size[1])) bottom_right = image.crop((width - crop_size[0], height - crop_size[1], width, height)) # 垂直拼接两个裁...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 5: [Bug]:Why is the GPU memory usage after quantizing the model to int8 W8A8 with llmcompressor almost the same as before quantization? bug;stale ### Your current environment ### 🐛 Describe the bug After using llmcompresso...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: abnormal. I'm not sure where the issue lies. Below is my test code: ``` import time import os from io import BytesIO import base64 from PIL import Image from transformers import AutoProcessor from vllm import LLM, Sampl...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 2: [Bug]:Why is the GPU memory usage after quantizing the model to int8 W8A8 with llmcompressor almost the same as before quantization? bug;stale ### Your current environment ### 🐛 Describe the bug After using llmcompresso...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: ass VLLMTimestampRecognition: def __init__(self, model_path, device='cuda:0'): self.model = LLM( model=model_path, dtype="auto", max_model_len=4096, max_num_seqs=1, gpu_memory_utilization=0.5, device=device
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: int8 W8A8 with llmcompressor almost the same as before quantization? bug;stale ### Your current environment ### 🐛 Describe the bug After using llmcompressor to quantize the fine-tuned QwenVL3B model VLM_R1 to an int8 W8...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
