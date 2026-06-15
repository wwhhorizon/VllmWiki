# vllm-project/vllm#12101: [Performance]: Question about TTFT for ngram speculative decoding

| 字段 | 值 |
| --- | --- |
| Issue | [#12101](https://github.com/vllm-project/vllm/issues/12101) |
| 状态 | closed |
| 标签 | performance;stale |
| 评论 | 4; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;quantization;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cuda;operator;quantization;sampling;triton |
| 症状 | build_error;nan_inf;slowdown |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Performance]: Question about TTFT for ngram speculative decoding

### Issue 正文摘录

### Proposal to improve performance ### Report of performance regression _No response_ ### Misc discussion on performance I am testing ngram speculative decoding for llama 3.3 70B model. Here is my config: base model: llama 3.3 70B instruct machine: 4 X H100 speculative method: ngram ngram-prompt-lookup-max: 5 num-speculative-tokens: 3 Here is command to start server: ``` python -m vllm.entrypoints.api_server --host=0.0.0.0 --port=7080 --model=/llama/Llama-3.3-70B-Instruct --tensor-parallel-size=4 --swap-space=16 --dtype=float16 --enable-chunked-prefill=True --gpu-memory-utilization=0.95 --speculative-model="[ngram]" --ngram-prompt-lookup-max=5 --num-speculative-tokens=3 ``` I've notice mean TTFT got improved from 135.34 ms to 115.42 ms: *) base (concurrency = 1): ``` ============ Serving Benchmark Result ============ Successful requests: 100 Benchmark duration (s): 493.30 Total input tokens: 105217 Total generated tokens: 25806 Average input length: 1052.17 Average output length: 258.06 Request throughput (req/s): 0.20 Input token throughput (tok/s): 213.29 Output token throughput (tok/s): 52.31 ---------------Time to First Token---------------- Mean TTFT (ms): 135.34 Median TTFT...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 8: TPOT (ms): 18.87 --------------------Latencies--------------------- Mean Latency (ms): 4932.52 Median Latency (ms): 5072.97 P99 Latency (ms): 7067.42 ======================================
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 6: del. Here is my config: base model: llama 3.3 70B instruct machine: 4 X H100 speculative method: ngram ngram-prompt-lookup-max: 5 num-speculative-tokens: 3 Here is command to start server: ``` python -m vllm.entrypoints...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 6: nce;stale ### Proposal to improve performance ### Report of performance regression _No response_ ### Misc discussion on performance I am testing ngram speculative decoding for llama 3.3 70B model. Here is my config: bas...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 5: c discussion on performance I am testing ngram speculative decoding for llama 3.3 70B model. Here is my config: base model: llama 3.3 70B instruct machine: 4 X H100 speculative method: ngram ngram-prompt-lookup-max: 5 n...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 4: /llama/Llama-3.3-70B-Instruct --tensor-parallel-size=4 --swap-space=16 --dtype=float16 --enable-chunked-prefill=True --gpu-memory-utilization=0.95 --speculative-model="[ngram]" --ngram-prompt-lookup-max=5 --num-speculat...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
