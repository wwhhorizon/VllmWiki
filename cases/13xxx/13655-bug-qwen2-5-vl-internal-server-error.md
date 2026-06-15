# vllm-project/vllm#13655: [Bug]: Qwen2.5 VL Internal Server Error

| 字段 | 值 |
| --- | --- |
| Issue | [#13655](https://github.com/vllm-project/vllm/issues/13655) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 23; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cuda;operator;sampling;triton |
| 症状 | build_error;nan_inf |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Qwen2.5 VL Internal Server Error

### Issue 正文摘录

### Your current environment I used the official docker image v0.7.2 and reinstalled vllm with commit d0a7a2769d92619afdcdc3b91c78098eaa9e38c0 and trainsformers 4.49.0. ### 🐛 Describe the bug vllm startup command: ```bash python3 -m vllm.entrypoints.openai.api_server \ --model /model/Qwen2.5-VL-72B-Instruct \ --port 23333 \ --trust-remote-code \ --tensor-parallel-size 4 \ --max-model-len 20000 \ --max-num-batched-tokens 20000 \ --max-num-seqs 1 \ --max-logprobs 0 \ --enforce-eager \ --gpu-memory-utilization 0.95 ``` The test input image is a 500*19 png. The server log: ```text INFO 02-20 23:56:14 logger.py:39] Received request chatcmpl-c10b409ab01b4abbaca5fa25c3d3d808: prompt: ' system\nYou are a helpful assistant. \n user\n \nHello \n assistant\n', params: SamplingParams(n=1, presence_penalty=0.0, frequency_penalty=0.0, repetition_penalty=1.0, temperature=1.0, top_p=1.0, top_k=-1, min_p=0.0, seed=None, stop=[], stop_token_ids=[], bad_words=[], include_stop_str_in_output=False, ignore_eos=False, max_tokens=19976, min_tokens=0, logprobs=None, prompt_logprobs=None, skip_special_tokens=True, spaces_between_special_tokens=True, truncate_prompt_tokens=None, guided_decoding=None), promp...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 5: L Internal Server Error bug ### Your current environment I used the official docker image v0.7.2 and reinstalled vllm with commit d0a7a2769d92619afdcdc3b91c78098eaa9e38c0 and trainsformers 4.49.0. ### 🐛 Describe the bug...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: ``` ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: [Bug]: Qwen2.5 VL Internal Server Error bug ### Your current environment I used the official docker image v0.7.2 and reinstalled vllm with commit d0a7a2769d92619afdcdc3b91c78098eaa9e38c0 and trainsformers 4.49.0. ### 🐛...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: g. The server log: ```text INFO 02-20 23:56:14 logger.py:39] Received request chatcmpl-c10b409ab01b4abbaca5fa25c3d3d808: prompt: ' system\nYou are a helpful assistant. \n user\n \nHello \n assistant\n', params: Sampling...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: odel_support;sampling_logits;speculative_decoding cuda;operator;sampling;triton build_error;nan_inf env_dependency Your current environment

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
