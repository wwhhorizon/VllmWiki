# vllm-project/vllm#5007: [Performance]: Vllm performance on L40s GPU

| 字段 | 值 |
| --- | --- |
| Issue | [#5007](https://github.com/vllm-project/vllm/issues/5007) |
| 状态 | closed |
| 标签 | performance |
| 评论 | 5; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | attention_kv_cache;distributed_parallel;frontend_api;model_support;quantization |
| 子分类 | throughput |
| Operator 关键词 | attention;cache;cuda;quantization;triton |
| 症状 | oom;slowdown |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Performance]: Vllm performance on L40s GPU

### Issue 正文摘录

### Proposal to improve performance _No response_ ### Report of performance regression Benchmark script performance: > root@13yper:/work/vllm_code/benchmarks#CUDA_VISIBLE_DEVICES=1 python3 benchmark_throughput.py --dataset ShareGPT_V3_unfiltered_cleaned_split.json --output-len 128 --model /work/llama-2-7b --gpu-memory-utilization 0.95 --device cuda > Namespace(backend='vllm', dataset='ShareGPT_V3_unfiltered_cleaned_split.json', input_len=None, output_len=128, model='/work/llama-2-7b', tokenizer='/work/llama-2-7b', quantization=None, tensor_parallel_size=1, n=1, use_beam_search=False, num_prompts=1000, seed=0, hf_max_batch_size=None, trust_remote_code=False, max_model_len=None, dtype='auto', gpu_memory_utilization=0.95, enforce_eager=False, kv_cache_dtype='auto', quantization_param_path=None, device='cuda', enable_prefix_caching=False, enable_chunked_prefill=False, max_num_batched_tokens=None, download_dir=None) > INFO 05-23 12:02:05 llm_engine.py:100] Initializing an LLM engine (v0.4.2) with config: model='/work/llama-2-7b', speculative_config=None, tokenizer='/work/llama-2-7b', skip_tokenizer_init=False, tokenizer_mode=auto, revision=None, tokenizer_revision=None, trust_remote_co...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 5: y --dataset ShareGPT_V3_unfiltered_cleaned_split.json --output-len 128 --model /work/llama-2-7b --gpu-memory-utilization 0.95 --device cuda > Namespace(backend='vllm', dataset='ShareGPT_V3_unfiltered_cleaned_split.json'...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 4: /work/llama-2-7b --gpu-memory-utilization 0.95 --device cuda > Namespace(backend='vllm', dataset='ShareGPT_V3_unfiltered_cleaned_split.json', input_len=None, output_len=128, model='/work/llama-2-7b', tokenizer='/work/ll...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 4: roposal to improve performance _No response_ ### Report of performance regression Benchmark script performance: > root@13yper:/work/vllm_code/benchmarks#CUDA_VISIBLE_DEVICES=1 python3 benchmark_throughput.py --dataset S...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 3: output_len=128, model='/work/llama-2-7b', tokenizer='/work/llama-2-7b', quantization=None, tensor_parallel_size=1, n=1, use_beam_search=False, num_prompts=1000, seed=0, hf_max_batch_size=None, trust_remote_code=False, m...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 3: am_path=None, device='cuda', enable_prefix_caching=False, enable_chunked_prefill=False, max_num_batched_tokens=None, download_dir=None) > INFO 05-23 12:02:05 llm_engine.py:100] Initializing an LLM engine (v0.4.2) with c...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
