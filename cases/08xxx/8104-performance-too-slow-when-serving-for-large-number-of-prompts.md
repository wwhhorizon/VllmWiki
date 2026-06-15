# vllm-project/vllm#8104: [Performance]: Too slow when serving for large number of prompts.

| 字段 | 值 |
| --- | --- |
| Issue | [#8104](https://github.com/vllm-project/vllm/issues/8104) |
| 状态 | closed |
| 标签 | performance;stale |
| 评论 | 4; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | attention_kv_cache;ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cache;cuda;operator;sampling;triton |
| 症状 | build_error;nan_inf;slowdown |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Performance]: Too slow when serving for large number of prompts.

### Issue 正文摘录

### Proposal to improve performance _No response_ ``` ### Report of performance regression Namespace(backend='vllm', base_url=None, host='localhost', port=8000, endpoint='/v1/completions', dataset=None, dataset_name='sharegpt', dataset_path='./ShareGPT_V3_unfiltered_cleaned_split.json', model='meta-llama/Meta-Llama-3-8B-Instruct', tokenizer=None, best_of=1, use_beam_search=False, num_prompts=1000, sharegpt_output_len=2000, sonnet_input_len=550, sonnet_output_len=150, sonnet_prefix_len=200, random_input_len=1024, random_output_len=128, random_range_ratio=1.0, request_rate=inf, seed=0, trust_remote_code=False, disable_tqdm=False, profile=False, save_result=False, metadata=None, result_dir=None, result_filename=None) Starting initial single prompt test run... Initial test run completed. Starting main benchmark run... Traffic request rate: inf ============ Serving Benchmark Result ============ Successful requests: 1000 Benchmark duration (s): 12105.85 Total input tokens: 19495 Total generated tokens: 1376769 Request throughput (req/s): 0.08 Input token throughput (tok/s): 1.61 Output token throughput (tok/s): 113.73 ---------------Time to First Token---------------- Mean TTFT (ms): 51...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 8: the performance of vLLM in my own server. Noticed that it's too slow to compile the whole project. Any suggestions or documentations? ### Your current environment (if you think it is necessary) ```text The output of `py...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 7: osal to improve performance _No response_ ``` ### Report of performance regression Namespace(backend='vllm', base_url=None, host='localhost', port=8000, endpoint='/v1/completions', dataset=None, dataset_name='sharegpt',...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 6: a-llama/Meta-Llama-3-8B-Instruct', tokenizer=None, best_of=1, use_beam_search=False, num_prompts=1000, sharegpt_output_len=2000, sonnet_input_len=550, sonnet_output_len=150, sonnet_prefix_len=200, random_input_len=1024,...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 5: ormance]: Too slow when serving for large number of prompts. performance;stale ### Proposal to improve performance _No response_ ``` ### Report of performance regression Namespace(backend='vllm', base_url=None, host='lo...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: ='sharegpt', dataset_path='./ShareGPT_V3_unfiltered_cleaned_split.json', model='meta-llama/Meta-Llama-3-8B-Instruct', tokenizer=None, best_of=1, use_beam_search=False, num_prompts=1000, sharegpt_output_len=2000, sonnet_...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
