# vllm-project/vllm#10230: [Feature]: The CPU backend supports mixture of experts (MoE)

| 字段 | 值 |
| --- | --- |
| Issue | [#10230](https://github.com/vllm-project/vllm/issues/10230) |
| 状态 | closed |
| 标签 | feature request;stale |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Feature]: The CPU backend supports mixture of experts (MoE)

### Issue 正文摘录

### 🚀 The feature, motivation and pitch With the advent of MoE models, it would be advantageous for vllm to support them with the CPU backend. Large MoE LLMs can have a significant memory footprint, beyond the capacity of many enthusiasts' GPUs but not beyond the capacity of their PCs. **Thank you for all the great work you do!** ### Alternatives I can't think of any alternatives. ### Additional context Running an MoE model fails when using CPU-only vllm (Built using git tag `v0.6.3.post1`): ``` pip show vllm | grep -i version Version: 0.6.3.post1+cpu ``` When running the following: ```bash VLLM_CPU_KVCACHE_SPACE=14 vllm serve Mixtral-8x22B-v0.1 --chat-template /mnt/work/demo-chess/llm/mixtral.jinja ``` Gives the following error when chat completion is attempted: ``` INFO: 127.0.0.1:50416 - "POST /v1/chat/completions HTTP/1.1" 200 OK INFO 11-11 11:42:38 engine.py:290] Added request chat-608977d2056b4fa3ab4b0b5b4489ded9. ERROR 11-11 11:42:38 engine.py:158] NotImplementedError('The CPU backend currently does not support MoE.') ``` ### Before submitting a new issue... - [X] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of...

## 候选优化模式

- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 2: [Feature]: The CPU backend supports mixture of experts (MoE) feature request;stale ### 🚀 The feature, motivation and pitch With the advent of MoE models, it would be advantageous for vllm to support them with the CPU ba...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: . Large MoE LLMs can have a significant memory footprint, beyond the capacity of many enthusiasts' GPUs but not beyond the capacity of their PCs. **Thank you for all the great work you do!** ### Alternatives I can't thi...
- [MoE、GEMM 与 Expert Routing](../patterns/moe_gemm_routing.md) - 分数 2: [Feature]: The CPU backend supports mixture of experts (MoE) feature request;stale ### 🚀 The feature, motivation and pitch With the advent of MoE models, it would be advantageous for vllm to support them with the CPU ba...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: [Feature]: The CPU backend supports mixture of experts (MoE) feature request;stale ### 🚀 The feature, motivation and pitch With the advent of MoE models, it would be advantageous for vllm to support them with the CPU ba...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: ``` ### Before submitting a new issue... - [X] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
