# vllm-project/vllm#4301: [Usage]: ValueError: Cannot find the config file for awq

| 字段 | 值 |
| --- | --- |
| Issue | [#4301](https://github.com/vllm-project/vllm/issues/4301) |
| 状态 | closed |
| 标签 | usage;stale |
| 评论 | 8; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;hardware_porting;model_support;quantization;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cuda;operator;quantization;sampling;triton |
| 症状 | build_error;nan_inf |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Usage]: ValueError: Cannot find the config file for awq

### Issue 正文摘录

### Your current environment ``` PyTorch version: 2.1.2+cu121 Is debug build: False CUDA used to build PyTorch: 12.1 ROCM used to build PyTorch: N/A OS: Ubuntu 20.04.6 LTS (x86_64) GCC version: (Ubuntu 9.4.0-1ubuntu1~20.04.2) 9.4.0 Clang version: Could not collect CMake version: version 3.29.2 Libc version: glibc-2.31 Python version: 3.10.10 (main, Mar 21 2023, 18:45:11) [GCC 11.2.0] (64-bit runtime) Python platform: Linux-5.15.0-1058-aws-x86_64-with-glibc2.31 Is CUDA available: True CUDA runtime version: 12.1.105 CUDA_MODULE_LOADING set to: LAZY GPU models and configuration: GPU 0: NVIDIA L4 Nvidia driver version: 535.161.08 cuDNN version: Probably one of the following: /usr/lib/x86_64-linux-gnu/libcudnn.so.8.9.7 /usr/lib/x86_64-linux-gnu/libcudnn_adv_infer.so.8.9.7 /usr/lib/x86_64-linux-gnu/libcudnn_adv_train.so.8.9.7 /usr/lib/x86_64-linux-gnu/libcudnn_cnn_infer.so.8.9.7 /usr/lib/x86_64-linux-gnu/libcudnn_cnn_train.so.8.9.7 /usr/lib/x86_64-linux-gnu/libcudnn_ops_infer.so.8.9.7 /usr/lib/x86_64-linux-gnu/libcudnn_ops_train.so.8.9.7 HIP runtime version: N/A MIOpen runtime version: N/A Is XNNPACK available: True CPU: Architecture: x86_64 CPU op-mode(s): 32-bit, 64-bit Byte Order: Li...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 7: onfig file for awq usage;stale ### Your current environment ``` PyTorch version: 2.1.2+cu121 Is debug build: False CUDA used to build PyTorch: 12.1 ROCM used to build PyTorch: N/A OS: Ubuntu 20.04.6 LTS (x86_64) GCC ver...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 5: rent environment ``` PyTorch version: 2.1.2+cu121 Is debug build: False CUDA used to build PyTorch: 12.1 ROCM used to build PyTorch: N/A OS: Ubuntu 20.04.6 LTS (x86_64) GCC version: (Ubuntu 9.4.0-1ubuntu1~20.04.2) 9.4.0...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 4: trust_remote_code=True, # mandatory for hf models dtype="bfloat16", gpu_memory_utilization=0.95, quantization="awq", max_model_len=8192, # max_new_tokens=128, # top_k=10, # top_p=0.95, # temper
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: [Usage]: ValueError: Cannot find the config file for awq usage;stale ### Your current environment ``` PyTorch version: 2.1.2+cu121 Is debug build: False CUDA used to build PyTorch: 12.1 ROCM used to build PyTorch: N/A O...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: [Usage]: ValueError: Cannot find the config file for awq usage;stale ### Your current environment ``` PyTorch version: 2.1.2+cu121 Is debug build: False CUDA used to build PyTorch: 12.1 ROCM used to build PyTorch: N/A O...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
