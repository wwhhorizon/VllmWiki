# vllm-project/vllm#33478: [RFC]: Introduce ATOM as model implementation backend for AMD GPU

| 字段 | 值 |
| --- | --- |
| Issue | [#33478](https://github.com/vllm-project/vllm/issues/33478) |
| 状态 | closed |
| 标签 | rocm;RFC |
| 评论 | 9; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | attention_kv_cache;frontend_api;hardware_porting;model_support;quantization;sampling_logits;scheduler_memory |
| 子分类 | precision |
| Operator 关键词 | attention;cache;cuda;fp8;kernel;operator |
| 症状 | build_error |
| 根因提示 | dtype;memory_layout |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [RFC]: Introduce ATOM as model implementation backend for AMD GPU

### Issue 正文摘录

### Motivation [ATOM](https://github.com/ROCm/ATOM) is a foundational component of AMD’s AI inference strategy. It is implemented by ROCm developers and can be used to serve as the model implementation backend for high-performance inference on AMD GPUs. It is built by integrating optimizations from ROCm’s high-performance operator library [aiter](https://github.com/ROCm/aiter/tree/main) and high-performance communication library [mori](https://github.com/ROCm/mori) into model execution path. The key motivation of introducing ATOM into vLLM as a model impl backend is two-fold: - Strengthen vLLM’s ecosystem for AMD GPUs. ATOM, working as the ROCm-optimized model impl backend, can help vLLM deliver more competitive performance on AMD GPUs - Balance user experience of AMD GPUs and ROCm iteration velocity: - A great out-of-the-box experience for vLLM frontend users (only one serving argument `--model-impl atom` to enable, reuse vLLM’s serving/runtime stack) - Fast, continuous development iteration on ROCm libraries (aiter/mori) and their model-side integration ### Background ATOM can deliver performance gains through following points with ROCm components: - Cross-layer / cross-module f...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: .com/ROCm/mori) into model execution path. The key motivation of introducing ATOM into vLLM as a model impl backend is two-fold: - Strengthen vLLM’s ecosystem for AMD GPUs. ATOM, working as the ROCm-optimized model impl...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 4: [RFC]: Introduce ATOM as model implementation backend for AMD GPU rocm;RFC ### Motivation [ATOM](https://github.com/ROCm/ATOM) is a foundational component of AMD’s AI inference strategy. It is implemented by ROCm develo...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: [RFC]: Introduce ATOM as model implementation backend for AMD GPU rocm;RFC ### Motivation [ATOM](https://github.com/ROCm/ATOM) is a foundational component of AMD’s AI inference strategy. It is implemented by ROCm develo...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 4: kv cache manager, cuda graph compilation, parallel strategies, PD infra, profiler and so on - Preserving the vLLM stack and its user experience Given above points, ATOM plans to integrate into vLLM as a model impl backe...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 3: and vLLM with ATOM model impl backend for Qwen3-235B-A22B-Instruct-2507-FP8 with TP8+EP8: Machine 350*8 | ISL/OSL (K=1000) | Concurrency | TTFT(ms) | TPOT(ms) | TTPS(tok/s) | TTPS Ratio (Compared to vLLM) -- | -- | -- |...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
