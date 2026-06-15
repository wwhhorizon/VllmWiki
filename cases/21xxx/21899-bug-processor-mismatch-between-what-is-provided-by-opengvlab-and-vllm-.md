# vllm-project/vllm#21899: [Bug]: Processor mismatch between what is provided by OpenGVLab and VLLM for InternVL leading to outputs of the processor being too large to be decoded for the tokenizer

| 字段 | 值 |
| --- | --- |
| Issue | [#21899](https://github.com/vllm-project/vllm/issues/21899) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 9; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;multimodal_vlm;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cuda;operator;sampling;triton |
| 症状 | build_error;mismatch;nan_inf |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Processor mismatch between what is provided by OpenGVLab and VLLM for InternVL leading to outputs of the processor being too large to be decoded for the tokenizer

### Issue 正文摘录

### Your current environment ============================== System Info ============================== OS : Ubuntu 22.04.5 LTS (x86_64) GCC version : (Ubuntu 11.4.0-1ubuntu1~22.04) 11.4.0 Clang version : Could not collect CMake version : Could not collect Libc version : glibc-2.35 ============================== PyTorch Info ============================== PyTorch version : 2.6.0+cu124 Is debug build : False CUDA used to build PyTorch : 12.4 ROCM used to build PyTorch : N/A ============================== Python Environment ============================== Python version : 3.10.18 (main, Jun 5 2025, 13:14:17) [GCC 11.2.0] (64-bit runtime) Python platform : Linux-5.15.0-130-generic-x86_64-with-glibc2.35 ============================== CUDA / GPU Info ============================== Is CUDA available : True CUDA runtime version : 12.4.99 CUDA_MODULE_LOADING set to : LAZY GPU models and configuration : GPU 0: NVIDIA H100 80GB HBM3 GPU 1: NVIDIA H100 80GB HBM3 GPU 2: NVIDIA H100 80GB HBM3 GPU 3: NVIDIA H100 80GB HBM3 GPU 4: NVIDIA H100 80GB HBM3 GPU 5: NVIDIA H100 80GB HBM3 GPU 6: NVIDIA H100 80GB HBM3 GPU 7: NVIDIA H100 80GB HBM3 Nvidia driver version : 535.183.01 cuDNN version : Could not...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 9: ========= OS : Ubuntu 22.04.5 LTS (x86_64) GCC version : (Ubuntu 11.4.0-1ubuntu1~22.04) 11.4.0 Clang version : Could not collect CMake version : Could not collect Libc version : glibc-2.35 ==============
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 9: ]: Processor mismatch between what is provided by OpenGVLab and VLLM for InternVL leading to outputs of the processor being too large to be decoded for the tokenizer bug;stale ### Your current environment ==============...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 6: [Bug]: Processor mismatch between what is provided by OpenGVLab and VLLM for InternVL leading to outputs of the processor being too large to be decoded for the tokenizer bug;stale ### Your current environment ==========...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 5: M for InternVL leading to outputs of the processor being too large to be decoded for the tokenizer bug;stale ### Your current environment ============================== System Info ============================== OS : Ub...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 3: === Versions of relevant libraries ============================== [pip3] flashinfer-python==0.2.5+cu124torch2.6 [pip3] mypy-extensions==1.0.0 [pip3] numpy==2.1.2 [pip3] nvidia-cublas-cu12==12.4.5.8 [pip3] nvidia-cuda-cu...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
