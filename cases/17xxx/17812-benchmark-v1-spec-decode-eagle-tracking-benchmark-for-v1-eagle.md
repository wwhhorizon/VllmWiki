# vllm-project/vllm#17812: [Benchmark][V1][Spec Decode][EAGLE] Tracking benchmark for V1 EAGLE

| 字段 | 值 |
| --- | --- |
| Issue | [#17812](https://github.com/vllm-project/vllm/issues/17812) |
| 状态 | closed |
| 标签 | performance;stale |
| 评论 | 6; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | attention_kv_cache;ci_build;frontend_api;model_support;speculative_decoding |
| 子分类 |  |
| Operator 关键词 | cache;cuda;gemm |
| 症状 | build_error |
| 根因提示 | env_dependency |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Benchmark][V1][Spec Decode][EAGLE] Tracking benchmark for V1 EAGLE

### Issue 正文摘录

We have been doing perf bench on MTBench so that e2e speedup and AL are comparable with other setups and academic papers. Thanks to @luyuzhe111 and others for the discussion and helping with measuring the gaps! ## llama 3 8b During model wt loading * https://github.com/vllm-project/vllm/pull/16035#issuecomment-2790985075 * SGL correction: https://github.com/vllm-project/vllm/pull/16035#issuecomment-2803265232 * SGL setup: https://docs.google.com/document/d/18ETJLsnxR88Qq3VDk5Mq-Hb7vuE9o3VNZ-hhz-OqAXk/edit?usp=sharing * https://github.com/vllm-project/vllm/pull/16035#issuecomment-2791642158 During KV Cache slot * https://github.com/vllm-project/vllm/pull/16370#issuecomment-2802319168 ## llama 3.1 8b * https://github.com/vllm-project/vllm/pull/16370#issuecomment-2810446121 * EAGLE - 1/3 * offline serving: * https://github.com/vllm-project/vllm/pull/16937#issuecomment-2828889840 * E1 Spec Bench AL: https://github.com/vllm-project/vllm/pull/23563 * online serving: * https://github.com/vllm-project/vllm/pull/17202#issue-3020819496 * https://github.com/vllm-project/vllm/pull/25916 - using chat endpoint correctly * ngram-eagle: https://github.com/vllm-project/vllm/pull/24344 torch compil...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: ly * ngram-eagle: https://github.com/vllm-project/vllm/pull/24344 torch compile & CUDA graph: * EAGLE 1 * https://github.com/vllm-project/vllm/pull/17211#issuecomment-2837880435 * https://github.com/vllm-project/vllm/pu...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 4: [Benchmark][V1][Spec Decode][EAGLE] Tracking benchmark for V1 EAGLE performance;stale We have been doing perf bench on MTBench so that e2e speedup and AL are comparable with other setups and academic papers. Thanks to @...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: and others for the discussion and helping with measuring the gaps! ## llama 3 8b During model wt loading * https://github.com/vllm-project/vllm/pull/16035#issuecomment-2790985075 * SGL correction: https://github.com/vll...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: -eagle: https://github.com/vllm-project/vllm/pull/24344 torch compile & CUDA graph: * EAGLE 1 * https://github.com/vllm-project/vllm/pull/17211#issuecomment-2837880435 * https://github.com/vllm-project/vllm/pull/17211#i...
- [KV Cache 容量、压缩与 Offload](../patterns/kv_cache_capacity_offload.md) - 分数 1: /github.com/vllm-project/vllm/pull/16035#issuecomment-2791642158 During KV Cache slot * https://github.com/vllm-project/vllm/pull/16370#issuecomment-2802319168 ## llama 3.1 8b * https://github.com/vllm-project/vllm/pull...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
