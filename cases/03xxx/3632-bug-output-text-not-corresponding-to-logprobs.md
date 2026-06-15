# vllm-project/vllm#3632: [Bug]: output text not corresponding to logprobs

| 字段 | 值 |
| --- | --- |
| Issue | [#3632](https://github.com/vllm-project/vllm/issues/3632) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | development |
| 工作域 | ci_build;hardware_porting;model_support;sampling_logits;speculative_decoding |
| 子分类 | env_compat |
| Operator 关键词 | cuda;operator;sampling;triton |
| 症状 | build_error |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: output text not corresponding to logprobs

### Issue 正文摘录

### Your current environment ```text The output of `python collect_env.py` PyTorch version: 2.1.2+cu118 Is debug build: False CUDA used to build PyTorch: 11.8 ROCM used to build PyTorch: N/A OS: Ubuntu 20.04.6 LTS (x86_64) GCC version: (Ubuntu 9.4.0-1ubuntu1~20.04.2) 9.4.0 Clang version: 10.0.0-4ubuntu1 CMake version: version 3.26.1 Libc version: glibc-2.31 Python version: 3.9.12 (main, Apr 5 2022, 06:56:58) [GCC 7.5.0] (64-bit runtime) Python platform: Linux-5.4.0-166-generic-x86_64-with-glibc2.31 Is CUDA available: True CUDA runtime version: 11.7.99 CUDA_MODULE_LOADING set to: LAZY GPU models and configuration: GPU 0: NVIDIA RTX A6000 GPU 1: NVIDIA RTX A6000 Nvidia driver version: 525.147.05 cuDNN version: Probably one of the following: /usr/local/cuda-11.7/targets/x86_64-linux/lib/libcudnn.so.8 /usr/local/cuda-11.7/targets/x86_64-linux/lib/libcudnn_adv_infer.so.8 /usr/local/cuda-11.7/targets/x86_64-linux/lib/libcudnn_adv_train.so.8 /usr/local/cuda-11.7/targets/x86_64-linux/lib/libcudnn_cnn_infer.so.8 /usr/local/cuda-11.7/targets/x86_64-linux/lib/libcudnn_cnn_train.so.8 /usr/local/cuda-11.7/targets/x86_64-linux/lib/libcudnn_ops_infer.so.8 /usr/local/cuda-11.7/targets/x86_64-linu...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 7: rrent environment ```text The output of `python collect_env.py` PyTorch version: 2.1.2+cu118 Is debug build: False CUDA used to build PyTorch: 11.8 ROCM used to build PyTorch: N/A
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 6: ython collect_env.py` PyTorch version: 2.1.2+cu118 Is debug build: False CUDA used to build PyTorch: 11.8 ROCM used to build PyTorch: N/A
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: True CUDA runtime version: 11.7.99 CUDA_MODULE_LOADING set to: LAZY GPU models and configuration: GPU 0: NVIDIA RTX A6000 GPU 1: NVIDIA RTX A6000 Nvidia driver version: 525.147.05 cuDNN version: Probably one of the foll...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 3: cted Vulnerability Meltdown: Not affected Vulnerability Mmio stale data: Not affected Vulnerability Retbleed: Vulnerable Vulnerability Spec store bypass: Mitigation; Speculative Store Bypass disabled via prctl and secco...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: cu118 [pip3] torchmetrics==1.0.1 [pip3] torchvision==0.14.1+cu117 [pip3] triton==2.1.0 [conda] blas 1.0 mkl [conda] mkl 2021.4.0 h06a4308_640 [conda] mkl-service 2.4.0 py39h7f8727e_0 [conda]

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
