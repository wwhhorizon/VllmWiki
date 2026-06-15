# vllm-project/vllm#25418: [Performance][Multimodal]: Per-request `mm_processor_kwargs` are very slow

| 字段 | 值 |
| --- | --- |
| Issue | [#25418](https://github.com/vllm-project/vllm/issues/25418) |
| 状态 | closed |
| 标签 | performance |
| 评论 | 5; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Performance][Multimodal]: Per-request `mm_processor_kwargs` are very slow

### Issue 正文摘录

### Proposal to improve performance Passing per-request `mm_processor_kwargs` like FPS as added in #13533 greatly reduces performance. ### Report of performance regression I tested this on latest `main` (239ef0c1ac0dfe68d8d2e28c54ecf9aa9bcd945b): ```shell vllm serve Qwen/Qwen2.5-VL-7B-Instruct vllm bench serve --backend openai-chat --endpoint-type openai-chat --model Qwen/Qwen2.5-VL-7B-Instruct --endpoint /v1/chat/completions --dataset-name hf --dataset-path lmarena-ai/VisionArena-Chat --hf-split train --num-prompts 100 ``` Baseline performance on a single L40s GPU ``` ============ Serving Benchmark Result ============ Successful requests: 100 Benchmark duration (s): 13.73 Total input tokens: 5280 Total generated tokens: 11260 Request throughput (req/s): 7.28 Output token throughput (tok/s): 819.84 Peak output token throughput (tok/s): 2509.00 Peak concurrent requests: 100.00 Total Token throughput (tok/s): 1204.27 ---------------Time to First Token---------------- Mean TTFT (ms): 4651.00 Median TTFT (ms): 4496.22 P99 TTFT (ms): 9359.00 -----Time per Output Token (excl. 1st token)------ Mean TPOT (ms): 80.28 Median TPOT (ms): 74.01 P99 TPOT (ms): 257.39 ---------------Inter-token...

## 候选优化模式

- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 6: added in #13533 greatly reduces performance. ### Report of performance regression I tested this on latest `main` (239ef0c1ac0dfe68d8d2e28c54ecf9aa9bcd945b): ```shell vllm serve Qwen/Qwen2.5-VL-7B-Instruct vllm bench ser...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 5: [Performance][Multimodal]: Per-request `mm_processor_kwargs` are very slow performance ### Proposal to improve performance Passing per-request `mm_processor_kwargs` like FPS as added in #13533 greatly reduces performanc...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: b): ```shell vllm serve Qwen/Qwen2.5-VL-7B-Instruct vllm bench serve --backend openai-chat --endpoint-type openai-chat --model Qwen/Qwen2.5-VL-7B-Instruct --endpoint /v1/chat/completions --dataset-name hf --dataset-path...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: [Performance][Multimodal]: Per-request `mm_processor_kwargs` are very slow performance ### Proposal to improve performance Passing per-request `mm_processor_kwargs` like FPS as added in #13533 greatly reduces performanc...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
