# vllm-project/vllm#12442: [Usage]: Shape mismatch when batch requests with openai chat completion apis and qwen2-vl

| 字段 | 值 |
| --- | --- |
| Issue | [#12442](https://github.com/vllm-project/vllm/issues/12442) |
| 状态 | closed |
| 标签 | usage;stale |
| 评论 | 13; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Usage]: Shape mismatch when batch requests with openai chat completion apis and qwen2-vl

### Issue 正文摘录

Parallel requests to a ray serve ‘OpenAI Chat Completions API’ based on this instruction: [Serve a Large Language Model with vLLM — Ray 2.41.0](https://docs.ray.io/en/latest/serve/tutorials/vllm-example.html) The model is qwen2-vl, and the request contains both text and image prompts. It is normal when call one request at one time, but get error when parallel requesting with ‘max_ongoing_requests >= 2’. The error stack shows below： ERROR 2025-01-23 00:22:21,963 vl_VLLMDeployment 4gtvteb2 e1d433cc-e551-4e5e-b10e-986dea9fe1ad /v1/chat/completions llm.py:128 - Error in generate() Traceback (most recent call last): File “/home/ray/anaconda3/lib/python3.9/site-packages/vllm/worker/model_runner_base.py”, line 116, in _wrapper return func(*args, **kwargs) File “/home/ray/anaconda3/lib/python3.9/site-packages/vllm/worker/model_runner.py”, line 1654, in execute_model hidden_or_intermediate_states = model_executable( File “/home/ray/anaconda3/lib/python3.9/site-packages/torch/nn/modules/module.py”, line 1736, in _wrapped_call_impl return self._call_impl(*args, **kwargs) File “/home/ray/anaconda3/lib/python3.9/site-packages/torch/nn/modules/module.py”, line 1747, in _call_impl return forward...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: Shape mismatch when batch requests with openai chat completion apis and qwen2-vl usage;stale Parallel requests to a ray serve ‘OpenAI Chat Completions API’ based on this instruction: [Serve a Large Language Model with v...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: [Usage]: Shape mismatch when batch requests with openai chat completion apis and qwen2-vl usage;stale Parallel requests to a ray serve ‘OpenAI Chat Completions API’ based on this instruction: [Serve a Large Language Mod...
- [Bitwise 确定性与数值等价](../patterns/bitwise_determinism_equivalence.md) - 分数 1: [Usage]: Shape mismatch when batch requests with openai chat completion apis and qwen2-vl usage;stale Parallel requests to a ray serve ‘OpenAI Chat Completions API’ based on this instruction: [Serve a Large Language Mod...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: [Usage]: Shape mismatch when batch requests with openai chat completion apis and qwen2-vl usage;stale Parallel requests to a ray serve ‘OpenAI Chat Completions API’ based on this instruction: [Serve a Large Language Mod...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: a Large Language Model with vLLM — Ray 2.41.0](https://docs.ray.io/en/latest/serve/tutorials/vllm-example.html) The model is qwen2-vl, and the request contains both text and image prompts. It is normal when call one req...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
