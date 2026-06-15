# vllm-project/vllm#40696: [Feature]: Prefix caching completely ineffective for Mamba-hybrid models (Qwen3.5) when prompt < block_size (528 tokens)

| 字段 | 值 |
| --- | --- |
| Issue | [#40696](https://github.com/vllm-project/vllm/issues/40696) |
| 状态 | open |
| 标签 | feature request |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | attention_kv_cache;ci_build;distributed_parallel;frontend_api;gemm_linear;hardware_porting;model_support;scheduler_memory |
| 子分类 | throughput |
| Operator 关键词 | attention;cache;cuda;operator;triton |
| 症状 | build_error |
| 根因提示 | dtype;env_dependency;memory_layout |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Feature]: Prefix caching completely ineffective for Mamba-hybrid models (Qwen3.5) when prompt < block_size (528 tokens)

### Issue 正文摘录

### 🚀 The feature, motivation and pitch ## Environment (Brief) - vLLM version: 0.19.1 - GPU: NVIDIA A100/H20 - Model: Qwen/Qwen3.5-4B (Mamba-hybrid architecture) ## Description When serving Mamba-hybrid models like Qwen3.5, vLLM sets the attention block size to **528 tokens** to align with the mamba page size: ``` INFO [config.py:281] Setting attention block size to 528 tokens to ensure that attention page size is >= mamba page size. ``` Since prefix caching operates at the **block** granularity, only **fully completed blocks** are cached. This means: - Prompt with ** 64), telling the user the minimum prompt length needed to benefit 4. **Decouple attention and mamba block sizes**: Use separate block sizes for the attention KV cache (small, e.g. 16) and the mamba state cache (large, 528), so prefix caching for attention layers is not penalized by mamba alignment requirements Option 4 seems the most correct — there's no fundamental reason the attention KV cache block size needs to match the mamba page size for prefix caching purposes. ## Environment (Detail)： ``` ============================== System Info ============================== OS : Ubuntu 22.04.5 LTS (x86_64) GCC version :...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 9: ### 🚀 The feature, motivation and pitch ## Environment (Brief) - vLLM version: 0.19.1 - GPU: NVIDIA A100/H20 - Model: Qwen/Qwen3.5-4B (Mamba-hybrid architecture) ## Description When serving Mamba-hybrid models like Qwen...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 6: and pitch ## Environment (Brief) - vLLM version: 0.19.1 - GPU: NVIDIA A100/H20 - Model: Qwen/Qwen3.5-4B (Mamba-hybrid architecture) ## Description When serving Mamba-hybrid models like Qwen3.5, vLLM sets the attention b...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 4: g completely ineffective for Mamba-hybrid models (Qwen3.5) when prompt < block_size (528 tokens) feature request ### 🚀 The feature, motivation and pitch ## Environment (Brief) - vLLM version: 0.19.1 - GPU: NVIDIA A100/H...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: [Feature]: Prefix caching completely ineffective for Mamba-hybrid models (Qwen3.5) when prompt < block_size (528 tokens) feature request ### 🚀 The feature, motivation and pitch ## Environment (Brief) - vLLM version: 0.1...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 3: === Versions of relevant libraries ============================== [pip3] flashinfer-python==0.6.6 [pip3] numpy==2.2.6 [pip3] nvidia-cublas-cu12==12.8.4.1 [pip3] nvidia-cuda-cupti-cu12==12.8.90 [pip3] nvidia-cuda-nvrtc-c...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
