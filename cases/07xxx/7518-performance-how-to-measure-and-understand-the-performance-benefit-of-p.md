# vllm-project/vllm#7518: [Performance]: How to measure and understand the performance benefit of prefix caching

| 字段 | 值 |
| --- | --- |
| Issue | [#7518](https://github.com/vllm-project/vllm/issues/7518) |
| 状态 | closed |
| 标签 | performance;stale |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | attention_kv_cache;ci_build;distributed_parallel;hardware_porting;model_support;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | attention;cuda;kernel;operator;sampling;triton |
| 症状 | build_error;nan_inf |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Performance]: How to measure and understand the performance benefit of prefix caching

### Issue 正文摘录

### Proposal to improve performance _No response_ ### Report of performance regression _No response_ ### Misc discussion on performance I am trying to understand how prefix caching helps with prompts of different lengths, so I ran the [benchmark_prefix_caching.py](https://github.com/vllm-project/vllm/blob/main/benchmarks/benchmark_prefix_caching.py) with different prompt lengths (basically `PROMPT * n` in the code). I also changed the `num_prompts` to 1 and set the output_len to 1. I also changed the [`model_runner.py`](https://github.com/vllm-project/vllm/blob/main/vllm/worker/model_runner.py) to understand where the benefit comes from. IMO, the benefit should come from model execution because prefix caching reduces the complexity of attention of `O(n^2)` to `O(n)`. I added the following timestamps for my understanding: ```diff diff --git a/vllm/worker/model_runner.py b/vllm/worker/model_runner.py index f9c26e0c..fdac9af4 100644 --- a/vllm/worker/model_runner.py +++ b/vllm/worker/model_runner.py @@ -1360,6 +1360,7 @@ class ModelRunner(GPUModelRunnerBase[ModelInputForGPUWithSamplingMetadata]): "finished_requests_ids": model_input.finished_requests_ids, "request_ids_to_seq_ids": mo...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 7: [43/60927] PyTorch version: 2.4.0+cu121 Is debug build: False CUDA used to build PyTorch: 12.1 ROCM used to build PyTorch: N/A OS: Ubuntu 20.04.5 LTS (x86_64)
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 6: tolist()` is called and the model executable is not really executing the cuda kernel synchronously. I guess this may relate to cuda graph but I saw the above result both with cuda graph enabled and disabled. I also trie...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 6: he `num_prompts` to 1 and set the output_len to 1. I also changed the [`model_runner.py`](https://github.com/vllm-project/vllm/blob/main/vllm/worker/model_runner.py) to understand where the benefit comes from. IMO, the...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 4: ure and understand the performance benefit of prefix caching performance;stale ### Proposal to improve performance _No response_ ### Report of performance regression _No response_ ### Misc discussion on performance I am...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 3: roposal to improve performance _No response_ ### Report of performance regression _No response_ ### Misc discussion on performance I am trying to understand how prefix caching helps with prompts of different lengths, so...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
