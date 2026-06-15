# vllm-project/vllm#22291: [Feature]: how to calculate --gpu-memory-utilization for a given max concurrency such as 5 req/s, 20 req/s and 50 req/s

| 字段 | 值 |
| --- | --- |
| Issue | [#22291](https://github.com/vllm-project/vllm/issues/22291) |
| 状态 | closed |
| 标签 | feature request;stale |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Feature]: how to calculate --gpu-memory-utilization for a given max concurrency such as 5 req/s, 20 req/s and 50 req/s

### Issue 正文摘录

### 🚀 The feature, motivation and pitch In the [pagedAttension][1] article, section-3.1 mentions a calculation which is `one-token-kvcache = 2 (key and value vector) * hidden-state-size * number-of-layers * data-type(int=8,float=32,bfloat=16)`. If multiplying the above result with `model-context-length(prompt and output)`, the final result becomes the gpu usage of kv-cache for one request. By the [config.json][2] of Qwen/Qwen2.5-7B-Instruct-GPTQ-Int8, the kv-cache usage for one token requires `2 * 3584 * 28 * 8 = 1605632 B = 1.53 MB`. The kv-cache usage for one user will use `1.53 * 3072 = 4.59 GB`, which seems incorrect by the below observation. which part is wrong? please correct me. Currently, I am running [Qwen/Qwen2.5-7B-Instruct-GPTQ-Int8][3] by vllm-v0.9.2. By adjusting the `--gpu-memory-utilization` option, there is the measurement result: 10.6 GB supports 5 req/s, 13.0 GB supports 20 req/s and 18.1 GB supports 50 req/s. Roughly, one request requires 0.16 GB for kv-cache, which is calculated as `(13 -10.6)/(20-5)` and verified by `(13 -10.6)/(20-5) = (18 -13)/(50-20)`. Is this calculation correct? [1]: https://arxiv.org/abs/2309.06180 [2]: https://huggingface.co/Qwen/Qwen2...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: a-type(int=8,float=32,bfloat=16)`. If multiplying the above result with `model-context-length(prompt and output)`, the final result becomes the gpu usage of kv-cache for one request. By the [config.json][2] of Qwen/Qwen...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: r a given max concurrency such as 5 req/s, 20 req/s and 50 req/s feature request;stale ### 🚀 The feature, motivation and pitch In the [pagedAttension][1] article, section-3.1 mentions a calculation which is `one-token-k...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: se_ ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [KV Cache 容量、压缩与 Offload](../patterns/kv_cache_capacity_offload.md) - 分数 1: xt-length(prompt and output)`, the final result becomes the gpu usage of kv-cache for one request. By the [config.json][2] of Qwen/Qwen2.5-7B-Instruct-GPTQ-Int8, the kv-cache usage for one token requires `2 * 3584 * 28...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
