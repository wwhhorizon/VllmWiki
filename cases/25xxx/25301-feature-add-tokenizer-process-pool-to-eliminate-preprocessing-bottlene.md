# vllm-project/vllm#25301: [Feature]: Add tokenizer process pool to eliminate preprocessing bottleneck

| 字段 | 值 |
| --- | --- |
| Issue | [#25301](https://github.com/vllm-project/vllm/issues/25301) |
| 状态 | closed |
| 标签 | feature request;stale |
| 评论 | 13; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Feature]: Add tokenizer process pool to eliminate preprocessing bottleneck

### Issue 正文摘录

### 🚀 The feature, motivation and pitch When the server experiences high concurrency with multiple long requests, the preprocessing time (which includes tokenization) becomes a bottleneck. This leads to increased overall latency and poor TTFT performance, as requests are forced to wait in a serialized queue for preprocessing (tokenization), even though the XPU compute resources might be available. The current implementation in vllm uses a single thread to handle the request (in serving_engine.py). ``` self._tokenizer_executor = ThreadPoolExecutor(max_workers=1) ``` The cost of these operations scales linearly with the length of the input/output sequences. Under high load with long contexts, a queue of requests forms, each waiting for the previous one to finish its tokenization. A multiprocessing-based tokenizer process pool can be utilized to parallelize the encoding and decoding steps, thus breaking the serialization bottleneck. The minor overhead of inter-process communication (IPC) is negligible compared to the massive gains in parallelizing long tokenization tasks. ### Alternatives _No response_ ### Additional context _No response_ ### Before submitting a new issue... - [x] Ma...

## 候选优化模式

- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 4: Add tokenizer process pool to eliminate preprocessing bottleneck feature request;stale ### 🚀 The feature, motivation and pitch When the server experiences high concurrency with multiple long requests, the preprocessing...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 2: udes tokenization) becomes a bottleneck. This leads to increased overall latency and poor TTFT performance, as requests are forced to wait in a serialized queue for preprocessing (tokenization), even though the XPU comp...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 1: tor = ThreadPoolExecutor(max_workers=1) ``` The cost of these operations scales linearly with the length of the input/output sequences. Under high load with long contexts, a queue of requests forms, each waiting for the...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: se_ ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
