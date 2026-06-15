# vllm-project/vllm#36302: [Installation]: undefined symbol: _ZN3c104cuda29c10_cuda_check_implementationEiPKcS2_jb

| 字段 | 值 |
| --- | --- |
| Issue | [#36302](https://github.com/vllm-project/vllm/issues/36302) |
| 状态 | open |
| 标签 | installation |
| 评论 | 14; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | ci_build;hardware_porting;quantization |
| 子分类 |  |
| Operator 关键词 | cuda;fp8 |
| 症状 | build_error;slowdown |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Installation]: undefined symbol: _ZN3c104cuda29c10_cuda_check_implementationEiPKcS2_jb

### Issue 正文摘录

### Your current environment ```text ============================== PyTorch Info ============================== PyTorch version : 2.9.1+cu130 Is debug build : False CUDA used to build PyTorch : 13.0 ROCM used to build PyTorch : N/A ============================== Python Environment ============================== Python version : 3.13.12 | packaged by Anaconda, Inc. | (main, Feb 24 2026, 16:13:31) [GCC 14.3.0] (64-bit runtime) Python platform : Linux-5.14.0-570.62.1.el9_6.x86_64-x86_64-with-glibc2.34 ============================== CUDA / GPU Info ============================== Is CUDA available : True CUDA runtime version : 13.0.88 CUDA_MODULE_LOADING set to : GPU models and configuration : GPU 0: NVIDIA H200 ============================== vLLM Info ============================== ROCM Version : Could not collect vLLM Version : 0.15.1 ``` ### How you are installing vllm ```sh git checkout tags/v0.15.1 VLLM_USE_PRECOMPILED=1 uv pip install -e . ``` Then when running ```sh vllm serve Qwen/Qwen3-32B-FP8 ``` It reports ``` undefined symbol: _ZN3c104cuda29c10_cuda_check_implementationEiPKcS2_jb ``` I checked by `ldd ./vllm/_C.abi3.so` and all libraries can be detected. I also tried `VLLM_...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 8: [Installation]: undefined symbol: _ZN3c104cuda29c10_cuda_check_implementationEiPKcS2_jb installation ### Your current environment ```text ============================== PyTorch Info ==============================
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 3: pip install -e . ``` Then when running ```sh vllm serve Qwen/Qwen3-32B-FP8 ``` It reports ``` undefined symbol: _ZN3c104cuda29c10_cuda_check_implementationEiPKcS2_jb ``` I checked by `ldd ./vllm/_C.abi3.so` and all libr...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: [Installation]: undefined symbol: _ZN3c104cuda29c10_cuda_check_implementationEiPKcS2_jb installation ### Your current environment ```text ============================== PyTorch Info ============================== PyTorc...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: UDA runtime version : 13.0.88 CUDA_MODULE_LOADING set to : GPU models and configuration : GPU 0: NVIDIA H200 ============================== vLLM Info ============================== ROCM Version : Could not collect vLLM...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 1: orch version : 2.9.1+cu130 Is debug build : False CUDA used to build PyTorch : 13.0 ROCM used to build PyTorch : N/A ============================== Python Environment ============================== Python version : 3.13...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
