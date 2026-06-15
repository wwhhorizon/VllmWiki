# vllm-project/vllm#37151: [Bug]: [ROCm][gfx1151] Engine Core segfaults in libhsa-runtime64.so when loading Qwen3-VL-32B-AWQ on AMD Ryzen AI MAX+ 395

| 字段 | 值 |
| --- | --- |
| Issue | [#37151](https://github.com/vllm-project/vllm/issues/37151) |
| 状态 | open |
| 标签 | bug;rocm |
| 评论 | 8; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;hardware_porting;model_support;quantization;sampling_logits;scheduler_memory;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cuda;kernel;operator;quantization;sampling;triton |
| 症状 | build_error;crash;nan_inf;nondeterministic |
| 根因提示 | dtype;env_dependency;memory_layout;race_condition |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: [ROCm][gfx1151] Engine Core segfaults in libhsa-runtime64.so when loading Qwen3-VL-32B-AWQ on AMD Ryzen AI MAX+ 395

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug --- # 🐛 Bug Report: Segmentation Fault in `libhsa-runtime64.so` on AMD Ryzen AI MAX+ 395 (gfx1151) with Qwen3-VL-32B-AWQ ## Describe the bug When attempting to run a **Qwen3-VL-32B-AWQ** model on an **AMD Ryzen AI MAX+ 395 (gfx1151)** APU using **vLLM (ROCm build)**, the Engine Core subprocess consistently crashes with a **Segmentation Fault** inside `libhsa-runtime64.so`. The crash occurs immediately after engine initialization logs (`No logitsprocs plugins installed`) and before weight loading completes. The main process reports `RuntimeError: Engine core initialization failed` with no Python traceback, as the child process is killed by the OS. ## 💻 Steps to Reproduce ### 1. Hardware - **CPU/GPU**: AMD Ryzen AI MAX+ 395 (Strix Halo) with Radeon 8060S (`gfx1151`) - **VRAM**: 96GB Unified Memory ### 2. OS - **Distribution**: Ubuntu 24.04.3 LTS - **Kernel**: `6.17.0-1012-oem` ### 3. Software Stack - **ROCm Version**: 7.0 (PyTorch `2.9.1+git8907517`, Hip Version: `7.0.51831`) - **vLLM Version**: `0.17.1rc1.dev172+g697e4ff35.rocm700` - **Python**: 3.12 - **Model**: `Qwen3-VL-32B-Instruct-AWQ-4bit` (compressed-tensors quantization) #...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 5: * model on an **AMD Ryzen AI MAX+ 395 (gfx1151)** APU using **vLLM (ROCm build)**, the Engine Core subprocess consistently crashes with a **Segmentation Fault** inside `libhsa-runtime64.so`. The crash occurs immediately...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 5: [Bug]: [ROCm][gfx1151] Engine Core segfaults in libhsa-runtime64.so when loading Qwen3-VL-32B-AWQ on AMD Ryzen AI MAX+ 395 bug;rocm ### Your current environment ### 🐛 Describe the bug --- # 🐛 Bug Report: Segmentation Fa...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 4: : 3.12 - **Model**: `Qwen3-VL-32B-Instruct-AWQ-4bit` (compressed-tensors quantization) ### 4. Command ```bash export PYTORCH_ROCM_ARCH=gfx1151 export HSA_OVERRIDE_GFX_VERSION=11.5.1 export HSA_NO_SCRATCH_RECLAIM=1 expor...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 3: ccurs with **large AWQ quantized models** using the `compressed-tensors` backend. - Setting `HSA_OVERRIDE_GFX_VERSION=11.5.1` allows initialization to proceed further but does **not** prevent the segfault in `libhsa-run...
- [Bitwise 确定性与数值等价](../patterns/bitwise_determinism_equivalence.md) - 分数 3: thon traceback, as the child process is killed by the OS. ## 💻 Steps to Reproduce ### 1. Hardware - **CPU/GPU**: AMD Ryzen AI MAX+ 395 (Strix Halo) with Radeon 8060S (`gfx1151`) - **VRAM**: 96GB Unified Memory ### 2. OS...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
