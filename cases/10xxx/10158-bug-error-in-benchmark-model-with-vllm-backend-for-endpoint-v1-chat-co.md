# vllm-project/vllm#10158: [Bug]: Error in benchmark model with vllm backend for endpoint /v1/chat/completions

| 字段 | 值 |
| --- | --- |
| Issue | [#10158](https://github.com/vllm-project/vllm/issues/10158) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 23; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: Error in benchmark model with vllm backend for endpoint /v1/chat/completions

### Issue 正文摘录

### Your current environment ### Model Input Dumps _No response_ ### 🐛 Describe the bug vllm benchmark script is falling for endpoint v1/chat/completions Namespace(**backend='vllm'**, base_url=None, host='10.244.2.102', port=8000, endpoint='**/v1/chat/completions**', dataset=None, **dataset_name='sharegpt', dataset_path='ShareGPT_V3_unfiltered_cleaned_split.json',** max_concurrency=None, model='Meta-Llama-3.1-70b-instruct', tokenizer='/mnt/models/meta-llama-3-1-70b-instruct/', best_of=1, use_beam_search=False, num_prompts=1000, logprobs=None, request_rate=3.0, burstiness=1.0, seed=0, trust_remote_code=False, disable_tqdm=True, profile=False, save_result=True, metadata=None, result_dir='result/Meta-Llama-3.1-70b-instruct/RR-3-TP-2-PP-1/IL-10', result_filename=None, ignore_eos=False, percentile_metrics='ttft,tpot,itl', metric_percentiles='99', goodput=None, sonnet_input_len=550, sonnet_output_len=150, sonnet_prefix_len=200, sharegpt_output_len=None, random_input_len=10, random_output_len=512, random_range_ratio=1.0, random_prefix_len=0, hf_subset=None, hf_split=None, hf_output_len=None) ERROR Starting initial single prompt test run... Traceback (most recent call last): File "/benchm...

## 候选优化模式

- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 4: [Bug]: Error in benchmark model with vllm backend for endpoint /v1/chat/completions bug;stale ### Your current environment ### Model Input Dumps _No response_ ### 🐛 Describe the bug vllm benchmark script is falling for...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: [Bug]: Error in benchmark model with vllm backend for endpoint /v1/chat/completions bug;stale ### Your current environment ### Model Input Dumps _No response_ ### 🐛 Describe the bug vllm benchmark script is falling for...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 2: '/mnt/models/meta-llama-3-1-70b-instruct/', best_of=1, use_beam_search=False, num_prompts=1000, logprobs=None, request_rate=3.0, burstiness=1.0, seed=0, trust_remote_code=False, disable_tqdm=True, profile=False, save_re...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: benchmark model with vllm backend for endpoint /v1/chat/completions bug;stale ### Your current environment ### Model Input Dumps _No response_ ### 🐛 Describe the bug vllm benchmark script is falling for endpoint v1/chat...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: [Bug]: Error in benchmark model with vllm backend for endpoint /v1/chat/completions bug;stale ### Your current environment ### Model Input Dumps _No response_ ### 🐛 Describe the bug vllm benchmark script is falling for...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
