# vllm-project/vllm#3127: Benchmarking script does not limit the maximum concurrency

| 字段 | 值 |
| --- | --- |
| Issue | [#3127](https://github.com/vllm-project/vllm/issues/3127) |
| 状态 | closed |
| 标签 |  |
| 评论 | 4; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> Benchmarking script does not limit the maximum concurrency

### Issue 正文摘录

The current benchmarking script if specified with `INF` arrivals, will not limit the maximum concurrency level as shown [here](https://github.com/vllm-project/vllm/blob/703e42ee4b3efed3c71e7ae7d15f0f96e05722d4/benchmarks/benchmark_serving.py#L191). If we can change it to below, we can limit the maximum concurrency to have a fine controlled load level. ``` semaphore = asyncio.Semaphore(max_concurrency) # Semaphore to limit concurrency async def make_request(request, sem): async with sem: # Ensure only max_concurrency tasks run in parallel prompt, prompt_len, output_len = request request_func_input = RequestFuncInput( model=model_id, prompt=prompt, api_url=api_url, prompt_len=prompt_len, output_len=output_len, best_of=best_of, use_beam_search=use_beam_search, ) # Call the request function directly here and return its result return await request_func(request_func_input=request_func_input, pbar=pbar) tasks = [] for request in input_requests: # Direct iteration may replace async iteration based on design # Enqueue task without immediately awaiting it tasks.append(make_request(request, semaphore)) # Manage inter-arrival time if request_rate != float("inf"): await asyncio.sleep(1.0 / req...

## 候选优化模式

- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 3: e(max_concurrency) # Semaphore to limit concurrency async def make_request(request, sem): async with sem: # Ensure only max_concurrency tasks run in parallel prompt, prompt_len, output_len = request request_func_input =...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: not limit the maximum concurrency The current benchmarking script if specified with `INF` arrivals, will not limit the maximum concurrency level as shown [here](https://github.com/vllm-project/vllm/blob/703e42ee4b3efed3...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: =output_len, best_of=best_of, use_beam_search=use_beam_search, ) # Call the request function directly here and return its result return await request_func(request_func_input=request_func_input, pbar=pbar) tasks = []
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: quest request_func_input = RequestFuncInput( model=model_id, prompt=prompt, api_url=api_url, prompt_len=prompt_len, output_len=output_len, best_of=best_of, use_beam_sear
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: Benchmarking script does not limit the maximum concurrency The current benchmarking script if specified with `INF` arrivals, will not limit the maximum concurrency level as shown [here](https://github.com/vllm-project/vl

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
