# vllm-project/vllm#4498: [Usage]: It seems that vllm doesn't perform well under high concurrency

| 字段 | 值 |
| --- | --- |
| Issue | [#4498](https://github.com/vllm-project/vllm/issues/4498) |
| 状态 | closed |
| 标签 | usage;stale |
| 评论 | 4; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;moe;sampling_logits;speculative_decoding |
| 子分类 | race_cond |
| Operator 关键词 | cuda;moe;operator;sampling;triton |
| 症状 | build_error;nan_inf |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Usage]: It seems that vllm doesn't perform well under high concurrency

### Issue 正文摘录

### Your current environment ``` PyTorch version: 2.3.0+cu121 Is debug build: False CUDA used to build PyTorch: 12.1 ROCM used to build PyTorch: N/A OS: Ubuntu 20.04.5 LTS (x86_64) GCC version: (Ubuntu 9.4.0-1ubuntu1~20.04.1) 9.4.0 Clang version: Could not collect CMake version: version 3.29.2 Libc version: glibc-2.31 Python version: 3.10.14 (main, Mar 21 2024, 16:24:04) [GCC 11.2.0] (64-bit runtime) Python platform: Linux-5.15.0-91-generic-x86_64-with-glibc2.31 Is CUDA available: True CUDA runtime version: 12.2.140 CUDA_MODULE_LOADING set to: LAZY GPU models and configuration: GPU 0: NVIDIA L20 GPU 1: NVIDIA L20 GPU 2: NVIDIA L20 GPU 3: NVIDIA L20 GPU 4: NVIDIA L20 GPU 5: NVIDIA L20 GPU 6: NVIDIA L20 GPU 7: NVIDIA L20 Nvidia driver version: 550.54.14 cuDNN version: Probably one of the following: /usr/lib/x86_64-linux-gnu/libcudnn.so.8.6.0 /usr/lib/x86_64-linux-gnu/libcudnn_adv_infer.so.8.6.0 /usr/lib/x86_64-linux-gnu/libcudnn_adv_train.so.8.6.0 /usr/lib/x86_64-linux-gnu/libcudnn_cnn_infer.so.8.6.0 /usr/lib/x86_64-linux-gnu/libcudnn_cnn_train.so.8.6.0 /usr/lib/x86_64-linux-gnu/libcudnn_ops_infer.so.8.6.0 /usr/lib/x86_64-linux-gnu/libcudnn_ops_train.so.8.6.0 HIP runtime version: N/...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 7: r high concurrency usage;stale ### Your current environment ``` PyTorch version: 2.3.0+cu121 Is debug build: False CUDA used to build PyTorch: 12.1 ROCM used to build PyTorch: N/A OS: Ubuntu 20.04.5 LTS (x86_64) GCC ver...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 5: rent environment ``` PyTorch version: 2.3.0+cu121 Is debug build: False CUDA used to build PyTorch: 12.1 ROCM used to build PyTorch: N/A OS: Ubuntu 20.04.5 LTS (x86_64) GCC version: (Ubuntu 9.4.0-1ubuntu1~20.04.1) 9.4.0...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 5: True CUDA runtime version: 12.2.140 CUDA_MODULE_LOADING set to: LAZY GPU models and configuration: GPU 0: NVIDIA L20 GPU 1: NVIDIA L20 GPU 2: NVIDIA L20 GPU 3: NVIDIA L20 GPU 4: NVIDIA L20 GPU 5: NVIDIA L20 GPU 6: NVIDI...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 3: e]: It seems that vllm doesn't perform well under high concurrency usage;stale ### Your current environment ``` PyTorch version: 2.3.0+cu121 Is debug build: False CUDA used to build PyTorch: 12.1 ROCM used to build PyTo...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 2: "content": "I need feedback on an answer. Please supply the evaluation strictly in JSON format, response format comprising only \"reasoning\" (请用中文简短说明评价的理由，即说明优点也说明缺点，除非实在没有优点或缺点), \"approach\" (请用中文简短说明这个问题应该的回答思路) an...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
