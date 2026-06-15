# vllm-project/vllm#21022: [Bug]: 0.9.1(V1) Hanging(RayChannelTimeoutError ) when inferencing guided_json in DeepSeek-R1/V3 (TP=8, PP=2)

| 字段 | 值 |
| --- | --- |
| Issue | [#21022](https://github.com/vllm-project/vllm/issues/21022) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | development |
| 工作域 | ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;quantization;sampling_logits |
| 子分类 | env_compat |
| Operator 关键词 | cuda;operator;quantization;sampling;triton |
| 症状 | build_error |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: 0.9.1(V1) Hanging(RayChannelTimeoutError ) when inferencing guided_json in DeepSeek-R1/V3 (TP=8, PP=2)

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug Because the service was found to be hanging when testing guided_json, the following script with a concurrency of 50 was used to test and reproduce the problem. ```python import aiohttp import asyncio import json import uuid import time import statistics from datetime import datetime from pydantic import BaseModel time_format = "%Y-%m-%d %H:%M:%S,%f" recordId = str(uuid.uuid4()) class Topic(BaseModel): 问题: str 答案: str async def async_post(session, url, model, is_stream): payload = { "max_tokens": 1024, "min_tokens": 0, "messages": [ {"role": "user", "content": "请你生成一对和python相关的问题和答案"} ], "guided_json": Topic.model_json_schema(), #"guided_json":{"properties":{"apiList":{"items":{"title":"api_name","type":"string"},"type":"array"},"resultList":{"items":{"api_name":{"title":"api_name","type":"string"},"queryList":{"items":{"title":"query","type":"string"},"type":"array"}},"type":"array"}}}, "model": model, "stream": is_stream, "skip_special_tokens": False, "include_stop_str_in_output": False, "ignore_eos": False, "seed": 46, #"temperature": 0.2, #"top_p": 1.0, "top_k": 1 } headers = { "Content-Type": "application/json" } st = time.ti...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: [Bug]: 0.9.1(V1) Hanging(RayChannelTimeoutError ) when inferencing guided_json in DeepSeek-R1/V3 (TP=8, PP=2) bug ### Your current environment ### 🐛 Describe the bug Because the service was found to be hanging when test...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: import statistics from datetime import datetime from pydantic import BaseModel time_format = "%Y-%m-%d %H:%M:%S,%f" recordId = str(uuid.uuid4()) class Topic(BaseModel): 问题: str 答案: str async def async_post(session, url,...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: ``` ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: time_format)} 首字耗时: {(fir - st)*1000:.6} ms") print(text.decode('utf-8')) else: print(text.decode('utf-8')) total_time = (time.time() - t1) * 1000 i += 1 t1 = time.time() end = time.time()
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: support;quantization;sampling_logits cuda;operator;quantization;sampling;triton build_error env_dependency Your current environment

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
