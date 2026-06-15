# vllm-project/vllm#32858: [Bug]: Use vllm to obtain Qwen3VL last token hidden status

| 字段 | 值 |
| --- | --- |
| Issue | [#32858](https://github.com/vllm-project/vllm/issues/32858) |
| 状态 | open |
| 标签 | bug;stale |
| 评论 | 11; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: Use vllm to obtain Qwen3VL last token hidden status

### Issue 正文摘录

### Your current environment from hdfs_io import hopen, hexists, hlist_files,hmv from qwen_vl_utils.vision_process import smart_resize import torch, base64, io from dataclasses import asdict import json import os import argparse import torch import base64 import re from PIL import Image from io import BytesIO import numpy as np # from vllm import LLM, SamplingParams from vllm import LLM, EngineArgs import requests from base64 import b64decode import sys import random from tqdm import tqdm from concurrent.futures import ThreadPoolExecutor, as_completed import os os.environ['VLLM_WORKER_MULTIPROC_METHOD'] = 'spawn' # 或者使用 spawn 模式 import torch.multiprocessing as mp mp.set_start_method('spawn', force=True) PIXEL_SIZE = 100 * 32 * 32 SIZE_FACTOR = 32 TXT_MAX_LEN = 1024 base_template = " system\n用一个词总结以下视频和文字. \n user\n {}\n \n assistant\n " # base_template_text = "用一个词总结这句话:\n{}\n " base_template_text = " system\n用一个词总结以下文字. \n user\n{} \n assistant\n " def qwen2_resize_image(image, min_pixels=PIXEL_SIZE, max_pixels=PIXEL_SIZE): """调整图像尺寸以适应模型输入要求""" # image = to_rgb(image) width, height = image.size resized_height, resized_width = smart_resize( height, width, factor=SIZE_FACTOR, min_...

## 候选优化模式

- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 4: t" engine_args = EngineArgs( model=checkpoint_path, dtype='float32', # 改为float32，减少bfloat16的精度波动 # dtype='bfloat16', # task="embed", runner='pooling', trust_remote_code=True, limit_mm_per_prompt={"image": 8, "video": 0}...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: [Bug]: Use vllm to obtain Qwen3VL last token hidden status bug;stale ### Your current environment from hdfs_io import hopen, hexists, hlist_files,hmv from qwen_vl_utils.vision_process import smart_resize import torch, b...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 3: [Bug]: Use vllm to obtain Qwen3VL last token hidden status bug;stale ### Your current environment from hdfs_io import hopen, hexists, hlist_files,hmv from qwen_vl_utils.vision_process import smart_resize import torch, b...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: token hidden status bug;stale ### Your current environment from hdfs_io import hopen, hexists, hlist_files,hmv from qwen_vl_utils.vision_process import smart_resize import torch, base64, io from dataclasses import asdic...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: hopen, hexists, hlist_files,hmv from qwen_vl_utils.vision_process import smart_resize import torch, base64, io from dataclasses import asdict import json import os import argparse import torch import base64 import re fr...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
