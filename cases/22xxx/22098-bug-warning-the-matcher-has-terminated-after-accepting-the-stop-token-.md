# vllm-project/vllm#22098: [Bug]: Warning: The matcher has terminated after accepting the stop token, but is trying to accept new token with id 198.

| 字段 | 值 |
| --- | --- |
| Issue | [#22098](https://github.com/vllm-project/vllm/issues/22098) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: Warning: The matcher has terminated after accepting the stop token, but is trying to accept new token with id 198.

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug when using vllm/vllm-openai:v0.10.0 with following config: ``` --model QuantTrio/Qwen3-235B-A22B-Instruct-2507-GPTQ-Int4-Int8Mix --api-key test --tensor-parallel-size 4 --disable-log-requests --guided-decoding-backend auto --max-model-len 222144 --max_num_batched_tokens 256 --enable-expert-parallel --speculative-config '{"method": "ngram", "num_speculative_tokens": 5, "prompt_lookup_max": 5, "prompt_lookup_min": 1}' --enable-auto-tool-choice --tool-call-parser hermes ``` during structured decoding each request logs: `/project/cpp/grammar_matcher.cc:369: Warning: The matcher has terminated after accepting the stop token, but is trying to accept new token with id 198.` I am also setting VLLM_USE_FLASHINFER_SAMPLER=0 due to https://github.com/vllm-project/vllm/issues/19483 response still follows provided schema ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: 🐛 Describe the bug when using vllm/vllm-openai:v0.10.0 with following config: ``` --model QuantTrio/Qwen3-235B-A22B-Instruct-2507-GPTQ-Int4-Int8Mix --api-key test --tensor-parallel-size 4 --disable-log-requests --guided...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 3: pting the stop token, but is trying to accept new token with id 198. bug;stale ### Your current environment ### 🐛 Describe the bug when using vllm/vllm-openai:v0.10.0 with following config: ``` --model QuantTrio/Qwen3-2...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 2: y test --tensor-parallel-size 4 --disable-log-requests --guided-decoding-backend auto --max-model-len 222144 --max_num_batched_tokens 256 --enable-expert-parallel --speculative-config '{"method": "ngram", "num_speculati...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 2: when using vllm/vllm-openai:v0.10.0 with following config: ``` --model QuantTrio/Qwen3-235B-A22B-Instruct-2507-GPTQ-Int4-Int8Mix --api-key test --tensor-parallel-size 4 --disable-log-requests --guided-decoding-backend a...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: ma ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), whi...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
