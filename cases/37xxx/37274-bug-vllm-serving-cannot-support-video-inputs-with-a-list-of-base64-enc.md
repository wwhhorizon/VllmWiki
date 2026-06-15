# vllm-project/vllm#37274: [Bug]: vLLM serving cannot support video inputs with a list of base64-encoded extracted JPEG frames

| 字段 | 值 |
| --- | --- |
| Issue | [#37274](https://github.com/vllm-project/vllm/issues/37274) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;frontend_api;gemm_linear;hardware_porting;model_support;multimodal_vlm;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cuda;operator;sampling;triton |
| 症状 | build_error;nan_inf |
| 根因提示 | env_dependency;shape |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: vLLM serving cannot support video inputs with a list of base64-encoded extracted JPEG frames

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug The vLLM serving cannot support video inputs with a list of base64-encoded extracted JPEG frames. This usage is needed, since in my case the input video could be rather long and the resolusion might be large, I'd like to resize and sparsely sample frames before sending the request to vllm server. A simple example: ```python import base64 import json import os import tempfile import cv2 import requests MODEL_NAME="Qwen/Qwen3.5-2B" REQUEST_URL= "http://localhost:41091/v1/chat/completions" video_url='https://videos.pexels.com/video-files/5992517/5992517-hd_1920_1080_30fps.mp4' print(f"Downloading video from {video_url}...") # 1. Download video response = requests.get(video_url, stream=True) if response.status_code == 200: temp_file = tempfile.NamedTemporaryFile(delete=False, suffix=".mp4") for chunk in response.iter_content(chunk_size=8192): temp_file.write(chunk) temp_file.close() video_path = temp_file.name else: print("Failed to download video") exit(1) print("Extracting frames...") # 2. Extract frames, resize, base64 encode cap = cv2.VideoCapture(video_path) if not cap.isOpened(): print("Error opening video file") exit(1) fps =...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: before sending the request to vllm server. A simple example: ```python import base64 import json import os import tempfile import cv2 import requests MODEL_NAME="Qwen/Qwen3.5-2B" REQUEST_URL= "http://localhost:41091/v1/...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: base64 import json import os import tempfile import cv2 import requests MODEL_NAME="Qwen/Qwen3.5-2B" REQUEST_URL= "http://localhost:41091/v1/chat/completions" video_url='https://videos.pexels.com/video-files/5992517/599...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 3: large, I'd like to resize and sparsely sample frames before sending the request to vllm server. A simple example: ```python import base64 import json import os import tempfile import cv2 import requests MODEL_NAME="Qwen...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 2: "fps": fps, "duration": duration, "video_backend": "jpeg_sequence", "frames_indices": list(range(total)), "do_sample_frames": False, } return frames, metadata return self.load_bytes(base64.b64decode(data)) ```
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: ... ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
