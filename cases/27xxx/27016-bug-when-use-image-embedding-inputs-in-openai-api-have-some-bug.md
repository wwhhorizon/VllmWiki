# vllm-project/vllm#27016: [Bug]: when use “Image Embedding Inputs” in openai api，have some bug

| 字段 | 值 |
| --- | --- |
| Issue | [#27016](https://github.com/vllm-project/vllm/issues/27016) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 13; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: when use “Image Embedding Inputs” in openai api，have some bug

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug 1. vllm serve /qwen2.5 2. mycode import base64 import requests from openai import OpenAI import torch import io openai_api_key = 'EMPTY' openai_api_base = "http://localhost:8000/v1" client = OpenAI( # defaults to os.environ.get("OPENAI_API_KEY") api_key=openai_api_key, base_url=openai_api_base, ) models = client.models.list() model = models.data[0].id em_path = "/workspace/mediak8s-audio-qwen2/mm_embeds.pt" gt_path = "/workspace/mediak8s-audio-qwen2/grid_thw.pt" # Audio input inference def run_vl(img_url: str) -> None: # base64 URL image_embedding = torch.load(em_path) grid_thw = torch.load(gt_path) buffer_e = io.BytesIO() torch.save(image_embedding, buffer_e) buffer_e.seek(0) binary_data_e = buffer_e.read() base64_image_embedding = base64.b64encode(binary_data_e).decode('utf-8') buffer_g = io.BytesIO() torch.save(grid_thw, buffer_g) buffer_g.seek(0) binary_data_g = buffer_g.read() base64_image_grid_thw = base64.b64encode(binary_data_g).decode('utf-8') embeds = { "type": "image_embeds", "image_embeds": { "image_embeds": f"{base64_image_embedding}" , # Required "image_grid_thw": f"{base64_image_grid_thw}" # Required by Qwen/Qwen2-...

## 候选优化模式

- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 3: [Bug]: when use “Image Embedding Inputs” in openai api，have some bug bug;stale ### Your current environment ### 🐛 Describe the bug 1. vllm serve /qwen2.5 2. mycode import base64 import requests from openai import OpenAI...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: ### Your current environment ### 🐛 Describe the bug 1. vllm serve /qwen2.5 2. mycode import base64 import requests from openai import OpenAI import torch import io openai_api_key = 'EMPTY' openai_api_base = "http://loca...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: environment ### 🐛 Describe the bug 1. vllm serve /qwen2.5 2. mycode import base64 import requests from openai import OpenAI import torch import io openai_api_key = 'EMPTY' openai_api_base = "http://localhost:8000/v1" cl...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: 500 ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 1: f._make_status_error_from_response(err.response) from None openai.InternalServerError: Error code: 500 ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
