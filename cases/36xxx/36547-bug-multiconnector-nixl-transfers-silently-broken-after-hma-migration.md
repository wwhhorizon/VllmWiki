# vllm-project/vllm#36547: [Bug] MultiConnector: NIXL transfers silently broken after HMA migration

| 字段 | 值 |
| --- | --- |
| Issue | [#36547](https://github.com/vllm-project/vllm/issues/36547) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 0; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;frontend_api;gemm_linear;hardware_porting;model_support;sampling_logits;scheduler_memory;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cuda;operator;sampling;triton |
| 症状 | build_error;nan_inf |
| 根因提示 | env_dependency;memory_layout |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | True |

## 源证据

### Issue 标题

> [Bug] MultiConnector: NIXL transfers silently broken after HMA migration

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug ## Bug Description When using `MultiConnector(OffloadingConnector + NixlConnector)` in a P/D disaggregated setup, **NIXL remote KV transfers never occur**. The decode server falls back to local compute for all prompt tokens. The `external_kv_transfer` Prometheus metric is always 0. Output correctness is unaffected (`temperature=0` produces identical text regardless of source), so **the bug is invisible without metric validation**. ### Reproduction Set up a prefill server, decode server, and proxy, all using `MultiConnector(OffloadingConnector + NixlConnector)`. Send a request through the proxy and check the decode server's `vllm:prompt_tokens_by_source_total{source="external_kv_transfer"}` metric. It stays at 0. We validated with 3 tests: 1. **Proxy correctness**: Send a prompt through the proxy (prefill -> NIXL -> decode). Output matches `prefill_direct`. This passes because the bug is silent - decode recomputes everything locally and still gets the right answer. 2. **NIXL metric validation (the failing test)**: Send a fresh prompt through the proxy. The decode server has no cache, so NIXL should transfer all prompt tokens from...

## 现有链接修复摘要

#35758 [Core][KVConnector] Support HMA+NixlConnector

## 候选优化模式

- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 5: a P/D disaggregated setup, **NIXL remote KV transfers never occur**. The decode server falls back to local compute for all prompt tokens. The `external_kv_transfer` Prometheus metric is always 0. Output correctness is u...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: test/), which can answer lots of frequently asked questions. correctness ci_build;distributed_parallel;frontend_api;gemm_linear;hardware_porting;model_support;sampling_logits;scheduler_memory;speculative_decoding cuda;o...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: of scope: ### Option A: Add `request_finished` shim to `NixlConnector` Smallest diff. `NixlConnector` wraps single-group block IDs and delegates to its existing path. [`nixl_connector.py#L405-L411`](https://github.com/v...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 3: v_cache_groups) == 1 return self.connector.request_finished(request, block_ids[0]) return self.connector.request_finished_all_groups(request, block_ids) ``` **Without MultiConnector (works):** ``` Scheduler isinstance(N...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 2: shed`. `MultiConnector` does not implement `SupportsHMA`. The scheduler dispatches based on `SupportsHMA` ([scheduler.py#L1972-L1980](https://github.com/vllm-project/vllm/blob/c4e744d/vllm/v1/core/sched/scheduler.py#L19...

## 关联 PR 证据

| PR | 链接类型 | 置信度 | PR 标题 | 证据 |
| --- | --- | ---: | --- | --- |
| [#35758](https://github.com/vllm-project/vllm/pull/35758) | mentioned | 0.45 | [Core][KVConnector] Support HMA+NixlConnector | `. this became an issue after `nixlconnector` adopted `supportshma` (#35758). `multiconnector` was not updated to handle the new hma dispatch path. ## proposed fix three options,… |

## Wiki 抽取状态

- 后续迭代应在可用时读取完整讨论评论。
