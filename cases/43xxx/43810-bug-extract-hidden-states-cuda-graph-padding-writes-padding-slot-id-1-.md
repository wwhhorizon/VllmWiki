# vllm-project/vllm#43810: [Bug]: extract_hidden_states CUDA graph padding writes PADDING_SLOT_ID=-1 into last hidden-state KV slot

| 字段 | 值 |
| --- | --- |
| Issue | [#43810](https://github.com/vllm-project/vllm/issues/43810) |
| 状态 | open |
| 标签 |  |
| 评论 | 0; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | attention_kv_cache;distributed_parallel;frontend_api;model_support;sampling_logits |
| 子分类 | shape_align |
| Operator 关键词 | activation;attention;cuda |
| 症状 | nondeterministic |
| 根因提示 | dtype;env_dependency;race_condition;shape |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: extract_hidden_states CUDA graph padding writes PADDING_SLOT_ID=-1 into last hidden-state KV slot

### Issue 正文摘录

### Environment - vLLM commit: `284e6f543d462016fc80c055ccbf088832c63129` - vLLM version: `0.1.dev1+g284e6f543` - Python: `3.10.12` - PyTorch: `2.11.0+cu130` - CUDA runtime reported by PyTorch: `13.0` - GPU: `NVIDIA A100-SXM4-40GB`, 40960 MiB - NVIDIA driver: `580.159.03` - Machine used for repro: GCP `a2-highgpu-1g` Spot VM in `asia-northeast1-c` ### Bug `ExtractHiddenStatesProposer` pads slot mappings with `PADDING_SLOT_ID = -1` for CUDA graph execution. The cache-only attention path then writes hidden states with: ```python kv_cache[slot_mapping // block_size, slot_mapping % block_size] = to_cache ``` That treats padded `slot_mapping == -1` as a real negative index, so padding rows write to `kv_cache[-1, block_size - 1]`. In the repro below, CUDA graph padding takes a 64-token drafter call to 128 rows, and the 64 padded rows overwrite the real hidden state in physical slot 79. This may be related to #39247, but this report is specifically about deterministic hidden-state corruption rather than an illegal memory access. ### Exact flags / shape - `speculative_config.method = "extract_hidden_states"` - `num_speculative_tokens = 1` - `ExampleHiddenStatesConnector` as KV producer -...

## 候选优化模式

- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 4: [Bug]: extract_hidden_states CUDA graph padding writes PADDING_SLOT_ID=-1 into last hidden-state KV slot ### Environment - vLLM commit: `284e6f543d462016fc80c055ccbf088832c63129` - vLLM version: `0.1.dev1+g284e6f543` -...
- [Bitwise 确定性与数值等价](../patterns/bitwise_determinism_equivalence.md) - 分数 3: 9. This may be related to #39247, but this report is specifically about deterministic hidden-state corruption rather than an illegal memory access. ### Exact flags / shape - `speculative_config.method = "extract_hidden_...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: onment - vLLM commit: `284e6f543d462016fc80c055ccbf088832c63129` - vLLM version: `0.1.dev1+g284e6f543` - Python: `3.10.12` - PyTorch: `2.11.0+cu130` - CUDA runtime reported by PyTorch: `13.0` - GPU: `NVIDIA A100-SXM4-40...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: [Bug]: extract_hidden_states CUDA graph padding writes PADDING_SLOT_ID=-1 into last hidden-state KV slot ### Environment - vLLM commit: `284e6f543d462016fc80c055ccbf088832c63129` - vLLM version: `0.1.dev1+g284e6f543` -...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: than an illegal memory access. ### Exact flags / shape - `speculative_config.method = "extract_hidden_states"` - `num_speculative_tokens = 1` - `ExampleHiddenStatesConnector` as KV producer - CUDA graph enabled: `enforc...

## Wiki 抽取状态

- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
