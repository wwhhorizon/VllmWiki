# vllm-project/vllm#13494: [Bug]: VLLM crashed with exception "Set changed size during iteration", when hosting Qwen2.5 VL 72B

| 字段 | 值 |
| --- | --- |
| Issue | [#13494](https://github.com/vllm-project/vllm/issues/13494) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | development |
| 工作域 | ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;scheduler_memory |
| 子分类 | env_compat |
| Operator 关键词 | cuda;gemm;triton |
| 症状 | build_error;crash |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: VLLM crashed with exception "Set changed size during iteration", when hosting Qwen2.5 VL 72B

### Issue 正文摘录

### Your current environment Collecting environment information... PyTorch version: 2.5.1+cu121 Is debug build: False CUDA used to build PyTorch: 12.1 ROCM used to build PyTorch: N/A OS: Ubuntu 22.04.4 LTS (x86_64) GCC version: (Ubuntu 11.4.0-1ubuntu1~22.04) 11.4.0 Clang version: Could not collect CMake version: version 3.30.1 Libc version: glibc-2.35 Python version: 3.10.15 (main, Oct 3 2024, 07:27:34) [GCC 11.2.0] (64-bit runtime) Python platform: Linux-5.10.134-008.12.kangaroo.al8.x86_64-x86_64-with-glibc2.35 Is CUDA available: True CUDA runtime version: 12.1.105 CUDA_MODULE_LOADING set to: LAZY GPU models and configuration: GPU 0: NVIDIA A100-SXM4-80GB Nvidia driver version: 470.199.02 cuDNN version: Probably one of the following: /usr/lib/x86_64-linux-gnu/libcudnn.so.8.9.0 /usr/lib/x86_64-linux-gnu/libcudnn_adv_infer.so.8.9.0 /usr/lib/x86_64-linux-gnu/libcudnn_adv_train.so.8.9.0 /usr/lib/x86_64-linux-gnu/libcudnn_cnn_infer.so.8.9.0 /usr/lib/x86_64-linux-gnu/libcudnn_cnn_train.so.8.9.0 /usr/lib/x86_64-linux-gnu/libcudnn_ops_infer.so.8.9.0 /usr/lib/x86_64-linux-gnu/libcudnn_ops_train.so.8.9.0 HIP runtime version: N/A MIOpen runtime version: N/A Is XNNPACK available: True CPU: A...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 8: Your current environment Collecting environment information... PyTorch version: 2.5.1+cu121 Is debug build: False CUDA used to build PyTorch: 12.1 ROCM used to build PyTorch: N/A OS: Ubuntu 22.04.4 LTS (x86_64) GCC vers...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 6: onment information... PyTorch version: 2.5.1+cu121 Is debug build: False CUDA used to build PyTorch: 12.1 ROCM used to build PyTorch: N/A OS: Ubuntu 22.04.4 LTS (x86_64) GCC version: (Ubuntu 11.4.0-1ubuntu1~22.04) 11.4....
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 5: crashed with exception "Set changed size during iteration", when hosting Qwen2.5 VL 72B bug ### Your current environment Collecting environment information... PyTorch version: 2.5.1+cu121 Is debug build: False CUDA used...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 3: ffected Vulnerability Meltdown: Not affected Vulnerability Mmio stale data: Vulnerable Vulnerability Retbleed: Not affected Vulnerability Spec store bypass: Vulnerable Vulnerability Spectre v1: Vulnerable: __user pointe...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: transformers==4.49.0 [pip3] transformers-stream-generator==0.0.5 [pip3] triton==3.1.0 [conda] msgpack-numpy 0.4.8 pypi_0 pypi [conda] numpy 1.26.4 pypi_0 pypi [conda] nvidia-cublas-cu12 12.1.3.1

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
