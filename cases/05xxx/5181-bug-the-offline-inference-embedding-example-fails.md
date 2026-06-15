# vllm-project/vllm#5181: [Bug]: The Offline Inference Embedding Example Fails

| 字段 | 值 |
| --- | --- |
| Issue | [#5181](https://github.com/vllm-project/vllm/issues/5181) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 6; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;hardware_porting;model_support;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cuda;operator;sampling;triton |
| 症状 | build_error;crash;nan_inf |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: The Offline Inference Embedding Example Fails

### Issue 正文摘录

### Your current environment ```text Collecting environment information... PyTorch version: 2.3.0 Is debug build: False CUDA used to build PyTorch: 11.8 ROCM used to build PyTorch: N/A OS: Ubuntu 20.04.6 LTS (x86_64) GCC version: (Ubuntu 9.4.0-1ubuntu1~20.04.2) 9.4.0 Clang version: Could not collect CMake version: version 3.29.3 Libc version: glibc-2.31 Python version: 3.10.14 (main, May 6 2024, 19:42:50) [GCC 11.2.0] (64-bit runtime) Python platform: Linux-5.15.0-106-generic-x86_64-with-glibc2.31 Is CUDA available: True CUDA runtime version: 12.5.40 CUDA_MODULE_LOADING set to: LAZY GPU models and configuration: GPU 0: NVIDIA RTX A6000 GPU 1: NVIDIA RTX 6000 Ada Generation GPU 2: NVIDIA RTX A6000 GPU 3: NVIDIA RTX 6000 Ada Generation Nvidia driver version: 550.54.15 cuDNN version: Probably one of the following: /usr/lib/x86_64-linux-gnu/libcudnn.so.8.9.7 /usr/lib/x86_64-linux-gnu/libcudnn_adv_infer.so.8.9.7 /usr/lib/x86_64-linux-gnu/libcudnn_adv_train.so.8.9.7 /usr/lib/x86_64-linux-gnu/libcudnn_cnn_infer.so.8.9.7 /usr/lib/x86_64-linux-gnu/libcudnn_cnn_train.so.8.9.7 /usr/lib/x86_64-linux-gnu/libcudnn_ops_infer.so.8.9.7 /usr/lib/x86_64-linux-gnu/libcudnn_ops_train.so.8.9.7 HIP runt...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 8: rrent environment ```text Collecting environment information... PyTorch version: 2.3.0 Is debug build: False CUDA used to build PyTorch: 11.8 ROCM used to build PyTorch: N/A OS: Ubuntu 20.04.6 LTS (x86_64) GCC version:...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 6: environment information... PyTorch version: 2.3.0 Is debug build: False CUDA used to build PyTorch: 11.8 ROCM used to build PyTorch: N/A OS: Ubuntu 20.04.6 LTS (x86_64) GCC version: (Ubuntu 9.4.0-1ubuntu1~20.04.2) 9.4.0...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: Fails bug ### Your current environment ```text Collecting environment information... PyTorch version: 2.3.0 Is debug build: False CUDA used to build PyTorch: 11.8 ROCM used to build PyTorch: N/A OS: Ubuntu 20.04.6 LTS (...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 3: cted Vulnerability Meltdown: Not affected Vulnerability Mmio stale data: Not affected Vulnerability Retbleed: Not affected Vulnerability Spec rstack overflow: Mitigation; safe RET Vulnerability Spec store bypass: Mitiga...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 2: ting environment information... PyTorch version: 2.3.0 Is debug build: False CUDA used to build PyTorch: 11.8 ROCM used to build PyTorch: N/A OS: Ubuntu 20.04.6 LTS (x86_64) GCC version: (Ubuntu 9.4.0-1ubuntu1~20.04.2)...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
