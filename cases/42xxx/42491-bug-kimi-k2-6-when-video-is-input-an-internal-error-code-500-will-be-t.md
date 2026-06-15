# vllm-project/vllm#42491: [Bug]: [Kimi K2.6] When video is input, an internal error code 500 will be triggered.

| 字段 | 值 |
| --- | --- |
| Issue | [#42491](https://github.com/vllm-project/vllm/issues/42491) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;frontend_api;gemm_linear;hardware_porting;model_support;sampling_logits |
| 子分类 | precision |
| Operator 关键词 | cuda;operator;sampling;triton |
| 症状 | build_error;crash;nan_inf |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: [Kimi K2.6] When video is input, an internal error code 500 will be triggered.

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug When I input the video according to the [example](https://huggingface.co/moonshotai/Kimi-K2.6) provided by Hugging Face, an error occurred. vllm is 0.20.0 ```python import base64 import requests import json from util import model, token, base_url url = "534ec86553a149b4af03b92075bd50a2.mp4" video_base64 = base64.b64encode(requests.get(url).content).decode() messages = [ { "role": "user", "content": [ {"type": "text", "text": "Describe the video in detail."}, { "type": "video_url", "video_url": {"url": f"data:video/mp4;base64,{video_base64}"}, }, ], } ] headers = { "Content-Type": "application/json", "token": token, "path": "/v1/chat/completions", } data = { "top_p": 0.5, "max_tokens": 100, "top_k": 5, "temperature": 0.0, "chat_template_kwargs": {"thinking": False}, "messages": messages, "model": model, "stream": False, } response = requests.post( base_url, data=json.dumps(data, ensure_ascii=False).encode("utf-8"), headers=headers, ) response.raise_for_status() print(json.loads(response.text)) # {'code': 'L00101', 'msg': '500 Internal Server Error: "{"error":{"message":"","type":"InternalServerError","param":null,"code":500}}"', '...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: 6) provided by Hugging Face, an error occurred. vllm is 0.20.0 ```python import base64 import requests import json from util import model, token, base_url url = "534ec86553a149b4af03b92075bd50a2.mp4" video_base64 = base...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: cribe the bug When I input the video according to the [example](https://huggingface.co/moonshotai/Kimi-K2.6) provided by Hugging Face, an error occurred. vllm is 0.20.0 ```python import base64 import requests import jso...
- [MoE、GEMM 与 Expert Routing](../patterns/moe_gemm_routing.md) - 分数 3: erver pid=138) File "/usr/local/lib/python3.10/dist-packages/starlette/routing.py", line 716, in __call__ (APIServer pid=138) await self.middleware_stack(scope, receive, send) (APIServer pid=138) File "/usr/local/lib/py...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 2: erver pid=138) File "/usr/local/lib/python3.10/dist-packages/starlette/routing.py", line 716, in __call__ (APIServer pid=138) await self.middleware_stack(scope, receive, send) (APIServer pid=138) File "/usr/local/lib/py...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: ``` ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
