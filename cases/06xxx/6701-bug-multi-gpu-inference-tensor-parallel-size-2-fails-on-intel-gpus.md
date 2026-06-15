# vllm-project/vllm#6701: [Bug]: multi-GPU inference (tensor_parallel_size=2) fails on Intel GPUs

| 字段 | 值 |
| --- | --- |
| Issue | [#6701](https://github.com/vllm-project/vllm/issues/6701) |
| 状态 | closed |
| 标签 | bug;ray;stale |
| 评论 | 15; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;quantization;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cuda;operator;quantization;sampling;triton |
| 症状 | build_error;crash;import_error;nan_inf |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: multi-GPU inference (tensor_parallel_size=2) fails on Intel GPUs

### Issue 正文摘录

### Your current environment ```text Collecting environment information... WARNING 07-23 19:11:42 _custom_ops.py:14] Failed to import from vllm._C with ModuleNotFoundError("No module named 'vllm._C'") PyTorch version: 2.1.0.post1+cxx11.abi Is debug build: False CUDA used to build PyTorch: None ROCM used to build PyTorch: N/A OS: openSUSE Leap 15.4 (x86_64) GCC version: (Spack GCC) 11.4.0 Clang version: Could not collect CMake version: version 3.30.1 Libc version: glibc-2.31 Python version: 3.10.14 (main, May 6 2024, 19:42:50) [GCC 11.2.0] (64-bit runtime) Python platform: Linux-5.14.21-150400.24.100-default-x86_64-with-glibc2.31 Is CUDA available: False CUDA runtime version: No CUDA CUDA_MODULE_LOADING set to: N/A GPU models and configuration: No CUDA Nvidia driver version: No CUDA cuDNN version: No CUDA HIP runtime version: N/A MIOpen runtime version: N/A Is XNNPACK available: True CPU: Architecture: x86_64 CPU op-mode(s): 32-bit, 64-bit Address sizes: 52 bits physical, 57 bits virtual Byte Order: Little Endian CPU(s): 208 On-line CPU(s) list: 0-207 Vendor ID: GenuineIntel Model name: Intel (R) Xeon (R) CPU Max 9470C CPU family: 6 Model: 143 Thread(s) per core: 2 Core(s) per sock...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 7: nment information... WARNING 07-23 19:11:42 _custom_ops.py:14] Failed to import from vllm._C with ModuleNotFoundError("No module named 'vllm._C'") PyTorch version: 2.1.0.post1+cxx11.abi Is debug build: False CUDA used t...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 5: 'vllm._C'") PyTorch version: 2.1.0.post1+cxx11.abi Is debug build: False CUDA used to build PyTorch: None ROCM used to build PyTorch: N/A OS: openSUSE Leap 15.4 (x86_64) GCC version: (Spack GCC) 11.4.0 Clang version: Co...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 4: _occup_llc cqm_mbm_total cqm_mbm_local split_lock_detect avx_vnni avx512_bf16 wbnoinvd dtherm ida arat pln pts hwp hwp_act_window hwp_epp hwp_pkg_req avx512vbmi umip pku ospke waitpkg avx512_vbmi2 gfni vaes vpclmulqdq a...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: ray;stale ### Your current environment ```text Collecting environment information... WARNING 07-23 19:11:42 _custom_ops.py:14] Failed to import from vllm._C with ModuleNotFoundError("No module named 'vllm._C'") PyTorch...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 3: multi-GPU inference (tensor_parallel_size=2) fails on Intel GPUs bug;ray;stale ### Your current environment ```text Collecting environment information... WARNING 07-23 19:11:42 _custom_ops.py:14] Failed to import from v...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
