# vllm-project/vllm#6299: [Bug]: Vllm 0.5.1+cu118 timeout when init CustomAllreduce

| 字段 | 值 |
| --- | --- |
| Issue | [#6299](https://github.com/vllm-project/vllm/issues/6299) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 22; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | ci_build;distributed_parallel;hardware_porting;model_support;speculative_decoding |
| 子分类 | kernel_eff |
| Operator 关键词 | cuda;triton |
| 症状 | build_error;crash |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Vllm 0.5.1+cu118 timeout when init CustomAllreduce

### Issue 正文摘录

### Your current environment ```text The output of `python collect_env.py` Collecting environment information... PyTorch version: 2.3.0+cu118 Is debug build: False CUDA used to build PyTorch: 11.8 ROCM used to build PyTorch: N/A OS: Ubuntu 20.04.5 LTS (x86_64) GCC version: (Ubuntu 9.4.0-1ubuntu1~20.04.1) 9.4.0 Clang version: Could not collect CMake version: version 3.29.0 Libc version: glibc-2.31 Python version: 3.8.10 (default, Nov 22 2023, 10:22:35) [GCC 9.4.0] (64-bit runtime) Python platform: Linux-3.10.0-1160.el7.x86_64-x86_64-with-glibc2.29 Is CUDA available: True CUDA runtime version: 11.8.89 CUDA_MODULE_LOADING set to: LAZY GPU models and configuration: GPU 0: NVIDIA A100-SXM4-80GB GPU 1: NVIDIA A100-SXM4-80GB Nvidia driver version: 535.104.05 cuDNN version: Probably one of the following: /usr/lib/x86_64-linux-gnu/libcudnn.so.8.7.0 /usr/lib/x86_64-linux-gnu/libcudnn_adv_infer.so.8.7.0 /usr/lib/x86_64-linux-gnu/libcudnn_adv_train.so.8.7.0 /usr/lib/x86_64-linux-gnu/libcudnn_cnn_infer.so.8.7.0 /usr/lib/x86_64-linux-gnu/libcudnn_cnn_train.so.8.7.0 /usr/lib/x86_64-linux-gnu/libcudnn_ops_infer.so.8.7.0 /usr/lib/x86_64-linux-gnu/libcudnn_ops_train.so.8.7.0 HIP runtime version: N/...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 7: of `python collect_env.py` Collecting environment information... PyTorch version: 2.3.0+cu118 Is debug build: False CUDA used to build PyTorch: 11.8 ROCM used to build PyTorch: N/A OS: Ubuntu 20.04.5 LTS (x86_64) GCC ve...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 6: onment information... PyTorch version: 2.3.0+cu118 Is debug build: False CUDA used to build PyTorch: 11.8 ROCM used to build PyTorch: N/A OS: Ubuntu 20.04.5 LTS (x86_64) GCC version: (Ubuntu 9.4.0-1ubuntu1~20.04.1) 9.4....
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: ```text The output of `python collect_env.py` Collecting environment information... PyTorch version: 2.3.0+cu118 Is debug build: False CUDA used to build PyTorch: 11.8 ROCM used to build PyTorch: N/A OS: Ubuntu 20.04.5...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: down: Not affected Vulnerability Spec store bypass: Mitigation; Speculative Store Bypass disabled via prctl and seccomp Vulnerability Spectre v1: Mitigation; Load fences, usercopy/swapgs barriers and __user pointer sani...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: .0+cu118 [pip3] torchtext==0.5.0 [pip3] torchvision==0.18.0+cu118 [pip3] triton==2.3.0 [pip3] tritonclient==2.19.0 [conda] Could not collectROCM Version: Could not collect Neuron SDK Version: N/A vLLM Version: 0.5.1 vLL...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
