# vllm-project/vllm#28224: [Bug]: DP with non-MoE models hangs

| 字段 | 值 |
| --- | --- |
| Issue | [#28224](https://github.com/vllm-project/vllm/issues/28224) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: DP with non-MoE models hangs

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug Starting up a vllm server with DP2 and a non-MoE model such as: ```python vllm serve meta-llama/Meta-Llama-3-8B-Instruct -dp 2 ``` and running lm eval such as: ```python lm_eval --model local-chat-completions --model_args base_url=http://localhost:8000/v1/chat/completions,model=meta-llama/Meta-Llama-3-8B-Instruct,num_concurrent=128,tokenized_requests=False --tasks gsm8k --apply_chat_template ``` leads to a hang at approximately 95% requests processed, at which point one of the ranks has 0 remaining requests, starts executing dummy batches, and gets out of sync. This causes hangs in the allreduce of `coordinate_batch_across_dp`. ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: Llama-3-8B-Instruct,num_concurrent=128,tokenized_requests=False --tasks gsm8k --apply_chat_template ``` leads to a hang at approximately 95% requests processed, at which point one of the ranks has 0 remaining requests,...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: [Bug]: DP with non-MoE models hangs bug ### Your current environment ### 🐛 Describe the bug Starting up a vllm server with DP2 and a non-MoE model such as: ```python vllm serve meta-llama/Meta-Llama-3-8B-Instruct -dp 2...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 2: vllm serve meta-llama/Meta-Llama-3-8B-Instruct -dp 2 ``` and running lm eval such as: ```python lm_eval --model local-chat-completions --model_args base_url=http://localhost:8000/v1/chat/completions,model=meta-llama/Met...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 1: a-llama/Meta-Llama-3-8B-Instruct,num_concurrent=128,tokenized_requests=False --tasks gsm8k --apply_chat_template ``` leads to a hang at approximately 95% requests processed, at which point one of the ranks has 0 remaini...
- [MoE、GEMM 与 Expert Routing](../patterns/moe_gemm_routing.md) - 分数 1: [Bug]: DP with non-MoE models hangs bug ### Your current environment ### 🐛 Describe the bug Starting up a vllm server with DP2 and a non-MoE model such as: ```python vllm serve meta-llama/Meta-Llama-3-8B-Instruct -dp 2...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
