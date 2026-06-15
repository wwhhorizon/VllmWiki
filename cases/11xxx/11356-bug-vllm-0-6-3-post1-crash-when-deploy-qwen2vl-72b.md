# vllm-project/vllm#11356: [Bug]: vllm 0.6.3.post1 crash when deploy qwen2vl 72b 

| 字段 | 值 |
| --- | --- |
| Issue | [#11356](https://github.com/vllm-project/vllm/issues/11356) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 4; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: vllm 0.6.3.post1 crash when deploy qwen2vl 72b 

### Issue 正文摘录

### Your current environment ### Model Input Dumps _No response_ ### 🐛 Describe the bug ``` python -m vllm.entrypoints.openai.api_server --model "path_to_qwen2_vl_72b_instruct" \ --tensor-parallel-size 8 \ --max-model-len 32768 \ ``` ``` from openai import OpenAI from vllm.assets.image import ImageAsset import os import base64 openai_api_key = "EMPTY" openai_api_base = "http://localhost:8000/v1" client = OpenAI( api_key=openai_api_key, base_url=openai_api_base, ) models = client.models.list() model = models.data[0].id question="What is the text in the illustrate?" image_path = "path_to_image" with open(image_path, "rb") as file: image_base64 = base64.b64encode(file.read()).decode('utf-8') stream = True response = client.chat.completions.create( model=model, messages=[{ 'role': 'user', 'content': [{ 'type': 'text', 'text': question, }, { 'type': 'image_url', 'image_url': { 'url': f"data:image/jpeg;base64,{image_base64}",, }, }], }], temperature=0.1, top_p=0.001, stream = stream, ) if stream: for iter in response: print(iter.choices[0].delta.content, end = "", flush=True) print("") else: print(response.choices[0].message.content) ``` launch server success, but while send a request,...

## 候选优化模式

- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 2: ceive, sender) File "/usr/local/lib/python3.10/site-packages/starlette/routing.py", line 756, in __call__ await self.middleware_stack(scope, receive, send) File "/usr/local/lib/python3.10/site-packages/starlette/routing...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: --max-model-len 32768 \ ``` ``` from openai import OpenAI from vllm.assets.image import ImageAsset import os import base64 openai_api_key = "EMPTY" openai_api_base = "http://localhost:8000/v1" client = OpenAI( api_key=o...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: ss, but while send a request, vllm server crash, I have tried increasing CUDA_VISIBLE_DEVICES, export VLLM_RPC_TIMEOUT=10000000, but it don't work,the image size is 500*500 (VllmWorkerProcess pid=162247) WARNING 12-18 1...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 2: rint(iter.choices[0].delta.content, end = "", flush=True) print("") else: print(response.choices[0].message.content) ``` launch server success, but while send a request, vllm server crash, I have tried increasing CUDA_V...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: [Bug]: vllm 0.6.3.post1 crash when deploy qwen2vl 72b bug ### Your current environment ### Model Input Dumps _No response_ ### 🐛 Describe the bug ``` python -m vllm.entrypoints.openai.api_server --model "path_to_qwen2_v...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
