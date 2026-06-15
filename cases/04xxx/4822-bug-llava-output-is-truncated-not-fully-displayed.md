# vllm-project/vllm#4822: [Bug]: llava, output is truncated, not fully displayed

| 字段 | 值 |
| --- | --- |
| Issue | [#4822](https://github.com/vllm-project/vllm/issues/4822) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: llava, output is truncated, not fully displayed

### Issue 正文摘录

### Your current environment ```text The output of `python collect_env.py` ``` ### 🐛 Describe the bug VLLM now supports the Llava model. We know that the Llava model has various chat templates, such as the Vicuna template and the Llama2 template. I have two questions: 1.How do I specify a chat template? 2.When I use the Llava module in the LLama language model for prediction, I find that the output is usually truncated and not fully displayed. The length after truncation is approximately 14 characters. What's going on with this? How can I avoid this situation? ``` import argparse import os import subprocess from PIL import Image import torch from PIL import Image from vllm import LLM from vllm.sequence import MultiModalData llm = LLM( model= "/media/star/8T/model/gpt/llava/llava-hf/llava-1.5-7b-hf", image_input_type="pixel_values", image_token_id=32000, image_input_shape="1,3,336,336", image_feature_size=576, gpu_memory_utilization=0.3, swap_space=8 ) from transformers import CLIPVisionModel, CLIPImageProcessor, CLIPVisionConfig image_processor= CLIPImageProcessor.from_pretrained("/media/star/8T/model/clip/openai_clip/clip-vit-large-patch14-336") image_path="/media/star/8T/tmp/gpt...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 5: collect_env.py` ``` ### 🐛 Describe the bug VLLM now supports the Llava model. We know that the Llava model has various chat templates, such as the Vicuna template and the Llama2 template. I have two questions: 1.How do...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: a template and the Llama2 template. I have two questions: 1.How do I specify a chat template? 2.When I use the Llava module in the LLama language model for prediction, I find that the output is usually truncated and not...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: r.preprocess(image_data, return_tensors='pt')['pixel_values'].half().to("cuda") question="desc the image in detail " prompt = " " * 576 + ( f"\n USER: desc the image in detail \nASSISTANT:") sampling_params = SamplingPa...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: ISTANT:") sampling_params = SamplingParams(temperature=0.8, top_p=0.95) RequestOutput = llm.generate(prompt, multi_modal_data=MultiModalData( type=MultiModalData.Type.IMAGE, data=image_tensor)) print(RequestOutput[0].ou...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
