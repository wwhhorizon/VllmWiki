# vllm-project/vllm#19697: [Bug]: Truncated && Incomplete Response from LLAMA4 Scout Prefix Caching

| 字段 | 值 |
| --- | --- |
| Issue | [#19697](https://github.com/vllm-project/vllm/issues/19697) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 5; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cuda;operator;sampling;triton |
| 症状 | build_error;nan_inf;slowdown |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Truncated && Incomplete Response from LLAMA4 Scout Prefix Caching

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug Model: LLAMA4 Scout Vllm Version: 0.9.1 V1 with Chunked Prefil and Prefix Caching Problem: I am running the same request (huge system prompt of 42k tokens + small instruction prompt) iteratively towards the same model endpoint. Occasionally, the response returned seems truncated and incomplete: ``` -------------------------------------------------- Iteration 1: E2E latency = 2.7865 seconds Iteration 2: E2E latency = 2.7842 seconds Iteration 3: E2E latency = 2.7867 seconds Iteration 4: E2E latency = 0.5738 seconds named Zeta who wants to try a new recipe. Iteration 5: E2E latency = 0.5911 seconds named Zeta. Zeta's goal is to create the perfect dish. Iteration 6: E2E latency = 2.7840 seconds Iteration 7: E2E latency = 2.7771 seconds Iteration 8: E2E latency = 2.7863 seconds Iteration 9: E2E latency = 2.7848 seconds Iteration 10: E2E latency = 2.7926 seconds ``` The following is the comparison with normal responses, check Iteration 1 2 4 against 3. ``` Iteration 1: E2E latency = 2.7820 seconds who had to make a cake for a customer who was a famous chef. ## The Cake Conundrum In the bustling kitchen of a high-end restaurant, a cooki...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 6: current environment ### 🐛 Describe the bug Model: LLAMA4 Scout Vllm Version: 0.9.1 V1 with Chunked Prefil and Prefix Caching Problem: I am running the same request (huge system prompt of 42k tokens + small instruction p...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: oblem: I am running the same request (huge system prompt of 42k tokens + small instruction prompt) iteratively towards the same model endpoint. Occasionally, the response returned seems truncated and incomplete: ``` ---...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 3: ]: Truncated && Incomplete Response from LLAMA4 Scout Prefix Caching bug;stale ### Your current environment ### 🐛 Describe the bug Model: LLAMA4 Scout Vllm Version: 0.9.1 V1 with Chunked Prefil and Prefix Caching Proble...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: [Bug]: Truncated && Incomplete Response from LLAMA4 Scout Prefix Caching bug;stale ### Your current environment ### 🐛 Describe the bug Model: LLAMA4 Scout Vllm Version: 0.9.1 V1 with Chunked Prefil and Prefix Caching Pr...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 2: ``` -------------------------------------------------- Iteration 1: E2E latency = 2.7865 seconds Iteration 2: E2E latency = 2.7842 seconds Iteration 3: E2E latency = 2.7867 seconds Iteration 4: E2E latency = 0.5738 seco...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
