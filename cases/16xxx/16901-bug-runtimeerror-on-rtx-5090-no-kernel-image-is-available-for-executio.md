# vllm-project/vllm#16901: [Bug]: RuntimeError on RTX 5090: "no kernel image is available for execution on the device

| 字段 | 值 |
| --- | --- |
| Issue | [#16901](https://github.com/vllm-project/vllm/issues/16901) |
| 状态 | closed |
| 标签 | installation |
| 评论 | 29; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | development |
| 工作域 | ci_build;frontend_api |
| 子分类 | env_compat |
| Operator 关键词 | cuda;kernel |
| 症状 | build_error |
| 根因提示 | env_dependency |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: RuntimeError on RTX 5090: "no kernel image is available for execution on the device

### Issue 正文摘录

### Your current environment ### Describe the bug When running [vLLM.log](https://github.com/user-attachments/files/19829093/vLLM.log) with a NVIDIA RTX 5090 GPU, I encountered the following error: RuntimeError: CUDA error: no kernel image is available for execution on the device From the logs, it seems that PyTorch does not support the compute capability of the RTX 5090 (sm_120): ### To Reproduce 1. Use RTX 5090 GPU 2. Install vLLM with Docker or system Python environment 3. Launch the vLLM OpenAI API server 4. Engine fails to start due to CUDA kernel compatibility issue ### Environment - **GPU**: NVIDIA GeForce RTX 5090 - **CUDA Driver Version**: 12.8 - **CUDA Toolkit**: 12.8.93 - **NVIDIA Driver**: 570.124.06 - **PyTorch Version**: 2.x (installed via pip) - **vLLM Version**: Latest (from PyPI) - **Python Version**: 3.10 - **OS**: Ubuntu 22.04 ### Additional Context It seems that the RTX 5090 uses a new compute capability (`sm_120`), which is currently not supported in the stable PyTorch build I'm using. Is there a recommended way to run vLLM with this GPU? Should I: - Switch to a nightly PyTorch build that supports sm_120? - Build PyTorch from source with `TORCH_CUDA_ARCH_LIST=...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 6: r on RTX 5090: "no kernel image is available for execution on the device installation ### Your current environment ### Describe the bug When running [vLLM.log](https://github.com/user-attachments/files/19829093/vLLM.log...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 5: [Bug]: RuntimeError on RTX 5090: "no kernel image is available for execution on the device installation ### Your current environment ### Describe the bug When running [vLLM.log](https://github.com/user-attachments/files...
- [Bitwise 确定性与数值等价](../patterns/bitwise_determinism_equivalence.md) - 分数 1: oes not support the compute capability of the RTX 5090 (sm_120): ### To Reproduce 1. Use RTX 5090 GPU 2. Install vLLM with Docker or system Python environment 3. Launch the vLLM OpenAI API server 4. Engine fails to star...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: .06 - **PyTorch Version**: 2.x (installed via pip) - **vLLM Version**: Latest (from PyPI) - **Python Version**: 3.10 - **OS**: Ubuntu 22.04 ### Additional Context It seems that the RTX 5090 uses a new compute capability...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
