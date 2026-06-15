# vllm-project/vllm#35254: [Performance]: curious new kernels from vllm 0.11.1

| 字段 | 值 |
| --- | --- |
| Issue | [#35254](https://github.com/vllm-project/vllm/issues/35254) |
| 状态 | open |
| 标签 | performance;stale |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | gemm_linear |
| 子分类 |  |
| Operator 关键词 | cuda;gemm;kernel |
| 症状 |  |
| 根因提示 | env_dependency |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Performance]: curious new kernels from vllm 0.11.1

### Issue 正文摘录

### Proposal to improve performance _No response_ ### Report of performance regression _No response_ ### Misc discussion on performance As described in these forum questions: https://discuss.vllm.ai/t/significant-speedup-observed-with-long-common-prefix-between-v0-11-0-and-v0-12-0/2379 https://discuss.vllm.ai/t/true-eager-backend/2396 **I observed that after upgrading from vllm 0.11.0 to 0.11.1, one observes a 4+ times performance gain on lightweight requests.** After some careful torch profiling, the stats for v0.11.1 (even in eager mode) looks like this: ``` ------------------------------------------------------- ------------ ------------ ------------ ------------ ------------ ------------ ------------ ------------ ------------ ------------ Name Self CPU % Self CPU CPU total % CPU total CPU time avg Self CUDA Self CUDA % CUDA total CUDA time avg # of Calls ------------------------------------------------------- ------------ ------------ ------------ ------------ ------------ ------------ ------------ ------------ ------------ ------------ aten::mm 8.09% 438.644ms 11.59% 628.257ms 32.334us 1.896s 79.66% 1.900s 97.775us 19430 execute_new_0_cached_80 0.00% 0.000us 0.00% 0.000us 0.0...

## 候选优化模式

- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: f CPU % Self CPU CPU total % CPU total CPU time avg Self CUDA Self CUDA % CUDA total CUDA time avg # of Calls ------------------------------------------------------- ------------ ------------ ------------ ------------ -...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 3: roposal to improve performance _No response_ ### Report of performance regression _No response_ ### Misc discussion on performance As described in these forum questions: https://discuss.vllm.ai/t/significant-speedup-obs...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 2: ix-between-v0-11-0-and-v0-12-0/2379 https://discuss.vllm.ai/t/true-eager-backend/2396 **I observed that after upgrading from vllm 0.11.0 to 0.11.1, one observes a 4+ times performance gain on lightweight requests.** Aft...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: [Performance]: curious new kernels from vllm 0.11.1 performance;stale ### Proposal to improve performance _No response_ ### Report of performance regression _No response_ ### Misc discussion on performance As described...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: frequently asked questions. performance gemm_linear cuda;gemm;kernel env_dependency Proposal to improve performance

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
