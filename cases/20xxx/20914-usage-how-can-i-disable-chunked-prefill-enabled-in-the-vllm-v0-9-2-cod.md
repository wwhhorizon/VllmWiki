# vllm-project/vllm#20914: [Usage]: How can I disable chunked_prefill_enabled in the vLLM v0.9.2 code?

| 字段 | 值 |
| --- | --- |
| Issue | [#20914](https://github.com/vllm-project/vllm/issues/20914) |
| 状态 | closed |
| 标签 | usage;stale |
| 评论 | 8; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Usage]: How can I disable chunked_prefill_enabled in the vLLM v0.9.2 code?

### Issue 正文摘录

### Your current environment How can I disable chunked_prefill_enabled in the vLLM v0.9.2 code? Even though I set the parameter ``--no-enable-chunked-prefill``, the log still outputs 'Chunked prefill is enabled'. This is my server-side commands: ```server-side commands python3 -m vllm.entrypoints.openai.api_server \ --model /nas_aisw/datasets/checkpoints/LLM/Qwen3-30B-A3B-FP8 \ --trust-remote-code \ --max-num-batched-tokens=4096 \ --max-model-len=16384 \ --no-enable-chunked-prefill \ --long-prefill-token-threshold=0 \ --enable-prefix-caching \ --disable-log-requests ``` This is part of the log of server： ``` INFO 07-14 08:31:58 [config.py:2244] Chunked prefill is enabled with max_num_batched_tokens=4096. ``` ### How would you like to use vllm ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: `server-side commands python3 -m vllm.entrypoints.openai.api_server \ --model /nas_aisw/datasets/checkpoints/LLM/Qwen3-30B-A3B-FP8 \ --trust-remote-code \ --max-num-batched-tokens=4096 \ --max-model-len=16384 \ --no-ena...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 3: [Usage]: How can I disable chunked_prefill_enabled in the vLLM v0.9.2 code? usage;stale ### Your current environment How can I disable chunked_prefill_enabled in the vLLM v0.9.2 code? Even though I set the parameter ``-...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 1: i.api_server \ --model /nas_aisw/datasets/checkpoints/LLM/Qwen3-30B-A3B-FP8 \ --trust-remote-code \ --max-num-batched-tokens=4096 \ --max-model-len=16384 \ --no-enable-chunked-prefill \ --long-prefill-token-threshold=0...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: llm ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
