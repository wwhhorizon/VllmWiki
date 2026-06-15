# vllm-project/vllm#11160: [Bug]: qwen2.5-72b-instruct-q4_K_S GGUF format Output error 

| 字段 | 值 |
| --- | --- |
| Issue | [#11160](https://github.com/vllm-project/vllm/issues/11160) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 10; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: qwen2.5-72b-instruct-q4_K_S GGUF format Output error 

### Issue 正文摘录

### Your current environment ### Model Input Dumps _No response_ ### 🐛 Describe the bug The service can be started, but the API cannot be stopped while it is being generated, and the output content is meaningless like ’0‘ or 'm' all stream like this: ``` { "id": "chatcmpl-e85b68fe1c39481f8f30cc8979247516", "object": "chat.completion.chunk", "created": 1734070518, "model": "qwen2.5-72b-instruct-q4_K_S", "choices": [ { "index": 0, "delta": { "content": "0" }, "logprobs": null, "finish_reason": null } ] } ``` server log ``` vllm-qwen2.5-72b-instruct-q4_K_S | INFO 12-12 22:23:19 logger.py:37] Received request chatcmpl-fe6ba732b45a4206a5826cdff2a3f35c: prompt: ' system\nYou are Qwen, created by Alibaba Cloud. You are a helpful assistant. \n user\n你好，你是谁 \n assistant\n', params: SamplingParams(n=1, presence_penalty=0.0, frequency_penalty=0.0, repetition_penalty=1.0, temperature=0.7, top_p=1.0, top_k=-1, min_p=0.0, seed=None, stop=[], stop_token_ids=[], bad_words=[], include_stop_str_in_output=False, ignore_eos=False, max_tokens=32735, min_tokens=0, logprobs=None, prompt_logprobs=None, skip_special_tokens=True, spaces_between_special_tokens=True, truncate_prompt_tokens=None, guided_decod...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: [Bug]: qwen2.5-72b-instruct-q4_K_S GGUF format Output error bug;stale ### Your current environment ### Model Input Dumps _No response_ ### 🐛 Describe the bug The service can be started, but the API cannot be stopped whi
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: [Bug]: qwen2.5-72b-instruct-q4_K_S GGUF format Output error bug;stale ### Your current environment ### Model Input Dumps _No response_ ### 🐛 Describe the bug The service can be started, but the API cannot be stopped whi...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 2: .5-72b-instruct-q4_K_S | INFO 12-12 22:23:20 metrics.py:449] Avg prompt throughput: 3.6 tokens/s, Avg generation throughput: 0.1 tokens/s, Running: 1 reqs, Swapped: 0 reqs, Pending: 0 reqs, GPU KV cache usage: 0.0%, CPU...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: tokens=32735, min_tokens=0, logprobs=None, prompt_logprobs=None, skip_special_tokens=True, spaces_between_special_tokens=True, truncate_prompt_tokens=None, guided_decoding=None), prompt_token_ids: None, lora_request: No...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: 76) ### Before submitting a new issue... - [X] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
