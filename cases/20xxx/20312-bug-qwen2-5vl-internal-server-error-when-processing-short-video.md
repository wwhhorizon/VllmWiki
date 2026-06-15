# vllm-project/vllm#20312: [Bug]: qwen2_5vl Internal Server Error when processing short video

| 字段 | 值 |
| --- | --- |
| Issue | [#20312](https://github.com/vllm-project/vllm/issues/20312) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 0; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;multimodal_vlm;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cuda;gemm;operator;sampling;triton |
| 症状 | build_error;crash;nan_inf |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: qwen2_5vl Internal Server Error when processing short video

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug - https://github.com/vllm-project/vllm/issues/19477 had mentioned this bug, and I have installed vllm==0.9.0. -with the newest function **load_bytes** of /vllm/multimodal/video.py ``` @classmethod def load_bytes(cls, data: bytes, num_frames: int = -1) -> npt.NDArray: import cv2 backend = cls().get_cv2_video_api() cap = cv2.VideoCapture(BytesIO(data), backend, []) if not cap.isOpened(): raise ValueError("Could not open video stream") total_frames_num = int(cap.get(cv2.CAP_PROP_FRAME_COUNT)) full_read = num_frames == -1 or total_frames_num modality: await asyncio.gather(*items) File "/usr/local/lib/python3.10/dist-packages/vllm/multimodal/utils.py", line 243, in fetch_video_async return await self.load_from_url_async( File "/usr/local/lib/python3.10/dist-packages/vllm/multimodal/utils.py", line 136, in load_from_url_async return self._load_file_url(url_spec, media_io) File "/usr/local/lib/python3.10/dist-packages/vllm/multimodal/utils.py", line 91, in _load_file_url return media_io.load_file(filepath) File "/usr/local/lib/python3.10/dist-packages/vllm/multimodal/video.py", line 177, in load_file return self.load_bytes(data) File "/...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 5: ub.com/vllm-project/vllm/issues/19477 had mentioned this bug, and I have installed vllm==0.9.0. -with the newest function **load_bytes** of /vllm/multimodal/video.py ``` @classmethod def load_bytes(cls, data: bytes, num...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: [Bug]: qwen2_5vl Internal Server Error when processing short video bug ### Your current environment ### 🐛 Describe the bug - https://github.com/vllm-project/vllm/issues/19477 had mentioned this bug, and I have installed...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: he newest function **load_bytes** of /vllm/multimodal/video.py ``` @classmethod def load_bytes(cls, data: bytes, num_frames: int = -1) -> npt.NDArray: import cv2 backend = cls().get_cv2_video_api() cap = cv2.VideoCaptur...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 2: bytes, num_frames: int = -1) -> npt.NDArray: import cv2 backend = cls().get_cv2_video_api() cap = cv2.VideoCapture(BytesIO(data), backend, []) if not cap.isOpened(): raise ValueError("Could not open video stream") total...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: 07-01 09:52:23 [protocol.py:57] The following fields were present in the request but ignored: {'do_sample'} INFO: 10.178.76.128:20037 - "POST /v1/chat/completions HTTP/1.1" 500 Internal Server Error WARNING 07-01 09:52:...

## Wiki 抽取状态

- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
