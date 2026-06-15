# vllm-project/vllm#2940: Benchmarking script for openai chat completion api are not supported

| 字段 | 值 |
| --- | --- |
| Issue | [#2940](https://github.com/vllm-project/vllm/issues/2940) |
| 状态 | closed |
| 标签 |  |
| 评论 | 0; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> Benchmarking script for openai chat completion api are not supported

### Issue 正文摘录

When running vllm with openai chat apis, the benchmarking script will fail as it asserts the backend API of `assert api_url.endswith("v1/completions")`. ``` python benchmark_serving.py --backend openai --model mistralai/Mistral-7B-v0.1 --dataset ShareGPT_V3_unfiltered_cleaned_split.json --save-result ``` The logs are as follows: ``` Namespace(backend='openai', version='N/A', base_url=None, host='localhost', port=8000, endpoint='/generate', dataset='ShareGPT_V3_unfiltered_cleaned_split.json', model='mistralai/Mistral-7B-v0.1', tokenizer=None, best_of=1, use_beam_search=False, num_prompts=1000, request_rate=inf, seed=0, trust_remote_code=False, disable_tqdm=False, save_result=True) 0%| | 0/1000 [00:00 main(args) File "/home/chenw/vllm/benchmarks/benchmark_serving.py", line 259, in main benchmark_result = asyncio.run( File "/home/chenw/miniconda3/envs/myenv/lib/python3.9/asyncio/runners.py", line 44, in run return loop.run_until_complete(main) File "/home/chenw/miniconda3/envs/myenv/lib/python3.9/asyncio/base_events.py", line 647, in run_until_complete return future.result() File "/home/chenw/vllm/benchmarks/benchmark_serving.py", line 195, in benchmark outputs = await asyncio.gather...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: ave-result ``` The logs are as follows: ``` Namespace(backend='openai', version='N/A', base_url=None, host='localhost', port=8000, endpoint='/generate', dataset='ShareGPT_V3_unfiltered_cleaned_split.json', model='mistra...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: th openai chat apis, the benchmarking script will fail as it asserts the backend API of `assert api_url.endswith("v1/completions")`. ``` python benchmark_serving.py --backend openai --model mistralai/Mistral-7B-v0.1 --d...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: model='mistralai/Mistral-7B-v0.1', tokenizer=None, best_of=1, use_beam_search=False, num_prompts=1000, request_rate=inf, seed=0, trust_remote_code=False, disable_tqdm=False, save_result=True) 0%| | 0/1000 [00:00 main(ar...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 1: mistralai/Mistral-7B-v0.1', tokenizer=None, best_of=1, use_beam_search=False, num_prompts=1000, request_rate=inf, seed=0, trust_remote_code=False, disable_tqdm=False, save_result=True) 0%| | 0/1000 [00:00 main(args) Fil...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: ("v1/completions")`. ``` python benchmark_serving.py --backend openai --model mistralai/Mistral-7B-v0.1 --dataset ShareGPT_V3_unfiltered_cleaned_split.json --save-result ``` The logs are as follows: ``` Namespace(backen...

## Wiki 抽取状态

- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
