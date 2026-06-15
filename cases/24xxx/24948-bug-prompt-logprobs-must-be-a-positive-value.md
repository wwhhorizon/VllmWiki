# vllm-project/vllm#24948: [Bug]: `prompt_logprobs` must be a positive value.

| 字段 | 值 |
| --- | --- |
| Issue | [#24948](https://github.com/vllm-project/vllm/issues/24948) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: `prompt_logprobs` must be a positive value.

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug I am using the latest vllm, i.e., version 0.10.2. I want to get the logprobs of the prompt. Specifically, at each position of the prompt, I would like to obtain all the logprobs in the vocabulary set. I follow the documentation in https://docs.vllm.ai/en/latest/api/vllm/sampling_params.html?h=sampling#vllm.sampling_params.SamplingParams.prompt_logprobs, which claims that "When set to -1, return all vocab_size log probabilities." to set `prompt_logprobs`. However, I got an error: `prompt_logprobs` must be a positive value. Could anyone help me fix this issue? Thanks! A piece of code below may help reproduce my issue ```python import asyncio import os import time from openai import OpenAI from transformers import AutoTokenizer os.environ["TOKENIZERS_PARALLELISM"] = "true" # vllm serve Qwen/Qwen2.5-0.5B-Instruct --port 8000 client = OpenAI( base_url="http://localhost:8000/v1", api_key="EMPTY", ) prompts = [ "Explain the theory of relativity in simple terms.", "What is the capital of France?", "Translate 'Hello, world' to Spanish.", "Who wrote 'To Kill a Mockingbird'?", "Summarize the plot of the movie Inception.", "Give me a recipe...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: nvironment ### 🐛 Describe the bug I am using the latest vllm, i.e., version 0.10.2. I want to get the logprobs of the prompt. Specifically, at each position of the prompt, I would like to obtain all the logprobs in the...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: from transformers import AutoTokenizer os.environ["TOKENIZERS_PARALLELISM"] = "true" # vllm serve Qwen/Qwen2.5-0.5B-Instruct --port 8000 client = OpenAI( base_url="http://localhost:8000/v1", api_key="EMPTY", ) prompts =...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: toTokenizer os.environ["TOKENIZERS_PARALLELISM"] = "true" # vllm serve Qwen/Qwen2.5-0.5B-Instruct --port 8000 client = OpenAI( base_url="http://localhost:8000/v1", api_key="EMPTY", ) prompts = [ "Explain the theory of r...
- [Bitwise 确定性与数值等价](../patterns/bitwise_determinism_equivalence.md) - 分数 1: ld anyone help me fix this issue? Thanks! A piece of code below may help reproduce my issue ```python import asyncio import os import time from openai import OpenAI from transformers import AutoTokenizer os.environ["TOK...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 1: plate( [{"role": "user", "content": prompt}], tokenize=False, add_generation_prompt=True, ) for prompt in prompts ] def send_request(prompt: str): print(f"🚀 Sending prompt: {prompt[:30]}...") try: completion = client.co...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
