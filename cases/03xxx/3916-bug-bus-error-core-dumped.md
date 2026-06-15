# vllm-project/vllm#3916: [Bug]: bus error (core dumped)

| 字段 | 值 |
| --- | --- |
| Issue | [#3916](https://github.com/vllm-project/vllm/issues/3916) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 16; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;hardware_porting;model_support;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cuda;operator;sampling;triton |
| 症状 | build_error;nan_inf |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: bus error (core dumped)

### Issue 正文摘录

### Your current environment ```text Collecting environment information... PyTorch version: 2.2.1+cu121 Is debug build: False CUDA used to build PyTorch: 12.1 ROCM used to build PyTorch: N/A OS: Ubuntu 20.04.5 LTS (x86_64) GCC version: (Ubuntu 9.4.0-1ubuntu1~20.04.2) 9.4.0 Clang version: Could not collect CMake version: version 3.26.0 Libc version: glibc-2.31 Python version: 3.10.13 (main, Sep 11 2023, 13:44:35) [GCC 11.2.0] (64-bit runtime) Python platform: Linux-5.15.0-89-generic-x86_64-with-glibc2.31 Is CUDA available: True CUDA runtime version: 12.1.105 CUDA_MODULE_LOADING set to: LAZY GPU models and configuration: GPU 0: NVIDIA GeForce RTX 3090 Nvidia driver version: 535.129.03 cuDNN version: Probably one of the following: /usr/local/cuda-12.1/targets/x86_64-linux/lib/libcudnn.so.8 /usr/local/cuda-12.1/targets/x86_64-linux/lib/libcudnn_adv_infer.so.8 /usr/local/cuda-12.1/targets/x86_64-linux/lib/libcudnn_adv_train.so.8 /usr/local/cuda-12.1/targets/x86_64-linux/lib/libcudnn_cnn_infer.so.8 /usr/local/cuda-12.1/targets/x86_64-linux/lib/libcudnn_cnn_train.so.8 /usr/local/cuda-12.1/targets/x86_64-linux/lib/libcudnn_ops_infer.so.8 /usr/local/cuda-12.1/targets/x86_64-linux/lib/libcu...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 7: rrent environment ```text Collecting environment information... PyTorch version: 2.2.1+cu121 Is debug build: False CUDA used to build PyTorch: 12.1 ROCM used to build PyTorch: N/A OS: Ubuntu 20.04.5 LTS (x86_64) GCC ver...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 6: onment information... PyTorch version: 2.2.1+cu121 Is debug build: False CUDA used to build PyTorch: 12.1 ROCM used to build PyTorch: N/A OS: Ubuntu 20.04.5 LTS (x86_64) GCC version: (Ubuntu 9.4.0-1ubuntu1~20.04.2) 9.4....
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: mped) bug ### Your current environment ```text Collecting environment information... PyTorch version: 2.2.1+cu121 Is debug build: False CUDA used to build PyTorch: 12.1 ROCM used to build PyTorch: N/A OS: Ubuntu 20.04.5...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: e Vulnerability Meltdown: Mitigation; PTI Vulnerability Mmio stale data: Mitigation; Clear CPU buffers; SMT vulnerable Vulnerability Retbleed: Not affected Vulnerability Spec rstack overflow: Not affected Vulnerability...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 2: tensions==1.0.0 [pip3] numpy==1.26.4 [pip3] torch==2.2.1 [pip3] torch-tb-profiler==0.4.3 [pip3] triton==2.2.0 [conda] numpy 1.26.4 pypi_0 pypi [conda] torch 2.2.1 pypi_0 pypi [conda] torch-tb-profiler 0

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
