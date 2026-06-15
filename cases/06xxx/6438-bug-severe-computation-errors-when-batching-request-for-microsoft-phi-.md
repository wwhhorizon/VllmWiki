# vllm-project/vllm#6438: [Bug]: Severe computation errors when batching request for microsoft/Phi-3-mini-128k-instruct

| 字段 | 值 |
| --- | --- |
| Issue | [#6438](https://github.com/vllm-project/vllm/issues/6438) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 6; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | attention_kv_cache;frontend_api |
| 子分类 | race_cond |
| Operator 关键词 | attention |
| 症状 | mismatch |
| 根因提示 | env_dependency |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Severe computation errors when batching request for microsoft/Phi-3-mini-128k-instruct

### Issue 正文摘录

### Your current environment I'm not able to run `collect_env.py` on this workstation vllm == 0.5.1 vllm-flash-attn == 2.5.9 torch == 2.3.0 Tested on a single A100-80GB The following message was observed: ``` Cannot use flash attention-2 backend due to sliding window Using XFormers backend ``` ### 🐛 Describe the bug Issue: - Scenario 1: calling `LLM.generate` with `max_num_seqs=64`. - Scenario 2: sending requests to Vllm OpenAI compatible server with 50 concurrent calls For both scenarios, many responses do not make any sense. While some responses seemed perfectly reasonable, others contain an excessive amount of white spaces and repeated characters. I was not able to reproduce this using single calls in Scenario 2. With a single call to the sever, all responses seemed correct. My speculation is that the batching computation for Phi-3 is incorrect.

## 现有链接修复摘要

#8254 [Bugfix] Fix LongRoPE bug

## 候选优化模式

- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 2: n a single A100-80GB The following message was observed: ``` Cannot use flash attention-2 backend due to sliding window Using XFormers backend ``` ### 🐛 Describe the bug Issue: - Scenario 1: calling `LLM.generate` with...
- [Bitwise 确定性与数值等价](../patterns/bitwise_determinism_equivalence.md) - 分数 2: ssive amount of white spaces and repeated characters. I was not able to reproduce this using single calls in Scenario 2. With a single call to the sever, all responses seemed correct. My speculation is that the batching...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: llm == 0.5.1 vllm-flash-attn == 2.5.9 torch == 2.3.0 Tested on a single A100-80GB The following message was observed: ``` Cannot use flash attention-2 backend due to sliding window Using XFormers backend ``` ### 🐛 Descr...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: [Bug]: Severe computation errors when batching request for microsoft/Phi-3-mini-128k-instruct bug;stale ### Your current environment I'm not able to run `collect_env.py` on this workstation vllm == 0.5.1 vllm-flash-attn...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: rect. correctness attention_kv_cache;frontend_api attention mismatch env_dependency #8254 [Bugfix] Fix LongRoPE bug Your current environment

## 关联 PR 证据

| PR | 链接类型 | 置信度 | PR 标题 | 证据 |
| --- | --- | ---: | --- | --- |
| [#8254](https://github.com/vllm-project/vllm/pull/8254) | closes_keyword | 0.95 | [Bugfix] Fix LongRoPE bug | FIX #6438 Models tested before this PR: - microsoft/Phi-3.5-mini-instruct - microsoft/Phi-3-mini-4k-instruct - microsoft/Phi-3-small-8k-instruct - microsoft/Phi-3-small-12 |

## Wiki 抽取状态

- 后续迭代应在可用时读取完整讨论评论。
