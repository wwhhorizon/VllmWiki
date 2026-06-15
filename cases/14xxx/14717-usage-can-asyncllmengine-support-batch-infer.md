# vllm-project/vllm#14717: [Usage]: Can AsyncLLMEngine support batch infer？

| 字段 | 值 |
| --- | --- |
| Issue | [#14717](https://github.com/vllm-project/vllm/issues/14717) |
| 状态 | closed |
| 标签 | usage;stale |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cuda;operator;sampling;triton |
| 症状 | build_error;nan_inf |
| 根因提示 | dtype;env_dependency;shape |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Usage]: Can AsyncLLMEngine support batch infer？

### Issue 正文摘录

### Your current environment ``` Collecting environment information... PyTorch version: 2.4.0+cu121 Is debug build: False CUDA used to build PyTorch: 12.1 ROCM used to build PyTorch: N/A OS: Ubuntu 24.04.1 LTS (x86_64) GCC version: (Ubuntu 13.3.0-6ubuntu2~24.04) 13.3.0 Clang version: Could not collect CMake version: Could not collect Libc version: glibc-2.39 Python version: 3.9.18 | packaged by conda-forge | (main, Dec 23 2023, 16:33:10) [GCC 12.3.0] (64-bit runtime) Python platform: Linux-6.8.0-41-generic-x86_64-with-glibc2.39 Is CUDA available: True CUDA runtime version: 12.0.140 CUDA_MODULE_LOADING set to: LAZY GPU models and configuration: GPU 0: Tesla V100-PCIE-32GB GPU 1: Tesla V100-PCIE-32GB Nvidia driver version: 550.120 cuDNN version: Probably one of the following: /usr/lib/x86_64-linux-gnu/libcudnn.so.9.6.0 /usr/lib/x86_64-linux-gnu/libcudnn_adv.so.9.6.0 /usr/lib/x86_64-linux-gnu/libcudnn_cnn.so.9.6.0 /usr/lib/x86_64-linux-gnu/libcudnn_engines_precompiled.so.9.6.0 /usr/lib/x86_64-linux-gnu/libcudnn_engines_runtime_compiled.so.9.6.0 /usr/lib/x86_64-linux-gnu/libcudnn_graph.so.9.6.0 /usr/lib/x86_64-linux-gnu/libcudnn_heuristic.so.9.6.0 /usr/lib/x86_64-linux-gnu/libcudnn_op...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 9: r current environment ``` Collecting environment information... PyTorch version: 2.4.0+cu121 Is debug build: False CUDA used to build PyTorch: 12.1 ROCM used to build PyTorch: N/A OS: Ubuntu 24.04.1 LTS (x86_64) GCC ver...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 5: onment information... PyTorch version: 2.4.0+cu121 Is debug build: False CUDA used to build PyTorch: 12.1 ROCM used to build PyTorch: N/A OS: Ubuntu 24.04.1 LTS (x86_64) GCC version: (Ubuntu 13.3.0-6ubuntu2~24.04) 13.3....
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: ？ usage;stale ### Your current environment ``` Collecting environment information... PyTorch version: 2.4.0+cu121 Is debug build: False CUDA used to build PyTorch: 12.1 ROCM used to build PyTorch: N/A OS: Ubuntu 24.04.1...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: [Usage]: Can AsyncLLMEngine support batch infer？ usage;stale ### Your current environment ``` Collecting environment information... PyTorch version: 2.4.0+cu121 Is debug build: False CUDA used to build PyTorch: 12.1 ROC...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: rch==2.4.0 [pip3] torchvision==0.19.0 [pip3] transformers==4.44.0 [pip3] triton==3.0.0 [conda] facenet-pytorch 2.6.0 pypi_0 pypi [conda] numpy 1.26.4 pypi_0 pypi [conda] nvidia-cublas-cu12 12.1.3.1

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
