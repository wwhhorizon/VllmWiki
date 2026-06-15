# vllm-project/vllm#24737: [Bug]: Qwen3 Reranker 500 error when submitting longer query

| 字段 | 值 |
| --- | --- |
| Issue | [#24737](https://github.com/vllm-project/vllm/issues/24737) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 6; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: Qwen3 Reranker 500 error when submitting longer query

### Issue 正文摘录

[logs (1).txt](https://github.com/user-attachments/files/22295419/logs.1.txt) ### Your current environment ```bash --host 0.0.0.0 --port 8000 --model tomaarsen/Qwen3-Reranker-8B-seq-cls --max-model-len 8128 ``` ### 🐛 Describe the bug ````python import asyncio import json import os from typing import Any, Optional import aiohttp from pydantic import BaseModel def format_queries( query: str, instruction: Optional[str] = None, ) -> str: """Format query using the specified Qwen3 template.""" prefix = ( ' system\nJudge whether the Document meets the requirements based on the Query and the ' 'Instruct provided. Note that the answer can only be "yes" or "no". \n user\n' ) if instruction is None: # Build enhanced instruction with context instruction_parts = ["Given a purchase description, evaluate how well each spend category matches the item."] instruction_parts.append("Consider procurement categorization.") instruction = " ".join(instruction_parts) # Follow the exact template structure: query_template = "{prefix} : {instruction}\n : {query}\n" query_template = "{prefix} : {instruction}\n : {query}\n" return query_template.format(prefix=prefix, instruction=instruction, query=query) def f...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: -seq-cls --max-model-len 8128 ``` ### 🐛 Describe the bug ````python import asyncio import json import os from typing import Any, Optional import aiohttp from pydantic import BaseModel def format_queries( query: str, ins...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: [Bug]: Qwen3 Reranker 500 error when submitting longer query bug;stale [logs (1).txt](https://github.com/user-attachments/files/22295419/logs.1.txt) ### Your current environment ```bash --host 0.0.0.0 --port 8000 --mode...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: [Bug]: Qwen3 Reranker 500 error when submitting longer query bug;stale [logs (1).txt](https://github.com/user-attachments/files/22295419/logs.1.txt) ### Your current environment ```bash --host 0.0.0.0 --port 8000 --mode...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 2: with context instruction_parts = ["Given a purchase description, evaluate how well each spend category matches the item."] instruction_parts.append("Consider procurement categorization.") instruction = " ".join(instruct...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: marker) if start_idx == -1: return formatted_text # Fallback to full text start_idx += len(start_marker) end_idx = formatted_text.find(end_marker, start_idx) if end_idx == -1: return formatted_text[start_idx:] # Fallb

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
