# vllm-project/vllm#12118: [Bug]: Fail to use deepseek-vl2

| 字段 | 值 |
| --- | --- |
| Issue | [#12118](https://github.com/vllm-project/vllm/issues/12118) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 18; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;hardware_porting;model_support;multimodal_vlm;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cuda;gemm;operator;sampling;triton |
| 症状 | build_error;crash;nan_inf |
| 根因提示 | env_dependency;shape |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Fail to use deepseek-vl2

### Issue 正文摘录

### Your current environment ### Model Input Dumps _No response_ ### 🐛 Describe the bug I run the original example of [deepseek-vl2 ](https://docs.vllm.ai/en/latest/getting_started/examples/vision_language.html) in the documentation: ```python from argparse import ArgumentParser from typing import List, Dict import torch from transformers import AutoModelForCausalLM import PIL.Image import random import random import os,sys from transformers import AutoTokenizer from vllm import LLM, SamplingParams from vllm.assets.image import ImageAsset from vllm.assets.video import VideoAsset from vllm.utils import FlexibleArgumentParser os.environ['https_proxy'] = 'http://127.0.0.1:7890' os.environ['http_proxy'] = 'http://127.0.0.1:7890' os.environ["CUDA_VISIBLE_DEVICES"] = "0,1" # Deepseek-VL2 def run_deepseek_vl2(question: str, modality: str): assert modality == "image" #model_name = "deepseek-ai/deepseek-vl2" model_name="/home/xxxx/model/deepseek-vl2" llm = LLM(model=model_name, max_model_len=4096, max_num_seqs=2, disable_mm_preprocessor_cache=args.disable_mm_preprocessor_cache, hf_overrides={"architectures": ["DeepseekVLV2ForCausalLM"]}) prompt = f" : \n{question}\n\n :" stop_token_ids = N...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 7: [Bug]: Fail to use deepseek-vl2 bug ### Your current environment ### Model Input Dumps _No response_ ### 🐛 Describe the bug I run the original example of [deepseek-vl2 ](https://docs.vllm.ai/en/latest/getting_started/ex...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 6: les/vision_language.html) in the documentation: ```python from argparse import ArgumentParser from typing import List, Dict import torch from transformers import AutoModelForCausalLM import PIL.Image import random impor...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: .1:7890' os.environ['http_proxy'] = 'http://127.0.0.1:7890' os.environ["CUDA_VISIBLE_DEVICES"] = "0,1" # Deepseek-VL2 def run_deepseek_vl2(question: str, modality: str): assert modality == "image" #model_name = "deepsee...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 2: l_data": { modality: data }, } else: # Batch inference if args.image_repeat_prob is not None: # Repeat images with specified probability of "image_repeat_prob" inputs = apply_image_repeat(args.image_repeat_prob,
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: dal_vlm;sampling_logits;speculative_decoding cuda;gemm;operator;sampling;triton build_error;crash;nan_inf env_dependency;shape Your current environment

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
