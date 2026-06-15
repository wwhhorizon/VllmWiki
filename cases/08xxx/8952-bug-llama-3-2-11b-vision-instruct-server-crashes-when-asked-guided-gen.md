# vllm-project/vllm#8952: [Bug]: Llama-3.2-11B-Vision-Instruct server crashes when asked guided generation

| 字段 | 值 |
| --- | --- |
| Issue | [#8952](https://github.com/vllm-project/vllm/issues/8952) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 8; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cuda;operator;sampling;triton |
| 症状 | build_error;crash;nan_inf |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Llama-3.2-11B-Vision-Instruct server crashes when asked guided generation

### Issue 正文摘录

### Your current environment ### Model Input Dumps _No response_ ### 🐛 Describe the bug I am serving Llama-3.2-11B-Vision-Instruct on my 1 A100/80G GPU with the following instruction. ```bash nohup vllm serve meta-llama/Llama-3.2-11B-Vision-Instruct --port 8000 --api-key qwen 2-4e1fbc5e56f7fbE1 --gpu-memory-utilization 0.9 --download_dir /workspace/vllm_models/ --cpu-offload-gb 5000 --swap-space 50 --max-model-le n 4096 --max_num_seqs=32 --enforce_eager > llama_vision-output_240930.log 2>&1 & ``` The server crashes whenever I add response_format or guided_json parameter in my client.chat.completions.create() method. # D0 Inference # If structured output is not used, it crashes when trying to use 40 seconds ```python import asyncio import nest_asyncio from openai import AsyncOpenAI # Allow nested event loops nest_asyncio.apply() async def run_batch_requests(img_urls, image_info_prompt): client = AsyncOpenAI( base_url=llama_v_url, api_key=llama_v_api_key, ) model = llama_v_model async def single_request(img_url, image_info_prompt): messages = [ # {"role": "system", "content": d0_system_prompt}, {"role": "user", "content": [{"type": "text", "text": image_info_prompt}, # Error: Prompt...

## 现有链接修复摘要

#9631 [Bugfix] Fix crash with llama 3.2 vision models and guided decoding

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: output is not used, it crashes when trying to use 40 seconds ```python import asyncio import nest_asyncio from openai import AsyncOpenAI # Allow nested event loops nest_asyncio.apply() async def run_batch_requests(img_u...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: [Bug]: Llama-3.2-11B-Vision-Instruct server crashes when asked guided generation bug ### Your current environment ### Model Input Dumps _No response_ ### 🐛 Describe the bug I am serving Llama-3.2-11B-Vision-Instruct on m
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: # 🐛 Describe the bug I am serving Llama-3.2-11B-Vision-Instruct on my 1 A100/80G GPU with the following instruction. ```bash nohup vllm serve meta-llama/Llama-3.2-11B-Vision-Instruct --port 8000 --api-key qwen 2-4e1fbc5...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: AI # Allow nested event loops nest_asyncio.apply() async def run_batch_requests(img_urls, image_info_prompt): client = AsyncOpenAI( base_url=llama_v_url, api_key=llama_v_api_key, ) model = llama_v_model async def single...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: odel_support;sampling_logits;speculative_decoding cuda;operator;sampling;triton build_error;crash;nan_inf env_dependency #9631 [Bugfix] Fix crash with llama 3.2 vision models and guided decoding Your current environment

## 关联 PR 证据

| PR | 链接类型 | 置信度 | PR 标题 | 证据 |
| --- | --- | ---: | --- | --- |
| [#9631](https://github.com/vllm-project/vllm/pull/9631) | closes_keyword | 0.95 | [Bugfix] Fix crash with llama 3.2 vision models and guided decoding | FIX #8952 **BEFORE SUBMITTING, PLEASE READ THE CHECKLIST BELOW AND FILL IN THE DESCRIPTION ABOVE** --- <details> <!-- inside this <details> section, markdown rendering do |

## Wiki 抽取状态

- 后续迭代应在可用时读取完整讨论评论。
