# vllm-project/vllm#20138: [Bug]: Distributed Tests (4 GPUs) failing in main branch CI

| 字段 | 值 |
| --- | --- |
| Issue | [#20138](https://github.com/vllm-project/vllm/issues/20138) |
| 状态 | closed |
| 标签 | bug;ci-failure |
| 评论 | 7; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | ci_build;distributed_parallel |
| 子分类 | memory |
| Operator 关键词 | cuda |
| 症状 | oom |
| 根因提示 |  |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Distributed Tests (4 GPUs) failing in main branch CI

### Issue 正文摘录

This is now consistently failing with CUDA OOM: https://buildkite.com/vllm/ci/builds/22221#01977f3a-71ea-41cb-bbeb-a43340a10124 I narrowed this down to https://github.com/vllm-project/vllm/pull/19572 which appears to have introduced the issue.

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: [Bug]: Distributed Tests (4 GPUs) failing in main branch CI bug;ci-failure This is now consistently failing with CUDA OOM: https://buildkite.com/vllm/ci/builds/22221#01977f3a-71ea-41cb-bbeb-a43340a10124 I narrowed this...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: g in main branch CI bug;ci-failure This is now consistently failing with CUDA OOM: https://buildkite.com/vllm/ci/builds/22221#01977f3a-71ea-41cb-bbeb-a43340a10124 I narrowed this down to https://github.com/vllm-project/...
- [KV Cache 容量、压缩与 Offload](../patterns/kv_cache_capacity_offload.md) - 分数 1: main branch CI bug;ci-failure This is now consistently failing with CUDA OOM: https://buildkite.com/vllm/ci/builds/22221#01977f3a-71ea-41cb-bbeb-a43340a10124 I narrowed this down to https://github.com/vllm-project/vllm/...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: [Bug]: Distributed Tests (4 GPUs) failing in main branch CI bug;ci-failure This is now consistently failing with CUDA OOM: https://buildkite.com/vllm/ci/builds/22221#01977f3a-71ea-41cb-bbeb-a43340a10124 I narrowed this...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
