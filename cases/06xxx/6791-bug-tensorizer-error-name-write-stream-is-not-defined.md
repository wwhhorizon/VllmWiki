# vllm-project/vllm#6791: [Bug]: tensorizer error: name '_write_stream' is not defined

| 字段 | 值 |
| --- | --- |
| Issue | [#6791](https://github.com/vllm-project/vllm/issues/6791) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;quantization;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cuda;operator;quantization;sampling;triton |
| 症状 | build_error;crash;nan_inf;oom |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: tensorizer error: name '_write_stream' is not defined

### Issue 正文摘录

### Your current environment ```text Collecting environment information... PyTorch version: 2.3.1+cu121 Is debug build: False CUDA used to build PyTorch: 12.1 ROCM used to build PyTorch: N/A OS: Ubuntu 24.04 LTS (x86_64) GCC version: (Ubuntu 13.2.0-23ubuntu4) 13.2.0 Clang version: Could not collect CMake version: version 3.30.1 Libc version: glibc-2.39 Python version: 3.10.14 (main, May 6 2024, 19:42:50) [GCC 11.2.0] (64-bit runtime) Python platform: Linux-6.8.0-1010-aws-x86_64-with-glibc2.39 Is CUDA available: True CUDA runtime version: 12.0.140 CUDA_MODULE_LOADING set to: LAZY GPU models and configuration: GPU 0: NVIDIA A10G Nvidia driver version: 535.183.01 cuDNN version: Could not collect HIP runtime version: N/A MIOpen runtime version: N/A Is XNNPACK available: True CPU: Architecture: x86_64 CPU op-mode(s): 32-bit, 64-bit Address sizes: 48 bits physical, 48 bits virtual Byte Order: Little Endian CPU(s): 8 On-line CPU(s) list: 0-7 Vendor ID: AuthenticAMD Model name: AMD EPYC 7R32 CPU family: 23 Model: 49 Thread(s) per core: 2 Core(s) per socket: 4 Socket(s): 1 Stepping: 0 BogoMIPS: 5600.00 Flags: fpu vme de pse tsc msr pae mce cx8 apic sep mtrr pge mca cmov pat pse36 clflush m...

## 现有链接修复摘要

#7889 [Doc]: Update tensorizer docs to include vllm[tensorizer]

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 7: rrent environment ```text Collecting environment information... PyTorch version: 2.3.1+cu121 Is debug build: False CUDA used to build PyTorch: 12.1 ROCM used to build PyTorch: N/A OS: Ubuntu 24.04 LTS (x86_64) GCC versi...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 5: onment information... PyTorch version: 2.3.1+cu121 Is debug build: False CUDA used to build PyTorch: 12.1 ROCM used to build PyTorch: N/A OS: Ubuntu 24.04 LTS (x86_64) GCC version: (Ubuntu 13.2.0-23ubuntu4) 13.2.0 Clang...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: fined bug ### Your current environment ```text Collecting environment information... PyTorch version: 2.3.1+cu121 Is debug build: False CUDA used to build PyTorch: 12.1 ROCM used to build PyTorch: N/A OS: Ubuntu 24.04 L...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 3: None, rope_theta=None, tokenizer_revision=None, trust_remote_code=False, dtype=torch.float16, max_seq_len=2048, download_dir=None, load_format=LoadFormat.AUTO, tensor_parallel_size=1, pipeline_parallel_size=1, disable_c...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 2: rch==2.3.1 [pip3] torchvision==0.18.1 [pip3] transformers==4.43.2 [pip3] triton==2.3.1 [conda] numpy 1.26.4 pypi_0 pypi [conda] nvidia-nccl-cu12 2.20.5 pypi_0 pypi [conda] torch 2.3.1

## 关联 PR 证据

| PR | 链接类型 | 置信度 | PR 标题 | 证据 |
| --- | --- | ---: | --- | --- |
| [#7889](https://github.com/vllm-project/vllm/pull/7889) | closes_keyword | 0.95 | [Doc]: Update tensorizer docs to include vllm[tensorizer] | FIX #6791 **BEFORE SUBMITTING, PLEASE READ THE CHECKLIST BELOW AND FILL IN THE DESCRIPTION ABOVE** --- <details> <!-- inside this <details> section, markdown rendering d |

## Wiki 抽取状态

- 后续迭代应在可用时读取完整讨论评论。
