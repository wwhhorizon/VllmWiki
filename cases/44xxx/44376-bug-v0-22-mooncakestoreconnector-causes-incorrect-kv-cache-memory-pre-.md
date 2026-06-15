# vllm-project/vllm#44376: [Bug]: [v0.22]MooncakeStoreConnector causes incorrect KV cache memory pre-check calculation for DeepSeek models(PP2 TP8) (fallback to MHA dimension)

| 字段 | 值 |
| --- | --- |
| Issue | [#44376](https://github.com/vllm-project/vllm/issues/44376) |
| 状态 | open |
| 标签 | bug |
| 评论 | 0; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | attention_kv_cache;distributed_parallel;frontend_api;model_support;moe;quantization;scheduler_memory |
| 子分类 | precision |
| Operator 关键词 | attention;cache;fp8;moe |
| 症状 | crash;mismatch |
| 根因提示 | dtype;env_dependency;memory_layout;shape |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: [v0.22]MooncakeStoreConnector causes incorrect KV cache memory pre-check calculation for DeepSeek models(PP2 TP8) (fallback to MHA dimension)

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug ### **Title:** [Bug] [v1 Engine] `MooncakeStoreConnector` causes incorrect KV cache memory pre-check calculation for DeepSeek models (fallback to MHA dimension) --- ### **Description** When deploying **DeepSeek-V4-Pro** (which utilizes **MLA** architecture) on a multi-node cluster using the new **vLLM V1 Engine**, we encountered a severe memory pre-check miscalculation when enabling KV cache offloading via `MooncakeStoreConnector`. * **Without KV Offloading:** The engine boots perfectly. The memory profiler correctly handles DeepSeek's MLA architecture, showing ample free memory capable of hosting up to **5 million KV cache tokens**. * **With KV Offloading enabled (`MooncakeStoreConnector`):** The initialization crashes immediately during the memory pre-check phase (`_check_enough_kv_cache_memory`). It naively estimates that a single GPU requires **223.68 GiB** of KV cache memory to support a `max_model_len` of `1,000,000`, leading to a `ValueError`. It highly implies that the `kv_transfer` / `MooncakeStoreConnector` initialization path currently lacks adaptation for DeepSeek's MLA compressed dimensions, incorrectly falling back...

## 候选优化模式

- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 4: ke Config (`mooncake_config.json`)** ```json { "mode": "embedded", "metadata_server": "P2PHANDSHAKE", "master_server_address": "192.168.180.132:50051", "global_segment_size": "120GB", "local_buffer_size": "8GB", "protoc...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: during the static memory pre-check. --- ### **Environment** * **vLLM Version:** v0.22.0 (running the new V1 Engine architecture) * **Model:** DeepSeek-V4-Pro * **Hardware:** 2 Nodes, 16x NVIDIA H100 GPUs (80GB SXM5) * *...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 3: --trust-remote-code \ --served-model-name deepseek_pro \ --kv-cache-dtype fp8 \ --block-size 256 \ --enable-expert-parallel \ --tensor-parallel-size 8 \ --pipeline-parallel-size 2 \ --nnodes 2 \ --node-rank 0 \ --master...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: escription** When deploying **DeepSeek-V4-Pro** (which utilizes **MLA** architecture) on a multi-node cluster using the new **vLLM V1 Engine**, we encountered a severe memory pre-check miscalculation when enabling KV ca...
- [KV Cache 容量、压缩与 Offload](../patterns/kv_cache_capacity_offload.md) - 分数 3: [Bug]: [v0.22]MooncakeStoreConnector causes incorrect KV cache memory pre-check calculation for DeepSeek models(PP2 TP8) (fallback to MHA dimension) bug ### Your current environment ### 🐛 Describe the bug ### **Title:**...

## Wiki 抽取状态

- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
