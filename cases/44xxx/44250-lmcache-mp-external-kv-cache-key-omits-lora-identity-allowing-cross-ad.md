# vllm-project/vllm#44250: LMCache MP external KV cache key omits LoRA identity, allowing cross-adapter KV hits

| 字段 | 值 |
| --- | --- |
| Issue | [#44250](https://github.com/vllm-project/vllm/issues/44250) |
| 状态 | open |
| 标签 |  |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | attention_kv_cache;distributed_parallel;frontend_api;model_support;scheduler_memory |
| 子分类 | wrong_output |
| Operator 关键词 | attention;cache;cuda |
| 症状 | nondeterministic |
| 根因提示 | env_dependency;memory_layout;race_condition |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> LMCache MP external KV cache key omits LoRA identity, allowing cross-adapter KV hits

### Issue 正文摘录

### Summary `LMCacheMPConnector` appears to namespace external KV cache entries by base model, token IDs/chunk hashes, token range, world/rank, and `cache_salt`, but not by LoRA adapter identity/version. With two different LoRA adapters loaded for the same base model, adapter B can get LMCache hits for KV blocks that were produced under adapter A when the prompt token IDs and `cache_salt` match. This is semantically unsafe for LoRAs that affect attention projections, because the stored K/V tensors are adapter-dependent. ### Environment - GPU: NVIDIA A100-SXM4-40GB on GCP - vLLM: `0.22.1rc1.dev38+gfd9e91d7e.cu129` - LMCache: `0.4.7.dev7` - PyTorch: `2.11.0+cu129`, CUDA `12.9` - Base model: `Qwen/Qwen2.5-7B-Instruct` - Local prefix caching disabled with `--no-enable-prefix-caching` - KV connector: ```bash --kv-transfer-config '{"kv_connector":"LMCacheMPConnector","kv_connector_module_path":"lmcache.integration.vllm.lmcache_mp_connector","kv_role":"kv_both"}' ``` ### Repro Setup I generated two deterministic PEFT LoRA adapters for the same base model and tokenizer: - `adapter_a` - sha256: `70e4b55af62be4779c2cfe1419c832d3c76b31f11f5f4a607bcbcd39cbcf94ef` - seed: `101` - `adapter_b` -...

## 候选优化模式

- [Bitwise 确定性与数值等价](../patterns/bitwise_determinism_equivalence.md) - 分数 6: ferent LoRA adapters loaded for the same base model, adapter B can get LMCache hits for KV blocks that were produced under adapter A when the prompt token IDs and `cache_salt` match. This is semantically unsafe for LoRA...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 5: en range, world/rank, and `cache_salt`, but not by LoRA adapter identity/version. With two different LoRA adapters loaded for the same base model, adapter B can get LMCache hits for KV blocks that were produced under ad...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 3: rs loaded for the same base model, adapter B can get LMCache hits for KV blocks that were produced under adapter A when the prompt token IDs and `cache_salt` match. This is semantically unsafe for LoRAs that affect atte...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: CacheMPConnector` appears to namespace external KV cache entries by base model, token IDs/chunk hashes, token range, world/rank, and `cache_salt`, but not by LoRA adapter identity/version. With two different LoRA adapte...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: tored K/V tensors are adapter-dependent. ### Environment - GPU: NVIDIA A100-SXM4-40GB on GCP - vLLM: `0.22.1rc1.dev38+gfd9e91d7e.cu129` - LMCache: `0.4.7.dev7` - PyTorch: `2.11.0+cu129`, CUDA `12.9` - Base model: `Qwen/...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
