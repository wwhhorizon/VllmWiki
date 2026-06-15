# vllm-project/vllm#21104: [Bug]: Benchmark script is not sending requests to serve with the given request rate

| 字段 | 值 |
| --- | --- |
| Issue | [#21104](https://github.com/vllm-project/vllm/issues/21104) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;quantization;sampling_logits;speculative_decoding |
| 子分类 | throughput |
| Operator 关键词 | cuda;operator;quantization;sampling;triton |
| 症状 | build_error;slowdown |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Benchmark script is not sending requests to serve with the given request rate

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug Benchmark script sends out requests slower than expected. Roughly 9% slower (183.52 actual QPS while target is set to 200) # Issue Details In the benchmark script, we're leveraging random generated intervals which follow gamma distributions to simulate poisson process with the given sample_rate. The random intervals define the time gap among request sends. However, in the current implementation, we do the sleep directly against the random intervals without considering actual elapsed time. This would introduce a small delay for each request and ultimately build up non-negligible gaps to affect server throughput readings. https://github.com/vllm-project/vllm/blob/fdc5b43d2017640a74f89c42ef61e1c79b4ffdd3/vllm/benchmarks/serve.py#L163-L165 By plotting the actual request sent time vs expected request sent time (with request-rate=200 and num-prompts=10000), we could see that there're delays for actual sent time, which results in smaller request sent rate and ultimately throughput readings. The impact is significant, we could see that request throughput is 183.52 when we have request-rate set to 200. The bottleneck is actually on benchm...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: time. This would introduce a small delay for each request and ultimately build up non-negligible gaps to affect server throughput readings. https://github.com/vllm-project/vllm/blob/fdc5b43d2017640a74f89c42ef61e1c79b4ff...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 3: --swap-space 16 \ --disable-log-requests \ --host :: \ --dtype float16 vllm bench serve \ --dataset-name random \ --model facebook/opt-125m \ --served-model-name facebook/opt-125m \ --random-input-len 700 \ --random-out...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: ntervals without considering actual elapsed time. This would introduce a small delay for each request and ultimately build up non-negligible gaps to affect server throughput readings. https://github.com/vllm-project/vll...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 3: [Bug]: Benchmark script is not sending requests to serve with the given request rate bug;stale ### Your current environment ### 🐛 Describe the bug Benchmark script sends out requests slower than expected. Roughly 9% slo...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 3: [Bug]: Benchmark script is not sending requests to serve with the given request rate bug;stale ### Your current environment ### 🐛 Describe the bug Benchmark script sends out requests slower than expected. Roughly 9% slo...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
