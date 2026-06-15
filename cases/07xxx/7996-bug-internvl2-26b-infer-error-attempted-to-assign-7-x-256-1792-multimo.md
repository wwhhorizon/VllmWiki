# vllm-project/vllm#7996: [Bug]: InternVL2-26B infer error:Attempted to assign 7 x 256 = 1792 multimodal tokens to 506 placeholders

| 字段 | 值 |
| --- | --- |
| Issue | [#7996](https://github.com/vllm-project/vllm/issues/7996) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 22; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: InternVL2-26B infer error:Attempted to assign 7 x 256 = 1792 multimodal tokens to 506 placeholders

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug ``` from dataclasses import dataclass from typing import Literal import torch from PIL import Image VLM_IMAGES_DIR = "vision_model_images" @dataclass(frozen=True) class ImageAsset: name: Literal["stop_sign", "cherry_blossom"] @property def pil_image(self) -> Image.Image: image_path = "image.jpg" return Image.open(image_path) """ This example shows how to use vLLM for running offline inference with the correct prompt format on vision language models. For most models, the prompt format should follow corresponding examples on HuggingFace model repository. """ from transformers import AutoTokenizer from vllm import LLM, SamplingParams # Input image and question image = ImageAsset("cherry_blossom").pil_image.convert("RGB") question = "What is the content of this image?" # InternVL def run_internvl(question): model_name = "/home/tdj/model/InternVL2-26B" llm = LLM( model=model_name,trust_remote_code=True, gpu_memory_utilization=0.9,tensor_parallel_size=8 ) tokenizer = AutoTokenizer.from_pretrained(model_name, trust_remote_code=True) messages = [{"role": "user", "content": f" \n{question}"}] prompt = tokenizer.apply_chat_template( messag...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 6: [Bug]: InternVL2-26B infer error:Attempted to assign 7 x 256 = 1792 multimodal tokens to 506 placeholders bug ### Your current environment ### 🐛 Describe the bug ``` from dataclasses import dataclass from typing import...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: our current environment ### 🐛 Describe the bug ``` from dataclasses import dataclass from typing import Literal import torch from PIL import Image VLM_IMAGES_DIR = "vision_model_images" @dataclass(frozen=True) class Ima...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: ed? ### Before submitting a new issue... - [X] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 1: prompt = tokenizer.apply_chat_template( messages, tokenize=False, add_generation_prompt=True ) # Stop tokens for InternVL # models variants may have different stop tokens # please refer to the model card for the correct...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
