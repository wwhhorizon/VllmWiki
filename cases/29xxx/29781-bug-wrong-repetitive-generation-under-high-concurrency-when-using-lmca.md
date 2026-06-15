# vllm-project/vllm#29781: [Bug]: Wrong / Repetitive Generation Under High Concurrency When Using LMCache CPU Offload

| 字段 | 值 |
| --- | --- |
| Issue | [#29781](https://github.com/vllm-project/vllm/issues/29781) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 45; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | attention_kv_cache;ci_build;distributed_parallel;frontend_api;gemm_linear;hardware_porting;model_support;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cache;cuda;kernel;operator;sampling;triton |
| 症状 | build_error;mismatch;nan_inf;nondeterministic |
| 根因提示 | env_dependency;memory_layout;race_condition |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Wrong / Repetitive Generation Under High Concurrency When Using LMCache CPU Offload

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug When enabling LMCache CPU offload (kv_both) with vLLM, model outputs become incorrect under high concurrency (~32 parallel requests). After processing approximately 100 data entries, the generated text contains large repetitive segments, and debugging shows KV cache inconsistency in the block table for affected requests. This appears to be a correctness issue related to LMCache’s CPU offload mode, KV transfer, or vLLM integration. Launch Command ```python python3 entrypoints/openai/api_server.py --model Qwen3/Qwen3-32B --tensor-parallel-size 1 --gpu-memory-utilization 0.97 --enforce-eager --reasoning-parser qwen3 --disable-cascade-attn --kv-transfer-config {"kv_connector":"LMCacheConnectorV1","kv_role":"kv_both"} ``` Environment Variables ```env LMCACHE_CONFIG_FILE="./cpu_offload.yaml" LMCACHE_USE_EXPERIMENTAL=True ``` cpu_offload.yaml ```yaml chunk_size: 16 local_cpu: true max_local_cpu_size: 10.0 ``` Dataset The test data is from:[ShareGPT_V3_unfiltered_cleaned_split.json](https://huggingface.co/datasets/anon8231489123/ShareGPT_Vicuna_unfiltered/resolve/main/ShareGPT_V3_unfiltered_cleaned_split.json). An example of an erroneous...

## 候选优化模式

- [KV Cache 容量、压缩与 Offload](../patterns/kv_cache_capacity_offload.md) - 分数 4: ng / Repetitive Generation Under High Concurrency When Using LMCache CPU Offload bug;stale ### Your current environment ### 🐛 Describe the bug When enabling LMCache CPU offload (kv_both) with vLLM, model outputs become...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: Describe the bug When enabling LMCache CPU offload (kv_both) with vLLM, model outputs become incorrect under high concurrency (~32 parallel requests). After processing approximately 100 data entries, the generated text...
- [Bitwise 确定性与数值等价](../patterns/bitwise_determinism_equivalence.md) - 分数 3: n**, and **disruption of water cycles**. ``` Debug Findings Using vLLM deterministic inference consistency debugging: Under faulty conditions, a single block ID in the block table has KV cache values for its 16-token ch...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: a 20-year period. 2. **Deforestation**: - Large areas of forest, especially in the Amazon, are cleared to make way for **pastureland** or to grow **feed crops** like soy. - This leads to **loss of biodiversity**, **soil...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: normal requests using the same prompt This indicates KV corruption / mismatched KV retrieval, likely tied to CPU–GPU KV transfer or LMCache block reuse. ### Before submitting a new issue... - [x] Make sure you already s...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
