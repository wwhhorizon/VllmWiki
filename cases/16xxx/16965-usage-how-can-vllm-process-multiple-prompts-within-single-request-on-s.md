# vllm-project/vllm#16965: [Usage]: How can vllm process multiple prompts within single request on server

| 字段 | 值 |
| --- | --- |
| Issue | [#16965](https://github.com/vllm-project/vllm/issues/16965) |
| 状态 | closed |
| 标签 | usage |
| 评论 | 5; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Usage]: How can vllm process multiple prompts within single request on server

### Issue 正文摘录

### Your current environment I have deployed qwen-32B model on my server. `CUDA_VISIBLE_DEVICES=6 python -m vllm.entrypoints.api_server --model "/home/my_path/Qwen-32B/" --tensor-parallel-size 1 --port 8047 --max_model_len 8192` Now I want to process multiple prompts within single request like this: ```text prompt = [f"{input_text}", f"{input_text}"] payload = { "prompt": ["what is your name?", "where are you from?"], "max_tokens": max_tokens, "temperature": temperature, "top_p": top_p, "repetition_penalty":1.2, } headers={"Content-Type": "application/json"} response = requests.post(url, headers=headers, data=payload, timeout=timeout) ``` But an error is reported: `TypeError: inputs must be a string, TextPrompt, or TokensPrompt` I wonder whether there is a way that a list of prompts can be processed within single request. ### How would you like to use vllm I want to process multiple prompts within single request on my server. ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked ques...

## 候选优化模式

- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: Your current environment I have deployed qwen-32B model on my server. `CUDA_VISIBLE_DEVICES=6 python -m vllm.entrypoints.api_server --model "/home/my_path/Qwen-32B/" --tensor-parallel-size 1 --port 8047 --max_model_len...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: le request on server usage ### Your current environment I have deployed qwen-32B model on my server. `CUDA_VISIBLE_DEVICES=6 python -m vllm.entrypoints.api_server --model "/home/my_path/Qwen-32B/" --tensor-parallel-size...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: [Usage]: How can vllm process multiple prompts within single request on server usage ### Your current environment I have deployed qwen-32B model on my server. `CUDA_VISIBLE_DEVICES=6 python -m vllm.entrypoints.api_serve...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
