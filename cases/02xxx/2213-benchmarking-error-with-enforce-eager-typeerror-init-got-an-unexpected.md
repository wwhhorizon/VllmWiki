# vllm-project/vllm#2213: Benchmarking Error with enforce_eager: TypeError: __init__() got an unexpected keyword argument 'enforce_eager'

| 字段 | 值 |
| --- | --- |
| Issue | [#2213](https://github.com/vllm-project/vllm/issues/2213) |
| 状态 | closed |
| 标签 |  |
| 评论 | 5; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> Benchmarking Error with enforce_eager: TypeError: __init__() got an unexpected keyword argument 'enforce_eager'

### Issue 正文摘录

I am trying to benchmark the throughput of my model using the ShareGPT dataset. ```shell python benchmarks/benchmark_throughput.py --model $MODEL --dataset ShareGPT_V3_unfiltered_cleaned_split.json ``` However with the latest version I get the following error: ```shell Namespace(backend='vllm', dataset='ShareGPT_V3_unfiltered_cleaned_split.json', dtype='auto', enforce_eager=False, hf_max_batch_size=None, input_len=None, max_model_len=None, model='/oda/llm/c2kreader/converted_1260_fp16_hf', n=1, num_prompts=1000, output_len=None, quantization=None, seed=0, tensor_parallel_size=1, tokenizer='/oda/llm/c2kreader/converted_1260_fp16_hf', trust_remote_code=False, use_beam_search=False) Traceback (most recent call last): File "benchmark_throughput.py", line 318, in main(args) File "benchmark_throughput.py", line 205, in main elapsed_time = run_vllm(requests, args.model, args.tokenizer, File "benchmark_throughput.py", line 76, in run_vllm llm = LLM( File "/usr/.venv/lib64/python3.8/site-packages/vllm/entrypoints/llm.py", line 78, in __init__ engine_args = EngineArgs( TypeError: __init__() got an unexpected keyword argument 'enforce_eager' ``` I didn't get this error with previous versions

## 候选优化模式

- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 3: Benchmarking Error with enforce_eager: TypeError: __init__() got an unexpected keyword argument 'enforce_eager' I am trying to benchmark the throughput of my model using the ShareGPT dataset. ```shell python benchmarks/
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 2: ace(backend='vllm', dataset='ShareGPT_V3_unfiltered_cleaned_split.json', dtype='auto', enforce_eager=False, hf_max_batch_size=None, input_len=None, max_model_len=None, model='/oda/llm/c2kreader/converted_1260_fp16_hf',...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: d argument 'enforce_eager' I am trying to benchmark the throughput of my model using the ShareGPT dataset. ```shell python benchmarks/benchmark_throughput.py --model $MODEL --dataset ShareGPT_V3_unfiltered_cleaned_split...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: r with the latest version I get the following error: ```shell Namespace(backend='vllm', dataset='ShareGPT_V3_unfiltered_cleaned_split.json', dtype='auto', enforce_eager=False, hf_max_batch_size=None, input_len=None, max...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: t ShareGPT_V3_unfiltered_cleaned_split.json ``` However with the latest version I get the following error: ```shell Namespace(backend='vllm', dataset='ShareGPT_V3_unfiltered_cleaned_split.json', dtype='auto', enforce_ea...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
