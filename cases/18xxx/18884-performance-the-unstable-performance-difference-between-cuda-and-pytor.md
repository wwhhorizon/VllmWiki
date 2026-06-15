# vllm-project/vllm#18884: [Performance]: The Unstable Performance Difference between CUDA and PyTorch

| 字段 | 值 |
| --- | --- |
| Issue | [#18884](https://github.com/vllm-project/vllm/issues/18884) |
| 状态 | closed |
| 标签 | performance;stale |
| 评论 | 4; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | model_support |
| 子分类 | precision |
| Operator 关键词 | cuda;kernel;operator;triton |
| 症状 | nan_inf |
| 根因提示 | dtype;env_dependency;race_condition;shape |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Performance]: The Unstable Performance Difference between CUDA and PyTorch

### Issue 正文摘录

### Proposal to improve performance _No response_ ### Report of performance regression _No response_ ### Misc discussion on performance I have encountered such a problem：I implemented a custom CUDA operator for matrix multiplication and compared its time performance with PyTorch’s einsum method. In a standalone Python test script, the execution time of the CUDA operator was significantly less than that of the einsum method. The code and results for the test time are as follows: import pytest import torch import time from vllm._custom_ops import decode_matrix as decode_matrix_cuda from vllm.platforms import current_platform def decode_matrix_torch( a_sm: torch.Tensor, # [NUM_TOKENS, NUM_HEADS, HEAD_SIZE] q: torch.Tensor, # [NUM_HEADS,NUM_TOKENS, HEAD_SIZE] k_cache: torch.Tensor, # [NUM_HEADS,NUM_TOKENS, HEAD_SIZE] window_factors: torch.Tensor, # [NUM_HEADS,1, 1] ): a_sm = torch.einsum('hmd,hnd->hmn', q, k_cache) * (k_cache.shape[-1] ** -0.5) return a_sm NUM_BATCH_TOKENS = [3, 256, 512, 613, 1024, 1536, 4096] NUM_QUERY_HEADS = [4, 8, 12, 32, 48, 64] HEAD_SIZES = [32, 48, 64, 96, 128, 256] DTYPES = [torch.float32, torch.half, torch.bfloat16] @pytest.mark.parametrize("num_tokens", NUM...

## 候选优化模式

- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 4: Y_HEADS = [4, 8, 12, 32, 48, 64] HEAD_SIZES = [32, 48, 64, 96, 128, 256] DTYPES = [torch.float32, torch.half, torch.bfloat16] @pytest.mark.parametrize("num_tokens", NUM_BATCH_TOKENS) @pytest.mark.parametrize("num_query_...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: [Performance]: The Unstable Performance Difference between CUDA and PyTorch performance;stale ### Proposal to improve performance _No response_ ### Report of performance regression _No response_ ### Misc discussion on p...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: he einsum method. The code and results for the test time are as follows: import pytest import torch import time from vllm._custom_ops import decode_matrix as decode_matrix_cuda from vllm.platforms import current_platfor...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: The Unstable Performance Difference between CUDA and PyTorch performance;stale ### Proposal to improve performance _No response_ ### Report of performance regression _No response_ ### Misc discussion on performance I ha...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 2: roposal to improve performance _No response_ ### Report of performance regression _No response_ ### Misc discussion on performance I have encountered such a problem：I implemented a custom CUDA operator for matrix multip...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
