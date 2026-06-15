# vllm-project/vllm#43308: [Performance]: Massive increase (~10x) in KV Cache capacity for Gemma 4 in v0.21.0

| 字段 | 值 |
| --- | --- |
| Issue | [#43308](https://github.com/vllm-project/vllm/issues/43308) |
| 状态 | closed |
| 标签 | performance |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | attention_kv_cache;frontend_api;model_support;quantization;scheduler_memory |
| 子分类 | kernel_eff |
| Operator 关键词 | attention;cache;quantization |
| 症状 |  |
| 根因提示 | env_dependency |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Performance]: Massive increase (~10x) in KV Cache capacity for Gemma 4 in v0.21.0

### Issue 正文摘录

### Proposal to improve performance _No response_ ### Report of performance regression _No response_ ### Misc discussion on performance **Obersvation** While testing Gemma 4 (specifically using [cyankiwi/gemma-4-31B-it-AWQ-4bit](https://huggingface.co/cyankiwi/gemma-4-31B-it-AWQ-4bit)) on an A100 80GB, I observed a massive increase in available KV cache capacity between vLLM v0.20.0 and v0.21.0. **Comparison Data** Using the same args and `--gpu-memory-utilization 0.9`: | vLLM Version | GPU KV Cache Size | Memory Cost per Token | | :--- | :--- | :--- | | **v0.20.0** | ~55k tokens | High | | **v0.21.0** | ~525k tokens | Low (~9.5x reduction) | Total available KV cache memory remained constant (~50 GB), indicating the efficiency gain is per token. **Technical Analysis** Gemma 4 utilizes several advanced memory-saving features: 1. **Alternating Attention:** Mix of local sliding-window layers (1024 tokens) and global full-context layers. 2. **Shared KV Cache:** The last $N$ layers reuse KV states from earlier layers. 3. **Dual RoPE:** Standard RoPE for sliding layers and pruned RoPE for global layers. (Source: [Hugging Face Blog](https://huggingface.co/blog/gemma4)) It appears that in...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: [Performance]: Massive increase (~10x) in KV Cache capacity for Gemma 4 in v0.21.0 performance ### Proposal to improve performance _No response_ ### Report of performance regression _No response_ ### Misc discussion on...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: [Performance]: Massive increase (~10x) in KV Cache capacity for Gemma 4 in v0.21.0 performance ### Proposal to improve performance _No response_ ### Report of performance regression _No response_ ### Misc discussion on...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 3: roposal to improve performance _No response_ ### Report of performance regression _No response_ ### Misc discussion on performance **Obersvation** While testing Gemma 4 (specifically using [cyankiwi/gemma-4-31B-it-AWQ-4...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: WQ-4bit](https://huggingface.co/cyankiwi/gemma-4-31B-it-AWQ-4bit)) on an A100 80GB, I observed a massive increase in available KV cache capacity between vLLM v0.20.0 and v0.21.0. **Comparison Data** Using the same args...
- [KV Cache 容量、压缩与 Offload](../patterns/kv_cache_capacity_offload.md) - 分数 2: [Performance]: Massive increase (~10x) in KV Cache capacity for Gemma 4 in v0.21.0 performance ### Proposal to improve performance _No response_ ### Report of performance regression _No response_ ### Misc discussion on...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
