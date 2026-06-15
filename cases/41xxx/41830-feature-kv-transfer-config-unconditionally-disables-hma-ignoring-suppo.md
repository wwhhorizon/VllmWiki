# vllm-project/vllm#41830: [Feature]: --kv-transfer-config unconditionally disables HMA, ignoring SupportsHMA on the connector

| 字段 | 值 |
| --- | --- |
| Issue | [#41830](https://github.com/vllm-project/vllm/issues/41830) |
| 状态 | closed |
| 标签 |  |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | attention_kv_cache;distributed_parallel;frontend_api;hardware_porting;model_support;quantization |
| 子分类 | memory |
| Operator 关键词 | attention;cache;fp8 |
| 症状 | crash;oom |
| 根因提示 | dtype;env_dependency;memory_layout;race_condition;shape |
| 硬件范围 | nvidia |
| 需要人工复核 | True |

## 源证据

### Issue 标题

> [Feature]: --kv-transfer-config unconditionally disables HMA, ignoring SupportsHMA on the connector

### Issue 正文摘录

## Bug `vllm/config/vllm.py:1292-1306` unconditionally disables the Hybrid KV cache Manager (HMA) whenever `--kv-transfer-config` is set, regardless of whether the connector subclasses `SupportsHMA`. For hybrid models (sliding-window, chunked-local, Mamba), HMA is what allocates per-group KV pools sized to each layer type's actual needs. With HMA disabled, `unify_hybrid_kv_cache_specs` (`vllm/v1/core/kv_cache_utils.py:1334`) collapses all sliding-window / chunked-local specs into `FullAttentionSpec`, ballooning per-request KV memory and OOMing the engine at startup. ## Reproduction DeepSeek-V4-Flash, 2× RTX PRO 6000 Blackwell, TP=2: ```yaml - --kv-transfer-config={"kv_connector":"SimpleCPUOffloadConnector","kv_role":"kv_both","kv_connector_extra_config":{"cpu_bytes_to_use":137438953472}} - --enable-prefix-caching --enable-chunked-prefill - --max-model-len=128000 --tensor-parallel-size=2 - --kv-cache-dtype=fp8 --block-size=256 ``` Result: ``` WARNING [config.py:1297] Turning off hybrid kv cache manager because `--kv-transfer-config` is set... WARNING [kv_cache_utils.py:1334] Hybrid KV cache manager is disabled for this hybrid model... ValueError: To serve at least one request with...

## 现有链接修复摘要

#29805 [Misc][Hybrid allocator + kv connector] Optionally enable hybrid allocator + KV cache connector | #39269 fix: allow HMA with KV events when explicitly enabled | #41847 [KV Transfer] Enable HMA by default for connectors that support it

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: s not None: # NOTE(Kuntai): turn HMA off for connector unless specifically enabled. need_disable_hybrid_kv_cache_manager = True logger.warning(...) ``` This disables HMA for *every* connector, even ones that subclass `S...
- [KV Cache 容量、压缩与 Offload](../patterns/kv_cache_capacity_offload.md) - 分数 4: Bug `vllm/config/vllm.py:1292-1306` unconditionally disables the Hybrid KV cache Manager (HMA) whenever `--kv-transfer-config` is set, regardless of whether the connector subclasses `SupportsHMA`. For hybrid models (sli...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 3: d-prefill - --max-model-len=128000 --tensor-parallel-size=2 - --kv-cache-dtype=fp8 --block-size=256 ``` Result: ``` WARNING [config.py:1297] Turning off hybrid kv cache manager because `--kv-transfer-config` is set... W...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: nd OOMing the engine at startup. ## Reproduction DeepSeek-V4-Flash, 2× RTX PRO 6000 Blackwell, TP=2: ```yaml - --kv-transfer-config={"kv_connector":"SimpleCPUOffloadConnector","kv_role":"kv_both","kv_connector_extra_con...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: [Feature]: --kv-transfer-config unconditionally disables HMA, ignoring SupportsHMA on the connector ## Bug `vllm/config/vllm.py:1292-1306` unconditionally disables the Hybrid KV cache Manager (HMA) whenever `--kv-transf...

## 关联 PR 证据

| PR | 链接类型 | 置信度 | PR 标题 | 证据 |
| --- | --- | ---: | --- | --- |
| [#29805](https://github.com/vllm-project/vllm/pull/29805) | mentioned | 0.45 | [Misc][Hybrid allocator + kv connector] Optionally enable hybrid allocator + KV cache connector | ed silently, and that a specific opt-in flag fixes it. ## related - #29805 — the pr that introduced the current unconditional auto-disable + the manual override flag (cc @nicklucc… |
| [#39269](https://github.com/vllm-project/vllm/pull/39269) | mentioned | 0.45 | fix: allow HMA with KV events when explicitly enabled | nditional auto-disable + the manual override flag (cc @nicklucche). - #39269 — open pr addressing the analogous bug in the `kv_events_config` branch (lines 1226-1228), with a diff… |
| [#41847](https://github.com/vllm-project/vllm/pull/41847) | closes_keyword | 0.95 | [KV Transfer] Enable HMA by default for connectors that support it | Close #41830 — change HMA from opt-in to opt-out for KV transfer connectors. Previously, `--kv-transfer-config` unconditionally disabled the Hybrid KV Cache Manager (HMA), requi |

## Wiki 抽取状态

- 后续迭代应在可用时读取完整讨论评论。
