# vllm-project/vllm#36917: [Bug]: GDN attention backend crashes with mixed decode/spec_decode batch when serving Qwen3.5 family models with MTP

| 字段 | 值 |
| --- | --- |
| Issue | [#36917](https://github.com/vllm-project/vllm/issues/36917) |
| 状态 | open |
| 标签 | bug |
| 评论 | 8; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | development |
| 工作域 | attention_kv_cache;ci_build;distributed_parallel;frontend_api;model_support;scheduler_memory;speculative_decoding |
| 子分类 | env_compat |
| Operator 关键词 | attention |
| 症状 | build_error;crash |
| 根因提示 | dtype;env_dependency;shape |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: GDN attention backend crashes with mixed decode/spec_decode batch when serving Qwen3.5 family models with MTP

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug ## (if it helps) Environment where we first spotted the bug - **vLLM version**: `v0.17.0rc1.dev164+gfff3711a2` - **GPU**: NVIDIA B200 (DGX B200) - **Model**: `Qwen/Qwen3.5-397B-A17B` - **TP**: 8 - **Docker**: yes (container `wsd-qwen3.5-397b-a17b-vllm`) - **OS**: Linux When serving `Qwen3.5-397B-A17B` with the recommended MTP speculative decoding config from vLLM recipes (`num_speculative_tokens=1`), the GDN attention backend crashes with a fatal `AssertionError` during concurrent request serving. The engine dies and all in-flight requests fail with `EngineDeadError`. I could reproduce this on my DGX spark and smaller models from the Qwen3.5 family. (see gist) ### Root cause The assertion at `vllm/v1/attention/backends/gdn_attn.py:310` fails: ```python assert not (num_decodes > 0 and num_spec_decodes > 0), ( f"num_decodes: {num_decodes}, num_spec_decodes: {num_spec_decodes}" ) ``` The GDN attention backend does not support mixed batches containing both regular decode tokens and speculative decode tokens. However, the V1 scheduler produces exactly this kind of heterogeneous batch under certain conditions. ### How to trigger The cr...

## 现有链接修复摘要

#36918 [Bugfix][Core] Fix gdn kernel mixed batch spec decode crash

## 候选优化模式

- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 6: [Bug]: GDN attention backend crashes with mixed decode/spec_decode batch when serving Qwen3.5 family models with MTP bug ### Your current environment ### 🐛 Describe the bug ## (if it helps) Environment where we first sp...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 5: g ## (if it helps) Environment where we first spotted the bug - **vLLM version**: `v0.17.0rc1.dev164+gfff3711a2` - **GPU**: NVIDIA B200 (DGX B200) - **Model**: `Qwen/Qwen3.5-397B-A17B` - **TP**: 8 - **Docker**: yes (con...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 4: ug - **vLLM version**: `v0.17.0rc1.dev164+gfff3711a2` - **GPU**: NVIDIA B200 (DGX B200) - **Model**: `Qwen/Qwen3.5-397B-A17B` - **TP**: 8 - **Docker**: yes (container `wsd-qwen3.5-397b-a17b-vllm`) - **OS**: Linux When s...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 3: e_config=SpeculativeConfig(method='mtp', model='...', num_spec_tokens=1) dtype=torch.bfloat16 max_seq_len=262144 tensor_parallel_size=8 enable_chunked_prefill=True enable_prefix_caching=False ``` ## Full stack trace ```...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: tention backend crashes with mixed decode/spec_decode batch when serving Qwen3.5 family models with MTP bug ### Your current environment ### 🐛 Describe the bug ## (if it helps) Environment where we first spotted the bug...

## 关联 PR 证据

| PR | 链接类型 | 置信度 | PR 标题 | 证据 |
| --- | --- | ---: | --- | --- |
| [#36918](https://github.com/vllm-project/vllm/pull/36918) | closes_keyword | 0.95 | [Bugfix][Core] Fix gdn kernel mixed batch spec decode crash  | Fix GDN attention backend crash with mixed decode/spec_decode batch (this address the following issue #36917). The V1 scheduler can produce batches containing both regular decode |

## Wiki 抽取状态

- 后续迭代应在可用时读取完整讨论评论。
