# vllm-project/vllm#9032: [Performance]: Transformers 4.45.1 slows down `outlines` guided decoding

| 字段 | 值 |
| --- | --- |
| Issue | [#9032](https://github.com/vllm-project/vllm/issues/9032) |
| 状态 | closed |
| 标签 | performance;structured-output;stale |
| 评论 | 7; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Performance]: Transformers 4.45.1 slows down `outlines` guided decoding

### Issue 正文摘录

### Report of performance regression I noticed that guided decoding was a bit slower on newer builds of vllm, but couldn't track down a commit that caused a performance regression. Instead it looks like upgrading transformers from `4.44.2` to `4.45.1` causes the issue. I ran a small artillery test with requests using guided decoding, using the code from commit `4f1ba0844`. This is the last commit before `mllama` support was added, so it's the last point where vllm will work with both transformers versions `4.44.2` and `4.45.1`. VLLM was run with 1xA100 gpu, using model `mistralai/Mistral-7B-Instruct-v0.2` The results with `4.44.2` installed: ``` http.codes.200: ................................................................ 240 http.downloaded_bytes: ......................................................... 91928 http.request_rate: ............................................................. 3/sec http.requests: ................................................................. 240 http.response_time: min: ......................................................................... 105 max: ......................................................................... 16348 mean: ..........

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: nce regression I noticed that guided decoding was a bit slower on newer builds of vllm, but couldn't track down a commit that caused a performance regression. Instead it looks like upgrading transformers from `4.44.2` t...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: rading transformers from `4.44.2` to `4.45.1` causes the issue. I ran a small artillery test with requests using guided decoding, using the code from commit `4f1ba0844`. This is the last commit before `mllama` support w...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 3: d decoding performance;structured-output;stale ### Report of performance regression I noticed that guided decoding was a bit slower on newer builds of vllm, but couldn't track down a commit that caused a performance reg...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: using the code from commit `4f1ba0844`. This is the last commit before `mllama` support was added, so it's the last point where vllm will work with both transformers versions `4.44.2` and `4.45.1`. VLLM was run with 1xA...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: 45.1 slows down `outlines` guided decoding performance;structured-output;stale ### Report of performance regression I noticed that guided decoding was a bit slower on newer builds of vllm, but couldn't track down a comm...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
