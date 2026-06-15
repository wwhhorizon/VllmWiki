# vllm-project/vllm#16339: [Bug]: TypeError when using guidance as backend

| 字段 | 值 |
| --- | --- |
| Issue | [#16339](https://github.com/vllm-project/vllm/issues/16339) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 7; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: TypeError when using guidance as backend

### Issue 正文摘录

### Your current environment vllm serve mistralai/Ministral-8B-Instruct-2410 --port 8888 --max-model-len 4096 --quantization fp8 --dtype auto --guided-decoding-backend guidance --tokenizer mistralai/Ministral-8B-Instruct-2410 ### 🐛 Describe the bug while setting 'guidance' as decoding backend I keep having this error: File "/home/ubuntu/venv/lib/python3.12/site-packages/vllm/v1/structured_output/backend_guidance.py", line 161, in validate_guidance_grammar err = llguidance.LLMatcher.validate_grammar(guidance_grm, ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ TypeError: LLMatcher.validate_grammar() got some positional-only arguments passed as keyword arguments: 'tokenizer' ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 3: mistralai/Ministral-8B-Instruct-2410 --port 8888 --max-model-len 4096 --quantization fp8 --dtype auto --guided-decoding-backend guidance --tokenizer mistralai/Ministral-8B-Instruct-2410 ### 🐛 Describe the bug while sett...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: [Bug]: TypeError when using guidance as backend bug;stale ### Your current environment vllm serve mistralai/Ministral-8B-Instruct-2410 --port 8888 --max-model-len 4096 --quantization fp8 --dtype auto --guided-decoding-b...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: er' ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: nment vllm serve mistralai/Ministral-8B-Instruct-2410 --port 8888 --max-model-len 4096 --quantization fp8 --dtype auto --guided-decoding-backend guidance --tokenizer mistralai/Ministral-8B-Instruct-2410 ### 🐛 Describe t...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: [Bug]: TypeError when using guidance as backend bug;stale ### Your current environment vllm serve mistralai/Ministral-8B-Instruct-2410 --port 8888 --max-model-len 4096 --quantization fp8 --dtype auto --guided-decoding-b...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
