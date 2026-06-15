# vllm-project/vllm#5246: how to compile with GLIBCXX_USE_CXX11_ABI=1 

| 字段 | 值 |
| --- | --- |
| Issue | [#5246](https://github.com/vllm-project/vllm/issues/5246) |
| 状态 | closed |
| 标签 | installation;stale |
| 评论 | 5; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | development |
| 工作域 | ci_build;frontend_api;hardware_porting;model_support;sampling_logits;speculative_decoding |
| 子分类 | env_compat |
| Operator 关键词 | cuda;operator;sampling;triton |
| 症状 | build_error |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> how to compile with GLIBCXX_USE_CXX11_ABI=1 

### Issue 正文摘录

### Your current environment Collecting environment information... PyTorch version: 2.2.0 Is debug build: False CUDA used to build PyTorch: 12.2 ROCM used to build PyTorch: N/A OS: Ubuntu 22.04.3 LTS (x86_64) GCC version: (Ubuntu 11.4.0-1ubuntu1~22.04) 11.4.0 Clang version: Could not collect CMake version: version 3.28.3 Libc version: glibc-2.35 Python version: 3.10.12 (main, Nov 20 2023, 15:14:05) [GCC 11.4.0] (64-bit runtime) Python platform: Linux-5.4.0-165-generic-x86_64-with-glibc2.35 Is CUDA available: True CUDA runtime version: 12.2.140 CUDA_MODULE_LOADING set to: LAZY GPU models and configuration: GPU 0: NVIDIA A100-SXM4-80GB GPU 1: NVIDIA A100-SXM4-80GB GPU 2: NVIDIA A100-SXM4-80GB GPU 3: NVIDIA A100-SXM4-80GB GPU 4: NVIDIA A100-SXM4-80GB GPU 5: NVIDIA A100-SXM4-80GB GPU 6: NVIDIA A100-SXM4-80GB GPU 7: NVIDIA A100-SXM4-80GB Nvidia driver version: 525.125.06 cuDNN version: Probably one of the following: /usr/lib/x86_64-linux-gnu/libcudnn.so.8.9.7 /usr/lib/x86_64-linux-gnu/libcudnn_adv_infer.so.8.9.7 /usr/lib/x86_64-linux-gnu/libcudnn_adv_train.so.8.9.7 /usr/lib/x86_64-linux-gnu/libcudnn_cnn_infer.so.8.9.7 /usr/lib/x86_64-linux-gnu/libcudnn_cnn_train.so.8.9.7 /usr/lib/x86_6...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 9: how to compile with GLIBCXX_USE_CXX11_ABI=1 installation;stale ### Your current environment Collecting environment information... PyTorch version: 2.2.0 Is debug build: False CUDA used to build PyTorch: 12.2 ROCM used t...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 6: environment information... PyTorch version: 2.2.0 Is debug build: False CUDA used to build PyTorch: 12.2 ROCM used to build PyTorch: N/A OS: Ubuntu 22.04.3 LTS (x86_64) GCC version: (Ubuntu 11.4.0-1ubuntu1~22.04) 11.4.0...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: nstallation;stale ### Your current environment Collecting environment information... PyTorch version: 2.2.0 Is debug build: False CUDA used to build PyTorch: 12.2 ROCM used to build PyTorch: N/A OS: Ubuntu 22.04.3 LTS (...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: how to compile with GLIBCXX_USE_CXX11_ABI=1 installation;stale ### Your current environment Collecting environment information... PyTorch version: 2.2.0 Is debug build: False CUDA used to build PyTorch: 12.2 ROCM used t...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: ] mypy-extensions==1.0.0 [pip3] numpy==1.22.2 [pip3] torch==2.2.0 [pip3] triton==2.2.0 [conda] Could not collectROCM Version: Could not collect Neuron SDK Version: N/A vLLM Version: 0.4.3 vLLM Build Flags: CUDA Archs: N...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
