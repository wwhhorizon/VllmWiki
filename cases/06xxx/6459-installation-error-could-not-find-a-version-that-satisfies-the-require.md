# vllm-project/vllm#6459: [Installation]: ERROR: Could not find a version that satisfies the requirement pyzmq (from versions: none)

| 字段 | 值 |
| --- | --- |
| Issue | [#6459](https://github.com/vllm-project/vllm/issues/6459) |
| 状态 | closed |
| 标签 | installation |
| 评论 | 4; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | development |
| 工作域 | ci_build;distributed_parallel;hardware_porting;model_support |
| 子分类 | env_compat |
| Operator 关键词 | cuda;operator;triton |
| 症状 | build_error;import_error |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Installation]: ERROR: Could not find a version that satisfies the requirement pyzmq (from versions: none)

### Issue 正文摘录

### Your current environment ```text Collecting environment information... WARNING 07-16 03:53:58 _custom_ops.py:14] Failed to import from vllm._C with ModuleNotFoundError("No module named 'vllm._C'") /disk3/renyanfu/liukaiyuan/project/opencompass/vllm/vllm/usage/usage_lib.py:19: RuntimeWarning: Failed to read commit hash: No module named 'vllm.commit_id' from vllm.version import __version__ as VLLM_VERSION PyTorch version: 2.3.1+cu121 Is debug build: False CUDA used to build PyTorch: 12.1 ROCM used to build PyTorch: N/A OS: Ubuntu 20.04.6 LTS (x86_64) GCC version: (Ubuntu 9.4.0-1ubuntu1~20.04.1) 9.4.0 Clang version: Could not collect CMake version: version 3.30.0 Libc version: glibc-2.31 Python version: 3.10.13 (main, Sep 11 2023, 13:44:35) [GCC 11.2.0] (64-bit runtime) Python platform: Linux-3.10.0-1127.19.1.el7.x86_64-x86_64-with-glibc2.31 Is CUDA available: True CUDA runtime version: 12.1.105 CUDA_MODULE_LOADING set to: LAZY GPU models and configuration: GPU 0: NVIDIA A100-SXM4-40GB GPU 1: NVIDIA A100-SXM4-40GB GPU 2: NVIDIA A100-SXM4-40GB GPU 3: NVIDIA A100-SXM4-40GB Nvidia driver version: 525.60.13 cuDNN version: Probably one of the following: /usr/lib/x86_64-linux-gnu/libcu...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 10: [Installation]: ERROR: Could not find a version that satisfies the requirement pyzmq (from versions: none) installation ### Your current environment ```text Collecting environment information... WARNING 07-16 03:53:58 _c
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 6: ion__ as VLLM_VERSION PyTorch version: 2.3.1+cu121 Is debug build: False CUDA used to build PyTorch: 12.1 ROCM used to build PyTorch: N/A OS: Ubuntu 20.04.6 LTS (x86_64) GCC version: (Ubuntu 9.4.0-1ubuntu1~20.04.1) 9.4....
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: tallation ### Your current environment ```text Collecting environment information... WARNING 07-16 03:53:58 _custom_ops.py:14] Failed to import from vllm._C with ModuleNotFoundError("No module named 'vllm._C'") /disk3/r...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: tic==0.2.2 [pip3] torchvision==0.18.1 [pip3] transformers==4.42.4 [pip3] triton==2.3.1 [conda] blas 1.0 mkl [conda] ffmpeg 4.3 hf484d3e_0 pytorch [conda] libjpeg-turbo 2.0.0 h9bf14
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 1: version__ as VLLM_VERSION PyTorch version: 2.3.1+cu121 Is debug build: False CUDA used to build PyTorch: 12.1 ROCM used to build PyTorch: N/A OS: Ubuntu 20.04.6 LTS (x86_64) GCC version: (Ubuntu 9.4.0-1ubuntu1~20.04.1)...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
