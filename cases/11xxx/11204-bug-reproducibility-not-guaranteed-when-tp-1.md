# vllm-project/vllm#11204: [Bug]: Reproducibility not guaranteed when tp > 1

| 字段 | 值 |
| --- | --- |
| Issue | [#11204](https://github.com/vllm-project/vllm/issues/11204) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 0; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;quantization;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cuda;fp8;kernel;operator;quantization;sampling;triton |
| 症状 | build_error;nan_inf |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Reproducibility not guaranteed when tp > 1

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug I expect to get the exact numbers back when using a fixed seed. When using TP=2. It works when using TP=1 | Model (tp=2) | --enforce-eager | (NO) --enforce-eager | |--------------------------------------------------------|-----------------|----------------------| | hugging-quants/Meta-Llama-3.1-70B-Instruct-AWQ-INT4 | ❌ | ❌ | | neuralmagic/Meta-Llama-3.1-70B-Instruct-FP8 | ❌ | ❌ | | neuralmagic/Meta-Llama-3.1-70B-Instruct-quantized.w8a8 | ❌ | ❌ | ```python import aiohttp import asyncio import difflib async def call_openai_api(): api_key = "{YOUR_API_KEY}" url = "http://{YOUR_ENDPOINT}/v1/chat/completions" headers = {"Content-Type": "application/json", "Authorization": f"Bearer {api_key}"} data = { "model": "hugging-quants/Meta-Llama-3.1-70B-Instruct-AWQ-INT4", "messages": [ { "role": "system", "content": "You are a helpful assistant generating random numbers.", }, { "role": "user", "content": "Give me 100 random numbers between 1 and 1000: ", }, ], "temperature": 0.6, "max_tokens": 1024, "seed": 4419, } async with aiohttp.ClientSession() as session: async with session.post(url, headers=headers, json=data) as response: response.ra...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 5: [Bug]: Reproducibility not guaranteed when tp > 1 bug ### Your current environment ### 🐛 Describe the bug I expect to get the exact numbers back when using a fixed seed. When using TP=2. It works when using TP=1 | Model
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 4: --------------------|-----------------|----------------------| | hugging-quants/Meta-Llama-3.1-70B-Instruct-AWQ-INT4 | ❌ | ❌ | | neuralmagic/Meta-Llama-3.1-70B-Instruct-FP8 | ❌ | ❌ | | neuralmagic/Meta-Llama-3.1-70B
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: e__ == "__main__": asyncio.run(call_multiple()) ``` As I am using `A100`. It happens way less often when using the `awq` kernels than when using the `FP8` kernels. I the error that exists in the following `vllm` version...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: ck when using a fixed seed. When using TP=2. It works when using TP=1 | Model (tp=2) | --enforce-eager | (NO) --enforce-eager | |--------------------------------------------------------|-----------------|---------------...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: gits;speculative_decoding cuda;fp8;kernel;operator;quantization;sampling;triton build_error;nan_inf dtype;env_dependency Your current environment

## Wiki 抽取状态

- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
