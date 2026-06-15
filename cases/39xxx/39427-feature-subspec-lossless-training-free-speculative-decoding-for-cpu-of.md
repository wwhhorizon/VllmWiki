# vllm-project/vllm#39427: [Feature]: SubSpec — Lossless Training-Free Speculative Decoding for CPU-Offloaded LLMs via Quantized Substitute Draft

| 字段 | 值 |
| --- | --- |
| Issue | [#39427](https://github.com/vllm-project/vllm/issues/39427) |
| 状态 | open |
| 标签 | feature request |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | attention_kv_cache;frontend_api;gemm_linear;model_support;quantization;speculative_decoding |
| 子分类 | memory |
| Operator 关键词 | cache;gemm;kernel;operator;quantization |
| 症状 |  |
| 根因提示 | dtype;memory_layout |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Feature]: SubSpec — Lossless Training-Free Speculative Decoding for CPU-Offloaded LLMs via Quantized Substitute Draft

### Issue 正文摘录

### 🚀 The feature, motivation and pitch vLLM's `--cpu-offload-gb` flag enables large models on memory-limited GPUs, but in practice the PCIe bottleneck makes it painful for interactive use — every forward pass stalls waiting for offloaded weights to come back from CPU RAM. Speculative decoding is the natural fix to amortize this cost, but `--speculative-model` requires a separate draft model — which either doesn't exist for custom-trained targets, or eats up the VRAM we're trying to save in the first place. I'd like to implement SubSpec , from our lab's NeurIPS 2025 paper: > **Speculate Deep and Accurate: Lossless and Training-Free Acceleration for Offloaded LLMs via Substitute Speculative Decoding** > Pei-Shuo Wang, Jian-Jia Chen, Chun-Che Yang, Chi-Chih Chang, Ning-Chi Huang, Mohamed S. Abdelfattah, Kai-Chiang Wu > https://arxiv.org/abs/2509.18344 Instead of a separate model, SubSpec builds a draft by replacing the CPU-offloaded layers with **low-bit quantized substitutes on GPU**, while sharing the GPU-resident layers and KV cache with the target model: ``` CPU RAM: [Offloaded layers, BF16] ← verify path (unchanged) GPU VRAM: [GPU-resident layers, BF16] ← shared by draft and ta...

## 候选优化模式

- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 6: — Lossless Training-Free Speculative Decoding for CPU-Offloaded LLMs via Quantized Substitute Draft feature request ### 🚀 The feature, motivation and pitch vLLM's `--cpu-offload-gb` flag enables large models on memory-l...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 6: [Feature]: SubSpec — Lossless Training-Free Speculative Decoding for CPU-Offloaded LLMs via Quantized Substitute Draft feature request ### 🚀 The feature, motivation and pitch vLLM's `--cpu-offload-gb` flag enables large...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: LLM/HQQ/GemLite stack, I ran two experiments on Qwen2.5-7B-Instruct with RTX 3090 Ti. **Experiment 1 — Operator verification**: CPU BF16 weights and GPU 4-bit HQQ weights coexist in the same process without conflicts. T...
- [KV Cache 容量、压缩与 Offload](../patterns/kv_cache_capacity_offload.md) - 分数 3: [Feature]: SubSpec — Lossless Training-Free Speculative Decoding for CPU-Offloaded LLMs via Quantized Substitute Draft feature request ### 🚀 The feature, motivation and pitch vLLM's `--cpu-offload-gb` flag enables large...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: ture, motivation and pitch vLLM's `--cpu-offload-gb` flag enables large models on memory-limited GPUs, but in practice the PCIe bottleneck makes it painful for interactive use — every forward pass stalls waiting for off...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
