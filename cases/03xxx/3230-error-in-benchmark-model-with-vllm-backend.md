# vllm-project/vllm#3230: Error in benchmark model with vllm backend

| 字段 | 值 |
| --- | --- |
| Issue | [#3230](https://github.com/vllm-project/vllm/issues/3230) |
| 状态 | closed |
| 标签 | stale |
| 评论 | 14; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> Error in benchmark model with vllm backend

### Issue 正文摘录

I couldn't benchmark my model, seems the benchmark send requests without wait for the response, so the following error is raised: ``` python benchmark_serving.py \ --backend vllm \ --model "MYMODEL/PATH" \ --port 8000 --host 0.0.0.0 \ --dataset ShareGPT_V3_unfiltered_cleaned_split.json \ --num-prompts 400 \ --endpoint /generate \ --save-result ``` I also run the service and I can access it thought http://0.0.0.0:8000 but I got this error: ``` Namespace(backend='vllm', version='N/A', base_url=None, host='0.0.0.0', port=8000, endpoint='/generate', dataset='ShareGPT_V3_unfiltered_cleaned_split.json', model='MYMODEL/PATH', tokenizer=None, best_of=1, use_beam_search=False, num_prompts=400, request_rate=inf, seed=0, trust_remote_code=False, disable_tqdm=False, save_result=True) Token indices sequence length is longer than the specified maximum sequence length for this model (515 > 255). Running this sequence through the model will result in indexing errors 0%| | 0/400 [00:00 main(args) File "~/benchmark/benchmark_serving.py", line 261, in main benchmark_result = asyncio.run( File "myconda/lib/python3.9/asyncio/runners.py", line 44, in run return loop.run_until_complete(main) File "mycon...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: ttp://0.0.0.0:8000 but I got this error: ``` Namespace(backend='vllm', version='N/A', base_url=None, host='0.0.0.0', port=8000, endpoint='/generate', dataset='ShareGPT_V3_unfiltered_cleaned_split.json', model='MYMODEL/P...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: Error in benchmark model with vllm backend stale I couldn't benchmark my model, seems the benchmark send requests without wait for the response, so the following error is raised: ``` python benchmark_serving.py \ --back...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: Error in benchmark model with vllm backend stale I couldn't benchmark my model, seems the benchmark send requests without wait for the response, so the following error is raised: ``` python benchmark_serving.py \ --back...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 1: ckages/numpy/lib/function_base.py", line 4283, in percentile return _quantile_unchecked( File "myconda/lib/python3.9/site-packages/numpy/lib/function_base.py", line 4555, in _quantile_unchecked return _ureduce(a, File "...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: split.json', model='MYMODEL/PATH', tokenizer=None, best_of=1, use_beam_search=False, num_prompts=400, request_rate=inf, seed=0, trust_remote_code=False, disable_tqdm=False, save_result=True) Token indices sequence lengt...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
