# vllm-project/vllm#35705: [Bug]: streaming mode+finish_reason length, delta content not empty with finish_reason length

| 字段 | 值 |
| --- | --- |
| Issue | [#35705](https://github.com/vllm-project/vllm/issues/35705) |
| 状态 | open |
| 标签 | bug;rocm;stale |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: streaming mode+finish_reason length, delta content not empty with finish_reason length

### Issue 正文摘录

### Your current environment vllm 0.15 and vllm 0.9.2 all tested, same problem. ubuntu2004 qwen3 8b model ### 🐛 Describe the bug Bug description: vllm serve qwen3 model, openai request as following: v1/chat/completions { "model": "HiModel_xh2_qwen3_8b_256_32k_b1_1chip_2cores_v0.7.0_20251231", "messages": [ \{"role": "system", "content": "你是一个诗词小助手"} , {"role": "user", "content": "tell me who you are?"} ], "max_completion_tokens":10, "max_tokens":10, "stream":true }} vllm response： data: {"id":"chatcmpl-8b2b91720edd4372b0579e89255b4828","object":"chat.completion.chunk","created":1772423572,"model":"qwen3_8b","choices":[{"index":0,"delta":{"role":"assistant","content":""},"logprobs":null,"finish_reason":null}]} data: {"id":"chatcmpl-8b2b91720edd4372b0579e89255b4828","object":"chat.completion.chunk","created":1772423572,"model":"qwen3_8b","choices":[{"index":0,"delta":{"content":" ."},"logprobs":null,"finish_reason":null}]} data: {"id":"chatcmpl-8b2b91720edd4372b0579e89255b4828","object":"chat.completion.chunk","created":1772423572,"model":"qwen3_8b","choices":[{"index":0,"delta":{"content":" "},"logprobs":null,"finish_reason":null}]} data: {"id":"chatcmpl-8b2b91720edd4372b0579e89255...

## 候选优化模式

- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: ish_reason length, delta content not empty with finish_reason length bug;rocm;stale ### Your current environment vllm 0.15 and vllm 0.9.2 all tested, same problem. ubuntu2004 qwen3 8b model ### 🐛 Describe the bug Bug de...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: vironment vllm 0.15 and vllm 0.9.2 all tested, same problem. ubuntu2004 qwen3 8b model ### 🐛 Describe the bug Bug description: vllm serve qwen3 model, openai request as following: v1/chat/completions { "model": "HiModel...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: eason length, delta content not empty with finish_reason length bug;rocm;stale ### Your current environment vllm 0.15 and vllm 0.9.2 all tested, same problem. ubuntu2004 qwen3 8b model ### 🐛 Describe the bug Bug descrip...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ug;rocm;stale ### Your current environment vllm 0.15 and vllm 0.9.2 all tested, same problem. ubuntu2004 qwen3 8b model ### 🐛 Describe the bug Bug description: vllm serve qwen3 model, openai request as following: v1/cha...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
