# vllm-project/vllm#5272: [Bug]: When I call the speculative model through the vllm interface, an error is reported: TypeError: 'type' object is not subscriptable

| 字段 | 值 |
| --- | --- |
| Issue | [#5272](https://github.com/vllm-project/vllm/issues/5272) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | development |
| 工作域 | ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;sampling_logits;scheduler_memory;speculative_decoding |
| 子分类 | env_compat |
| Operator 关键词 | cuda;operator;sampling;triton |
| 症状 | build_error;crash |
| 根因提示 | env_dependency;memory_layout |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: When I call the speculative model through the vllm interface, an error is reported: TypeError: 'type' object is not subscriptable

### Issue 正文摘录

### Your current environment ```text Collecting environment information... PyTorch version: 2.1.2+cu121 Is debug build: False CUDA used to build PyTorch: 12.1 ROCM used to build PyTorch: N/A OS: Enterprise Linux Server 7.2 (Paladin) (x86_64) GCC version: (GCC) 9.2.1 20200522 (Alibaba 9.2.1-3 2.17) Clang version: Could not collect CMake version: version 3.29.3 Libc version: glibc-2.30 Python version: 3.8.18 (default, Sep 11 2023, 13:40:15) [GCC 11.2.0] (64-bit runtime) Python platform: Linux-5.10.134-13.al8.x86_64-x86_64-with-glibc2.17 Is CUDA available: True CUDA runtime version: Could not collect CUDA_MODULE_LOADING set to: LAZY GPU models and configuration: GPU 0: NVIDIA A800-SXM4-80GB GPU 1: NVIDIA A800-SXM4-80GB Nvidia driver version: 470.161.03 cuDNN version: Probably one of the following: /usr/local/cuda/targets/x86_64-linux/lib/libcudnn.so.8.9.3 /usr/local/cuda/targets/x86_64-linux/lib/libcudnn_adv_infer.so.8.9.3 /usr/local/cuda/targets/x86_64-linux/lib/libcudnn_adv_train.so.8.9.3 /usr/local/cuda/targets/x86_64-linux/lib/libcudnn_cnn_infer.so.8.9.3 /usr/local/cuda/targets/x86_64-linux/lib/libcudnn_cnn_train.so.8.9.3 /usr/local/cuda/targets/x86_64-linux/lib/libcudnn_ops_infe...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 7: rrent environment ```text Collecting environment information... PyTorch version: 2.1.2+cu121 Is debug build: False CUDA used to build PyTorch: 12.1 ROCM used to build PyTorch: N/A OS: Enterprise Linux Server 7.2 (Paladi...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 5: onment information... PyTorch version: 2.1.2+cu121 Is debug build: False CUDA used to build PyTorch: 12.1 ROCM used to build PyTorch: N/A OS: Enterprise Linux Server 7.2 (Paladin) (x86_64) GCC version: (GCC) 9.2.1 20200...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: [Bug]: When I call the speculative model through the vllm interface, an error is reported: TypeError: 'type' object is not subscriptable bug ### Your current environment ```text Collecting environment information... PyT...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 3: nvironment information... PyTorch version: 2.1.2+cu121 Is debug build: False CUDA used to build PyTorch: 12.1 ROCM used to build PyTorch: N/A OS: Enterprise Linux Server 7.2 (Paladin) (x86_64) GCC version: (GCC) 9.2.1 2...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: [Bug]: When I call the speculative model through the vllm interface, an error is reported: TypeError: 'type' object is not subscriptable bug ### Your current environment ```text Collecting environment information... PyT...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
