# vllm-project/vllm#13467: [Usage]: How different between 'obtain the full response' and 'fixed length output' when using benchmark performance test

| 字段 | 值 |
| --- | --- |
| Issue | [#13467](https://github.com/vllm-project/vllm/issues/13467) |
| 状态 | closed |
| 标签 | usage;stale |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Usage]: How different between 'obtain the full response' and 'fixed length output' when using benchmark performance test

### Issue 正文摘录

### Your current environment I noticed that the official way of using the benchmark to call the chat API doesn't involve continuous concurrency and doesn't obtain the full response. However, I use Locust to continuously and concurrently call the chat API and obtain the full output. 1、When these two methods are used to evaluate the performance of the model and the accelerator card, what are the differences? 2、The benchmark script also provides a test method with fixed - length input and output. What are the differences in calculating the token output rate between this method and the test method of asking random questions and obtaining a full response? ### How would you like to use vllm I want to run inference of a [specific model](put link here). I don't know how to integrate it with vllm. ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 3: between 'obtain the full response' and 'fixed length output' when using benchmark performance test usage;stale ### Your current environment I noticed that the official way of using the benchmark to call the chat API doe...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: ce test usage;stale ### Your current environment I noticed that the official way of using the benchmark to call the chat API doesn't involve continuous concurrency and doesn't obtain the full response. However, I use Lo...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: lm. ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: t. 1、When these two methods are used to evaluate the performance of the model and the accelerator card, what are the differences? 2、The benchmark script also provides a test method with fixed - length input and output....
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: e' and 'fixed length output' when using benchmark performance test usage;stale ### Your current environment I noticed that the official way of using the benchmark to call the chat API doesn't involve continuous concurre...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
