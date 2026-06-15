# vllm-project/vllm#43093: [Bug]:  Fix two crashes that prevent DeepSeek-V4-Flash  + OffloadingConnector

| 字段 | 值 |
| --- | --- |
| Issue | [#43093](https://github.com/vllm-project/vllm/issues/43093) |
| 状态 | open |
| 标签 | bug |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | development |
| 工作域 | attention_kv_cache;distributed_parallel;quantization |
| 子分类 |  |
| Operator 关键词 | cache;fp8 |
| 症状 | crash |
| 根因提示 | dtype;memory_layout |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]:  Fix two crashes that prevent DeepSeek-V4-Flash  + OffloadingConnector

### Issue 正文摘录

### Your current environment H200 + v0.21.0 + deepseek-v4-flash ### 🐛 Describe the bug [kv_offload] Fix stale cache_config.block_size used as hash_block_size in OffloadingSpec Running DeepSeek-V4-Flash with KV offloading enabled causes the engine to crash immediately at startup with one of these assertion errors: ``` # Error 1 — stale block_size causes divisibility check to fail AssertionError: gpu_block_size=64 not divisible by hash_block_size=256. ``` ``` # Error 2 — only visible after fixing Error 1 AssertionError: If 'block_size' is specified in kv_connector_extra_config, there must be at least one KV cache group, and all groups must have the same block size. ``` A typical failing command looks like: ``` vllm serve deepseek-ai/DeepSeek-V4-Flash \ --block-size 256 \ --kv-cache-dtype fp8 \ --no-disable-hybrid-kv-cache-manager \ --kv-transfer-config '{\"kv_connector\":\"OffloadingConnector\",\"kv_role\":\"kv_both\",\"kv_connector_extra_config\":{\"block_size\":256}}' ``` ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/),...

## 候选优化模式

- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 3: serve deepseek-ai/DeepSeek-V4-Flash \ --block-size 256 \ --kv-cache-dtype fp8 \ --no-disable-hybrid-kv-cache-manager \ --kv-transfer-config '{\"kv_connector\":\"OffloadingConnector\",\"kv_role\":\"kv_both\",\"kv_connect...
- [KV Cache 容量、压缩与 Offload](../patterns/kv_cache_capacity_offload.md) - 分数 3: [Bug]: Fix two crashes that prevent DeepSeek-V4-Flash + OffloadingConnector bug ### Your current environment H200 + v0.21.0 + deepseek-v4-flash ### 🐛 Describe the bug [kv_offload] Fix stale cache_config.block_size used...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 3: ek-v4-flash ### 🐛 Describe the bug [kv_offload] Fix stale cache_config.block_size used as hash_block_size in OffloadingSpec Running DeepSeek-V4-Flash with KV offloading enabled causes the engine to crash immediately at...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: only visible after fixing Error 1 AssertionError: If 'block_size' is specified in kv_connector_extra_config, there must be at least one KV cache group, and all groups must have the same block size. ``` A typical failing...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: ``` ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
