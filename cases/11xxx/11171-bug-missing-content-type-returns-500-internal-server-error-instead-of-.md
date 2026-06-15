# vllm-project/vllm#11171: [Bug]: Missing Content Type returns 500 Internal Server Error instead of 415 Unsupported Media Type

| 字段 | 值 |
| --- | --- |
| Issue | [#11171](https://github.com/vllm-project/vllm/issues/11171) |
| 状态 | closed |
| 标签 | bug;help wanted;good first issue |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | development |
| 工作域 | ci_build;distributed_parallel;frontend_api;hardware_porting;model_support |
| 子分类 | install |
| Operator 关键词 | cuda;triton |
| 症状 | crash |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Missing Content Type returns 500 Internal Server Error instead of 415 Unsupported Media Type

### Issue 正文摘录

### Your current environment ### Model Input Dumps _No response_ ### 🐛 Describe the bug This is essentially a "remainder" from [this issue](https://github.com/vllm-project/vllm/issues/4041). Pydantic validates the protocol, but you guys forgot to check whether the data you pass through pydantic is actually a JSON document, so it just crashes in a random place. ```bash #!/bin/env bash source .env curl -v 127.0.0.1:8000/v1/chat/completions \ -H "Authorization: Bearer $VLLM_API_KEY" \ -d '{ "model": "AIDC-AI/Marco-o1", "messages": [ { "role": "user", "content": "why is the sky blue?" } ], "stream": false }' echo ``` ``` ./vllm-crash.sh * Trying 127.0.0.1:8000... * Connected to 127.0.0.1 (127.0.0.1) port 8000 > POST /v1/chat/completions HTTP/1.1 > Host: 127.0.0.1:8000 > User-Agent: curl/8.5.0 > Accept: */* > Authorization: Bearer --- > Content-Length: 147 > Content-Type: application/x-www-form-urlencoded > < HTTP/1.1 500 Internal Server Error < date: Fri, 13 Dec 2024 11:20:00 GMT < server: uvicorn < content-length: 21 < content-type: text/plain; charset=utf-8 < * Connection #0 to host 127.0.0.1 left intact Internal Server Error ``` Note that the error message itself is completely mean...

## 候选优化模式

- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 4: ^^^^^^^^^^^^^ | File "/usr/local/lib/python3.12/dist-packages/anyio/_backends/_asyncio.py", line 763, in __aexit__ | raise BaseExceptionGroup( | ExceptionGroup: unhandled errors in a TaskGroup (1 sub-exception) +-+-----...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: | File "/usr/local/lib/python3.12/dist-packages/anyio/_backends/_asyncio.py", line 763, in __aexit__ | raise BaseExceptionGroup( | ExceptionGroup: unhandled errors in a TaskGroup (1 sub-exception) +-+---------------- 1...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: ``` ### Before submitting a new issue... - [X] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 1: "user", "content": "why is the sky blue?" } ], "stream": false }' echo ``` ``` ./vllm-crash.sh * Trying 127.0.0.1:8000... * Connected to 127.0.0.1 (127.0.0.1) port 8000 > POST /v1/chat/completions HTTP/1.1 > Host: 127.0...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: pe bug;help wanted;good first issue ### Your current environment ### Model Input Dumps _No response_ ### 🐛 Describe the bug This is essentially a "remainder" from [this issue](https://github.com/vllm-project/vllm/issues...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
