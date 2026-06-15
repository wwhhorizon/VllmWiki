# vllm-project/vllm#40322: [Doc]: Jetson Orin + vLLM Qwen3-0.6B quantized models – GPU active but no speedup, need optimization tips

| 字段 | 值 |
| --- | --- |
| Issue | [#40322](https://github.com/vllm-project/vllm/issues/40322) |
| 状态 | open |
| 标签 | documentation |
| 评论 | 0; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | quantization |
| 子分类 | latency_reg |
| Operator 关键词 | cuda;fp8;quantization |
| 症状 | build_error;slowdown |
| 根因提示 | dtype |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Doc]: Jetson Orin + vLLM Qwen3-0.6B quantized models – GPU active but no speedup, need optimization tips

### Issue 正文摘录

### 📚 The doc issue Hi everyone, I’m testing Qwen3-0.6B variants (FP16 / FP8 / GPTQ-Int8 / GPTQ-Int4) on a Jetson AGX Orin (JetPack 6.2) using vLLM, and seeing some unexpected behavior. Observed behavior: jtop shows GPU VRAM usage at ~25GB, and the process is clearly using the GPU. However, generation speed stays around 23–26 tok/s across all models, with no speedup from FP8 or GPTQ quantization. Even more surprising: the vLLM GPU version is slower than the MNN CPU-only version, which runs at ~42 tok/s. Questions: Why isn’t FP8 / GPTQ giving the expected speed boost on Orin with vLLM? Is this a Jetson-specific limitation with vLLM, or are there key optimizations I’m missing? Are there known ways to improve vLLM performance for small models like 0.6B on Orin? Context: vLLM built from source for JetPack 6.2 / CUDA 12.6. Running with enforce_eager=True, logs show Inductor compilation was disabled. Quantization settings are set as per docs (quantization=fp8 for FP8, gptq_marlin for GPTQ). Any insights or tips would be really appreciated! Thanks. ### Suggest a potential alternative/fix _No response_ ### Before submitting a new issue... - [x] Make sure you already searched for relevant...

## 候选优化模式

- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 4: [Doc]: Jetson Orin + vLLM Qwen3-0.6B quantized models – GPU active but no speedup, need optimization tips documentation ### 📚 The doc issue Hi everyone, I’m testing Qwen3-0.6B variants (FP16 / FP8 / GPTQ-Int8 / GPTQ-Int...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: up from FP8 or GPTQ quantization. Even more surprising: the vLLM GPU version is slower than the MNN CPU-only version, which runs at ~42 tok/s. Questions: Why isn’t FP8 / GPTQ giving the expected speed boost on Orin with...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: ns I’m missing? Are there known ways to improve vLLM performance for small models like 0.6B on Orin? Context: vLLM built from source for JetPack 6.2 / CUDA 12.6. Running with enforce_eager=True, logs show Inductor compi...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: [Doc]: Jetson Orin + vLLM Qwen3-0.6B quantized models – GPU active but no speedup, need optimization tips documentation ### 📚 The doc issue Hi everyone, I’m testing Qwen3-0.6B variants (FP16 / FP8 / GPTQ-Int8 / GPTQ-Int...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ed optimization tips documentation ### 📚 The doc issue Hi everyone, I’m testing Qwen3-0.6B variants (FP16 / FP8 / GPTQ-Int8 / GPTQ-Int4) on a Jetson AGX Orin (JetPack 6.2) using vLLM, and seeing some unexpected behavior...

## Wiki 抽取状态

- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
