# vllm-project/vllm#2993: vLLM benchmarking script do not support the openAI compatible API server.

| 字段 | 值 |
| --- | --- |
| Issue | [#2993](https://github.com/vllm-project/vllm/issues/2993) |
| 状态 | closed |
| 标签 |  |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> vLLM benchmarking script do not support the openAI compatible API server.

### Issue 正文摘录

The benchmarking script to run is below: ``` python benchmark_serving.py --backend vllm --endpoint /v1/completions --num-prompts 1 --model mistralai/Mistral-7B-v0.1 --dataset ShareGPT_V3_unfiltered_cleaned_split.json ``` The assert only allows `/generate` endpoint for vllm backend. ``` Namespace(backend='vllm', version='N/A', base_url=None, host='localhost', port=8000, endpoint='/v1/completions', dataset='ShareGPT_V3_unfiltered_cleaned_split.json', model='mistralai/Mistral-7B-v0.1', tokenizer=None, best_of=1, use_beam_search=False, num_prompts=1, request_rate=inf, seed=0, trust_remote_code=False, disable_tqdm=False, save_result=False) 0%| | 0/1 [00:00 main(args) File "/home/chenw/wangchen615/vllm/benchmarks/benchmark_serving.py", line 259, in main benchmark_result = asyncio.run( File "/home/chenw/miniconda3/envs/myenv/lib/python3.9/asyncio/runners.py", line 44, in run return loop.run_until_complete(main) File "/home/chenw/miniconda3/envs/myenv/lib/python3.9/asyncio/base_events.py", line 647, in run_until_complete return future.result() File "/home/chenw/wangchen615/vllm/benchmarks/benchmark_serving.py", line 195, in benchmark outputs = await asyncio.gather(*tasks) File "/home/chen...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: ows `/generate` endpoint for vllm backend. ``` Namespace(backend='vllm', version='N/A', base_url=None, host='localhost', port=8000, endpoint='/v1/completions', dataset='ShareGPT_V3_unfiltered_cleaned_split.json', model=...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: e benchmarking script to run is below: ``` python benchmark_serving.py --backend vllm --endpoint /v1/completions --num-prompts 1 --model mistralai/Mistral-7B-v0.1 --dataset ShareGPT_V3_unfiltered_cleaned_split.json ```...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: model='mistralai/Mistral-7B-v0.1', tokenizer=None, best_of=1, use_beam_search=False, num_prompts=1, request_rate=inf, seed=0, trust_remote_code=False, disable_tqdm=False, save_result=False) 0%| | 0/1 [00:00 main(args
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 1: mistralai/Mistral-7B-v0.1', tokenizer=None, best_of=1, use_beam_search=False, num_prompts=1, request_rate=inf, seed=0, trust_remote_code=False, disable_tqdm=False, save_result=False) 0%| | 0/1 [00:00 main(args) Fil
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: k_serving.py --backend vllm --endpoint /v1/completions --num-prompts 1 --model mistralai/Mistral-7B-v0.1 --dataset ShareGPT_V3_unfiltered_cleaned_split.json ``` The assert only allows `/generate` endpoint for vllm backe...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
