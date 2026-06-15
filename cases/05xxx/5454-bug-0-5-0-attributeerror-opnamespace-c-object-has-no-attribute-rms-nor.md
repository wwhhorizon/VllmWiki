# vllm-project/vllm#5454: [Bug]: 0.5.0 AttributeError: '_OpNamespace' '_C' object has no attribute 'rms_norm'

| 字段 | 值 |
| --- | --- |
| Issue | [#5454](https://github.com/vllm-project/vllm/issues/5454) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 21; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | development |
| 工作域 | activation_norm;ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;speculative_decoding |
| 子分类 | env_compat |
| Operator 关键词 | activation;cuda;operator;triton |
| 症状 | build_error;crash |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: 0.5.0 AttributeError: '_OpNamespace' '_C' object has no attribute 'rms_norm'

### Issue 正文摘录

### Your current environment ``` Collecting environment information... PyTorch version: 2.3.0+cu121 Is debug build: False CUDA used to build PyTorch: 12.1 ROCM used to build PyTorch: N/A OS: Ubuntu 22.04.2 LTS (x86_64) GCC version: (Ubuntu 11.3.0-1ubuntu1~22.04.1) 11.3.0 Clang version: Could not collect CMake version: version 3.29.5 Libc version: glibc-2.35 Python version: 3.10.14 | packaged by conda-forge | (main, Mar 20 2024, 12:45:18) [GCC 12.3.0] (64-bit runtime) Python platform: Linux-5.10.134-13.an8.x86_64-x86_64-with-glibc2.35 Is CUDA available: True CUDA runtime version: 12.1.105 CUDA_MODULE_LOADING set to: LAZY GPU models and configuration: GPU 0: NVIDIA L40S GPU 1: NVIDIA L40S GPU 2: NVIDIA L40S GPU 3: NVIDIA L40S Nvidia driver version: 535.129.03 cuDNN version: Probably one of the following: /usr/lib/x86_64-linux-gnu/libcudnn.so.8.9.3 /usr/lib/x86_64-linux-gnu/libcudnn_adv_infer.so.8.9.3 /usr/lib/x86_64-linux-gnu/libcudnn_adv_train.so.8.9.3 /usr/lib/x86_64-linux-gnu/libcudnn_cnn_infer.so.8.9.3 /usr/lib/x86_64-linux-gnu/libcudnn_cnn_train.so.8.9.3 /usr/lib/x86_64-linux-gnu/libcudnn_ops_infer.so.8.9.3 /usr/lib/x86_64-linux-gnu/libcudnn_ops_train.so.8.9.3 HIP runtime versi...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 7: r current environment ``` Collecting environment information... PyTorch version: 2.3.0+cu121 Is debug build: False CUDA used to build PyTorch: 12.1 ROCM used to build PyTorch: N/A OS: Ubuntu 22.04.2 LTS (x86_64) GCC ver...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 5: onment information... PyTorch version: 2.3.0+cu121 Is debug build: False CUDA used to build PyTorch: 12.1 ROCM used to build PyTorch: N/A OS: Ubuntu 22.04.2 LTS (x86_64) GCC version: (Ubuntu 11.3.0-1ubuntu1~22.04.1) 11....
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 5: rms_norm' bug ### Your current environment ``` Collecting environment information... PyTorch version: 2.3.0+cu121 Is debug build: False CUDA used to build PyTorch: 12.1 ROCM used to build PyTorch: N/A OS: Ubuntu 22.04.2...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 2: nvironment information... PyTorch version: 2.3.0+cu121 Is debug build: False CUDA used to build PyTorch: 12.1 ROCM used to build PyTorch: N/A OS: Ubuntu 22.04.2 LTS (x86_64) GCC version: (Ubuntu 11.3.0-1ubuntu1~22.04.1)...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: ffected Vulnerability Meltdown: Not affected Vulnerability Mmio stale data: Not affected Vulnerability Retbleed: Not affected Vulnerability Spec store bypass: Mitigation; Speculative Store Bypass disabled via prctl and...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
