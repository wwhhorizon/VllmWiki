# vllm-project/vllm#279: Possibility of Passing Prompts as List[str] to AsyncEngine.generate()

| 字段 | 值 |
| --- | --- |
| Issue | [#279](https://github.com/vllm-project/vllm/issues/279) |
| 状态 | closed |
| 标签 | good first issue;feature request |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> Possibility of Passing Prompts as List[str] to AsyncEngine.generate()

### Issue 正文摘录

Hi! Thank you for your amazing framework! I have tried serving a GPT BigCode model using vllm together with ray following the example: https://github.com/ray-project/ray/blob/3d3183d944424a960a2c6ce048abd1316c901c1e/doc/source/serve/doc_code/vllm_example.py And in my use case the response is in "non-streaming" format. I directly passed the request to the vllm async engine to use the continuous batching ability. However, when I tested it with stress testing tool, I found the improvement of the latency and throughput is not that good. One reason behind might be that the average length of testing input prompt is quite long (around 1000 tokens) which uses almost all space of KV cache in GPU and some of them are duplicated. Therefore I may need to do a preprocessing of the request in the batch level first to filter out some duplicate requests then pass the request to vllm engine. Currently, if I want to use async engine, I can only pass one prompt to the pool at one time. May I know if you have the plan to add a function like allowing adding multi prompts into the pool at one time (each with a different request_id) and retrieve them based on request_id?

## 候选优化模式

- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 3: llm async engine to use the continuous batching ability. However, when I tested it with stress testing tool, I found the improvement of the latency and throughput is not that good. One reason behind might be that the av...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: Thank you for your amazing framework! I have tried serving a GPT BigCode model using vllm together with ray following the example: https://github.com/ray-project/ray/blob/3d3183d944424a960a2c6ce048abd1316c901c1e/doc/sou...
- [KV Cache 容量、压缩与 Offload](../patterns/kv_cache_capacity_offload.md) - 分数 1: prompt is quite long (around 1000 tokens) which uses almost all space of KV cache in GPU and some of them are duplicated. Therefore I may need to do a preprocessing of the request in the batch level first to filter out...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: Prompts as List[str] to AsyncEngine.generate() good first issue;feature request Hi! Thank you for your amazing framework! I have tried serving a GPT BigCode model using vllm together with ray following the example: http...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
