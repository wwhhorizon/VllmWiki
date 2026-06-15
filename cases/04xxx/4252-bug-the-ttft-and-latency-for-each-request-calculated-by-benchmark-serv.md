# vllm-project/vllm#4252: [Bug]: the ttft and latency for each request calculated by benchmark_serving.py seems abnormal

| 字段 | 值 |
| --- | --- |
| Issue | [#4252](https://github.com/vllm-project/vllm/issues/4252) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;quantization;speculative_decoding |
| 子分类 |  |
| Operator 关键词 | cuda;operator;quantization;triton |
| 症状 | build_error;mismatch;slowdown |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: the ttft and latency for each request calculated by benchmark_serving.py seems abnormal

### Issue 正文摘录

### Your current environment ```text The output of `python collect_env.py` ``` Collecting environment information... PyTorch version: 2.2.1+cu121 Is debug build: False CUDA used to build PyTorch: 12.1 ROCM used to build PyTorch: N/A OS: Ubuntu 22.04.3 LTS (x86_64) GCC version: (Ubuntu 11.4.0-1ubuntu1~22.04) 11.4.0 Clang version: Could not collect CMake version: version 3.27.6 Libc version: glibc-2.35 Python version: 3.10.12 (main, Jun 11 2023, 05:26:28) [GCC 11.4.0] (64-bit runtime) Python platform: Linux-5.15.0-52-shopee-generic-x86_64-with-glibc2.35 Is CUDA available: True CUDA runtime version: 12.2.140 CUDA_MODULE_LOADING set to: LAZY GPU models and configuration: GPU 0: NVIDIA A30 GPU 1: NVIDIA A30 Nvidia driver version: 535.104.12 cuDNN version: Probably one of the following: /usr/lib/x86_64-linux-gnu/libcudnn.so.8.9.5 /usr/lib/x86_64-linux-gnu/libcudnn_adv_infer.so.8.9.5 /usr/lib/x86_64-linux-gnu/libcudnn_adv_train.so.8.9.5 /usr/lib/x86_64-linux-gnu/libcudnn_cnn_infer.so.8.9.5 /usr/lib/x86_64-linux-gnu/libcudnn_cnn_train.so.8.9.5 /usr/lib/x86_64-linux-gnu/libcudnn_ops_infer.so.8.9.5 /usr/lib/x86_64-linux-gnu/libcudnn_ops_train.so.8.9.5 HIP runtime version: N/A MIOpen runtime...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 7: python collect_env.py` ``` Collecting environment information... PyTorch version: 2.2.1+cu121 Is debug build: False CUDA used to build PyTorch: 12.1 ROCM used to build PyTorch: N/A OS: Ubuntu 22.04.3 LTS (x86_64) GCC ve...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 5: onment information... PyTorch version: 2.2.1+cu121 Is debug build: False CUDA used to build PyTorch: 12.1 ROCM used to build PyTorch: N/A OS: Ubuntu 22.04.3 LTS (x86_64) GCC version: (Ubuntu 11.4.0-1ubuntu1~22.04) 11.4....
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: `text The output of `python collect_env.py` ``` Collecting environment information... PyTorch version: 2.2.1+cu121 Is debug build: False CUDA used to build PyTorch: 12.1 ROCM used to build PyTorch: N/A OS: Ubuntu 22.04....
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 3: [Bug]: the ttft and latency for each request calculated by benchmark_serving.py seems abnormal bug ### Your current environment ```text The output of `python collect_env.py` ``` Collecting environment information... PyT...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 3: [Bug]: the ttft and latency for each request calculated by benchmark_serving.py seems abnormal bug ### Your current environment ```text The output of `python collect_env.py` ``` Collecting environment information... PyT...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
