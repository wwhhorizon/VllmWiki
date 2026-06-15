# vllm-project/vllm#43450: [Performance]: V1 sample_tokens p99 can include sampled-output readiness; moving the wait to get_output did not improve serving throughput in my setup

| 字段 | 值 |
| --- | --- |
| Issue | [#43450](https://github.com/vllm-project/vllm/issues/43450) |
| 状态 | open |
| 标签 | performance |
| 评论 | 0; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | ci_build;frontend_api;hardware_porting;model_support;sampling_logits;scheduler_memory |
| 子分类 | throughput |
| Operator 关键词 | cuda;operator;sampling |
| 症状 | build_error;slowdown |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | True |

## 源证据

### Issue 标题

> [Performance]: V1 sample_tokens p99 can include sampled-output readiness; moving the wait to get_output did not improve serving throughput in my setup

### Issue 正文摘录

### Proposal to improve performance I am not proposing an immediate performance patch or claiming a serving throughput win. This issue is a profiling/attribution discussion: in my setup, V1 `sample_tokens` p99 appears to include sampled-output readiness/event-sync work. A comparison path moves the visible wait out of `sample_tokens` and into `AsyncModelRunnerOutput.get_output()`, but steady-state serving throughput did not improve. The possible future direction, if maintainers think this matters, would be to clarify ownership of sampled-output readiness and avoid interpreting a lower `sample_tokens` p99 as a serving-level win unless `get_output`, ITL, and steady-state throughput are measured too. ### Report of performance regression This is not a regression claim. I am not claiming that vLLM `0.21.0` regressed versus a previous release, and I am not claiming that the comparison path improves current serving performance. The evidence below is about where sampled-output readiness appears in profiler timings. ### Misc discussion on performance ## Summary I found a reproducible V1 profiling-attribution issue on vLLM `0.21.0`: in my setup, `sample_tokens` p99 appears to include a sampl...

## 现有链接修复摘要

#22760 [Disagg][Perf] Use CUDA event sync instead of blocking `tolist` to avoid unintentional copy ops blocking across different CUDA strea…

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 7: mings. ### Misc discussion on performance ## Summary I found a reproducible V1 profiling-attribution issue on vLLM `0.21.0`: in my setup, `sample_tokens` p99 appears to include a sampled-output readiness/event-sync wait...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 6: direction, if maintainers think this matters, would be to clarify ownership of sampled-output readiness and avoid interpreting a lower `sample_tokens` p99 as a serving-level win unless `get_output`, ITL, and steady-stat...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 5: -output readiness; moving the wait to get_output did not improve serving throughput in my setup performance ### Proposal to improve performance I am not proposing an immediate performance patch or claiming a serving thr...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: arison path moves the visible wait out of `sample_tokens` and into `AsyncModelRunnerOutput.get_output()`, but steady-state serving throughput did not improve. The possible future direction, if maintainers think this mat...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 3: ken counts and logprob counts matched in all reported rows. - Continuous decode throughput and streaming ITL did not improve in this setup. Caveat: `VLLM_USE_V2_MODEL_RUNNER=1` is not a minimal one-line readiness-split...

## 关联 PR 证据

| PR | 链接类型 | 置信度 | PR 标题 | 证据 |
| --- | --- | ---: | --- | --- |
| [#22760](https://github.com/vllm-project/vllm/pull/22760) | mentioned | 0.45 | [Disagg][Perf] Use CUDA event sync instead of blocking `tolist` to avoid unintentional copy ops blocking across different CUDA streams, improving disagg TTIT/TTFT | iness and blocking behavior around `sampled_token_ids.tolist()`, with #22760 listed there as the event-sync/non-blocking-copy mitigation. this issue is adjacent but narrower: it i… |

## Wiki 抽取状态

- 后续迭代应在可用时读取完整讨论评论。
