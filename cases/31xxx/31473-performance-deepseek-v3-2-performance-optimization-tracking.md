# vllm-project/vllm#31473: [Performance]: DeepSeek-V3.2 Performance Optimization Tracking

| 字段 | 值 |
| --- | --- |
| Issue | [#31473](https://github.com/vllm-project/vllm/issues/31473) |
| 状态 | open |
| 标签 | performance |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | attention_kv_cache;distributed_parallel;hardware_porting;quantization;sampling_logits |
| 子分类 |  |
| Operator 关键词 | attention;cuda;fp8;kernel;sampling |
| 症状 |  |
| 根因提示 | dtype;shape |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Performance]: DeepSeek-V3.2 Performance Optimization Tracking

### Issue 正文摘录

## Overview This issue tracks performance optimization efforts for **DeepSeek-V3.2** (`deepseek-ai/DeepSeek-V3.2-Exp`) inference in vLLM. ## Optimization Areas ### 1. General - [ ] Indexer overlap (multistream cuda): https://github.com/vllm-project/vllm/issues/35226 ### 2. Prefill Perf - [ ] Support TP without padding — update kernel to support head counts of 16 and remove [padding logic](https://github.com/vllm-project/vllm/blob/b9793e6a8c30bc42f35d2a1eac919284aea27f76/vllm/v1/attention/backends/mla/flashmla_sparse.py#L928-L938) - [ ] Support PCP - [ ] Optimize top-k - [ ] Optimize concat: https://github.com/vllm-project/vllm/pull/34917 - [ ] Gather and upconvert: https://github.com/vllm-project/vllm/pull/35290 #### FP8 KV-Cache Specific - [X] Use sparse prefill kernel, https://github.com/vllm-project/vllm/pull/27532 - [ ] Use prefill kernels for TP (once kernels support it) — [remove mixed batch mode fallback](https://github.com/vllm-project/vllm/blob/b9793e6a8c30bc42f35d2a1eac919284aea27f76/vllm/v1/attention/backends/mla/flashmla_sparse.py#L46-L56) ### 3. Short-Context Prefill Perf **Issue**: We currently use the absorbed approach (data-movement friendly MQA) for prefill instea...

## 现有链接修复摘要

#35474 [Perf][DeepSeek-V3] Dynamic MLA/MHA Routing for Sub-1024 Token Prefill (~3x TTFT Speedup)

## 候选优化模式

- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 4: ect/vllm/blob/b9793e6a8c30bc42f35d2a1eac919284aea27f76/vllm/v1/attention/backends/mla/flashmla_sparse.py#L928-L938) - [ ] Support PCP - [ ] Optimize top-k - [ ] Optimize concat: https://github.com/vllm-project/vllm/pull...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 4: her and upconvert: https://github.com/vllm-project/vllm/pull/35290 #### FP8 KV-Cache Specific - [X] Use sparse prefill kernel, https://github.com/vllm-project/vllm/pull/27532 - [ ] Use prefill kernels for TP (once kerne...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 4: ## Optimization Areas ### 1. General - [ ] Indexer overlap (multistream cuda): https://github.com/vllm-project/vllm/issues/35226 ### 2. Prefill Perf - [ ] Support TP without padding — update kernel to support head count...
- [MoE、GEMM 与 Expert Routing](../patterns/moe_gemm_routing.md) - 分数 3: kends/mla/flashmla_sparse.py#L928-L938) - [ ] Support PCP - [ ] Optimize top-k - [ ] Optimize concat: https://github.com/vllm-project/vllm/pull/34917 - [ ] Gather and upconvert: https://github.com/vllm-project/vllm/pull...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 3: istream cuda): https://github.com/vllm-project/vllm/issues/35226 ### 2. Prefill Perf - [ ] Support TP without padding — update kernel to support head counts of 16 and remove [padding logic](https://github.com/vllm-proje...

## 关联 PR 证据

| PR | 链接类型 | 置信度 | PR 标题 | 证据 |
| --- | --- | ---: | --- | --- |
| [#35474](https://github.com/vllm-project/vllm/pull/35474) | closes_keyword | 0.95 | [Perf][DeepSeek-V3] Dynamic MLA/MHA Routing for Sub-1024 Token Prefill (~3x TTFT Speedup) | Closes #31473 |

## Wiki 抽取状态

- 后续迭代应在可用时读取完整讨论评论。
