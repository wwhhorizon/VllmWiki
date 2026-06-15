# vllm-project/vllm#19001: [Usage]: How to use DeepSeek-R1-0528-Qwen3-8B with function call

| 字段 | 值 |
| --- | --- |
| Issue | [#19001](https://github.com/vllm-project/vllm/issues/19001) |
| 状态 | open |
| 标签 | usage;unstale |
| 评论 | 55; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cuda;operator;sampling;triton |
| 症状 | build_error;nan_inf |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Usage]: How to use DeepSeek-R1-0528-Qwen3-8B with function call

### Issue 正文摘录

### Your current environment ```text Collecting environment information... INFO 06-01 16:03:45 [__init__.py:243] Automatically detected platform cuda. PyTorch version: 2.7.0+cu126 Is debug build: False CUDA used to build PyTorch: 12.6 ROCM used to build PyTorch: N/A OS: Ubuntu 22.04.5 LTS (x86_64) GCC version: (Ubuntu 11.4.0-1ubuntu1~22.04) 11.4.0 Clang version: Could not collect CMake version: version 3.22.1 Libc version: glibc-2.35 Python version: 3.12.10 | packaged by conda-forge | (main, Apr 10 2025, 22:21:13) [GCC 13.3.0] (64-bit runtime) Python platform: Linux-6.8.0-48-generic-x86_64-with-glibc2.35 Is CUDA available: True CUDA runtime version: 12.4.131 CUDA_MODULE_LOADING set to: LAZY GPU models and configuration: GPU 0: NVIDIA RTX A4000 GPU 1: NVIDIA RTX A4000 GPU 2: NVIDIA RTX A4000 GPU 3: NVIDIA RTX A4000 GPU 4: NVIDIA RTX A4000 GPU 5: NVIDIA RTX A4000 Nvidia driver version: 565.57.01 cuDNN version: Probably one of the following: /usr/lib/x86_64-linux-gnu/libcudnn.so.8.9.7 /usr/lib/x86_64-linux-gnu/libcudnn.so.9.5.1 /usr/lib/x86_64-linux-gnu/libcudnn_adv.so.9.5.1 /usr/lib/x86_64-linux-gnu/libcudnn_adv_infer.so.8.9.7 /usr/lib/x86_64-linux-gnu/libcudnn_adv_train.so.8.9.7 /u...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 9: 16:03:45 [__init__.py:243] Automatically detected platform cuda. PyTorch version: 2.7.0+cu126 Is debug build: False CUDA used to build PyTorch: 12.6 ROCM used to build PyTorch: N/A OS: Ubuntu 22.04.5 LTS (x86_64) GCC ve...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 7: [Usage]: How to use DeepSeek-R1-0528-Qwen3-8B with function call usage;unstale ### Your current environment ```text Collecting environment information... INFO 06-01 16:03:45 [__init__.py:243] Automatically detected plat...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 6: .. INFO 06-01 16:03:45 [__init__.py:243] Automatically detected platform cuda. PyTorch version: 2.7.0+cu126 Is debug build: False CUDA used to build PyTorch: 12.6 ROCM used to build PyTorch: N/A OS: Ubuntu 22.04.5 LTS (...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 2: y detected platform cuda. PyTorch version: 2.7.0+cu126 Is debug build: False CUDA used to build PyTorch: 12.6 ROCM used to build PyTorch: N/A OS: Ubuntu 22.04.5 LTS (x86_64) GCC version: (Ubuntu 11.4.0-1ubuntu1~22.04) 1...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: [Usage]: How to use DeepSeek-R1-0528-Qwen3-8B with function call usage;unstale ### Your current environment ```text Collecting environment information... INFO 06-01 16:03:45 [__init__.py:243] Automatically detected plat...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
