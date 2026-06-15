# vllm-project/vllm#18467: [Usage]: Can vllm distributed load model?

| 字段 | 值 |
| --- | --- |
| Issue | [#18467](https://github.com/vllm-project/vllm/issues/18467) |
| 状态 | closed |
| 标签 | usage;stale |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;sampling_logits;speculative_decoding |
| 子分类 | memory |
| Operator 关键词 | cuda;operator;sampling;triton |
| 症状 | build_error;oom |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Usage]: Can vllm distributed load model?

### Issue 正文摘录

### Your current environment ```text ============================== System Info ============================== OS : Ubuntu 22.04.5 LTS (x86_64) GCC version : (Ubuntu 11.4.0-1ubuntu1~22.04) 11.4.0 Clang version : Could not collect CMake version : version 3.30.4 Libc version : glibc-2.35 ============================== PyTorch Info ============================== PyTorch version : 2.5.1+cu124 Is debug build : False CUDA used to build PyTorch : 12.4 ROCM used to build PyTorch : N/A ============================== Python Environment ============================== Python version : 3.10.12 (main, Sep 11 2024, 15:47:36) [GCC 11.4.0] (64-bit runtime) Python platform : Linux-5.4.0-216-generic-x86_64-with-glibc2.35 ============================== CUDA / GPU Info ============================== Is CUDA available : True CUDA runtime version : 12.6.77 CUDA_MODULE_LOADING set to : LAZY GPU models and configuration : GPU 0: NVIDIA GeForce RTX 2080 Ti GPU 1: NVIDIA GeForce RTX 2080 Ti GPU 2: NVIDIA GeForce RTX 2080 Ti GPU 3: NVIDIA GeForce RTX 2080 Ti Nvidia driver version : 560.35.03 cuDNN version : Probably one of the following: /usr/lib/x86_64-linux-gnu/libcudnn.so.9.5.0 /usr/lib/x86_64-linux-gnu/l...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 8: ========= OS : Ubuntu 22.04.5 LTS (x86_64) GCC version : (Ubuntu 11.4.0-1ubuntu1~22.04) 11.4.0 Clang version : Could not collect CMake version : version 3.30.4 Libc version : glibc-2.35 =================
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 6: version : 2.5.1+cu124 Is debug build : False CUDA used to build PyTorch : 12.4 ROCM used to build PyTorch : N/A ============================== Python Environment ============================== Python version : 3.10.12 (...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: [Usage]: Can vllm distributed load model? usage;stale ### Your current environment ```text ============================== System Info ============================== OS : Ubuntu 22.04.5 LTS (x86_64) GCC version
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 2: d is as follows ``` vllm serve /home/Qwen3-8B --tensor-parallel-size 4 --dtype float16 --gpu-memory-utilization 0.8 --max-model-len 512 ``` ### Before submitting a new issue... - [x] Make sure you already searched for r...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: [Usage]: Can vllm distributed load model? usage;stale ### Your current environment ```text ============================== System Info ============================== OS : Ubuntu 22.04.5 LTS (x86_64) GCC version : (Ubu

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
