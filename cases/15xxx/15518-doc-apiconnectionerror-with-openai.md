# vllm-project/vllm#15518: [Doc]: APIConnectionError with OpenAI

| 字段 | 值 |
| --- | --- |
| Issue | [#15518](https://github.com/vllm-project/vllm/issues/15518) |
| 状态 | closed |
| 标签 | documentation |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | development |
| 工作域 | ci_build;frontend_api;model_support;sampling_logits |
| 子分类 | debug |
| Operator 关键词 | cuda;sampling |
| 症状 | crash |
| 根因提示 | env_dependency |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Doc]: APIConnectionError with OpenAI

### Issue 正文摘录

### 📚 The doc issue Hello, While going through the documentation's QuickStart section (https://docs.vllm.ai/en/latest/getting_started/quickstart.html#openai-compatible-server), I haven't been able to resolve the `APIConnectionError: Connection error.` with the OpenAI API. The very same code in the documentation, except the `openai_api_key` where I input my API key: ``` import os os.environ['HF_HOME'] = '~/scratch/LLM/cache/' import torch torch.cuda.empty_cache() from openai import OpenAI # Modify OpenAI's API key and API base to use vLLM's API server. openai_api_key = "my own API key I got from OpenAI" openai_api_base = "http://localhost:8000/v1" client = OpenAI( api_key=openai_api_key, base_url=openai_api_base, ) completion = client.completions.create(model="Qwen/Qwen2.5-1.5B-Instruct", prompt="San Francisco is a") print("Completion result:", completion) ``` The error: ``` --------------------------------------------------------------------------- ConnectError Traceback (most recent call last) File ~/.conda/envs/vllm/lib/python3.12/site-packages/httpx/_transports/default.py:101, in map_httpcore_exceptions() 100 try: --> 101 yield 102 except Exception as exc: File ~/.conda/envs/vl...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: documentation, except the `openai_api_key` where I input my API key: ``` import os os.environ['HF_HOME'] = '~/scratch/LLM/cache/' import torch torch.cuda.empty_cache() from openai import OpenAI # Modify OpenAI's API key...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 3: port, timeout, local_address, socket_options) 202 exc_map: ExceptionMapping = { 203 socket.timeout: ConnectTimeout, 204 OSError: ConnectError, 205 } --> 207 with map_exceptions(exc_map): 208 sock = socket.create_connect...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: the `openai_api_key` where I input my API key: ``` import os os.environ['HF_HOME'] = '~/scratch/LLM/cache/' import torch torch.cuda.empty_cache() from openai import OpenAI # Modify OpenAI's API key and API base to use v...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: ort os os.environ['HF_HOME'] = '~/scratch/LLM/cache/' import torch torch.cuda.empty_cache() from openai import OpenAI # Modify OpenAI's API key and API base to use vLLM's API server. openai_api_key = "my own API key I g...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: ", logger, request, kwargs) as trace: --> 124 stream = self._network_backend.connect_tcp(**kwargs) 125 trace.return_value = stream File ~/.conda/envs/vllm/lib/python3.12/site-packages/httpcore/_backends/sync.py:207, in...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
