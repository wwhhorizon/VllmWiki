# vllm-project/vllm#9459: [Usage]: How to pass the model path to the vllm serve command

| 字段 | 值 |
| --- | --- |
| Issue | [#9459](https://github.com/vllm-project/vllm/issues/9459) |
| 状态 | closed |
| 标签 | usage |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;hardware_porting;model_support;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cuda;operator;sampling |
| 症状 | build_error;nan_inf |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Usage]: How to pass the model path to the vllm serve command

### Issue 正文摘录

### Your current environment PyTorch version: 2.4.0 Is debug build: False CUDA used to build PyTorch: 12.6 ROCM used to build PyTorch: N/A OS: Ubuntu 22.04.5 LTS (aarch64) GCC version: (Ubuntu 11.4.0-1ubuntu1~22.04) 11.4.0 Clang version: Could not collect CMake version: version 3.30.4 Libc version: glibc-2.35 Python version: 3.10.12 (main, Sep 11 2024, 15:47:36) [GCC 11.4.0] (64-bit runtime) Python platform: Linux-5.15.148-tegra-aarch64-with-glibc2.35 Is CUDA available: True CUDA runtime version: 12.6.77 CUDA_MODULE_LOADING set to: LAZY GPU models and configuration: GPU 0: Orin (nvgpu) Nvidia driver version: 540.4.0 cuDNN version: Probably one of the following: /usr/lib/aarch64-linux-gnu/libcudnn.so.9.4.0 /usr/lib/aarch64-linux-gnu/libcudnn_adv.so.9.4.0 /usr/lib/aarch64-linux-gnu/libcudnn_cnn.so.9.4.0 /usr/lib/aarch64-linux-gnu/libcudnn_engines_precompiled.so.9.4.0 /usr/lib/aarch64-linux-gnu/libcudnn_engines_runtime_compiled.so.9.4.0 /usr/lib/aarch64-linux-gnu/libcudnn_graph.so.9.4.0 /usr/lib/aarch64-linux-gnu/libcudnn_heuristic.so.9.4.0 /usr/lib/aarch64-linux-gnu/libcudnn_ops.so.9.4.0 HIP runtime version: N/A MIOpen runtime version: N/A Is XNNPACK available: True CPU: Architectur...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 7: th to the vllm serve command usage ### Your current environment PyTorch version: 2.4.0 Is debug build: False CUDA used to build PyTorch: 12.6 ROCM used to build PyTorch: N/A OS: Ubuntu 22.04.5 LTS (aarch64) GCC version:...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 5: [Usage]: How to pass the model path to the vllm serve command usage ### Your current environment PyTorch version: 2.4.0 Is debug build: False CUDA used to build PyTorch: 12.6 ROCM used to build PyTorch: N/A OS: Ubuntu 2...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 4: # Your current environment PyTorch version: 2.4.0 Is debug build: False CUDA used to build PyTorch: 12.6 ROCM used to build PyTorch: N/A OS: Ubuntu 22.04.5 LTS (aarch64) GCC version: (Ubuntu 11.4.0-1ubuntu1~22.04) 11.4....
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: cted Vulnerability Meltdown: Not affected Vulnerability Mmio stale data: Not affected Vulnerability Retbleed: Not affected Vulnerability Spec rstack overflow: Not affected Vulnerability Spec store bypass: Mitigation; Sp...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 1: e ### Your current environment PyTorch version: 2.4.0 Is debug build: False CUDA used to build PyTorch: 12.6 ROCM used to build PyTorch: N/A OS: Ubuntu 22.04.5 LTS (aarch64) GCC version: (Ubuntu 11.4.0-1ubuntu1~22.04) 1...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
