# vllm-project/vllm#6469: [Usage]: PeftModelForCausalLM is not JSON serializable

| 字段 | 值 |
| --- | --- |
| Issue | [#6469](https://github.com/vllm-project/vllm/issues/6469) |
| 状态 | closed |
| 标签 | usage |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cuda;operator;sampling;triton |
| 症状 | build_error;crash;nan_inf |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Usage]: PeftModelForCausalLM is not JSON serializable

### Issue 正文摘录

### Your current environment ```text ollecting environment information... PyTorch version: 2.3.1+cu121 Is debug build: False CUDA used to build PyTorch: 12.1 ROCM used to build PyTorch: N/A OS: Ubuntu 20.04.6 LTS (x86_64) GCC version: (Ubuntu 9.4.0-1ubuntu1~20.04.2) 9.4.0 Clang version: Could not collect CMake version: version 3.30.0 Libc version: glibc-2.31 Python version: 3.10.14 (main, May 6 2024, 19:42:50) [GCC 11.2.0] (64-bit runtime) Python platform: Linux-5.15.0-113-generic-x86_64-with-glibc2.31 Is CUDA available: True CUDA runtime version: 12.1.105 CUDA_MODULE_LOADING set to: LAZY GPU models and configuration: GPU 0: NVIDIA GeForce RTX 4090 GPU 1: NVIDIA GeForce RTX 4090 GPU 2: NVIDIA GeForce RTX 4090 GPU 3: NVIDIA GeForce RTX 4090 Nvidia driver version: 555.42.02 cuDNN version: Probably one of the following: /data/jiangyulong/software/cuda121/targets/x86_64-linux/lib/libcudnn.so.8.9.2 /data/jiangyulong/software/cuda121/targets/x86_64-linux/lib/libcudnn_adv_infer.so.8.9.2 /data/jiangyulong/software/cuda121/targets/x86_64-linux/lib/libcudnn_adv_train.so.8.9.2 /data/jiangyulong/software/cuda121/targets/x86_64-linux/lib/libcudnn_cnn_infer.so.8.9.2 /data/jiangyulong/software/c...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 7: urrent environment ```text ollecting environment information... PyTorch version: 2.3.1+cu121 Is debug build: False CUDA used to build PyTorch: 12.1 ROCM used to build PyTorch: N/A OS: Ubuntu 20.04.6 LTS (x86_64) GCC ver...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 6: onment information... PyTorch version: 2.3.1+cu121 Is debug build: False CUDA used to build PyTorch: 12.1 ROCM used to build PyTorch: N/A OS: Ubuntu 20.04.6 LTS (x86_64) GCC version: (Ubuntu 9.4.0-1ubuntu1~20.04.2) 9.4....
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 5: [Usage]: PeftModelForCausalLM is not JSON serializable usage ### Your current environment ```text ollecting environment information... PyTorch version: 2.3.1+cu121 Is debug build: False CUDA used to build PyTorch: 12.1...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 3: cted Vulnerability Meltdown: Not affected Vulnerability Mmio stale data: Mitigation; Clear CPU buffers; SMT vulnerable Vulnerability Retbleed: Mitigation; Enhanced IBRS Vulnerability Spec rstack overflow: Not affected V...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 2: nvironment information... PyTorch version: 2.3.1+cu121 Is debug build: False CUDA used to build PyTorch: 12.1 ROCM used to build PyTorch: N/A OS: Ubuntu 20.04.6 LTS (x86_64) GCC version: (Ubuntu 9.4.0-1ubuntu1~20.04.2)...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
