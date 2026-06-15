# vllm-project/vllm#27063: [Feature]: Improvements to front-end embedding response

| 字段 | 值 |
| --- | --- |
| Issue | [#27063](https://github.com/vllm-project/vllm/issues/27063) |
| 状态 | closed |
| 标签 | feature request |
| 评论 | 17; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Feature]: Improvements to front-end embedding response

### Issue 正文摘录

### 🚀 The feature, motivation and pitch I will describe here in more detail what was said [here](https://github.com/vllm-project/vllm/pull/26414#issuecomment-3396192879). We use the OpenAI interface from vLLM in our ETL service, our main task is batch generation and vector matching. When processing large batch responses, we notice the collector overhead and the resource consumption of receiving uncompressed JSON text, which contains a vector of values ​​in Base64 strings. This results in significant memory usage and garbage collection, and also puts a strain on the network. I'd like to suggest several improvements. 1. Response compression if the client sends the 'accept-encoding' header: 'zstd, gzip' 2. This is quite radical, but would be very effective. Add a new request parameter, for example, `is_binary_response`. If true, return the response not as JSON, but simply as a binary tuple. We always know the tuple length when making a request, so it will be very easy to parse a binary response with this structure: `Index: UInt16, tokens: UInt32, vector: FixedList` 3. This is a small thing, but still, endian, our ETL service often doesn't work with the vector, it just saves it to ano...

## 候选优化模式

- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: ucture: `Index: UInt16, tokens: UInt32, vector: FixedList` 3. This is a small thing, but still, endian, our ETL service often doesn't work with the vector, it just saves it to another database, for example, in Postgres,...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: [Feature]: Improvements to front-end embedding response feature request ### 🚀 The feature, motivation and pitch I will describe here in more detail what was said [here](https://github.com/vllm-project/vllm/pull/26414#is...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
