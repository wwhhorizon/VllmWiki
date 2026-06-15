# vllm-project/vllm#6254: [Bug]: Engine timeout error due to request step residual

| 字段 | 值 |
| --- | --- |
| Issue | [#6254](https://github.com/vllm-project/vllm/issues/6254) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 0; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | development |
| 工作域 | ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;sampling_logits;speculative_decoding |
| 子分类 | env_compat |
| Operator 关键词 | cuda;operator;sampling;triton |
| 症状 | build_error |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Engine timeout error due to request step residual

### Issue 正文摘录

### Your current environment ```text Collecting environment information... PyTorch version: 2.3.0+cu121 Is debug build: False CUDA used to build PyTorch: 12.1 ROCM used to build PyTorch: N/A OS: Debian GNU/Linux 11 (bullseye) (x86_64) GCC version: (Debian 10.2.1-6) 10.2.1 20210110 Clang version: Could not collect CMake version: version 3.29.2 Libc version: glibc-2.31 Python version: 3.9.2 (default, Feb 28 2021, 17:03:44) [GCC 10.2.1 20210110] (64-bit runtime) Python platform: Linux-5.4.143.bsk.8-amd64-x86_64-with-glibc2.31 Is CUDA available: True CUDA runtime version: 10.0.130 CUDA_MODULE_LOADING set to: LAZY GPU models and configuration: GPU 0: NVIDIA L40 GPU 1: NVIDIA L40 GPU 2: NVIDIA L40 GPU 3: NVIDIA L40 Nvidia driver version: Could not collect cuDNN version: /usr/lib/x86_64-linux-gnu/libcudnn.so.7.6.0 HIP runtime version: N/A MIOpen runtime version: N/A Is XNNPACK available: True CPU: Architecture: x86_64 CPU op-mode(s): 32-bit, 64-bit Byte Order: Little Endian Address sizes: 52 bits physical, 57 bits virtual CPU(s): 180 On-line CPU(s) list: 0-179 Thread(s) per core: 2 Core(s) per socket: 45 Socket(s): 2 NUMA node(s): 2 Vendor ID: GenuineIntel CPU family: 6 Model: 143 Model...

## 现有链接修复摘要

#6255 [BugFix]: fix engine timeout due to request abort

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 7: rrent environment ```text Collecting environment information... PyTorch version: 2.3.0+cu121 Is debug build: False CUDA used to build PyTorch: 12.1 ROCM used to build PyTorch: N/A OS: Debian GNU/Linux 11 (bullseye) (x86...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 5: onment information... PyTorch version: 2.3.0+cu121 Is debug build: False CUDA used to build PyTorch: 12.1 ROCM used to build PyTorch: N/A OS: Debian GNU/Linux 11 (bullseye) (x86_64) GCC version: (Debian 10.2.1-6) 10.2.1...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 4: avx512cd sha_ni avx512bw avx512vl xsaveopt xsavec xgetbv1 xsaves avx512_bf16 wbnoinvd arat avx512vbmi umip pku ospke waitpkg avx512_vbmi2 gfni vaes vpclmulqdq avx512_vnni avx512_bitalg avx512_vpopcntdq rdpid cldemote mo...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: idual bug ### Your current environment ```text Collecting environment information... PyTorch version: 2.3.0+cu121 Is debug build: False CUDA used to build PyTorch: 12.1 ROCM used to build PyTorch: N/A OS: Debian GNU/Lin...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 2: ir64b md_clear arch_capabilities Versions of relevant libraries: [pip3] flashinfer==0.0.8+cu121torch2.3 [pip3] numpy==1.23.4 [pip3] nvidia-nccl-cu11==2.14.3 [pip3] nvidia-nccl-cu12==2.20.5 [pip3] torch==2.3.0 [pip3] tor...

## 关联 PR 证据

| PR | 链接类型 | 置信度 | PR 标题 | 证据 |
| --- | --- | ---: | --- | --- |
| [#6255](https://github.com/vllm-project/vllm/pull/6255) | closes_keyword | 0.95 | [BugFix]: fix engine timeout due to request abort | FIX #6254 (*link existing issues this PR will resolve*) ![image](https://github.com/vllm-project/vllm/assets/62173185/6899948a-124a-4763-9a0f-d548eeb1da41) **BEFORE SUBMITTIN |

## Wiki 抽取状态

- 后续迭代应在可用时读取完整讨论评论。
