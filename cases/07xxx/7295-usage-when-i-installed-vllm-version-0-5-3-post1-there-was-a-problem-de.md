# vllm-project/vllm#7295: [Usage]: When I installed vllm version 0.5.3.post1, there was a problem deploying qwen2

| 字段 | 值 |
| --- | --- |
| Issue | [#7295](https://github.com/vllm-project/vllm/issues/7295) |
| 状态 | closed |
| 标签 | usage |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | development |
| 工作域 | ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;speculative_decoding |
| 子分类 | env_compat |
| Operator 关键词 | cuda;operator;triton |
| 症状 | build_error |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Usage]: When I installed vllm version 0.5.3.post1, there was a problem deploying qwen2

### Issue 正文摘录

### Your current environment ```text The output of `python collect_env.py` ``` Collecting environment information... PyTorch version: 2.3.1+cu121 Is debug build: False CUDA used to build PyTorch: 12.1 ROCM used to build PyTorch: N/A OS: Ubuntu 20.04.6 LTS (x86_64) GCC version: (Ubuntu 9.4.0-1ubuntu1~20.04.2) 9.4.0 Clang version: Could not collect CMake version: version 3.30.1 Libc version: glibc-2.31 Python version: 3.10.14 (main, May 6 2024, 19:42:50) [GCC 11.2.0] (64-bit runtime) Python platform: Linux-5.15.0-78-generic-x86_64-with-glibc2.31 Is CUDA available: True CUDA runtime version: 12.1.105 CUDA_MODULE_LOADING set to: LAZY GPU models and configuration: GPU 0: Quadro RTX 8000 GPU 1: Quadro RTX 8000 GPU 2: Quadro RTX 8000 GPU 3: Quadro RTX 8000 GPU 4: Quadro RTX 8000 GPU 5: Quadro RTX 8000 GPU 6: Quadro RTX 8000 GPU 7: Quadro RTX 8000 Nvidia driver version: 535.183.01 cuDNN version: Probably one of the following: /usr/lib/x86_64-linux-gnu/libcudnn.so.8.9.0 /usr/lib/x86_64-linux-gnu/libcudnn_adv_infer.so.8.9.0 /usr/lib/x86_64-linux-gnu/libcudnn_adv_train.so.8.9.0 /usr/lib/x86_64-linux-gnu/libcudnn_cnn_infer.so.8.9.0 /usr/lib/x86_64-linux-gnu/libcudnn_cnn_train.so.8.9.0 /usr/li...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 8: [Usage]: When I installed vllm version 0.5.3.post1, there was a problem deploying qwen2 usage ### Your current environment ```text The output of `python collect_env.py` ``` Collecting environment information... PyTorch...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 6: onment information... PyTorch version: 2.3.1+cu121 Is debug build: False CUDA used to build PyTorch: 12.1 ROCM used to build PyTorch: N/A OS: Ubuntu 20.04.6 LTS (x86_64) GCC version: (Ubuntu 9.4.0-1ubuntu1~20.04.2) 9.4....
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 5: When I installed vllm version 0.5.3.post1, there was a problem deploying qwen2 usage ### Your current environment ```text The output of `python collect_env.py` ``` Collecting environment information... PyTorch version:...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: able Vulnerability Meltdown: Mitigation; PTI Vulnerability Mmio stale data: Mitigation; Clear CPU buffers; SMT vulnerable Vulnerability Retbleed: Not affected Vulnerability Spec store bypass: Mitigation; Speculative Sto...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: u121 [pip3] torchvision==0.18.1+cu121 [pip3] transformers==4.43.3 [pip3] triton==2.3.1 [conda] numpy 1.26.4 py310hb13e2d6_0 conda-forge [conda] nvidia-nccl-cu12 2.20.5 pypi_0 pypi [conda] pyzmq 26.0.3

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
