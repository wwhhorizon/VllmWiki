# vllm-project/vllm#9561: [Bug]: benchmark serving does not support --best_of>1

| 字段 | 值 |
| --- | --- |
| Issue | [#9561](https://github.com/vllm-project/vllm/issues/9561) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cuda;operator;sampling;triton |
| 症状 | build_error;crash;nan_inf |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: benchmark serving does not support --best_of>1

### Issue 正文摘录

### Your current environment ### Model Input Dumps _No response_ ### 🐛 Describe the bug I ran the following command to launch the server: ``` vllm serve /data/llm/Meta-Llama-3.1-8B-Instruct --swap-space 16 --disable-log-requests ``` Then I ran the benchmark serving test, but I found it failed when the --best_of option was set to a value >1. --best_of 1 is ok: ```text -> % python benchmark_serving.py --model /data/llm/Meta-Llama-3.1-8B-Instruct --dataset-name random --best_of 1 Namespace(backend='vllm', base_url=None, host='localhost', port=8000, endpoint='/v1/completions', dataset=None, dataset_name='random', dataset_path=None, max_concurrency=None, model='/data/llm/Meta-Llama-3.1-8B-Instruct', tokenizer=None, best_of=1, use_beam_search=False, num_prompts=1000, logprobs=None, request_rate=inf, seed=0, trust_remote_code=False, disable_tqdm=False, profile=False, save_result=False, metadata=None, result_dir=None, result_filename=None, ignore_eos=False, percentile_metrics='ttft,tpot,itl', metric_percentiles='99', goodput=None, sonnet_input_len=550, sonnet_output_len=150, sonnet_prefix_len=200, sharegpt_output_len=None, random_input_len=1024, random_output_len=128, random_range_ratio=1...

## 候选优化模式

- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 4: [Bug]: benchmark serving does not support --best_of>1 bug ### Your current environment ### Model Input Dumps _No response_ ### 🐛 Describe the bug I ran the following command to launch the server: ``` vllm serve /data/l
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: arks/benchmark_serving.py", line 761, in main benchmark_result = asyncio.run( File "/opt/miniconda3/envs/vllm-fjy/lib/python3.10/asyncio/runners.py", line 44, in run return loop.run_until_complete(main) File "/opt/minic...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: ng does not support --best_of>1 bug ### Your current environment ### Model Input Dumps _No response_ ### 🐛 Describe the bug I ran the following command to launch the server: ``` vllm serve /data/llm/Meta-Llama-3.1-8B-In...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 2: m/Meta-Llama-3.1-8B-Instruct --dataset-name random --best_of 1 Namespace(backend='vllm', base_url=None, host='localhost', port=8000, endpoint='/v1/completions', dataset=None, dataset_name='random', dataset_path=None, ma...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: a/llm/Meta-Llama-3.1-8B-Instruct', tokenizer=None, best_of=1, use_beam_search=False, num_prompts=1000, logprobs=None, request_rate=inf, seed=0, trust_remote_code=False, disable_tqdm=False, profile=False, save_result=Fal...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
