# vllm-project/vllm#42966: [Bug]: vllm:cache_config_info reports stale block_size=16 for hybrid Mamba models

| 字段 | 值 |
| --- | --- |
| Issue | [#42966](https://github.com/vllm-project/vllm/issues/42966) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | attention_kv_cache;ci_build;distributed_parallel;frontend_api;gemm_linear;hardware_porting;model_support;sampling_logits;speculative_decoding |
| 子分类 | race_cond |
| Operator 关键词 | attention;cuda;operator;sampling;triton |
| 症状 | build_error;nan_inf |
| 根因提示 | env_dependency;memory_layout |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: vllm:cache_config_info reports stale block_size=16 for hybrid Mamba models

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug ## Description When serving hybrid Mamba models (e.g. `Qwen/Qwen3.6-35B-A3B`, architecture `Qwen3_5MoeForConditionalGeneration`), `_align_hybrid_block_size()` correctly enlarges `block_size` in the worker process (e.g. to 528 or 1056 tokens) to ensure the attention page size is >= the Mamba page size. However, this updated value is never synced back to the parent APIServer process, so the Prometheus metric `vllm:cache_config_info` reports the stale default `block_size=16`. ## Reproduction Running an Hybrid model, for example: `vllm serve Qwen/Qwen3.6-35B-A3B --tensor-parallel-size 4` Startup log shows: > [interface.py:645] Setting attention block size to 528 tokens to ensure that attention page size is >= mamba page size. But when I do `curl http://localhost:8000/metrics` I see: > vllm:cache_config_info{block_size="16", ...} ## Root cause `EngineCoreReadyResponse` (vllm/v1/engine/__init__.py) is used to sync post-initialization state from the EngineCore subprocess back to the frontend. It syncs `max_model_len` and `num_gpu_blocks`, but not `block_size`. The update to `cache_config.block_size` made by `_align_hybrid_block_size()`...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: nswer lots of frequently asked questions. correctness attention_kv_cache;ci_build;distributed_parallel;frontend_api;gemm_linear;hardware_porting;model_support;sampling_logits;speculative_decoding attention;cuda;operator...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 3: [Bug]: vllm:cache_config_info reports stale block_size=16 for hybrid Mamba models bug ### Your current environment ### 🐛 Describe the bug ## Description When serving hybrid Mamba models (e.g. `Qwen/Qwen3.6-35B-A3B`, arc...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: [Bug]: vllm:cache_config_info reports stale block_size=16 for hybrid Mamba models bug ### Your current environment ### 🐛 Describe the bug ## Description When serving hybrid Mamba models (e.g. `Qwen/Qwen3.6-35B-A3B`, arc...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: cription When serving hybrid Mamba models (e.g. `Qwen/Qwen3.6-35B-A3B`, architecture `Qwen3_5MoeForConditionalGeneration`), `_align_hybrid_block_size()` correctly enlarges `block_size` in the worker process (e.g. to 528...
- [MoE、GEMM 与 Expert Routing](../patterns/moe_gemm_routing.md) - 分数 2: g hybrid Mamba models (e.g. `Qwen/Qwen3.6-35B-A3B`, architecture `Qwen3_5MoeForConditionalGeneration`), `_align_hybrid_block_size()` correctly enlarges `block_size` in the worker process (e.g. to 528 or 1056 tokens) to...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
