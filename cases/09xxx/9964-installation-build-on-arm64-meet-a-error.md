# vllm-project/vllm#9964: [Installation]: build on arm64 meet a error

| 字段 | 值 |
| --- | --- |
| Issue | [#9964](https://github.com/vllm-project/vllm/issues/9964) |
| 状态 | closed |
| 标签 | installation;stale |
| 评论 | 15; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;hardware_porting;model_support;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cuda;operator;sampling;triton |
| 症状 | build_error;crash;import_error;nan_inf |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Installation]: build on arm64 meet a error

### Issue 正文摘录

### Your current environment ```text The output of `python collect_env.py` (pytorch_gpu) ➜ vllm git:(main) ✗ python collect_env.py Collecting environment information... WARNING 11-03 12:55:08 _custom_ops.py:19] Failed to import from vllm._C with ModuleNotFoundError("No module named 'vllm._C'") INFO 11-03 12:55:08 importing.py:15] Triton not installed or not compatible; certain GPU-related functions will not be available. PyTorch version: 2.6.0.dev20241101+cu124 Is debug build: False CUDA used to build PyTorch: 12.4 ROCM used to build PyTorch: N/A OS: openEuler 24.03 (LTS) (aarch64) GCC version: (GCC) 12.3.1 (openEuler 12.3.1-36.oe2403) Clang version: Could not collect CMake version: version 3.30.5 Libc version: glibc-2.38 Python version: 3.10.15 (main, Oct 3 2024, 07:21:53) [GCC 11.2.0] (64-bit runtime) Python platform: Linux-6.6.0-yxk-aarch64-with-glibc2.38 Is CUDA available: True CUDA runtime version: 12.4.131 CUDA_MODULE_LOADING set to: LAZY GPU models and configuration: GPU 0: NVIDIA A100-PCIE-40GB Nvidia driver version: 550.54.15 cuDNN version: Could not collect HIP runtime version: N/A MIOpen runtime version: N/A Is XNNPACK available: True CPU: Architecture: aarch64 CPU op-m...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 11: [Installation]: build on arm64 meet a error installation;stale ### Your current environment ```text The output of `python collect_env.py` (pytorch_gpu) ➜ vllm git:(main) ✗ python collect_env.py Collecting environment in
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 7: vailable. PyTorch version: 2.6.0.dev20241101+cu124 Is debug build: False CUDA used to build PyTorch: 12.4 ROCM used to build PyTorch: N/A OS: openEuler 24.03 (LTS) (aarch64) GCC version: (GCC) 12.3.1 (openEuler 12.3.1-3...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 3: p sve2 sveaes svepmull svebitperm svesha3 svesm4 flagm2 frint svei8mm svebf16 i8mm bf16 dgh rng ecv L1d cache: 8 MiB (128 instances) L1i cache: 16 MiB (128 instances) L2 cache: 128 MiB (128 instances) L3 cache:
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 3: be available. PyTorch version: 2.6.0.dev20241101+cu124 Is debug build: False CUDA used to build PyTorch: 12.4 ROCM used to build PyTorch: N/A OS: openEuler 24.03 (LTS) (aarch64) GCC version: (GCC) 12.3.1 (openEuler 12.3...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: gpu) ➜ vllm git:(main) ✗ python collect_env.py Collecting environment information... WARNING 11-03 12:55:08 _custom_ops.py:19] Failed to import from vllm._C with ModuleNotFoundError("No module named 'vllm._C'") INFO 11-...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
