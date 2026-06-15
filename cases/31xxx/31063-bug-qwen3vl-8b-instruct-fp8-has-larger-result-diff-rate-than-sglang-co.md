# vllm-project/vllm#31063: [Bug]: Qwen3VL-8B-instruct-FP8 has larger result diff rate than sglang compared with transformers

| 字段 | 值 |
| --- | --- |
| Issue | [#31063](https://github.com/vllm-project/vllm/issues/31063) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 4; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | attention_kv_cache;ci_build;hardware_porting;model_support;multimodal_vlm;quantization;sampling_logits |
| 子分类 | precision |
| Operator 关键词 | cuda;fp8;sampling |
| 症状 | nondeterministic |
| 根因提示 | dtype;env_dependency;race_condition;shape |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Qwen3VL-8B-instruct-FP8 has larger result diff rate than sglang compared with transformers

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug the script is ``` import os, json, torch from PIL import Image from transformers import AutoProcessor from vllm import LLM, SamplingParams from qwen_vl_utils import process_vision_info from tqdm import tqdm import time import cv2 import pandas as pd import numpy as np from PIL import Image import requests from io import BytesIO import random from transformers import Qwen3VLForConditionalGeneration, AutoProcessor import sglang as sgl from sglang.srt.parser.conversation import chat_templates def set_seeds(seed_list, device=None): if isinstance(seed_list, (tuple, list)): seed = sum(seed_list) else: seed = seed_list random.seed(seed) np.random.seed(seed) torch.manual_seed(seed) torch.cuda.manual_seed_all(seed) torch.cuda.deterministic = True torch.cuda.benchmark = False torch.backends.cudnn.deterministic = True torch.backends.cudnn.benchmark = False return torch.Generator(device).manual_seed(seed) def get_rect_area(binary_mask): binary_mask = binary_mask.copy() contours, _ = cv2.findContours(binary_mask*255, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE) if len(contours)==0: # print('no area to mask') return binary_mask,[0,0,0,0] all_poin...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 5: Your current environment ### 🐛 Describe the bug the script is ``` import os, json, torch from PIL import Image from transformers import AutoProcessor from vllm import LLM, SamplingParams from qwen_vl_utils import proces...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 5: [Bug]: Qwen3VL-8B-instruct-FP8 has larger result diff rate than sglang compared with transformers bug;stale ### Your current environment ### 🐛 Describe the bug the script is ``` import os, json, torch from PIL import Im...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 5: [Bug]: Qwen3VL-8B-instruct-FP8 has larger result diff rate than sglang compared with transformers bug;stale ### Your current environment ### 🐛 Describe the bug the script is ``` import os, json, torch from PIL import Im...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 3: rch.cuda.deterministic = True torch.cuda.benchmark = False torch.backends.cudnn.deterministic = True torch.backends.cudnn.benchmark = False return torch.Generator(device).manual_seed(seed) def get_rect_area(binary_mask)...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: eed(seed) np.random.seed(seed) torch.manual_seed(seed) torch.cuda.manual_seed_all(seed) torch.cuda.deterministic = True torch.cuda.benchmark = False torch.backends.cudnn.deterministic = True torch.backends.cudnn.benchma...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
