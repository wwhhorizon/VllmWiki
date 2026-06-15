# vllm-project/vllm#3752: [Usage]: Expected output when prompt_logprobs=1

| 字段 | 值 |
| --- | --- |
| Issue | [#3752](https://github.com/vllm-project/vllm/issues/3752) |
| 状态 | closed |
| 标签 | usage |
| 评论 | 5; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | development |
| 工作域 | ci_build;frontend_api;hardware_porting;model_support;sampling_logits;speculative_decoding |
| 子分类 | env_compat |
| Operator 关键词 | cuda;operator;triton |
| 症状 | build_error |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Usage]: Expected output when prompt_logprobs=1

### Issue 正文摘录

### Your current environment ```text PyTorch version: 2.1.2+cu121 Is debug build: False CUDA used to build PyTorch: 12.1 ROCM used to build PyTorch: N/A OS: Ubuntu 20.04.5 LTS (x86_64) GCC version: (Ubuntu 9.4.0-1ubuntu1~20.04.2) 9.4.0 Clang version: 10.0.0-4ubuntu1 CMake version: version 3.28.3 Libc version: glibc-2.31 Python version: 3.9.18 (main, Sep 11 2023, 13:41:44) [GCC 11.2.0] (64-bit runtime) Python platform: Linux-5.4.0-156-generic-x86_64-with-glibc2.31 Is CUDA available: True CUDA runtime version: 12.1.105 CUDA_MODULE_LOADING set to: LAZY GPU models and configuration: Could not collect Nvidia driver version: Could not collect cuDNN version: Probably one of the following: /usr/local/cuda-11.4/targets/x86_64-linux/lib/libcudnn.so.8.6.0 /usr/local/cuda-11.4/targets/x86_64-linux/lib/libcudnn_adv_infer.so.8.6.0 /usr/local/cuda-11.4/targets/x86_64-linux/lib/libcudnn_adv_train.so.8.6.0 /usr/local/cuda-11.4/targets/x86_64-linux/lib/libcudnn_cnn_infer.so.8.6.0 /usr/local/cuda-11.4/targets/x86_64-linux/lib/libcudnn_cnn_train.so.8.6.0 /usr/local/cuda-11.4/targets/x86_64-linux/lib/libcudnn_ops_infer.so.8.6.0 /usr/local/cuda-11.4/targets/x86_64-linux/lib/libcudnn_ops_train.so.8.6.0...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 6: en prompt_logprobs=1 usage ### Your current environment ```text PyTorch version: 2.1.2+cu121 Is debug build: False CUDA used to build PyTorch: 12.1 ROCM used to build PyTorch: N/A OS: Ubuntu 20.04.5 LTS (x86_64) GCC ver...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 5: environment ```text PyTorch version: 2.1.2+cu121 Is debug build: False CUDA used to build PyTorch: 12.1 ROCM used to build PyTorch: N/A OS: Ubuntu 20.04.5 LTS (x86_64) GCC version: (Ubuntu 9.4.0-1ubuntu1~20.04.2) 9.4.0...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: True CUDA runtime version: 12.1.105 CUDA_MODULE_LOADING set to: LAZY GPU models and configuration: Could not collect Nvidia driver version: Could not collect cuDNN version: Probably one of the following: /usr/local/cuda...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 3: ffected Vulnerability Meltdown: Not affected Vulnerability Mmio stale data: Mitigation; Clear CPU buffers; SMT vulnerable Vulnerability Retbleed: Not affected Vulnerability Spec store bypass: Mitigation; Speculative Sto...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: s of relevant libraries: [pip3] numpy==1.26.4 [pip3] torch==2.1.2 [pip3] triton==2.1.0 [conda] numpy 1.26.4 py39h474f0d3_0 conda-forge [conda] pytorch-cuda 12.1 ha16c6d3_5 pytorch [conda] torch 2.1.2

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
