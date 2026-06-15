# vllm-project/vllm#17788: [Performance]: benchmark_serving results for Qwen3-32B vs Qwen2-32B-FP8 are almost the same.

| 字段 | 值 |
| --- | --- |
| Issue | [#17788](https://github.com/vllm-project/vllm/issues/17788) |
| 状态 | closed |
| 标签 | performance;stale |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;quantization;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cuda;fp8;kernel;operator;quantization;sampling;triton |
| 症状 | build_error;nan_inf;slowdown |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Performance]: benchmark_serving results for Qwen3-32B vs Qwen2-32B-FP8 are almost the same.

### Issue 正文摘录

### Proposal to improve performance _No response_ ### Report of performance regression I am running vllm on a single H100 NVL node with 95GB VRAM and vllm 0.8.5.post1. Deployed Qwen3 32B fp16 using: ``` vllm serve "Qwen/Qwen3-32B" \ --host 0.0.0.0 \ --port 8000 \ --download-dir /workspace \ --dtype bfloat16 \ --max-model-len 32000 \ --enable-chunked-prefill \ --enable-prefix-caching \ --seed 42 \ --max-num-seqs 32 \ --disable-log-requests ``` and then ran the benchmark_serving script via: ``` python3 benchmark_serving.py --dataset-path /root/ShareGPT_V3_unfiltered_cleaned_split.json --host 0.0.0.0 --port 8000 --model "Qwen/Qwen3-32B" --temperature 0.7 --top-k 20 --top-p 0.8 ``` and the results: ``` ============ Serving Benchmark Result ============ Successful requests: 1000 Benchmark duration (s): 306.78 Total input tokens: 217393 Total generated tokens: 200516 Request throughput (req/s): 3.26 Output token throughput (tok/s): 653.61 Total Token throughput (tok/s): 1362.23 ---------------Time to First Token---------------- Mean TTFT (ms): 146809.12 Median TTFT (ms): 148069.33 P99 TTFT (ms): 286485.34 -----Time per Output Token (excl. 1st token)------ Mean TPOT (ms): 47.06 Median TP...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 8: ly detected platform cuda. Collecting environment information... PyTorch version: 2.6.0+cu124 Is debug build: False CUDA used to build PyTorch: 12.4 ROCM used to build PyTorch: N/A OS: Debian GNU/Linux 12 (bookworm) (x8...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 7: [Performance]: benchmark_serving results for Qwen3-32B vs Qwen2-32B-FP8 are almost the same. performance;stale ### Proposal to improve performance _No response_ ### Report of performance regression I am running vllm on...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 6: se_ ### Report of performance regression I am running vllm on a single H100 NVL node with 95GB VRAM and vllm 0.8.5.post1. Deployed Qwen3 32B fp16 using: ``` vllm serve "Qwen/Qwen3-32B" \ --host 0.0.0.0 \ --port 8000 \ -...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 6: [Performance]: benchmark_serving results for Qwen3-32B vs Qwen2-32B-FP8 are almost the same. performance;stale ### Proposal to improve performance _No response_ ### Report of performance regression I am running vllm on...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 5: [Performance]: benchmark_serving results for Qwen3-32B vs Qwen2-32B-FP8 are almost the same. performance;stale ### Proposal to improve performance _No response_ ### Report of performance regression I am running vllm on...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
