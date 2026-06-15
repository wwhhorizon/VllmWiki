# vllm-project/vllm#10578: [Usage]: Use difference SamplingParams for each sample in batch inference via openai api

| 字段 | 值 |
| --- | --- |
| Issue | [#10578](https://github.com/vllm-project/vllm/issues/10578) |
| 状态 | closed |
| 标签 | usage;stale |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Usage]: Use difference SamplingParams for each sample in batch inference via openai api

### Issue 正文摘录

### Your current environment ```text The output of `python collect_env.py` ``` ### How would you like to use vllm I want use difference SamplingParams for each sample in batch inference via openai api. I can set `SamplingParams` for vllm via `extra_body`, but I want use difference `top_p` and `top_k` for each sample. How I do it? ``` from openai import OpenAI # Set OpenAI's API key and API base to use vLLM's API server. openai_api_base = "http://localhost:8001/v1" client = OpenAI( base_url=openai_api_base, ) chat_response = client.completions.create( model="qwen2.5/transformers/72b-instruct/1", prompt=['this is test']*16, max_tokens=4096, temperature = 1, extra_body={'top_p': 1.0, 'top_k': 50} ) ``` I can do it when use `llm.generate` but I can't found way do via openai api. Anyone can help? ``` llm.generate( prompts=['this is test']*16, sampling_params=[list_of_sampling_params], # It's work ) ``` ### Before submitting a new issue... - [X] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: i_base, ) chat_response = client.completions.create( model="qwen2.5/transformers/72b-instruct/1", prompt=['this is test']*16, max_tokens=4096, temperature = 1, extra_body={'top_p': 1.0, 'top_k': 50}
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: rence `top_p` and `top_k` for each sample. How I do it? ``` from openai import OpenAI # Set OpenAI's API key and API base to use vLLM's API server. openai_api_base = "http://localhost:8001/v1" client = OpenAI( base_url=...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: ``` ### Before submitting a new issue... - [X] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: e SamplingParams for each sample in batch inference via openai api usage;stale ### Your current environment ```text The output of `python collect_env.py` ``` ### How would you like to use vllm I want use difference Samp...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: odel="qwen2.5/transformers/72b-instruct/1", prompt=['this is test']*16, max_tokens=4096, temperature = 1, extra_body={'top_p': 1.0, 'top_k': 50} ) ``` I can do it when use `llm.generate` but I can't found way do

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
