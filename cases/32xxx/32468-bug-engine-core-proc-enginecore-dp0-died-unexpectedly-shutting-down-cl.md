# vllm-project/vllm#32468: [Bug]: Engine core proc EngineCore_DP0 died unexpectedly, shutting down client.

| 字段 | 值 |
| --- | --- |
| Issue | [#32468](https://github.com/vllm-project/vllm/issues/32468) |
| 状态 | open |
| 标签 | bug;stale |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: Engine core proc EngineCore_DP0 died unexpectedly, shutting down client.

### Issue 正文摘录

### 🐛 Describe the bug - in case of vllm engine usage, in the end of script, some error info occur `ERROR 01-16 17:16:49 [core_client.py:605] Engine core proc EngineCore_DP0 died unexpectedly, shutting down client.` ``` # Requires vllm>=0.14.0 from io import BytesIO import requests import torch from PIL import Image from vllm import LLM def get_image_from_url(url) -> Image.Image: response = requests.get(url) img = Image.open(BytesIO(response.content)).convert("RGB") return img model = LLM(model="models/Qwen/Qwen3-VL-Embedding-2B", runner="pooling") image = get_image_from_url("https://qianwen-res.oss-cn-beijing.aliyuncs.com/Qwen-VL/assets/demo.jpeg") image_placeholder = " " inputs = [ { "prompt": "A woman playing with her dog on a beach at sunset.", }, { "prompt": "A woman shares a joyful moment with her golden retriever on a sun-drenched beach at sunset, as the dog offers its paw in a heartwarming display of companionship and trust." }, { "prompt": image_placeholder, "multi_modal_data": {"image": image}, }, { "prompt": f"{image_placeholder}\nA woman shares a joyful moment with her golden retriever on a sun-drenched beach at sunset, as the dog offers its paw in a heartwarming displ...

## 候选优化模式

- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: sunset, as the dog offers its paw in a heartwarming display of companionship and trust." }, { "prompt": image_placeholder, "multi_modal_data": {"image": image}, }, { "prompt": f"{image_placeholder}\nA woman shares a joy...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: g = Image.open(BytesIO(response.content)).convert("RGB") return img model = LLM(model="models/Qwen/Qwen3-VL-Embedding-2B", runner="pooling") image = get_image_from_url("https://qianwen-res.oss-cn-beijing.aliyuncs.com/Qw...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: ne core proc EngineCore_DP0 died unexpectedly, shutting down client. bug;stale ### 🐛 Describe the bug - in case of vllm engine usage, in the end of script, some error info occur `ERROR 01-16 17:16:49 [core_client.py:605...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: on 0.24.1 transformers 4.57.5 triton 3.5.1 vllm 0.14.0rc2.dev98+g03da3b52e ``` ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chat
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: nexpectedly, shutting down client.` ``` # Requires vllm>=0.14.0 from io import BytesIO import requests import torch from PIL import Image from vllm import LLM def get_image_from_url(url) -> Image.Image: response = reque...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
