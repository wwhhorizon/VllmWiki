# vllm-project/vllm#12005: [Bug]: Very slow guided decoding with Outlines backend since v0.6.5

| 字段 | 值 |
| --- | --- |
| Issue | [#12005](https://github.com/vllm-project/vllm/issues/12005) |
| 状态 | closed |
| 标签 | bug;structured-output;stale |
| 评论 | 9; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | attention_kv_cache;ci_build;distributed_parallel;frontend_api;model_support;sampling_logits |
| 子分类 | memory |
| Operator 关键词 | cuda;triton |
| 症状 | slowdown |
| 根因提示 | env_dependency |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Very slow guided decoding with Outlines backend since v0.6.5

### Issue 正文摘录

### Your current environment ### Model Input Dumps N/A ### 🐛 Describe the bug ```python from vllm import LLM, SamplingParams from vllm.sampling_params import GuidedDecodingParams from pydantic import BaseModel from transformers import AutoTokenizer class Person(BaseModel): name: str description: str prompt = """ [INST] > You are a json text extractor. return the following json {"name": "the game name", "description": "description of the game in around 400 words"} > { CD Projekt Red is ramping up production on The Witcher 4, and of course it's looking into using AI } [/INST]""" llm = LLM(model="meta-llama/Llama-3.1-8B-Instruct") result = llm.generate( prompts=[prompt] * 2000, sampling_params=SamplingParams( temperature=0.6, max_tokens=1024, guided_decoding=GuidedDecodingParams(json=Person.model_json_schema(), backend="outlines"), ), ) print(result) ``` Running the above with vLLM 0.6.4, there are massive differences in both time and (CPU) memory consumption. With the older versions it consumes ~4GB RAM and the newer ones it consumes >50GB RAM, and also takes orders of magnitude longer to even start generating. Related to this Outlines issue: https://github.com/dottxt-ai/outlines/is...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 5: ### Model Input Dumps N/A ### 🐛 Describe the bug ```python from vllm import LLM, SamplingParams from vllm.sampling_params import GuidedDecodingParams from pydantic import BaseModel from transformers import AutoTokenizer...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 2: [Bug]: Very slow guided decoding with Outlines backend since v0.6.5 bug;structured-output;stale ### Your current environment ### Model Input Dumps N/A ### 🐛 Describe the bug ```python from vllm import LLM, SamplingParam...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: 51. ### Before submitting a new issue... - [X] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: 5 bug;structured-output;stale ### Your current environment ### Model Input Dumps N/A ### 🐛 Describe the bug ```python from vllm import LLM, SamplingParams from vllm.sampling_params import GuidedDecodingParams from pydan...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: guided decoding with Outlines backend since v0.6.5 bug;structured-output;stale ### Your current environment ### Model Input Dumps N/A ### 🐛 Describe the bug ```python from vllm import LLM, SamplingParams from vllm.sampl...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
