# vllm-project/vllm#22064: [Bug]: RuntimeError: Index put requires the source and destination dtypes match

| 字段 | 值 |
| --- | --- |
| Issue | [#22064](https://github.com/vllm-project/vllm/issues/22064) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 0; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;hardware_porting;model_support;multimodal_vlm;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cuda;gemm;operator;sampling;triton |
| 症状 | build_error;nan_inf |
| 根因提示 | dtype;env_dependency;shape |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: RuntimeError: Index put requires the source and destination dtypes match

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug ```shell vllm serve /home/jovyan/Qwen2-VL-2B-Instruct --limit-mm-per-prompt.image 218400001 --allowed-local-media-path /home/jovyan/vllm ``` ```python from transformers import AutoProcessor from PIL import Image import io import base64 import requests import json import torch from openai import OpenAI image_path = "/home/jovyan/vllm/downloads/lion.jpg" model = "/home/jovyan/Qwen2-VL-2B-Instruct" pixel_values = torch.load("/home/jovyan/vllm/downloads/image_embeds2_1.pt", map_location="cpu") image_grid_thw = torch.load("/home/jovyan/vllm/downloads/grid_thw2_1.pt", map_location="cpu") print(f"pixel_values shape: {pixel_values.shape} -- {pixel_values.dtype}") print( f"image_grid_thw shape: {image_grid_thw.shape} --- {image_grid_thw.dtype}" ) def encode_image_embedding_to_base64(image_embedding) -> str: """ Encode image embedding to base64 string """ buffer = io.BytesIO() torch.save(image_embedding, buffer) buffer.seek(0) binary_data = buffer.read() base64_image_embedding = base64.b64encode(binary_data).decode('utf-8') return base64_image_embedding base64_image_embedding = encode_image_embedding_to_base64(pixel_values) base64_image_gr...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: ed-local-media-path /home/jovyan/vllm ``` ```python from transformers import AutoProcessor from PIL import Image import io import base64 import requests import json import torch from openai import OpenAI image_path = "/...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: environment ### 🐛 Describe the bug ```shell vllm serve /home/jovyan/Qwen2-VL-2B-Instruct --limit-mm-per-prompt.image 218400001 --allowed-local-media-path /home/jovyan/vllm ``` ```python from transformers import AutoProc...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 4: mport AutoProcessor from PIL import Image import io import base64 import requests import json import torch from openai import OpenAI image_path = "/home/jovyan/vllm/downloads/lion.jpg" model = "/home/jovyan/Qwen2-VL-2B-...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 3: [Bug]: RuntimeError: Index put requires the source and destination dtypes match bug ### Your current environment ### 🐛 Describe the bug ```shell vllm serve /home/jovyan/Qwen2-VL-2B-Instruct --limit-mm-per-prompt.image 2...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: ``` ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...

## Wiki 抽取状态

- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
