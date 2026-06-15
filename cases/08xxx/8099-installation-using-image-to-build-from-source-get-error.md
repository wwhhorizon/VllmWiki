# vllm-project/vllm#8099: [Installation]: Using Image to build from source get error

| 字段 | 值 |
| --- | --- |
| Issue | [#8099](https://github.com/vllm-project/vllm/issues/8099) |
| 状态 | closed |
| 标签 | installation;stale |
| 评论 | 6; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;gemm_linear;hardware_porting;model_support;quantization;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cuda;operator;quantization;sampling;triton |
| 症状 | build_error;crash;nan_inf |
| 根因提示 | env_dependency;memory_layout |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Installation]: Using Image to build from source get error

### Issue 正文摘录

### Your current environment ```text Collecting environment information... PyTorch version: 2.1.0a0+32f93b1 Is debug build: False CUDA used to build PyTorch: 12.2 ROCM used to build PyTorch: N/A OS: Ubuntu 22.04.3 LTS (x86_64) GCC version: (Ubuntu 11.4.0-1ubuntu1~22.04) 11.4.0 Clang version: Could not collect CMake version: version 3.27.6 Libc version: glibc-2.35 Python version: 3.10.12 (main, Jun 11 2023, 05:26:28) [GCC 11.4.0] (64-bit runtime) Python platform: Linux-5.15.153.1-2.cm2-x86_64-with-glibc2.35 Is CUDA available: True CUDA runtime version: 12.2.140 CUDA_MODULE_LOADING set to: LAZY GPU models and configuration: GPU 0: NVIDIA A16 GPU 1: NVIDIA A16 Nvidia driver version: 550.54.15 cuDNN version: Probably one of the following: /usr/lib/x86_64-linux-gnu/libcudnn.so.8.9.5 /usr/lib/x86_64-linux-gnu/libcudnn_adv_infer.so.8.9.5 /usr/lib/x86_64-linux-gnu/libcudnn_adv_train.so.8.9.5 /usr/lib/x86_64-linux-gnu/libcudnn_cnn_infer.so.8.9.5 /usr/lib/x86_64-linux-gnu/libcudnn_cnn_train.so.8.9.5 /usr/lib/x86_64-linux-gnu/libcudnn_ops_infer.so.8.9.5 /usr/lib/x86_64-linux-gnu/libcudnn_ops_train.so.8.9.5 HIP runtime version: N/A MIOpen runtime version: N/A Is XNNPACK available: True CPU: A...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 11: [Installation]: Using Image to build from source get error installation;stale ### Your current environment ```text Collecting environment information... PyTorch version: 2.1.0a0+32f93b1 Is debug build: False CUDA used to
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 5: nt information... PyTorch version: 2.1.0a0+32f93b1 Is debug build: False CUDA used to build PyTorch: 12.2 ROCM used to build PyTorch: N/A OS: Ubuntu 22.04.3 LTS (x86_64) GCC version: (Ubuntu 11.4.0-1ubuntu1~22.04) 11.4....
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 4: onment information... PyTorch version: 2.1.0a0+32f93b1 Is debug build: False CUDA used to build PyTorch: 12.2 ROCM used to build PyTorch: N/A OS: Ubuntu 22.04.3 LTS (x86_64) GCC version: (Ubuntu 11.4.0-1ubuntu1~22.04) 1...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: ion;stale ### Your current environment ```text Collecting environment information... PyTorch version: 2.1.0a0+32f93b1 Is debug build: False CUDA used to build PyTorch: 12.2 ROCM used to build PyTorch: N/A OS: Ubuntu 22....
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 3: [Installation]: Using Image to build from source get error installation;stale ### Your current environment ```text Collecting environment information... PyTorch version: 2.1.0a0+32f93b1 Is debug build: False CUDA used t...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
