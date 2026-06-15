# vllm-project/vllm#16821: [Bug]: benchmark with mii backend occurs Error

| 字段 | 值 |
| --- | --- |
| Issue | [#16821](https://github.com/vllm-project/vllm/issues/16821) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 0; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cuda;kernel;operator;sampling;triton |
| 症状 | build_error;crash;nan_inf |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: benchmark with mii backend occurs Error

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug server environment: deepspeed 0.16.3 deepspeed-kernels 0.0.1.dev1698255861 deepspeed-mii 0.3.1+fcd0a5b server command: `$ python -m mii.entrypoints.openai_api_server --tensor-parallel 1 --model meta-llama/Meta-Llama-3-8B --port 8000` client command: `$ python vllm/benchmarks/benchmark_serving.py --dataset-name sharegpt --dataset-path ./ShareGPT_V3_unfiltered_cleaned_split.json --model meta-llama/Meta-Llama-3-8B --num_prompts 500 --request-rate 4 --port 8000 --backend deepspeed-mii` error log: > INFO 04-18 06:30:36 [__init__.py:239] Automatically detected platform cuda. > Namespace(backend='deepspeed-mii', base_url=None, host='127.0.0.1', port=8000, endpoint='/v1/completions', dataset_name='sharegpt', dataset_path='./ShareGPT_V3_unfiltered_cleaned_split.json', max_concurrency=None, model='meta-llama/Meta-Llama-3-8B', tokenizer=None, use_beam_search=False, num_prompts=500, logprobs=None, request_rate=4.0, burstiness=1.0, seed=0, trust_remote_code=False, disable_tqdm=False, profile=False, save_result=False, save_detailed=False, metadata=None, result_dir=None, result_filename=None, ignore_eos=False, percentile_metrics='ttft,tpot,itl'...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: ks/benchmark_serving.py", line 684, in main > benchmark_result = asyncio.run( > ^^^^^^^^^^^^ > File "/home/ishi/.pyenv/versions/3.12.7/lib/python3.12/asyncio/runners.py", line 194, in run > return runner.run(main) > ^^^...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 4: [Bug]: benchmark with mii backend occurs Error bug ### Your current environment ### 🐛 Describe the bug server environment: deepspeed 0.16.3 deepspeed-kernels 0.0.1.dev1698255861 deepspeed-mii
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: nd: `$ python -m mii.entrypoints.openai_api_server --tensor-parallel 1 --model meta-llama/Meta-Llama-3-8B --port 8000` client command: `$ python vllm/benchmarks/benchmark_serving.py --dataset-name sharegpt --dataset-pat...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 2: [Bug]: benchmark with mii backend occurs Error bug ### Your current environment ### 🐛 Describe the bug server environment: deepspeed 0.16.3 deepspeed-kernels 0.0.1.dev1698255861 deepspeed-mii 0.3.1+fcd0
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: > INFO 04-18 06:30:36 [__init__.py:239] Automatically detected platform cuda. > Namespace(backend='deepspeed-mii', base_url=None, host='127.0.0.1', port=8000, endpoint='/v1/completions', dataset_name='sharegpt', dataset...

## Wiki 抽取状态

- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
