# vllm-project/vllm#18150: [Bug]: Timeout Error with Gemma Models in vLLM 0.8.5

| 字段 | 值 |
| --- | --- |
| Issue | [#18150](https://github.com/vllm-project/vllm/issues/18150) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 9; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | attention_kv_cache;ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;multimodal_vlm;scheduler_memory |
| 子分类 | throughput |
| Operator 关键词 | cache;cuda;triton |
| 症状 | build_error;slowdown |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Timeout Error with Gemma Models in vLLM 0.8.5

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug ### Issue Description When using vLLM 0.8.5 with Gemma models (specifically ``google/gemma-3-4b-it``), the OpenAI-compatible chat completions endpoint hangs indefinitely and eventually times out with an APITimeoutError, despite the model actively generating tokens. **Important**: **This issue occurs ONLY with Gemma models**. The same code works perfectly with LLaVa (e.g., ``llava-hf/llava-1.5-7b-hf``) and other models. ### Bug Behavior 1. The request hangs for a long time (minutes) 2. Server logs show active generation (~19-20 tokens/sec) 3. Eventually results in a timeout error: ``` raise APITimeoutError(request=request) from err openai.APITimeoutError: Request timed out. ``` 4. When setting ``max_tokens`` parameter in the ``client.chat.completions.create()`` function (OpenAI client) call, it still times out or returns empty content: ``` choices=[Choice(finish_reason='length', index=0, logprobs=None, message=ChatCompletionMessage(content='', refusal=None, role='assistant'))] ``` ### Reproduction Steps 1. Install vLLM 0.8.5: ``pip install vllm==0.8.5`` 2. Start the server with a Gemma model (here is the specific command I used to...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 6: [Bug]: Timeout Error with Gemma Models in vLLM 0.8.5 bug;stale ### Your current environment ### 🐛 Describe the bug ### Issue Description When using vLLM 0.8.5 with Gemma models (specifically ``google/gemma-3-4b-it``), t...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 5: e bug ### Issue Description When using vLLM 0.8.5 with Gemma models (specifically ``google/gemma-3-4b-it``), the OpenAI-compatible chat completions endpoint hangs indefinitely and eventually times out with an APITimeout...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 5: [Bug]: Timeout Error with Gemma Models in vLLM 0.8.5 bug;stale ### Your current environment ### 🐛 Describe the bug ### Issue Description When using vLLM 0.8.5 with Gemma models (specifically ``google/gemma-3-4b-it``), t...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 3: periods: ``` INFO 05-13 13:58:21 [loggers.py:111] Engine 000: Avg prompt throughput: 41.3 tokens/s, Avg generation throughput: 19.3 tokens/s, Running: 1 reqs, Waiting: 0 reqs, GPU KV cache usage: 0.8%, Prefix cache hit...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: .5. ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
