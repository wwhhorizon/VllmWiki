# vllm-project/vllm#12715: [Usage]: How to get class labels when `task=classify`?

| 字段 | 值 |
| --- | --- |
| Issue | [#12715](https://github.com/vllm-project/vllm/issues/12715) |
| 状态 | closed |
| 标签 | usage |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;hardware_porting;model_support;sampling_logits |
| 子分类 | precision |
| Operator 关键词 | cuda;operator;sampling |
| 症状 | build_error;nan_inf |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Usage]: How to get class labels when `task=classify`?

### Issue 正文摘录

### Your current environment ```text 2025-02-03 23:31:24.987378: E external/local_xla/xla/stream_executor/cuda/cuda_fft.cc:485] Unable to register cuFFT factory: Attempting to register factory for plugin cuFFT when one has already been registered 2025-02-03 23:31:25.008825: E external/local_xla/xla/stream_executor/cuda/cuda_dnn.cc:8454] Unable to register cuDNN factory: Attempting to register factory for plugin cuDNN when one has already been registered 2025-02-03 23:31:25.014917: E external/local_xla/xla/stream_executor/cuda/cuda_blas.cc:1452] Unable to register cuBLAS factory: Attempting to register factory for plugin cuBLAS when one has already been registered 2025-02-03 23:31:26.415478: W tensorflow/compiler/tf2tensorrt/utils/py_utils.cc:38] TF-TRT Warning: Could not find TensorRT INFO 02-03 23:31:27 __init__.py:183] Automatically detected platform cuda. Collecting environment information... PyTorch version: 2.5.1+cu121 Is debug build: False CUDA used to build PyTorch: 12.1 ROCM used to build PyTorch: N/A OS: Ubuntu 22.04.3 LTS (x86_64) GCC version: (Ubuntu 11.4.0-1ubuntu1~22.04) 11.4.0 Clang version: 14.0.0-1ubuntu1.1 CMake version: version 3.31.2 Libc version: glibc-2.35 Pyt...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 9: one has already been registered 2025-02-03 23:31:26.415478: W tensorflow/compiler/tf2tensorrt/utils/py_utils.cc:38] TF-TRT Warning: Could not find TensorRT INFO 02-03 23:31:27 __init__.py:183] Automatically detected pla...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 5: ext 2025-02-03 23:31:24.987378: E external/local_xla/xla/stream_executor/cuda/cuda_fft.cc:485] Unable to register cuFFT factory: Attempting to register factory for plugin cuFFT when one has already been registered 2025-...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 5: _.py:183] Automatically detected platform cuda. Collecting environment information... PyTorch version: 2.5.1+cu121 Is debug build: False CUDA used to build PyTorch: 12.1 ROCM used to build PyTorch: N/A OS: Ubuntu 22.04....
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: nown Vulnerability Meltdown: Vulnerable Vulnerability Mmio stale data: Vulnerable Vulnerability Reg file data sampling: Not affected Vulnerability Retbleed: Vulnerable Vulnerability Spec rstack overflow: Not affected Vu...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 1: nvironment information... PyTorch version: 2.5.1+cu121 Is debug build: False CUDA used to build PyTorch: 12.1 ROCM used to build PyTorch: N/A OS: Ubuntu 22.04.3 LTS (x86_64) GCC version: (Ubuntu 11.4.0-1ubuntu1~22.04) 1...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
