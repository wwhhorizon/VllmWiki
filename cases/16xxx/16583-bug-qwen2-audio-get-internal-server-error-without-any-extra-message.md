# vllm-project/vllm#16583: [Bug]: Qwen2-Audio get Internal Server Error without any extra message

| 字段 | 值 |
| --- | --- |
| Issue | [#16583](https://github.com/vllm-project/vllm/issues/16583) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cuda;operator;sampling;triton |
| 症状 | build_error;nan_inf |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Qwen2-Audio get Internal Server Error without any extra message

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug Bug Reproduction Steps - vllm serve /data/modelscope/Qwen2-Audio-7B-Instruct - client python code like this: ```python from openai import OpenAI audio_url = "https://vllm-public-assets.s3.us-west-2.amazonaws.com/multimodal_asset/winning_call.ogg" client = OpenAI( api_key="xxx", base_url="http://192.168.0.3:8000/v1", ) rsp = client.chat.completions.create( messages=[ { "role": "user", "content": [ { "type": "text", "text": "What's in this audio?", }, { "type": "audio_url", "audio_url": { # Any format supported by librosa is supported "url": audio_url, }, }, ], }, ], model="/data/modelscope/Qwen2-Audio-7B-Instruct", ) print(rsp) ``` - client error message: openai.InternalServerError: Error code: 500 - service error message: ``` INFO: 192.168.0.3:44784 - "POST /v1/chat/completions HTTP/1.1" 500 Internal Server Error INFO 04-14 17:12:57 [logger.py:39] Received request chatcmpl-3d16551626b74af0925e9f32603f2249: prompt: " system\nYou are a helpful assistant. \n user\nWhat's in this audio? \n assistant\n", params: SamplingParams(n=1, presence_penalty=0.0, frequency_penalty=0.0, repetition_penalty=1.1, temperature=0.7, top_p=0.5, top_k=2...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: Audio-7B-Instruct - client python code like this: ```python from openai import OpenAI audio_url = "https://vllm-public-assets.s3.us-west-2.amazonaws.com/multimodal_asset/winning_call.ogg" client = OpenAI( api_key="xxx",...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: [Bug]: Qwen2-Audio get Internal Server Error without any extra message bug ### Your current environment ### 🐛 Describe the bug Bug Reproduction Steps - vllm serve /data/modelscope/Qwen2-Audio-7B-Instruct - client python...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: ``` ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: 1" 500 Internal Server Error INFO 04-14 17:12:57 [logger.py:39] Received request chatcmpl-3d16551626b74af0925e9f32603f2249: prompt: " system\nYou are a helpful assistant. \n user\nWhat's in this audio? \n assistant\n",...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: odel_support;sampling_logits;speculative_decoding cuda;operator;sampling;triton build_error;nan_inf env_dependency Your current environment

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
