# vllm-project/vllm#3818: [Bug]: When deployed on multiple nodes using ray, the 'torch.cuda.is_available()' on worker node is False

| 字段 | 值 |
| --- | --- |
| Issue | [#3818](https://github.com/vllm-project/vllm/issues/3818) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 6; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | development |
| 工作域 | ci_build;distributed_parallel;hardware_porting;model_support;speculative_decoding |
| 子分类 | env_compat |
| Operator 关键词 | cuda;operator;triton |
| 症状 | build_error |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: When deployed on multiple nodes using ray, the 'torch.cuda.is_available()' on worker node is False

### Issue 正文摘录

### Your current environment ```text PyTorch version: 2.1.2+cu121 Is debug build: False CUDA used to build PyTorch: 12.1 ROCM used to build PyTorch: N/A OS: Ubuntu 22.04.3 LTS (x86_64) GCC version: (Ubuntu 11.4.0-1ubuntu1~22.04) 11.4.0 Clang version: Could not collect CMake version: version 3.29.0 Libc version: glibc-2.35 Python version: 3.11.5 (main, Sep 11 2023, 13:54:46) [GCC 11.2.0] (64-bit runtime) Python platform: Linux-3.10.0-1160.102.1.el7.x86_64-x86_64-with-glibc2.35 Is CUDA available: True CUDA runtime version: 12.2.140 CUDA_MODULE_LOADING set to: LAZY GPU models and configuration: GPU 0: NVIDIA A800-SXM4-80GB GPU 1: NVIDIA A800-SXM4-80GB GPU 2: NVIDIA A800-SXM4-80GB GPU 3: NVIDIA A800-SXM4-80GB GPU 4: NVIDIA A800-SXM4-80GB GPU 5: NVIDIA A800-SXM4-80GB GPU 6: NVIDIA A800-SXM4-80GB GPU 7: NVIDIA A800-SXM4-80GB Nvidia driver version: 535.129.03 cuDNN version: Probably one of the following: /usr/lib/x86_64-linux-gnu/libcudnn.so.8.9.5 /usr/lib/x86_64-linux-gnu/libcudnn_adv_infer.so.8.9.5 /usr/lib/x86_64-linux-gnu/libcudnn_adv_train.so.8.9.5 /usr/lib/x86_64-linux-gnu/libcudnn_cnn_infer.so.8.9.5 /usr/lib/x86_64-linux-gnu/libcudnn_cnn_train.so.8.9.5 /usr/lib/x86_64-linux-gnu/li...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 8: er node is False bug;stale ### Your current environment ```text PyTorch version: 2.1.2+cu121 Is debug build: False
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 5: [Bug]: When deployed on multiple nodes using ray, the 'torch.cuda.is_available()' on worker node is False bug;stale ### Your current environment ```text PyTorch version: 2.1.2+cu121
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: GPU models and configuration: GPU 0: NVIDIA A800-SXM4-80GB GPU 1: NVIDIA A800-SXM4-80GB GPU 2: NVIDIA A800-SXM4-80GB GPU 3: NVIDIA A800-SXM4-80GB GPU 4: NVIDIA A800-SXM4-80GB GPU 5: NVIDIA A800-SXM4-80GB GPU 6: NVIDIA A...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: s using ray, the 'torch.cuda.is_available()' on worker node is False bug;stale ### Your current environment ```text PyTorch version: 2.1.2+cu121 Is debug
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: [pip3] triton==2.1.0 [conda] numpy 1.26.2

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
