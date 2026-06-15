# vllm-project/vllm#4589: [Bug]: Loading GenerationConfig to SamplingParams.stop_token_ids interfere with ignore_eos=True

| 字段 | 值 |
| --- | --- |
| Issue | [#4589](https://github.com/vllm-project/vllm/issues/4589) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 4; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: Loading GenerationConfig to SamplingParams.stop_token_ids interfere with ignore_eos=True

### Issue 正文摘录

### Your current environment There is a [patch](https://github.com/vllm-project/vllm/commit/a134ef6f5e6c24d3cd459c63557e5db276db25b2) https://github.com/vllm-project/vllm/pull/4182 to load stop_token_ids from GenerationConfig to work around with in Llama3-Instruct. However, this logic interferes with ignore_eos=True because the current logic treats eos_token_ids as stop_token_ids and doesn't check ignore_eos. See [stop_checker](https://github.com/vllm-project/vllm/blob/main/vllm/engine/output_processor/stop_checker.py#L44) ### 🐛 Describe the bug Test: Model: Llama-2-70b-chat-hf ``` curl http://localhost:8086/v1/completions \ -H "Content-Type: application/json" \ -d '{ "model": "/models/Llama-2-70b-chat-hf", "prompt": "Write a Python function to find the nth Fibonacci number. The function should be efficient and handle cases where n is very large.", "max_tokens": 200, "temperature": 0, "ignore_eos": true, "repetition_penalty": 1.3, "logprobs": 5 }' ``` Response: v0.3.1 ``` {"id":"cmpl-14e9a1807fe743ce8b5c9e179cd7ceeb","object":"text_completion","created":1893216,"model":"/models/Llama-2-70b-chat-hf","choices":[{"index":0,"text":"\nA good approach would be to use memoization, which...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: [Bug]: Loading GenerationConfig to SamplingParams.stop_token_ids interfere with ignore_eos=True bug ### Your current environment There is a [patch](https://github.com/vllm-project/vllm/commit/a134ef6f5e6c24d3cd459c63557...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: x problems. Finally make sure your code has proper error handling mechanisms in place (e g., checking if negative integers have been passed). A new study published in Nature Communications suggests that climate change m...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: t-hf", "prompt": "Write a Python function to find the nth Fibonacci number. The function should be efficient and handle cases where n is very large.", "max_tokens": 200, "temperature": 0, "ignore_eos": true, "repetition...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: lm/engine/output_processor/stop_checker.py#L44) ### 🐛 Describe the bug Test: Model: Llama-2-70b-chat-hf ``` curl http://localhost:8086/v1/completions \ -H "Content-Type: application/json" \ -d '{ "model": "/models/Llama...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
