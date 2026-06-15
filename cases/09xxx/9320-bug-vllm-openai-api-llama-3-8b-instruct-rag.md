# vllm-project/vllm#9320: [Bug]: 当vLLM 部署实现 OpenAI API，并且生成模型使用llama 3 8b instruct做RAG任务时，模型生成不停

| 字段 | 值 |
| --- | --- |
| Issue | [#9320](https://github.com/vllm-project/vllm/issues/9320) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 4; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;multimodal_vlm;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cuda;sampling;triton |
| 症状 | build_error;mismatch;nan_inf |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: 当vLLM 部署实现 OpenAI API，并且生成模型使用llama 3 8b instruct做RAG任务时，模型生成不停

### Issue 正文摘录

### Your current environment ### Model Input Dumps _No response_ ### 🐛 Describe the bug 我在本地使用vllm将llama3 8b instruct模型以openai api的形式搭载到GPU上，并执行如下代码： ``` import time import asyncio import openai from openai import OpenAI from typing import List, Dict def inference(#async api_key: str, api_base: str, client: OpenAI, model_path: str, messages, model_name: str = "davinci", message_index: int = 0, ): time_start = time.time() chat_outputs = client.chat.completions.create( model=model_path, messages=messages, ) time_end = time.time() print(f"Total time: {time_end - time_start:.2f}s") return { "model": model_name, "message_index": message_index, "response": chat_outputs.choices[0].message.content } def main():#async api_key = "YOUR_API_KEY" api_base1 = "http://localhost:114514/v1" api_base2 = "http://localhost:1919810/v1" client1 = OpenAI(api_key=api_key, base_url=api_base1) client2 = OpenAI(api_key=api_key, base_url=api_base2) model_path1 = "/data00/LLaMA-3-8b-Instruct/" model_path2 = "/data00/yifei_chen/multi_llms_for_CoT/models/Qwen/Qwen2___5-7B-Instruct" time_start = time.time() content = ( "Act as a critic. Given a question, referenced documents, and some hallucination problems and...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 6: [Bug]: 当vLLM 部署实现 OpenAI API，并且生成模型使用llama 3 8b instruct做RAG任务时，模型生成不停 bug;stale ### Your current environment ### Model Input Dumps _No response_ ### 🐛 Describe the bug 我在本地使用vllm将llama3 8b instruct模型以openai api的形式搭载到GP...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 5: e bug 我在本地使用vllm将llama3 8b instruct模型以openai api的形式搭载到GPU上，并执行如下代码： ``` import time import asyncio import openai from openai import OpenAI from typing import List, Dict def inference(#async api_key: str, api_base: str,...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 4: s in causality or conditional logic, that is, errors in logical relationships, " "such as incorrect causal links, overgeneralizations, or misinterpreted conditions. " "It also includes that a specific detail in the refe...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: ug]: 当vLLM 部署实现 OpenAI API，并且生成模型使用llama 3 8b instruct做RAG任务时，模型生成不停 bug;stale ### Your current environment ### Model Input Dumps _No response_ ### 🐛 Describe the bug 我在本地使用vllm将llama3 8b instruct模型以openai api的形式搭载到GPU上...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: upport;multimodal_vlm;sampling_logits;speculative_decoding cuda;sampling;triton build_error;mismatch;nan_inf env_dependency Your current environment

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
