# vllm-project/vllm#29281: [Usage]: Removing last generated token from output and kv cache

| 字段 | 值 |
| --- | --- |
| Issue | [#29281](https://github.com/vllm-project/vllm/issues/29281) |
| 状态 | closed |
| 标签 | usage |
| 评论 | 0; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Usage]: Removing last generated token from output and kv cache

### Issue 正文摘录

### Your current environment ```text vLLM 0.11.2 ``` ### How would you like to use vllm Hey guys, i am currently working on a research project where i load a moe-like model and i want to do routing based on the sequence state. The goal is to let expert 0 generate until it reaches the eos token, then remove the eos token and finish generation with expert 1 until the eos token is hit a second time. I want to do this to use different strengths of both models. My current approach is to modify GPUModelRunner and Scheduler to remove the eos token from output, reduce num_computed_tokens by 1 and compute a static routing tensor based on the sequence state which i pass as additional model input, to route to expert 0 or 1. Now i am having some issues with unexpected output, especially with tensor_parallelism>1 on multiple gpus. I was wondering if there already is a reliable solution to remove the last generated token from output and kv cache, so that the computation leading to eos does not interfere with the second expert. Or maybe there is even a better way to do this? Thank you! ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the ch...

## 候选优化模式

- [MoE、GEMM 与 Expert Routing](../patterns/moe_gemm_routing.md) - 分数 3: Hey guys, i am currently working on a research project where i load a moe-like model and i want to do routing based on the sequence state. The goal is to let expert 0 generate until it reaches the eos token, then remove...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: w would you like to use vllm Hey guys, i am currently working on a research project where i load a moe-like model and i want to do routing based on the sequence state. The goal is to let expert 0 generate until it reach...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: ing on a research project where i load a moe-like model and i want to do routing based on the sequence state. The goal is to let expert 0 generate until it reaches the eos token, then remove the eos token and finish gen...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: expert 0 or 1. Now i am having some issues with unexpected output, especially with tensor_parallelism>1 on multiple gpus. I was wondering if there already is a reliable solution to remove the last generated token from o...
- [KV Cache 容量、压缩与 Offload](../patterns/kv_cache_capacity_offload.md) - 分数 1: [Usage]: Removing last generated token from output and kv cache usage ### Your current environment ```text vLLM 0.11.2 ``` ### How would you like to use vllm Hey guys, i am currently working on a research project where...

## Wiki 抽取状态

- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
