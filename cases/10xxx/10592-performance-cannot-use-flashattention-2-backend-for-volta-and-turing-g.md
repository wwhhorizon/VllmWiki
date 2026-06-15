# vllm-project/vllm#10592: [Performance]: Cannot use FlashAttention-2 backend for Volta and Turing GPUs.

| 字段 | 值 |
| --- | --- |
| Issue | [#10592](https://github.com/vllm-project/vllm/issues/10592) |
| 状态 | closed |
| 标签 | performance;stale |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | attention_kv_cache |
| 子分类 |  |
| Operator 关键词 | attention |
| 症状 |  |
| 根因提示 | env_dependency |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Performance]: Cannot use FlashAttention-2 backend for Volta and Turing GPUs.

### Issue 正文摘录

### Proposal to improve performance ![image](https://github.com/user-attachments/assets/c70acb43-596a-490c-8409-8e90d180d0fc) I would like to ask if I cannot use FlashAttention because my gpu is v100. ### Report of performance regression _No response_ ### Misc discussion on performance _No response_ ### Your current environment (if you think it is necessary) ```text The output of `python collect_env.py` ``` ### Before submitting a new issue... - [X] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 2: [Performance]: Cannot use FlashAttention-2 backend for Volta and Turing GPUs. performance;stale ### Proposal to improve performance ![image](https://github.com/user-attachments/assets/c70acb43-596a-490c-8409-8e90d180d0f...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 2: ot use FlashAttention because my gpu is v100. ### Report of performance regression _No response_ ### Misc discussion on performance _No response_ ### Your current environment (if you think it is necessary) ```text The o...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: frequently asked questions. performance attention_kv_cache attention env_dependency Proposal to improve performance
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: ``` ### Before submitting a new issue... - [X] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: nnot use FlashAttention-2 backend for Volta and Turing GPUs. performance;stale ### Proposal to improve performance ![image](https://github.com/user-attachments/assets/c70acb43-596a-490c-8409-8e90d180d0fc) I would like t...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
