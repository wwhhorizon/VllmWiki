# vllm-project/vllm#6734: [Bug]: vllm-0.5.3.post1部署Qwen2-72b-instruct-awq模型，刚开始服务正常，但是并发高的时候就报错

| 字段 | 值 |
| --- | --- |
| Issue | [#6734](https://github.com/vllm-project/vllm/issues/6734) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 7; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;frontend_api |
| 子分类 |  |
| Operator 关键词 | cuda;kernel |
| 症状 | build_error;mismatch |
| 根因提示 | env_dependency |
| 硬件范围 | nvidia |
| 需要人工复核 | True |

## 源证据

### Issue 标题

> [Bug]: vllm-0.5.3.post1部署Qwen2-72b-instruct-awq模型，刚开始服务正常，但是并发高的时候就报错

### Issue 正文摘录

### Your current environment cuda-12.2 torch-2.3.1 vllm-0.5.3.post1 ### 🐛 Describe the bug [rank1]:[E ProcessGroupNCCL.cpp:1414] [PG 2 Rank 1] Process group watchdog thread terminated with exception: CUDA error: an illegal memory access was encountered CUDA kernel errors might be asynchronously reported at some other API call, so the stacktrace below might be incorrect. For debugging consider passing CUDA_LAUNCH_BLOCKING=1. Compile with `TORCH_USE_CUDA_DSA` to enable device-side assertions. Exception raised from c10_cuda_check_implementation at ../c10/cuda/CUDAException.cpp:43 (most recent call first): frame #0: c10::Error::Error(c10::SourceLocation, std::string) + 0x57 (0x7f0c70fb1897 in /data/anaconda3/envs/qwen/lib/python3.10/site-packages/torch/lib/libc10.so) frame #1: c10::detail::torchCheckFail(char const*, char const*, unsigned int, std::string const&) + 0x64 (0x7f0c70f61b25 in /data/anaconda3/envs/qwen/lib/python3.10/site-packages/torch/lib/libc10.so) frame #2: c10::cuda::c10_cuda_check_implementation(int, char const*, char const*, int, bool) + 0x118 (0x7f0c71089718 in /data/anaconda3/envs/qwen/lib/python3.10/site-packages/torch/lib/libc10_cuda.so) frame #3: c10d::ProcessG...

## 现有链接修复摘要

#4 Use FlashAttention for `multi_query_kv_attention` | #6 Automatically configure KV cache size | #7 Support beam search & parallel generation | #7142 [BugFix] Potential Fix to CUDA Illegal Memory Error

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: ght be incorrect. For debugging consider passing CUDA_LAUNCH_BLOCKING=1. Compile with `TORCH_USE_CUDA_DSA` to enable device-side assertions. Exception raised from c10_cuda_check_implementation at ../c10/cuda/CUDAExcepti...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: 72b-instruct-awq模型，刚开始服务正常，但是并发高的时候就报错 bug ### Your current environment cuda-12.2 torch-2.3.1 vllm-0.5.3.post1 ### 🐛 Describe the bug [rank1]:[E ProcessGroupNCCL.cpp:1414] [PG 2 Rank 1] Process group watchdog thread ter...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: [Bug]: vllm-0.5.3.post1部署Qwen2-72b-instruct-awq模型，刚开始服务正常，但是并发高的时候就报错 bug ### Your current environment cuda-12.2 torch-2.3.1 vllm-0.5.3.post1 ### 🐛 Describe the bug [rank1]:[E ProcessGroupNCCL.cpp:1414] [PG 2 Rank 1] Pr...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: uild;frontend_api cuda;kernel build_error;mismatch env_dependency #4 Use FlashAttention for `multi_query_kv_attention` | #6 Automatically configure KV cache size | #7 Support beam search & parallel generation | #7142 [B...
- [Bitwise 确定性与数值等价](../patterns/bitwise_determinism_equivalence.md) - 分数 1: ear to be %d ' correctness ci_build;frontend_api cuda;kernel build_error;mismatch env_dependency #4 Use FlashAttention for `multi_query_kv_attention` | #6 Automatically configure KV cache size | #7 Support beam search &...

## 关联 PR 证据

| PR | 链接类型 | 置信度 | PR 标题 | 证据 |
| --- | --- | ---: | --- | --- |
| [#4](https://github.com/vllm-project/vllm/pull/4) | mentioned | 0.45 | Use FlashAttention for `multi_query_kv_attention` | /qwen/lib/python3.10/site-packages/torch/lib/libtorch_cuda.so) frame #4: c10d::processgroupnccl::worknccl::iscompleted() + 0x58 (0x7f0c7228a9e8 in /data/anaconda3/envs/qwen/lib/py… |
| [#6](https://github.com/vllm-project/vllm/pull/6) | mentioned | 0.45 | Automatically configure KV cache size | /qwen/lib/python3.10/site-packages/torch/lib/libtorch_cuda.so) frame #6: c10d::processgroupnccl::ncclcommwatchdog() + 0x10c (0x7f0c72290dcc in /data/anaconda3/envs/qwen/lib/python… |
| [#7](https://github.com/vllm-project/vllm/pull/7) | mentioned | 0.45 | Support beam search & parallel generation | /qwen/lib/python3.10/site-packages/torch/lib/libtorch_cuda.so) frame #7: <unknown function> + 0xdbbf4 (0x7f0cbdd45bf4 in /data/anaconda3/envs/qwen/bin/../lib/libstdc++.so.6) frame |
| [#7142](https://github.com/vllm-project/vllm/pull/7142) | closes_keyword | 0.95 | [BugFix] Potential Fix to CUDA Illegal Memory Error | FIX #6833 , #7003, #6734, #5938 and potentially more (*link existing issues this PR will resolve*) **BEFORE SUBMITTING, PLEASE READ THE CHECKLIST BELOW AND FILL IN THE DESCRIPTI |

## Wiki 抽取状态

- 后续迭代应在可用时读取完整讨论评论。
