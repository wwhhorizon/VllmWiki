# vllm-project/vllm#6725: [Bug]: 8-way tensor parallelism w/ Punica broken on Ubuntu 20.04 (effectively Azure) since v0.5

| 字段 | 值 |
| --- | --- |
| Issue | [#6725](https://github.com/vllm-project/vllm/issues/6725) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 5; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;hardware_porting;model_support;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cuda;operator;sampling;triton |
| 症状 | build_error;crash;nan_inf;slowdown |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: 8-way tensor parallelism w/ Punica broken on Ubuntu 20.04 (effectively Azure) since v0.5

### Issue 正文摘录

### Your current environment ```text PyTorch version: 2.3.1+cu121 Is debug build: False CUDA used to build PyTorch: 12.1 ROCM used to build PyTorch: N/A **OS: Ubuntu 20.04.6 LTS (x86_64)** **GCC version: (Ubuntu 9.4.0-1ubuntu1~20.04.2) 9.4.0** Clang version: Could not collect CMake version: version 3.30.1 **Libc version: glibc-2.31** Python version: 3.10.2 | packaged by conda-forge | (main, Feb 1 2022, 19:29:00) [GCC 9.4.0] (64-bit runtime) Python platform: Linux-5.15.0-1068-azure-x86_64-with-glibc2.31 Is CUDA available: True CUDA runtime version: 12.1.105 CUDA_MODULE_LOADING set to: LAZY GPU models and configuration: GPU 0: NVIDIA A100-SXM4-40GB GPU 1: NVIDIA A100-SXM4-40GB GPU 2: NVIDIA A100-SXM4-40GB GPU 3: NVIDIA A100-SXM4-40GB GPU 4: NVIDIA A100-SXM4-40GB GPU 5: NVIDIA A100-SXM4-40GB GPU 6: NVIDIA A100-SXM4-40GB GPU 7: NVIDIA A100-SXM4-40GB Nvidia driver version: 535.183.06 cuDNN version: Probably one of the following: /usr/lib/x86_64-linux-gnu/libcudnn.so.8.9.7 /usr/lib/x86_64-linux-gnu/libcudnn.so.9.2.1 /usr/lib/x86_64-linux-gnu/libcudnn_adv.so.9.2.1 /usr/lib/x86_64-linux-gnu/libcudnn_adv_infer.so.8.9.7 /usr/lib/x86_64-linux-gnu/libcudnn_adv_train.so.8.9.7 /usr/lib/x86_64-l...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 9: zure) since v0.5 bug;stale ### Your current environment ```text PyTorch version: 2.3.1+cu121 Is debug build: False CUDA used to build PyTorch: 12.1 ROCM used to build PyTorch: N/A **OS: Ubuntu 20.04.6 LTS (x86_64)** **G...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 6: [Bug]: 8-way tensor parallelism w/ Punica broken on Ubuntu 20.04 (effectively Azure) since v0.5 bug;stale ### Your current environment ```text PyTorch version: 2.3.1+cu121 Is debug build: False CUDA used to build PyTorc...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: True CUDA runtime version: 12.1.105 CUDA_MODULE_LOADING set to: LAZY GPU models and configuration: GPU 0: NVIDIA A100-SXM4-40GB GPU 1: NVIDIA A100-SXM4-40GB GPU 2: NVIDIA A100-SXM4-40GB GPU 3: NVIDIA A100-SXM4-40GB GPU...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 3: lism w/ Punica broken on Ubuntu 20.04 (effectively Azure) since v0.5 bug;stale ### Your current environment ```text PyTorch version: 2.3.1+cu121 Is debug build: False CUDA used to build PyTorch: 12.1 ROCM used to build...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 2: rent environment ```text PyTorch version: 2.3.1+cu121 Is debug build: False CUDA used to build PyTorch: 12.1 ROCM used to build PyTorch: N/A **OS: Ubuntu 20.04.6 LTS (x86_64)** **GCC version: (Ubuntu 9.4.0-1ubuntu1~20.0...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
