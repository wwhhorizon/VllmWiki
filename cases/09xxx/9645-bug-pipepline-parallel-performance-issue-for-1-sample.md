# vllm-project/vllm#9645: [Bug]: pipepline parallel performance issue for 1 sample.

| 字段 | 值 |
| --- | --- |
| Issue | [#9645](https://github.com/vllm-project/vllm/issues/9645) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: pipepline parallel performance issue for 1 sample.

### Issue 正文摘录

### Your current environment ### Model Input Dumps - ### 🐛 Describe the bug * model: Yi-9B * device: A100, for pipeline parallel, we use 2 x A100 * scripts: https://github.com/vllm-project/vllm/blob/main/examples/api_client.py * Serial request, time cost: 25s ```py response = post_http_request(prompt, api_url, n, stream) output = get_response(results) ``` * Parallel request, time cost: 6s ```py num_request = 16 with ThreadPoolExecutor(max_workers=num_request) as pool: futures = [pool.submit(post_http_request, (prompt, api_url)) for _ in range(num_request)] results = [future.result() for future in futures] import ipdb; ipdb.set_trace() results = [get_response(r) for r in results] print(f"time cost: {time.time() - begin}") ``` ### Before submitting a new issue... - [X] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: # Model Input Dumps - ### 🐛 Describe the bug * model: Yi-9B * device: A100, for pipeline parallel, we use 2 x A100 * scripts: https://github.com/vllm-project/vllm/blob/main/examples/api_client.py * Serial request, time...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: [Bug]: pipepline parallel performance issue for 1 sample. bug;stale ### Your current environment ### Model Input Dumps - ### 🐛 Describe the bug * model: Yi-9B * device: A100, for pipeline parallel, we use 2 x A100 * scr...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: _request)] results = [future.result() for future in futures] import ipdb; ipdb.set_trace() results = [get_response(r) for r in results] print(f"time cost: {time.time() - begin}") ``` ### Before submitting a new issue......
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: mance issue for 1 sample. bug;stale ### Your current environment ### Model Input Dumps - ### 🐛 Describe the bug * model: Yi-9B * device: A100, for pipeline parallel, we use 2 x A100 * scripts: https://github.com/vllm-pr...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
