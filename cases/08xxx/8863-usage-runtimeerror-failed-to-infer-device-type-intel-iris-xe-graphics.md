# vllm-project/vllm#8863: [Usage]: RuntimeError: Failed to infer device type (Intel Iris Xe Graphics)

| 字段 | 值 |
| --- | --- |
| Issue | [#8863](https://github.com/vllm-project/vllm/issues/8863) |
| 状态 | closed |
| 标签 | usage;stale |
| 评论 | 10; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | ci_build;hardware_porting;model_support;multimodal_vlm |
| 子分类 |  |
| Operator 关键词 | cuda;triton |
| 症状 | build_error;crash;import_error |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Usage]: RuntimeError: Failed to infer device type (Intel Iris Xe Graphics)

### Issue 正文摘录

### Your current environment ```text Collecting environment information... WARNING 09-26 20:43:46 _custom_ops.py:18] Failed to import from vllm._C with ModuleNotFoundError("No module named 'vllm._C'") INFO 09-26 20:43:46 importing.py:10] Triton not installed; certain GPU-related functions will not be available. C:\Users\sasha\vllm\vllm\vllm\connections.py:8: RuntimeWarning: Failed to read commit hash: No module named 'vllm.commit_id' from vllm.version import __version__ as VLLM_VERSION PyTorch version: 2.4.0+cpu Is debug build: False CUDA used to build PyTorch: None ROCM used to build PyTorch: N/A OS: Microsoft Windows 10 Enterprise GCC version: Could not collect Clang version: Could not collect CMake version: Could not collect Libc version: N/A Python version: 3.10.14 | packaged by Anaconda, Inc. | (main, May 6 2024, 19:44:50) [MSC v.1916 64 bit (AMD64)] (64-bit runtime) Python platform: Windows-10-10.0.19045-SP0 Is CUDA available: False CUDA runtime version: No CUDA CUDA_MODULE_LOADING set to: N/A GPU models and configuration: No CUDA Nvidia driver version: No CUDA cuDNN version: No CUDA HIP runtime version: N/A MIOpen runtime version: N/A Is XNNPACK available: True CPU: Archite...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 7: nment information... WARNING 09-26 20:43:46 _custom_ops.py:18] Failed to import from vllm._C with ModuleNotFoundError("No module named 'vllm._C'") INFO 09-26 20:43:46 importing.py:10] Triton not installed; certain GPU-r...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 5: age;stale ### Your current environment ```text Collecting environment information... WARNING 09-26 20:43:46 _custom_ops.py:18] Failed to import from vllm._C with ModuleNotFoundError("No module named 'vllm._C'") INFO 09-...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 4: rsion__ as VLLM_VERSION PyTorch version: 2.4.0+cpu Is debug build: False CUDA used to build PyTorch: None ROCM used to build PyTorch: N/A OS: Microsoft Windows 10 Enterprise GCC version: Could not collect Clang version:...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: dError("No module named 'vllm._C'") INFO 09-26 20:43:46 importing.py:10] Triton not installed; certain GPU-related functions will not be available. C:\Users\sasha\vllm\vllm\vllm\connections.py:8: RuntimeWarning: Failed...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 1: __version__ as VLLM_VERSION PyTorch version: 2.4.0+cpu Is debug build: False CUDA used to build PyTorch: None ROCM used to build PyTorch: N/A OS: Microsoft Windows 10 Enterprise GCC version: Could not collect Clang vers...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
