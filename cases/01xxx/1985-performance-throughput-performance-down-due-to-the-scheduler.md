# vllm-project/vllm#1985: 【Performance】throughput performance down due to the scheduler 

| 字段 | 值 |
| --- | --- |
| Issue | [#1985](https://github.com/vllm-project/vllm/issues/1985) |
| 状态 | closed |
| 标签 |  |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> 【Performance】throughput performance down due to the scheduler 

### Issue 正文摘录

In https://github.com/vllm-project/vllm/commit/c1376e0f825e88e32b5aca85c676fe547bcb03c9, `num_tokens` is splited into `batch_size * seq_len`, this will cause the throughput performance down. I compare the two commit * base(v0.2.1): [651c614](https://github.com/vllm-project/vllm/commit/651c614aa43e497a2e2aab473493ba295201ab20) * new: [c1376e0](https://github.com/vllm-project/vllm/commit/c1376e0f825e88e32b5aca85c676fe547bcb03c9) Test case: llama7B @ Nvidia A10 Test command: ```bash python3 benchmark_throughput.py \ --backend vllm \ --dataset ShareGPT_V3_unfiltered_cleaned_split.json \ --model huggyllama/llama-7b \ --num-prompts 200 ``` Test result: * base(v0.2.1): Throughput: 1.82 requests/s, 856.51 tokens/s * new: Throughput: 1.76 requests/s, 830.07 tokens/s The reason of throughput donw is mostly because new scheduler introduce more padding tokens in one forward iteration. ```python num_paddings = num_batched_tokens - sum(new_seq_lens) if num_paddings > self.scheduler_config.max_paddings: break seq_lens = new_seq_lens ```` For example, if `new_seq_lens = [344, 16]` and `max_paddings = 256`, since `344 - 16 = 328 > 256`, so 344 and 16 cannot be composed here and can only forward wi...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: oject/vllm/commit/c1376e0f825e88e32b5aca85c676fe547bcb03c9) Test case: llama7B @ Nvidia A10 Test command: ```bash python3 benchmark_throughput.py \ --backend vllm \ --dataset ShareGPT_V3_unfiltered_cleaned_split.json \...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 3: 【Performance】throughput performance down due to the scheduler In https://github.com/vllm-project/vllm/commit/c1376e0f825e88e32b5aca85c676fe547bcb03c9, `num_tokens` is splited into `batch_size * seq_len`, this will cause...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: 【Performance】throughput performance down due to the scheduler In https://github.com/vllm-project/vllm/commit/c1376e0f825e88e32b5aca85c676fe547bcb03c9, `num_tokens` is splited into `batch_size * seq_len`, this will cause...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: vidia A10 Test command: ```bash python3 benchmark_throughput.py \ --backend vllm \ --dataset ShareGPT_V3_unfiltered_cleaned_split.json \ --model huggyllama/llama-7b \ --num-prompts 200 ``` Test result: * base(v0.2.1): T...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
