# vllm-project/vllm#20174: [Performance]: Inefficient prefill attention compared to HuggingFace

| 字段 | 值 |
| --- | --- |
| Issue | [#20174](https://github.com/vllm-project/vllm/issues/20174) |
| 状态 | closed |
| 标签 | performance;stale |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | attention_kv_cache;ci_build;distributed_parallel;gemm_linear;hardware_porting;model_support;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | attention;cuda;kernel;operator;sampling;triton |
| 症状 | build_error;nan_inf;slowdown |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Performance]: Inefficient prefill attention compared to HuggingFace

### Issue 正文摘录

### Proposal to improve performance _No response_ ### Report of performance regression While benchmarking vLLM for offline inference against HuggingFace Transformers, I observed that the prefill attention in vLLM is significantly slower under certain conditions. With input_len=128 and max_num_seqs=1 on GPT2 model, vLLM defaults to using FlashAttention. In this setup, vLLM invokes two separate kernels (`flash::prepare_varlen_num_blocks_kernel` and `cutlass::device_kernel >`). This results in a total latency of ~9μs (without additional kernel launch overhead). In comparison, HuggingFace Transformers uses `pytorch_flash::flash_fwd_kernel` and completes the same computation in ~6μs. To reproduce the result, you can run the `benchmark_throughput.py` script in vLLM repo with the configuration above. ### Misc discussion on performance _No response_ ### Your current environment (if you think it is necessary) ```text The output of `python collect_env.py` ============================== System Info ============================== OS : Ubuntu 22.04.5 LTS (x86_64) GCC version : (Ubuntu 11.4.0-1ubuntu1~22.04) 11.4.0 Clang version : 16.0.6 (++20231112100510+7cbf1a259152-1~exp1~20231112100554.106)...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 8: [Performance]: Inefficient prefill attention compared to HuggingFace performance;stale ### Proposal to improve performance _No response_ ### Report of performance regression While benchmarking vLLM for offline inference...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 5: version : 2.7.0+cu126 Is debug build : False CUDA used to build PyTorch : 12.6 ROCM used to build PyTorch : N/A ============================== Python Environment ============================== Python version : 3.10.17 (...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 5: roposal to improve performance _No response_ ### Report of performance regression While benchmarking vLLM for offline inference against HuggingFace Transformers, I observed that the prefill attention in vLLM is signific...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: [Performance]: Inefficient prefill attention compared to HuggingFace performance;stale ### Proposal to improve performance _No response_ ### Report of performance regression While benchmarking vLLM for offline inference...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 4: [Performance]: Inefficient prefill attention compared to HuggingFace performance;stale ### Proposal to improve performance _No response_ ### Report of performance regression While benchmarking vLLM for offline inference...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
