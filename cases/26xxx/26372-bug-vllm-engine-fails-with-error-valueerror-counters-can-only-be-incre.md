# vllm-project/vllm#26372: [Bug]: vLLM engine fails with error: 'ValueError: Counters can only be incremented by non-negative amounts.'

| 字段 | 值 |
| --- | --- |
| Issue | [#26372](https://github.com/vllm-project/vllm/issues/26372) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 11; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: vLLM engine fails with error: 'ValueError: Counters can only be incremented by non-negative amounts.'

### Issue 正文摘录

### 🐛 Describe the bug When serving an LLM with speculative decoding, engine breaks due to duplicate request id (Docker Image: vllm/vllm-openai:v0.11.0) Serve Command: ``` command: - vllm - serve - /mnt/models/qwen3-30b-a3b-instruct - --host - "0.0.0.0" - --port - "8000" - --uvicorn-log-level - warning - --enable-log-requests - --enable-log-outputs - --served-model-name - qwen3 - --trust-remote-code - --gpu-memory-utilization - "0.9" - --enable-prefix-caching - --max-model-len - "12288" - --enable-auto-tool-choice - --tool-call-parser - hermes - --speculative-config - '{"method": "ngram", "num_speculative_tokens": 4, "prompt_lookup_max": 4}' ``` ``` (APIServer pid=1) ERROR 10-07 11:17:01 [async_llm.py:480] AsyncLLM output_handler failed. (APIServer pid=1) ERROR 10-07 11:17:01 [async_llm.py:480] Traceback (most recent call last): (APIServer pid=1) ERROR 10-07 11:17:01 [async_llm.py:480] File "/usr/local/lib/python3.12/dist-packages/vllm/v1/engine/async_llm.py", line 474, in output_handler (APIServer pid=1) ERROR 10-07 11:17:01 [async_llm.py:480] logger_manager.record( (APIServer pid=1) ERROR 10-07 11:17:01 [async_llm.py:480] File "/usr/local/lib/python3.12/dist-packages/vllm/v1/met...

## 候选优化模式

- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 4: -negative amounts.' bug ### 🐛 Describe the bug When serving an LLM with speculative decoding, engine breaks due to duplicate request id (Docker Image: vllm/vllm-openai:v0.11.0) Serve Command: ``` command: - vllm - serve...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: penai:v0.11.0) Serve Command: ``` command: - vllm - serve - /mnt/models/qwen3-30b-a3b-instruct - --host - "0.0.0.0" - --port - "8000" - --uvicorn-log-level - warning - --enable-log-requests - --enable-log-outputs - --se...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: M with speculative decoding, engine breaks due to duplicate request id (Docker Image: vllm/vllm-openai:v0.11.0) Serve Command: ``` command: - vllm - serve - /mnt/models/qwen3-30b-a3b-instruct - --host - "0.0.0.0" - --po...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: ng. ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
