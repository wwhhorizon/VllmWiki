# vllm-project/vllm#36463: [Bug]: Qwen3.5-27B fails to start with CPU KV cache offloading (`--kv_offloading_backend native`) while Qwen3-32B works fine

| 字段 | 值 |
| --- | --- |
| Issue | [#36463](https://github.com/vllm-project/vllm/issues/36463) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | attention_kv_cache;ci_build;distributed_parallel;frontend_api;gemm_linear;hardware_porting;model_support;speculative_decoding |
| 子分类 | cold_start |
| Operator 关键词 | attention;cache;cuda;operator;triton |
| 症状 | build_error;crash |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Qwen3.5-27B fails to start with CPU KV cache offloading (`--kv_offloading_backend native`) while Qwen3-32B works fine

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug ## Bug Description Qwen3.5-27B fails to start when CPU KV cache offloading is enabled via `--kv_offloading_backend native --kv_offloading_size 500`, while Qwen3-32B starts successfully with the exact same offloading configuration in the same environment. The error occurs during KV cache initialization with: ``` ValueError: Hybrid KV cache manager is disabled but failed to convert the KV cache specs to one unified type. ``` It appears that Qwen3.5-27B uses a hybrid attention architecture (likely mixing full attention and sliding window attention layers), and when `--disable-hybrid-kv-cache-manager` is set, the engine attempts to unify the KV cache specs into a single type but fails because the different attention types produce incompatible KV cache specs. This issue does not occur with Qwen3-32B, which uses a uniform attention architecture. The root cause seems to be in `vllm/v1/core/kv_cache_utils.py` at `unify_hybrid_kv_cache_specs()`, which cannot reconcile the different KV cache spec types when the hybrid KV cache manager is disabled **and** CPU offloading is enabled simultaneously. ## Expected Behavior Qwen3.5-27B should be a...

## 现有链接修复摘要

#36636 [Bugfix] Fix KV cache offloading for hybrid attention models (e.g. Qwen3.5-27B)

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 5: kv_cache_utils.py` at `unify_hybrid_kv_cache_specs()`, which cannot reconcile the different KV cache spec types when the hybrid KV cache manager is disabled **and** CPU offloading is enabled simultaneously. ## Expected...
- [KV Cache 容量、压缩与 Offload](../patterns/kv_cache_capacity_offload.md) - 分数 3: [Bug]: Qwen3.5-27B fails to start with CPU KV cache offloading (`--kv_offloading_backend native`) while Qwen3-32B works fine bug ### Your current environment ### 🐛 Describe the bug ## Bug Description Qwen3.5-27B fails t...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: [Bug]: Qwen3.5-27B fails to start with CPU KV cache offloading (`--kv_offloading_backend native`) while Qwen3-32B works fine bug ### Your current environment ### 🐛 Describe the bug ## Bug Description Qwen3.5-27B fails to
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 2: wen3.5-27B fails to start with CPU KV cache offloading (`--kv_offloading_backend native`) while Qwen3-32B works fine bug ### Your current environment ### 🐛 Describe the bug ## Bug Description Qwen3.5-27B fails to start...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: e unified type. ``` It appears that Qwen3.5-27B uses a hybrid attention architecture (likely mixing full attention and sliding window attention layers), and when `--disable-hybrid-kv-cache-manager` is set, the engine at...

## 关联 PR 证据

| PR | 链接类型 | 置信度 | PR 标题 | 证据 |
| --- | --- | ---: | --- | --- |
| [#36636](https://github.com/vllm-project/vllm/pull/36636) | closes_keyword | 0.95 | [Bugfix] Fix KV cache offloading for hybrid attention models (e.g. Qwen3.5-27B) | Fix #36463: Qwen3.5-27B fails to start with CPU KV cache offloading (`--kv_offloading_backend native`) while Qwen3-32B works fine. The root cause is that KV offloading auto-disabl |

## Wiki 抽取状态

- 后续迭代应在可用时读取完整讨论评论。
