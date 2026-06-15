# vllm-project/vllm#21094: [Enhancement]:  add concurrency in benchmark result table

| 字段 | 值 |
| --- | --- |
| Issue | [#21094](https://github.com/vllm-project/vllm/issues/21094) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Enhancement]:  add concurrency in benchmark result table

### Issue 正文摘录

### Your current environment vLLM v0.9.2rc2 ### 🐛 Describe the bug when using `vllm/benchmarks/benchmark_serving.py` the `--max-concurrency X` only shows in normal stdout logging and saving result json, but is missing in **formatted result table** (`============ Serving Benchmark Result ============ `) the concurrency is important factor impact the performance result , sometimes even than `Successful requests`. So I think it's necessary to put this info into formatted result table output. current output table: ```Namespace(backend='openai-chat', base_url='https://api.groq.com/openai', host='127.0.0.1', port=8000, endpoint='/v1/chat/completions', dataset_name='sharegpt', dataset_path='/mnt/models/ShareGPT_Vicuna_unfiltered/ShareGPT_V3_unfiltered_cleaned_split.json', max_concurrency=3, model='moonshotai/Kimi-K2-Instruct', tokenizer=None, use_beam_search=False, num_prompts=10, logprobs=None, request_rate=inf, burstiness=1.0, seed=0, trust_remote_code=True, disable_tqdm=False, profile=False, save_result=True, save_detailed=True, append_result=False, metadata=None, result_dir=None, result_filename=None, ignore_eos=False, percentile_metrics='ttft,tpot,itl', metric_percentiles='99', good...

## 候选优化模式

- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 6: [Enhancement]: add concurrency in benchmark result table bug ### Your current environment vLLM v0.9.2rc2 ### 🐛 Describe the bug when using `vllm/benchmarks/benchmark_serving.py` the `--max-concurrency X` only shows in n...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: s in normal stdout logging and saving result json, but is missing in **formatted result table** (`============ Serving Benchmark Result ============ `) the concurrency is important factor impact the performance result ,...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 2: , model='moonshotai/Kimi-K2-Instruct', tokenizer=None, use_beam_search=False, num_prompts=10, logprobs=None, request_rate=inf, burstiness=1.0, seed=0, trust_remote_code=True, disable_tqdm=False, profile=False, save_resu...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: nto formatted result table output. current output table: ```Namespace(backend='openai-chat', base_url='https://api.groq.com/openai', host='127.0.0.1', port=8000, endpoint='/v1/chat/completions', dataset_name='sharegpt',...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: =========== Serving Benchmark Result ============ `) the concurrency is important factor impact the performance result , sometimes even than `Successful requests`. So I think it's necessary to put this info into formatt...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
