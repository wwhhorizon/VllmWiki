# vllm-project/vllm#34129: [Bug]: Online FP8 quantization does not split MoE expert weights across GPUs with TP/EP for Qwen3NextForCausalLM

| 字段 | 值 |
| --- | --- |
| Issue | [#34129](https://github.com/vllm-project/vllm/issues/34129) |
| 状态 | open |
| 标签 | bug;stale |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | attention_kv_cache;distributed_parallel;model_support;moe;quantization |
| 子分类 | memory |
| Operator 关键词 | attention;cuda;fp8;moe;quantization |
| 症状 | oom |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Online FP8 quantization does not split MoE expert weights across GPUs with TP/EP for Qwen3NextForCausalLM

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug ## Your current environment - vLLM version: 0.15.1 - PyTorch version: 2.7 - CUDA version: 12.8 - GPU: 2x NVIDIA RTX PRO 6000 Black (95 GiB each) - OS: Ubuntu Linux 6.14.0 ## Model Qwen3-Coder-Next (Qwen3NextForCausalLM) - Hybrid Mamba-Attention + MoE architecture - 512 experts, 10 active per token, 48 layers - bf16 model size on disk: ~149 GiB ## 🐛 Describe the bug When using online FP8 quantization (`--quantization fp8`) on the bf16 Qwen3-Coder-Next model with Tensor Parallelism or Expert Parallelism, per-GPU memory usage is nearly the same as single GPU. The MoE expert weights in `SharedFusedMoE` are not being split across GPUs during the `create_weights` phase. ### Evidence | Configuration | Per-GPU peak memory | |---|---| | TP=1, fp8 | 95.46 GiB | | TP=2, fp8 | 95.02 GiB | | TP=2 + EP, fp8 | 94.49 GiB | TP=2 only reduces per-GPU memory by **0.44 GiB** — the 512 MoE experts are clearly not being split. In contrast, the pre-quantized FP8 model (`Qwen3-Coder-Next-FP8`) with TP=2 loads at **37.52 GiB per GPU**, confirming the architecture itself supports TP splitting. ### Reproduction ```bash # Single GPU — OOM (needs 95.46 GiB,...

## 候选优化模式

- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 4: [Bug]: Online FP8 quantization does not split MoE expert weights across GPUs with TP/EP for Qwen3NextForCausalLM bug;stale ### Your current environment ### 🐛 Describe the bug ## Your current environment - vLLM version:...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 4: rrent environment - vLLM version: 0.15.1 - PyTorch version: 2.7 - CUDA version: 12.8 - GPU: 2x NVIDIA RTX PRO 6000 Black (95 GiB each) - OS: Ubuntu Linux 6.14.0 ## Model Qwen3-Coder-Next (Qwen3NextForCausalLM) - Hybrid...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: uantization does not split MoE expert weights across GPUs with TP/EP for Qwen3NextForCausalLM bug;stale ### Your current environment ### 🐛 Describe the bug ## Your current environment - vLLM version: 0.15.1 - PyTorch ve...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: onment ### 🐛 Describe the bug ## Your current environment - vLLM version: 0.15.1 - PyTorch version: 2.7 - CUDA version: 12.8 - GPU: 2x NVIDIA RTX PRO 6000 Black (95 GiB each) - OS: Ubuntu Linux 6.14.0 ## Model Qwen3-Cod...
- [KV Cache 容量、压缩与 Offload](../patterns/kv_cache_capacity_offload.md) - 分数 2: wen3-Coder-Next model with Tensor Parallelism or Expert Parallelism, per-GPU memory usage is nearly the same as single GPU. The MoE expert weights in `SharedFusedMoE` are not being split across GPUs during the `create_w...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
