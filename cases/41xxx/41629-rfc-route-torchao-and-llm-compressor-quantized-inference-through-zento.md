# vllm-project/vllm#41629: [RFC]: Route TorchAO and LLM-Compressor Quantized Inference through zentorch on AMD Zen CPUs

| 字段 | 值 |
| --- | --- |
| Issue | [#41629](https://github.com/vllm-project/vllm/issues/41629) |
| 状态 | open |
| 标签 | rocm;RFC |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | activation_norm;ci_build;gemm_linear;hardware_porting;model_support;quantization |
| 子分类 | memory |
| Operator 关键词 | cuda;fp8;gemm;kernel;operator;quantization |
| 症状 | build_error |
| 根因提示 | dtype;env_dependency;memory_layout |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | True |

## 源证据

### Issue 标题

> [RFC]: Route TorchAO and LLM-Compressor Quantized Inference through zentorch on AMD Zen CPUs

### Issue 正文摘录

### Motivation. vLLM already has a first-class `ZenCpuPlatform` (`vllm/platforms/zen_cpu.py`) that is auto-detected on AMD Zen hosts when zentorch is installed, and unquantized GEMM on this platform is already routed through `zentorch_linear_unary` via `dispatch_cpu_unquantized_gemm`. However, quantized inference paths on Zen CPUs are currently sub-optimal: - The TorchAO quantized path (`TorchAOLinearMethod`) is unaware of the Zen platform and always falls back to `F.linear`, bypassing zentorch's int8 dynamic-activation kernels. - Compressed models produced by **LLM-Compressor** (compressed-tensors format) — including dynamic DA8W8 INT8 scaled-mm linears and W4A16 weight-only quantized (AWQ/GPTQ) linears — currently route through generic oneDNN / Marlin CPU kernels rather than zentorch's optimized ops. For W4A16 and DA8W8 workloads, zentorch's kernels are substantially faster on AMD EPYC platforms. This RFC proposes extending the relevant quantization linear methods to dispatch a **specific, enumerated set** of quantized linear schemes — TorchAO DA8W8 (`Int8Tensor` with per-row weight quantization granularity), compressed-tensors W8A8 dynamic-symmetric, and compressed-tensors W4A1...

## 现有链接修复摘要

#41813 [CPU][Zen] Route W8A8 and W4A16 linear inference through zentorch on AMD Zen CPUs

## 候选优化模式

- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 6: [RFC]: Route TorchAO and LLM-Compressor Quantized Inference through zentorch on AMD Zen CPUs rocm;RFC ### Motivation. vLLM already has a first-class `ZenCpuPlatform` (`vllm/platforms/zen_cpu.py`) that is auto-detected o...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 5: rms/zen_cpu.py`) that is auto-detected on AMD Zen hosts when zentorch is installed, and unquantized GEMM on this platform is already routed through `zentorch_linear_unary` via `dispatch_cpu_unquantized_gemm`. However, q...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 4: and LLM-Compressor Quantized Inference through zentorch on AMD Zen CPUs rocm;RFC ### Motivation. vLLM already has a first-class `ZenCpuPlatform` (`vllm/platforms/zen_cpu.py`) that is auto-detected on AMD Zen hosts when...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 3: on this platform is already routed through `zentorch_linear_unary` via `dispatch_cpu_unquantized_gemm`. However, quantized inference paths on Zen CPUs are currently sub-optimal: - The TorchAO quantized path (`TorchAOLin...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: ear`, bypassing zentorch's int8 dynamic-activation kernels. - Compressed models produced by **LLM-Compressor** (compressed-tensors format) — including dynamic DA8W8 INT8 scaled-mm linears and W4A16 weight-only quantized...

## 关联 PR 证据

| PR | 链接类型 | 置信度 | PR 标题 | 证据 |
| --- | --- | ---: | --- | --- |
| [#41813](https://github.com/vllm-project/vllm/pull/41813) | mentioned | 0.45 | [CPU][Zen] Route W8A8 and W4A16 linear inference through zentorch on AMD Zen CPUs | zendnn-5-2-1-on-amd-epyc-cpus.html) - reference implementation pr: : #41813 ### before submitting a new issue... - [x] make sure you already searched for relevant issues, and aske… |

## Wiki 抽取状态

- 后续迭代应在可用时读取完整讨论评论。
