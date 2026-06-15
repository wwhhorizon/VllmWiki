# vllm-project/vllm#19724: [Bug]: Strange cuda out of memory when runing llava1.5 7b on 80G A100

| 字段 | 值 |
| --- | --- |
| Issue | [#19724](https://github.com/vllm-project/vllm/issues/19724) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 0; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;multimodal_vlm;sampling_logits |
| 子分类 | memory |
| Operator 关键词 | cuda;gemm;triton |
| 症状 | build_error;oom |
| 根因提示 | env_dependency;shape |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Strange cuda out of memory when runing llava1.5 7b on 80G A100

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug Use the example code in the doc and get this error ``` ''' This code is used to generate response from vLLM using llava and llava onevision models with single image input. I got cuda out of memory at the second sample. ''' import setuptools.dist import os import random from contextlib import contextmanager from dataclasses import asdict from typing import NamedTuple, Optional from huggingface_hub import snapshot_download from transformers import AutoTokenizer from vllm import LLM, EngineArgs, SamplingParams from vllm.assets.image import ImageAsset from vllm.assets.video import VideoAsset from vllm.lora.request import LoRARequest from vllm.utils import FlexibleArgumentParser from vllm.multimodal.utils import fetch_image from PIL import Image import json from tqdm import tqdm def convert_image_mode(image: Image.Image, to_mode: str): if image.mode == to_mode: return image elif image.mode == "RGBA" and to_mode == "RGB": return rgba_to_rgb(image) else: return image.convert(to_mode) class ModelRequestData(NamedTuple): engine_args: EngineArgs prompts: list[str] stop_token_ids: Optional[list[int]] = None lora_requests: Optional[list[LoRA...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 7: e is used to generate response from vLLM using llava and llava onevision models with single image input. I got cuda out of memory at the second sample. ''' import setuptools.dist import os import random from contextlib...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: h single image input. I got cuda out of memory at the second sample. ''' import setuptools.dist import os import random from contextlib import contextmanager from dataclasses import asdict from typing import NamedTuple,...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: [Bug]: Strange cuda out of memory when runing llava1.5 7b on 80G A100 bug ### Your current environment ### 🐛 Describe the bug Use the example code in the doc and get this error ``` ''' This code is used to generate resp...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: ;hardware_porting;model_support;multimodal_vlm;sampling_logits cuda;gemm;triton build_error;oom env_dependency;shape Your current environment
- [KV Cache 容量、压缩与 Offload](../patterns/kv_cache_capacity_offload.md) - 分数 1: odel_support;multimodal_vlm;sampling_logits cuda;gemm;triton build_error;oom env_dependency;shape Your current environment

## Wiki 抽取状态

- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
