# vllm-project/vllm#16258: [Usage]: The performance of ngram speculative decoding

| 字段 | 值 |
| --- | --- |
| Issue | [#16258](https://github.com/vllm-project/vllm/issues/16258) |
| 状态 | closed |
| 标签 | usage |
| 评论 | 11; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | attention_kv_cache;ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;quantization;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cache;cuda;operator;quantization;sampling;triton |
| 症状 | build_error;nan_inf;nondeterministic;slowdown |
| 根因提示 | dtype;env_dependency;race_condition;shape |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Usage]: The performance of ngram speculative decoding

### Issue 正文摘录

### Your current environment ### How would you like to use vllm Hi For the past day or so, I have been testing the performance gains of the n-gram model for speculation. I was benchmarking standard models such as `opt-125m` or `starcoder2-3b`. My use case is the standard code generation problem. I have seen that regardless of the configuration, the inference of the sample model n-gram model is Pareto worse than the inference without the n-gram model, pretty much regardless of the contents of the `speculative_config`. ## My initial benchmarks ### Setup ```bash model = "opt-125m" tokenizer = "opt-125m" engine_args = {gpu_memory_utilization = 0.90, tensor_parallel_size = 1} sampling_params = {n = 1, temperature = 0.0, top_k = 1, logprobs = 1, spaces_between_special_tokens = false, max_tokens = 1024} ``` ### Speculative Decoding When running my benchmarks with: `speculative_config = {speculative_model = "[ngram]", num_speculative_tokens = 5, ngram_prompt_lookup_max = 2}` I see in the logs: ```bash ... INFO 04-08 10:43:07 metrics.py:455] Avg prompt throughput: 33127.2 tokens/s, Avg generation throughput: 238.0 tokens/s, Running: 4 reqs, Swapped: 0 reqs, Pending: 0 reqs, GPU KV cache us...

## 候选优化模式

- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 6: ining the text in the dataset" ) parser.add_argument( "--dtype", type=str, default="float16", choices=["float16", "bfloat16", "float32", "int8", "int4"], help="Data type for model weights" ) parser.add_argument( "--with...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: = {n = 1, temperature = 0.0, top_k = 1, logprobs = 1, spaces_between_special_tokens = false, max_tokens = 1024} ``` ### Speculative Decoding When running my benchmarks with: `speculative_config = {speculative_model = "[...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 4: How would you like to use vllm Hi For the past day or so, I have been testing the performance gains of the n-gram model for speculation. I was benchmarking standard models such as `opt-125m` or `starcoder2-3b`. My use c...
- [Bitwise 确定性与数值等价](../patterns/bitwise_determinism_equivalence.md) - 分数 3: ly for low values of `num_speculative_tokens`. So I wrote simple code to reproduce the problem. ## Simple code to reproduce ```python import argparse import time from typing import List, Dict, Any, Optional import json...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: past day or so, I have been testing the performance gains of the n-gram model for speculation. I was benchmarking standard models such as `opt-125m` or `starcoder2-3b`. My use case is the standard code generation proble...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
