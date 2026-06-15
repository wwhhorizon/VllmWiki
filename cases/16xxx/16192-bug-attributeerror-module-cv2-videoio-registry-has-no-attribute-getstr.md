# vllm-project/vllm#16192: [Bug]: AttributeError: module 'cv2.videoio_registry' has no attribute 'getStreamBufferedBackends'

| 字段 | 值 |
| --- | --- |
| Issue | [#16192](https://github.com/vllm-project/vllm/issues/16192) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;multimodal_vlm;quantization;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cuda;operator;quantization;sampling;triton |
| 症状 | build_error;crash;nan_inf |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: AttributeError: module 'cv2.videoio_registry' has no attribute 'getStreamBufferedBackends'

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug ``` shell vllm serve Qwen/Qwen2.5-VL-7B-Instruct ``` ```python from openai import OpenAI import base64 def video_to_data_url(video_path): with open(video_path, "rb") as video_file: base64_video = base64.b64encode(video_file.read()).decode('utf-8') return f"data:video/mp4;base64,{base64_video}" video_path = '/root/vllm/space_woaudio.mp4' video_data_url = video_to_data_url(video_path) # video_data_url = "https://qianwen-res.oss-cn-beijing.aliyuncs.com/Qwen2-VL/space_woaudio.mp4" openai_api_key = "None" openai_api_base = "http://localhost:8000/v1" client = OpenAI( api_key=openai_api_key, base_url=openai_api_base, ) chat_response = client.chat.completions.create( model="Qwen/Qwen2.5-VL-7B-Instruct", messages=[ { "role": "system", "content": "You are a helpful assistant." }, { "role": "user", "content": [ { "type": "video_url", "video_url": { "url": video_data_url }, }, { "type": "text", "text": "Please describe the specific process of this video." }, ] }, ]) print("Chat response:", chat_response) ``` ``` python File "/root/vllm/vllm/entrypoints/openai/serving_chat.py", line 181, in create_chat_completion ) = await self._preprocess_ch...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 5: ` shell vllm serve Qwen/Qwen2.5-VL-7B-Instruct ``` ```python from openai import OpenAI import base64 def video_to_data_url(video_path): with open(video_path, "rb") as video_file: base64_video = base64.b64encode(video_fi...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: Your current environment ### 🐛 Describe the bug ``` shell vllm serve Qwen/Qwen2.5-VL-7B-Instruct ``` ```python from openai import OpenAI import base64 def video_to_data_url(video_path): with open(video_path, "rb") as vi...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 2: eError: module 'cv2.videoio_registry' has no attribute 'getStreamBufferedBackends' bug ### Your current environment ### 🐛 Describe the bug ``` shell vllm serve Qwen/Qwen2.5-VL-7B-Instruct ``` ```python from openai impor...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: ``` ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: s video_file: base64_video = base64.b64encode(video_file.read()).decode('utf-8') return f"data:video/mp4;base64,{base64_video}" video_path = '/root/vllm/space_woaudio.mp4' video_data_url = video_to_data_url(video_path)...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
