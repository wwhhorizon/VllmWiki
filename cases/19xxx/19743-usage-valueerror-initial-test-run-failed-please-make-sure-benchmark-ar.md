# vllm-project/vllm#19743: [Usage]: ValueError: Initial test run failed - Please make sure benchmark arguments are correctly specified. Error: Gateway Time-out

| 字段 | 值 |
| --- | --- |
| Issue | [#19743](https://github.com/vllm-project/vllm/issues/19743) |
| 状态 | closed |
| 标签 | usage;stale |
| 评论 | 5; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Usage]: ValueError: Initial test run failed - Please make sure benchmark arguments are correctly specified. Error: Gateway Time-out

### Issue 正文摘录

### Your current environment VLLM VERSION：0.9.1 python3 /benchmark_serving.py --host 10.170.27.74 --port 8000 --save-result --save-detailed --backend openai --model /workspace/models/qwen2.5_7B_Instruct --endpoint /v1/completions --dataset-name custom --dataset-path /workspace/system-agent-prompt-1500.jsonl --custom-skip-chat-template --num-prompts 300 --max-concurrency 16 --result-dir "./log/" Namespace(backend='openai', base_url=None, host='10.170.27.74', port=8000, endpoint='/v1/completions', dataset_name='custom', dataset_path='/workspace/system-agent-prompt-1500.jsonl', max_concurrency=16, model='/workspace/models/qwen2.5_7B_Instruct', tokenizer=None, use_beam_search=False, num_prompts=300, logprobs=None, request_rate=inf, burstiness=1.0, seed=0, trust_remote_code=False, disable_tqdm=False, profile=False, save_result=True, save_detailed=True, append_result=False, metadata=None, result_dir='./log/', result_filename=None, ignore_eos=False, percentile_metrics='ttft,tpot,itl', metric_percentiles='99', goodput=None, custom_output_len=256, custom_skip_chat_template=True, sonnet_input_len=550, sonnet_output_len=150, sonnet_prefix_len=200, sharegpt_output_len=None, random_input_len=1...

## 候选优化模式

- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 4: [Usage]: ValueError: Initial test run failed - Please make sure benchmark arguments are correctly specified. Error: Gateway Time-out usage;stale ### Your current environment VLLM VERSION：0.9.1 python3 /benchmark_serving...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: test run failed - Please make sure benchmark arguments are correctly specified. Error: Gateway Time-out usage;stale ### Your current environment VLLM VERSION：0.9.1 python3 /benchmark_serving.py --host 10.170.27.74 --por...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: 0.27.74 --port 8000 --save-result --save-detailed --backend openai --model /workspace/models/qwen2.5_7B_Instruct --endpoint /v1/completions --dataset-name custom --dataset-path /workspace/system-agent-prompt-1500.jsonl...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 2: workspace/models/qwen2.5_7B_Instruct', tokenizer=None, use_beam_search=False, num_prompts=300, logprobs=None, request_rate=inf, burstiness=1.0, seed=0, trust_remote_code=False, disable_tqdm=False, profile=False, save_re...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: nchmark arguments are correctly specified. Error: Gateway Time-out usage;stale ### Your current environment VLLM VERSION：0.9.1 python3 /benchmark_serving.py --host 10.170.27.74 --port 8000 --save-result --save-detailed...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
