# vllm-project/vllm#38291: [Feature]: Add Rotorquant support

| 字段 | 值 |
| --- | --- |
| Issue | [#38291](https://github.com/vllm-project/vllm/issues/38291) |
| 状态 | open |
| 标签 | feature request |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | attention_kv_cache;frontend_api;gemm_linear;model_support;quantization;sampling_logits |
| 子分类 | precision |
| Operator 关键词 | attention;cache;cuda;gemm;kernel;quantization;sampling |
| 症状 | slowdown |
| 根因提示 | dtype;shape |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Feature]: Add Rotorquant support

### Issue 正文摘录

### 🚀 The feature, motivation and pitch **RotorQuant** is a Clifford algebra-based reimagining of TurboQuant (ICLR 2026) for KV cache compression. It replaces the dense d×d random orthogonal rotation matrix used in TurboQuant with lightweight Clifford rotors from Cl(3,0), achieving **10–19× faster** quantization on NVIDIA GPUs, **9–31× faster** on Apple Silicon, and using **44× fewer parameters** — all while matching TurboQuant's attention fidelity on real models. - **Paper/Report:** https://www.scrya.com/rotorquant/ - **Code:** https://github.com/scrya-com/rotorquant - **Related issue:** #38171 (TurboQuant support request) ### Why this matters for vLLM KV cache memory is the primary bottleneck for long-context serving. At 8K tokens on Qwen2.5-3B (36 layers), the KV cache is ~289 MB in FP16. RotorQuant compresses this to ~58 MB at 3-bit (5× compression) with 99.0% attention cosine similarity — comparable to TurboQuant (99.5%) but with dramatically lower computational overhead for the rotation step. The core advantage for a serving engine like vLLM is the **quantize/dequantize speed**: TurboQuant's rotation requires a 128×128 dense matmul (16,384 FMAs per vector), while RotorQuant'...

## 候选优化模式

- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 5: roduct uses only ~100 FMAs per vector. This translates directly to lower latency on the KV cache write path. ### How RotorQuant works 1. **Chunk** the d-dimensional KV vector into groups of 3 dimensions (43 groups for d...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 3: [Feature]: Add Rotorquant support feature request ### 🚀 The feature, motivation and pitch **RotorQuant** is a Clifford algebra-based reimagining of TurboQuant (ICLR 2026) for KV cache compression. It replaces the dense...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: , same as TurboQuant Stage 2. ### Benchmarks (from official website) **CUDA fused kernel speed (RTX PRO 4000, d=128, 3-bit):** | n_vectors | TurboQuant | RotorQuant CUDA | Speedup | |-----------|-----------|------------...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: arameters** — all while matching TurboQuant's attention fidelity on real models. - **Paper/Report:** https://www.scrya.com/rotorquant/ - **Code:** https://github.com/scrya-com/rotorquant - **Related issue:** #38171 (Tur...
- [MoE、GEMM 与 Expert Routing](../patterns/moe_gemm_routing.md) - 分数 2: .9874 | 81.2% | 93.8% | RotorQuant matches or exceeds TurboQuant on top-k retrieval accuracy at 4K context, despite slightly lower cosine similarity on synthetic benchmarks. The Clifford rotor decorrelation appears to b...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
