# vllm-project/vllm#8031: [Usage]: How can I determine the maximum number of concurrent requests?

| 字段 | 值 |
| --- | --- |
| Issue | [#8031](https://github.com/vllm-project/vllm/issues/8031) |
| 状态 | closed |
| 标签 | usage;stale |
| 评论 | 14; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | ci_build;distributed_parallel;frontend_api;hardware_porting;model_support |
| 子分类 | throughput |
| Operator 关键词 | cuda;operator;triton |
| 症状 | build_error;oom |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Usage]: How can I determine the maximum number of concurrent requests?

### Issue 正文摘录

### Your current environment ```text PyTorch version: 2.3.0+cu121 Is debug build: False CUDA used to build PyTorch: 12.1 ROCM used to build PyTorch: N/A OS: Ubuntu 18.04.1 LTS (x86_64) GCC version: (Ubuntu 7.5.0-3ubuntu1~18.04) 7.5.0 Clang version: Could not collect CMake version: version 3.29.5 Libc version: glibc-2.27 Python version: 3.10.14 (main, May 6 2024, 19:42:50) [GCC 11.2.0] (64-bit runtime) Python platform: Linux-4.15.0-29-generic-x86_64-with-glibc2.27 Is CUDA available: True CUDA runtime version: Could not collect CUDA_MODULE_LOADING set to: LAZY GPU models and configuration: GPU 0: Tesla V100-PCIE-32GB GPU 1: Tesla V100-PCIE-32GB GPU 2: Tesla V100-PCIE-32GB GPU 3: Tesla V100-PCIE-32GB GPU 4: Tesla V100-PCIE-32GB GPU 5: Tesla V100-PCIE-32GB GPU 6: Tesla V100-PCIE-32GB GPU 7: Tesla V100-PCIE-32GB Nvidia driver version: 535.129.03 cuDNN version: Probably one of the following: /home/username/cuda/cuda-11.8/targets/x86_64-linux/lib/libcudnn.so.8.6.0 /home/username/cuda/cuda-11.8/targets/x86_64-linux/lib/libcudnn_adv_infer.so.8.6.0 /home/username/cuda/cuda-11.8/targets/x86_64-linux/lib/libcudnn_adv_train.so.8.6.0 /home/username/cuda/cuda-11.8/targets/x86_64-linux/lib/libcud...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 7: rent requests? usage;stale ### Your current environment ```text PyTorch version: 2.3.0+cu121 Is debug build: False CUDA used to build PyTorch: 12.1 ROCM used to build PyTorch: N/A OS: Ubuntu 18.04.1 LTS (x86_64) GCC ver...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 5: environment ```text PyTorch version: 2.3.0+cu121 Is debug build: False CUDA used to build PyTorch: 12.1 ROCM used to build PyTorch: N/A OS: Ubuntu 18.04.1 LTS (x86_64) GCC version: (Ubuntu 7.5.0-3ubuntu1~18.04) 7.5.0 Cl...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: runtime version: Could not collect CUDA_MODULE_LOADING set to: LAZY GPU models and configuration: GPU 0: Tesla V100-PCIE-32GB GPU 1: Tesla V100-PCIE-32GB GPU 2: Tesla V100-PCIE-32GB GPU 3: Tesla V100-PCIE-32GB GPU 4: Te...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: [Usage]: How can I determine the maximum number of concurrent requests? usage;stale ### Your current environment ```text PyTorch version: 2.3.0+cu121 Is debug build: False CUDA used to build PyTorch: 12.1 ROCM used to b...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 2: e GPU requirements for a knowledge base application scenario. Given that evaluating GPU resources differs significantly from traditional IT architecture assessments, I hope you can provide me with more guidance. Thank y...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
