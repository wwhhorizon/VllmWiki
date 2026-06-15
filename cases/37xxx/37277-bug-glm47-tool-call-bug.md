# vllm-project/vllm#37277: [Bug]: GLM47 Tool Call Bug

| 字段 | 值 |
| --- | --- |
| Issue | [#37277](https://github.com/vllm-project/vllm/issues/37277) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: GLM47 Tool Call Bug

### Issue 正文摘录

### Your current environment Env：vllm 0.17.1 GLM4.7 FP8， openai api 8*h20 python3 -m vllm.entrypoints.openai.api_server \ --host "0.0.0.0" \ --port "8000" \ --model /models/GLM-4.7-FP8/ \ --served-model-name local-glm4-7 \ --tensor-parallel-size "8" \ --enable-chunked-prefill \ --enable-expert-parallel \ --max_num_batched_tokens "4096" \ --gpu-memory-utilization "0.9" \ --enable-prefix-caching \ --enable-auto-tool-choice \ --tool-call-parser glm47 \ --reasoning-parser glm45 \ --speculative-config.num_speculative_tokens "1" \ --speculative-config.method mtp \ --enable-prompt-tokens-details \ --uvicorn-log-level info ### 🐛 Describe the bug Using tool call Might fail ``` `#!/usr/bin/env python3 # -*- coding: utf-8 -*- """ Simple tool to test LLM structured output support. """ import os from typing import List, Optional from pydantic import BaseModel, Field from langchain_openai import ChatOpenAI import time # --- 1. Define the structured output schema --- class TestProfile(BaseModel): """Schema for the extracted user profile.""" name: str = Field(description="Full name of the user") age: int = Field(description="Age of the user") email: Optional[str] = Field(default=None, description...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: nts.openai.api_server \ --host "0.0.0.0" \ --port "8000" \ --model /models/GLM-4.7-FP8/ \ --served-model-name local-glm4-7 \ --tensor-parallel-size "8" \ --enable-chunked-prefill \ --enable-expert-parallel \ --max_num_b...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: g: utf-8 -*- """ Simple tool to test LLM structured output support. """ import os from typing import List, Optional from pydantic import BaseModel, Field from langchain_openai import ChatOpenAI import time # --- 1. Defi...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: 28 years old. I enjoy hiking and photography.", "The user is Taylor Smith, age 35, contact at taylor.s@mail.com. Likes reading sci-fi and gaming.", "Chris Lee. 42. Interests include jazz music and woodworking.", ] # ---...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: ame local-glm4-7 \ --tensor-parallel-size "8" \ --enable-chunked-prefill \ --enable-expert-parallel \ --max_num_batched_tokens "4096" \ --gpu-memory-utilization "0.9" \ --enable-prefix-caching \ --enable-auto-tool-choic...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 2: l ``` `#!/usr/bin/env python3 # -*- coding: utf-8 -*- """ Simple tool to test LLM structured output support. """ import os from typing import List, Optional from pydantic import BaseModel, Field from langchain_openai im...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
