# vllm-project/vllm#15533: [Usage]: Evaluation score under V1 engine is low

| 字段 | 值 |
| --- | --- |
| Issue | [#15533](https://github.com/vllm-project/vllm/issues/15533) |
| 状态 | closed |
| 标签 | usage;stale |
| 评论 | 11; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | development |
| 工作域 | ci_build;distributed_parallel;frontend_api;hardware_porting;model_support |
| 子分类 | env_compat |
| Operator 关键词 | cuda;operator;triton |
| 症状 | build_error |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Usage]: Evaluation score under V1 engine is low

### Issue 正文摘录

### Your current environment ```text The output of `python collect_env.py` ``` Collecting environment information... PyTorch version: 2.6.0+cu124 Is debug build: False CUDA used to build PyTorch: 12.4 ROCM used to build PyTorch: N/A OS: Ubuntu 20.04.4 LTS (x86_64) GCC version: (Ubuntu 9.4.0-1ubuntu1~20.04.1) 9.4.0 Clang version: Could not collect CMake version: Could not collect Libc version: glibc-2.31 Python version: 3.10.13 (main, Sep 11 2023, 13:44:35) [GCC 11.2.0] (64-bit runtime) Python platform: Linux-4.18.0-193.14.2.el8_2.x86_64-x86_64-with-glibc2.31 Is CUDA available: True CUDA runtime version: 12.2.140 CUDA_MODULE_LOADING set to: LAZY GPU models and configuration: GPU 0: NVIDIA A800-SXM4-80GB Nvidia driver version: 535.104.12 cuDNN version: Probably one of the following: /usr/lib/x86_64-linux-gnu/libcudnn.so.8.4.0 /usr/lib/x86_64-linux-gnu/libcudnn_adv_infer.so.8.4.0 /usr/lib/x86_64-linux-gnu/libcudnn_adv_train.so.8.4.0 /usr/lib/x86_64-linux-gnu/libcudnn_cnn_infer.so.8.4.0 /usr/lib/x86_64-linux-gnu/libcudnn_cnn_train.so.8.4.0 /usr/lib/x86_64-linux-gnu/libcudnn_ops_infer.so.8.4.0 /usr/lib/x86_64-linux-gnu/libcudnn_ops_train.so.8.4.0 HIP runtime version: N/A MIOpen runtime...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 8: python collect_env.py` ``` Collecting environment information... PyTorch version: 2.6.0+cu124 Is debug build: False CUDA used to build PyTorch: 12.4 ROCM used to build PyTorch: N/A OS: Ubuntu 20.04.4 LTS (x86_64) GCC ve...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 5: onment information... PyTorch version: 2.6.0+cu124 Is debug build: False CUDA used to build PyTorch: 12.4 ROCM used to build PyTorch: N/A OS: Ubuntu 20.04.4 LTS (x86_64) GCC version: (Ubuntu 9.4.0-1ubuntu1~20.04.1) 9.4....
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 5: `text The output of `python collect_env.py` ``` Collecting environment information... PyTorch version: 2.6.0+cu124 Is debug build: False CUDA used to build PyTorch: 12.4 ROCM used to build PyTorch: N/A OS: Ubuntu 20.04....
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 2: transformers==4.50.0 [pip3] transformers-stream-generator==0.0.5 [pip3] triton==3.2.0 [conda] numpy 1.26.4 pypi_0 pypi [conda] nvidia-cublas-cu12 12.4.5.8 pypi_0 pypi [conda] nvidia-cuda-cupti-cu12 12.4.127
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: [Usage]: Evaluation score under V1 engine is low usage;stale ### Your current environment ```text The output of `python collect_env.py` ``` Collecting environment information... PyTorch version: 2.6.0+cu124 Is debug bui...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
