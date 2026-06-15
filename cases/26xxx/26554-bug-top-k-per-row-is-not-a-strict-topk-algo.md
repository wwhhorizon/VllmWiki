# vllm-project/vllm#26554: [Bug]: top_k_per_row is not a strict Topk Algo

| 字段 | 值 |
| --- | --- |
| Issue | [#26554](https://github.com/vllm-project/vllm/issues/26554) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 6; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: top_k_per_row is not a strict Topk Algo

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug Hi @dcampora ,I just read your `topk_per_row` kernel, and I have some questions here. In first pass, you extract each fp32 element's first 9 bit to scatter into different histogram bin. then, the final pass element is 3072, you will read up to 3072 elements if the bit equals to the threasholdbinIdx. And do FinalPassSort and TopkSort. My question is, if we have 10000 elements which first 9bit is equal, it will only read first 3072 elements to do TopK, and it is not a strict global topk algorithem?... ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: .. ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), whi...
- [MoE、GEMM 与 Expert Routing](../patterns/moe_gemm_routing.md) - 分数 1: [Bug]: top_k_per_row is not a strict Topk Algo bug ### Your current environment ### 🐛 Describe the bug Hi @dcampora ,I just read your `topk_per_row` kernel, and I have some questions here. In first pass, you extract eac...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
