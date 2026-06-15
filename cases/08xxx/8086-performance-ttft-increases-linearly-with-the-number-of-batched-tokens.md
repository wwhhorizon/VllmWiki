# vllm-project/vllm#8086: [Performance]: TTFT increases linearly with the number of batched tokens

| 字段 | 值 |
| --- | --- |
| Issue | [#8086](https://github.com/vllm-project/vllm/issues/8086) |
| 状态 | closed |
| 标签 | performance;stale |
| 评论 | 4; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;hardware_porting;model_support;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cuda;operator;sampling;triton |
| 症状 | build_error;nan_inf |
| 根因提示 | env_dependency;shape |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Performance]: TTFT increases linearly with the number of batched tokens

### Issue 正文摘录

### Proposal to improve performance I have observed that TTFT increases linearly with a total number of batched tokens. For example, given 100k batch - TTFT is around 2min when an average prompt+completion length is 200 - TTFT is around 10min (increase 5X) when an average prompt+completion length is 2000 (increase 10x) This has been observed for several LLama3 model and the following parameters ``` enable_prefix_caching=True, block_size=3 max_num_batched_tokens=16000 max_model_len=16000 use_v2_block_manager=True ``` I would of course expect Requests Per Second (or similar metrics) to increase with increase in prompt+completion length, but why this happens so dramatically with TTFT (5X with 10X increase in prompt length)? Would be helpful for clarification and suggestions on resolution (e.g. adjusting continuous batching). Thanks in advance! ### Report of performance regression _No response_ ### Misc discussion on performance _No response_ ### Your current environment (if you think it is necessary) ```text PyTorch version: 2.3.1+cu121 Is debug build: False CUDA used to build PyTorch: 12.1 ROCM used to build PyTorch: N/A OS: Ubuntu 22.04.4 LTS (x86_64) GCC version: (Ubuntu 11.4.0-1u...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 7: Your current environment (if you think it is necessary) ```text PyTorch version: 2.3.1+cu121 Is debug build: False CUDA used to build PyTorch: 12.1 ROCM used to build PyTorch: N/A OS: Ubuntu 22.04.4 LTS (x86_64) GCC ver...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 5: s necessary) ```text PyTorch version: 2.3.1+cu121 Is debug build: False CUDA used to build PyTorch: 12.1 ROCM used to build PyTorch: N/A OS: Ubuntu 22.04.4 LTS (x86_64) GCC version: (Ubuntu 11.4.0-1ubuntu1~22.04) 11.4.0...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: letion length is 2000 (increase 10x) This has been observed for several LLama3 model and the following parameters ``` enable_prefix_caching=True, block_size=3 max_num_batched_tokens=16000 max_model_len=16000 use_v2_bloc...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 3: ]: TTFT increases linearly with the number of batched tokens performance;stale ### Proposal to improve performance I have observed that TTFT increases linearly with a total number of batched tokens. For example, given 1...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 3: ting continuous batching). Thanks in advance! ### Report of performance regression _No response_ ### Misc discussion on performance _No response_ ### Your current environment (if you think it is necessary) ```text PyTor...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
