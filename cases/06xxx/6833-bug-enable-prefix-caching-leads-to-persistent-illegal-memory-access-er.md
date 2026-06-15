# vllm-project/vllm#6833: [Bug]: enable_prefix_caching leads to persistent illegal memory access error 

| 字段 | 值 |
| --- | --- |
| Issue | [#6833](https://github.com/vllm-project/vllm/issues/6833) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 10; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | attention_kv_cache;ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;sampling_logits;scheduler_memory;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cuda;operator;sampling;triton |
| 症状 | build_error;crash;nan_inf |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: enable_prefix_caching leads to persistent illegal memory access error 

### Issue 正文摘录

### Your current environment ```text Collecting environment information... PyTorch version: 2.3.1+cu121 Is debug build: False CUDA used to build PyTorch: 12.1 ROCM used to build PyTorch: N/A OS: Ubuntu 22.04.4 LTS (x86_64) GCC version: (Ubuntu 11.4.0-1ubuntu1~22.04) 11.4.0 Clang version: Could not collect CMake version: version 3.30.1 Libc version: glibc-2.35 Python version: 3.11.0rc1 (main, Aug 12 2022, 10:02:14) [GCC 11.2.0] (64-bit runtime) Python platform: Linux-5.15.0-1064-aws-x86_64-with-glibc2.35 Is CUDA available: True CUDA runtime version: Could not collect CUDA_MODULE_LOADING set to: LAZY GPU models and configuration: GPU 0: NVIDIA A10G Nvidia driver version: 535.161.07 cuDNN version: Probably one of the following: /usr/lib/x86_64-linux-gnu/libcudnn.so.8.9.7 /usr/lib/x86_64-linux-gnu/libcudnn_adv_infer.so.8.9.7 /usr/lib/x86_64-linux-gnu/libcudnn_adv_train.so.8.9.7 /usr/lib/x86_64-linux-gnu/libcudnn_cnn_infer.so.8.9.7 /usr/lib/x86_64-linux-gnu/libcudnn_cnn_train.so.8.9.7 /usr/lib/x86_64-linux-gnu/libcudnn_ops_infer.so.8.9.7 /usr/lib/x86_64-linux-gnu/libcudnn_ops_train.so.8.9.7 HIP runtime version: N/A MIOpen runtime version: N/A Is XNNPACK available: True CPU: Architectur...

## 现有链接修复摘要

#7018 [Bugfix] Fix block table for seqs that have prefix cache hits | #7142 [BugFix] Potential Fix to CUDA Illegal Memory Error

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 8: rrent environment ```text Collecting environment information... PyTorch version: 2.3.1+cu121 Is debug build: False CUDA used to build PyTorch: 12.1 ROCM used to build PyTorch: N/A OS: Ubuntu 22.04.4 LTS (x86_64) GCC ver...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 5: onment information... PyTorch version: 2.3.1+cu121 Is debug build: False CUDA used to build PyTorch: 12.1 ROCM used to build PyTorch: N/A OS: Ubuntu 22.04.4 LTS (x86_64) GCC version: (Ubuntu 11.4.0-1ubuntu1~22.04) 11.4....
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 5: bug;stale ### Your current environment ```text Collecting environment information... PyTorch version: 2.3.1+cu121 Is debug build: False CUDA used to build PyTorch: 12.1 ROCM used to build PyTorch: N/A OS: Ubuntu 22.04.4...
- [KV Cache 容量、压缩与 Offload](../patterns/kv_cache_capacity_offload.md) - 分数 3: the error - trying 0.4.2 and other versions does not help - decreasing gpu memory usage to 0.8 does not help - using os.environ["VLLM_ATTENTION_BACKEND"]="XFORMERS" leads to `The Python process exited with exit code 139...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 3: able_prefix_caching leads to persistent illegal memory access error bug;stale ### Your current environment ```text Collecting environment information... PyTorch version: 2.3.1+cu121 Is debug build: False CUDA used to bu...

## 关联 PR 证据

| PR | 链接类型 | 置信度 | PR 标题 | 证据 |
| --- | --- | ---: | --- | --- |
| [#7018](https://github.com/vllm-project/vllm/pull/7018) | mentioned | 0.6 | [Bugfix] Fix block table for seqs that have prefix cache hits | ion generate the incorrect result or invalid memory access like #7003 #6833 and #5543 **BEFORE SUBMITTING, PLEASE READ THE CHECKLIST BELOW AND FILL IN THE DESCRIPTION ABOVE** -- |
| [#7142](https://github.com/vllm-project/vllm/pull/7142) | closes_keyword | 0.95 | [BugFix] Potential Fix to CUDA Illegal Memory Error | FIX #6833 , #7003, #6734, #5938 and potentially more (*link existing issues this PR will resolve*) **BEFORE SUBMITTING, PLEASE READ THE CHECKLIST BELOW AND FILL IN THE DESCRIPTI |

## Wiki 抽取状态

- 后续迭代应在可用时读取完整讨论评论。
