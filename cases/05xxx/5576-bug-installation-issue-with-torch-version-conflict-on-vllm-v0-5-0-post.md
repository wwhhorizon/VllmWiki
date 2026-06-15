# vllm-project/vllm#5576: [Bug]: Installation Issue with torch Version Conflict on vllm v0.5.0.post1

| 字段 | 值 |
| --- | --- |
| Issue | [#5576](https://github.com/vllm-project/vllm/issues/5576) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 6; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | development |
| 工作域 | ci_build;hardware_porting;model_support;sampling_logits;speculative_decoding |
| 子分类 | env_compat |
| Operator 关键词 | cuda;operator;sampling |
| 症状 | build_error |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Installation Issue with torch Version Conflict on vllm v0.5.0.post1

### Issue 正文摘录

### Your current environment ```text Collecting environment information... PyTorch version: 2.3.1 Is debug build: False CUDA used to build PyTorch: 12.1 ROCM used to build PyTorch: N/A OS: Ubuntu 22.04.2 LTS (x86_64) GCC version: (Ubuntu 11.3.0-1ubuntu1~22.04.1) 11.3.0 Clang version: Could not collect CMake version: Could not collect Libc version: glibc-2.35 Python version: 3.12.3 | packaged by Anaconda, Inc. | (main, May 6 2024, 19:46:43) [GCC 11.2.0] (64-bit runtime) Python platform: Linux-5.4.0-165-generic-x86_64-with-glibc2.35 Is CUDA available: True CUDA runtime version: Could not collect CUDA_MODULE_LOADING set to: LAZY GPU models and configuration: GPU 0: NVIDIA A800-SXM4-80GB Nvidia driver version: 535.54.03 cuDNN version: Probably one of the following: /usr/lib/x86_64-linux-gnu/libcudnn.so.8.9.0 /usr/lib/x86_64-linux-gnu/libcudnn_adv_infer.so.8.9.0 /usr/lib/x86_64-linux-gnu/libcudnn_adv_train.so.8.9.0 /usr/lib/x86_64-linux-gnu/libcudnn_cnn_infer.so.8.9.0 /usr/lib/x86_64-linux-gnu/libcudnn_cnn_train.so.8.9.0 /usr/lib/x86_64-linux-gnu/libcudnn_ops_infer.so.8.9.0 /usr/lib/x86_64-linux-gnu/libcudnn_ops_train.so.8.9.0 HIP runtime version: N/A MIOpen runtime version: N/A Is XNN...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 8: [Bug]: Installation Issue with torch Version Conflict on vllm v0.5.0.post1 bug ### Your current environment ```text Collecting environment information... PyTorch version: 2.3.1 Is debug build: False CUDA used to build P...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 5: environment information... PyTorch version: 2.3.1 Is debug build: False CUDA used to build PyTorch: 12.1 ROCM used to build PyTorch: N/A OS: Ubuntu 22.04.2 LTS (x86_64) GCC version: (Ubuntu 11.3.0-1ubuntu1~22.04.1) 11.3...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: post1 bug ### Your current environment ```text Collecting environment information... PyTorch version: 2.3.1 Is debug build: False CUDA used to build PyTorch: 12.1 ROCM used to build PyTorch: N/A OS: Ubuntu 22.04.2 LTS (...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: cted Vulnerability Meltdown: Not affected Vulnerability Mmio stale data: Mitigation; Clear CPU buffers; SMT disabled Vulnerability Retbleed: Not affected Vulnerability Spec store bypass: Mitigation; Speculative Store By...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 1: ting environment information... PyTorch version: 2.3.1 Is debug build: False CUDA used to build PyTorch: 12.1 ROCM used to build PyTorch: N/A OS: Ubuntu 22.04.2 LTS (x86_64) GCC version: (Ubuntu 11.3.0-1ubuntu1~22.04.1)...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
