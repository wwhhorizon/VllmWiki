# vllm-project/vllm#1550: [Benchmark] Bottleneck of vLLM as of 2023 11 02

| 字段 | 值 |
| --- | --- |
| Issue | [#1550](https://github.com/vllm-project/vllm/issues/1550) |
| 状态 | closed |
| 标签 |  |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Benchmark] Bottleneck of vLLM as of 2023 11 02

### Issue 正文摘录

I use ```py-spy``` to profile the pid of process when running the `benchmark/benchmark_throughput.py` on 4 GPUs with llama-2-70b-chat model. The first most time spent on ```torch.repeat_interleave``` which lies in the ```multi_query_kv_attention``` as discuss in issue https://github.com/pytorch/pytorch/issues/31980. The following 4 graphs shows the function call duration on 4 GPUs. ![profile_70b_0](https://github.com/vllm-project/vllm/assets/29171856/7c7b4101-d10d-43d6-8f7a-e6937eb8029b) ![profile_70b_1](https://github.com/vllm-project/vllm/assets/29171856/824c8515-a9a6-427c-ab64-87fb328af293) ![profile_70b_2](https://github.com/vllm-project/vllm/assets/29171856/cd0d8c57-acac-457f-a7d6-d0cfe0141871) ![profile_70b_3](https://github.com/vllm-project/vllm/assets/29171856/2e336059-a690-4595-a947-a3ba4c5fba8c) The second bottleneck is the ```_prune_hidden_state``` function. Hope that this could provide some insights to move forward in optimizing the framework. [Update] There seems to have some PR going on in pytorch (https://github.com/pytorch/pytorch/pull/51869) but it seems that it was not merged.

## 候选优化模式

- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 3: [Benchmark] Bottleneck of vLLM as of 2023 11 02 I use ```py-spy``` to profile the pid of process when running the `benchmark/benchmark_throughput.py` on 4 GPUs with llama-2-70b-chat model. The first most time spent on ``
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: cess when running the `benchmark/benchmark_throughput.py` on 4 GPUs with llama-2-70b-chat model. The first most time spent on ```torch.repeat_interleave``` which lies in the ```multi_query_kv_attention``` as discuss in...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
