# vllm-project/vllm#22483: [Bug]: OSS-20B [backend_xgrammar.py:160] Failed to advance FSM

| 字段 | 值 |
| --- | --- |
| Issue | [#22483](https://github.com/vllm-project/vllm/issues/22483) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;sampling_logits;scheduler_memory;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cuda;operator;sampling;triton |
| 症状 | build_error;nan_inf |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: OSS-20B [backend_xgrammar.py:160] Failed to advance FSM

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug (EngineCore_0 pid=344054) ERROR 08-08 02:53:13 [backend_xgrammar.py:160] Failed to advance FSM for request resp_20217d9f89044056949fa9498cdd56a4 for tokens 410. Please file an issue. (EngineCore_0 pid=344054) ERROR 08-08 02:53:13 [backend_xgrammar.py:160] Failed to advance FSM for request resp_20217d9f89044056949fa9498cdd56a4 for tokens 745. Please file an issue. (EngineCore_0 pid=344054) ERROR 08-08 02:53:13 [backend_xgrammar.py:160] Failed to advance FSM for request resp_20217d9f89044056949fa9498cdd56a4 for tokens 256. Please file an issue. (EngineCore_0 pid=344054) ERROR 08-08 02:53:13 [backend_xgrammar.py:160] Failed to advance FSM for request resp_20217d9f89044056949fa9498cdd56a4 for tokens 77. Please file an issue. (EngineCore_0 pid=344054) ERROR 08-08 02:53:13 [backend_xgrammar.py:160] Failed to advance FSM for request resp_20217d9f89044056949fa9498cdd56a4 for tokens 134186. Please file an issue. (EngineCore_0 pid=344054) ERROR 08-08 02:53:13 [backend_xgrammar.py:160] Failed to advance FSM for request resp_20217d9f89044056949fa9498cdd56a4 for tokens 256. Please file an issue. (EngineCore_0 pid=344054) ERROR 08-08 02:53:14...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: .0.1:33680 - "POST /v1/responses HTTP/1.1" 200 OK ```python from openai import OpenAI from pydantic import BaseModel openai_api_key = "EMPTY" model_name = "openai/gpt-oss-20b" openai_api_base = "http://localhost:8000/v1...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: [Bug]: OSS-20B [backend_xgrammar.py:160] Failed to advance FSM bug ### Your current environment ### 🐛 Describe the bug (EngineCore_0 pid=344054) ERROR 08-08 02:53:13 [backend_xgrammar.py:160] Failed to advance FSM for r...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: .1" 200 OK ```python from openai import OpenAI from pydantic import BaseModel openai_api_key = "EMPTY" model_name = "openai/gpt-oss-20b" openai_api_base = "http://localhost:8000/v1" print(f"Connecting to model '{model_n...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 3: ERROR 08-08 02:53:13 [backend_xgrammar.py:160] Failed to advance FSM for request resp_20217d9f89044056949fa9498cdd56a4 for tokens 410. Please file an issue. (EngineCore_0 pid=344054) ERROR 08-08 02:53:13 [backend_xgramm...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 2: [Bug]: OSS-20B [backend_xgrammar.py:160] Failed to advance FSM bug ### Your current environment ### 🐛 Describe the bug (EngineCore_0 pid=344054) ERROR 08-08 02:53:13 [backend_xgrammar.py:160] Failed to advance FSM for r...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
