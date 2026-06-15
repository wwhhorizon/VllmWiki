# vllm-project/vllm#9694: [Usage]: GetTimeoutError when run distributed inference on ray with tensor parallel size > 1

| 字段 | 值 |
| --- | --- |
| Issue | [#9694](https://github.com/vllm-project/vllm/issues/9694) |
| 状态 | closed |
| 标签 | usage |
| 评论 | 0; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cuda;operator;sampling;triton |
| 症状 | build_error;crash;nan_inf;oom |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Usage]: GetTimeoutError when run distributed inference on ray with tensor parallel size > 1

### Issue 正文摘录

### Your current environment ```text $ python collect_env.py Collecting environment information... 2024-10-25 11:12:58.116681: E external/local_xla/xla/stream_executor/cuda/cuda_fft.cc:485] Unable to register cuFFT factory: Attempting to register factory for plugin cuFFT when one has already been registered 2024-10-25 11:12:58.167780: E external/local_xla/xla/stream_executor/cuda/cuda_dnn.cc:8454] Unable to register cuDNN factory: Attempting to register factory for plugin cuDNN when one has already been registered 2024-10-25 11:12:58.183402: E external/local_xla/xla/stream_executor/cuda/cuda_blas.cc:1452] Unable to register cuBLAS factory: Attempting to register factory for plugin cuBLAS when one has already been registered 2024-10-25 11:12:58.215052: I tensorflow/core/platform/cpu_feature_guard.cc:210] This TensorFlow binary is optimized to use available CPU instructions in performance-critical operations. To enable the following instructions: AVX2 AVX512F FMA, in other operations, rebuild TensorFlow with the appropriate compiler flags. 2024-10-25 11:12:59.873142: W tensorflow/compiler/tf2tensorrt/utils/py_utils.cc:38] TF-TRT Warning: Could not find TensorRT PyTorch version: 2.4....

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 8: ble the following instructions: AVX2 AVX512F FMA, in other operations, rebuild TensorFlow with the appropriate compiler flags. 2024-10-25 11:12:59.873142: W tensorflow/compiler/tf2tensorrt/utils/py_utils.cc:38] TF-TRT W...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 5: ... 2024-10-25 11:12:58.116681: E external/local_xla/xla/stream_executor/cuda/cuda_fft.cc:485] Unable to register cuFFT factory: Attempting to register factory for plugin cuFFT when one has already been registered 2024-...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 5: nt environment ```text $ python collect_env.py Collecting environment information... 2024-10-25 11:12:58.116681: E external/local_xla/xla/stream_executor/cuda/cuda_fft.cc:485] Unable to register cuFFT factory: Attemptin...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 3: : Could not find TensorRT PyTorch version: 2.4.0+cu121 Is debug build: False CUDA used to build PyTorch: 12.1 ROCM used to build PyTorch: N/A OS: Ubuntu 22.04.4 LTS (x86_64) GCC version: (Ubuntu 11.4.0-1ubuntu1~22.04) 1...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 3: Vulnerability Meltdown: Mitigation; PTI Vulnerability Mmio stale data: Mitigation; Clear CPU buffers; SMT Host state unknown Vulnerability Reg file data sampling: Not affected Vulnerability Retbleed: Mitigation; IBRS Vu...

## Wiki 抽取状态

- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
