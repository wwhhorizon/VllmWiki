# vllm-project/vllm#5532: [Bug]: Very slow execution of from_lora_tensors() when using mp instead of ray as --distributed-executor-backend.

| 字段 | 值 |
| --- | --- |
| Issue | [#5532](https://github.com/vllm-project/vllm/issues/5532) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 0; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;speculative_decoding |
| 子分类 |  |
| Operator 关键词 | cuda;operator;triton |
| 症状 | build_error;slowdown |
| 根因提示 | dtype;env_dependency;shape |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Very slow execution of from_lora_tensors() when using mp instead of ray as --distributed-executor-backend.

### Issue 正文摘录

### Your current environment ```text The output of `python collect_env.py` The output of `python collect_env.py` Python 3.10.12 (main, Nov 20 2023, 15:14:05) [GCC 11.4.0] on linux Type "help", "copyright", "credits" or "license" for more information. >>> quit Use quit() or Ctrl-D (i.e. EOF) to exit >>> quit() root@vllm-0-4-3-predictor-00001-deployment-54797fd955-p7b8g:/vllm-workspace# python3 collect_env.py Collecting environment information... PyTorch version: 2.3.0+cu121 Is debug build: False CUDA used to build PyTorch: 12.1 ROCM used to build PyTorch: N/A OS: Ubuntu 22.04.4 LTS (x86_64) GCC version: (Ubuntu 11.4.0-1ubuntu1~22.04) 11.4.0 Clang version: Could not collect CMake version: version 3.29.5 Libc version: glibc-2.35 Python version: 3.10.12 (main, Nov 20 2023, 15:14:05) [GCC 11.4.0] (64-bit runtime) Python platform: Linux-5.4.0-65-generic-x86_64-with-glibc2.35 Is CUDA available: True CUDA runtime version: Could not collect CUDA_MODULE_LOADING set to: LAZY GPU models and configuration: GPU 0: NVIDIA A100-SXM4-80GB GPU 1: NVIDIA A100-SXM4-80GB Nvidia driver version: 535.86.10 cuDNN version: Could not collect HIP runtime version: N/A MIOpen runtime version: N/A Is XNNPACK av...

## 现有链接修复摘要

#6109 [Bugfix] set OMP_NUM_THREADS to 1 by default when using the multiproc_gpu_executor

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 7: ce# python3 collect_env.py Collecting environment information... PyTorch version: 2.3.0+cu121 Is debug build: False CUDA used to build PyTorch: 12.1 ROCM used to build PyTorch: N/A OS: Ubuntu 22.04.4 LTS (x86_64) GCC ve...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 6: onment information... PyTorch version: 2.3.0+cu121 Is debug build: False CUDA used to build PyTorch: 12.1 ROCM used to build PyTorch: N/A OS: Ubuntu 22.04.4 LTS (x86_64) GCC version: (Ubuntu 11.4.0-1ubuntu1~22.04) 11.4....
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 5: .0] on linux Type "help", "copyright", "credits" or "license" for more information. >>> quit Use quit() or Ctrl-D (i.e. EOF) to exit >>> quit() root@vllm-0-4-3-predictor-00001-deployment-54797fd955-p7b8g:/vllm-workspace...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 2: om_lora_tensors() when using mp instead of ray as --distributed-executor-backend. bug ### Your current environment ```text The output of `python collect_env.py` The output of `python collect_env.py` Python 3.10.12 (main...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 2: avx512cd sha_ni avx512bw avx512vl xsaveopt xsavec xgetbv1 xsaves avx512_bf16 wbnoinvd arat avx512vbmi umip pku ospke avx512_vbmi2 gfni vaes vpclmulqdq avx512_vnni avx512_bitalg avx512_vpopcntdq rdpid cldemote movdiri mo...

## 关联 PR 证据

| PR | 链接类型 | 置信度 | PR 标题 | 证据 |
| --- | --- | ---: | --- | --- |
| [#6109](https://github.com/vllm-project/vllm/pull/6109) | closes_keyword | 0.95 | [Bugfix] set OMP_NUM_THREADS to 1 by default when using the multiproc_gpu_executor | FIX #5532 **BEFORE SUBMITTING, PLEASE READ THE CHECKLIST BELOW AND FILL IN THE DESCRIPTION ABOVE** --- <details> <!-- inside this <details> section, markdown rendering do |

## Wiki 抽取状态

- 后续迭代应在可用时读取完整讨论评论。
