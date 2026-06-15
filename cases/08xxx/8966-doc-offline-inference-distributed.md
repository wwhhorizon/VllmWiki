# vllm-project/vllm#8966: [Doc]: Offline Inference Distributed

| 字段 | 值 |
| --- | --- |
| Issue | [#8966](https://github.com/vllm-project/vllm/issues/8966) |
| 状态 | closed |
| 标签 | documentation;ray;stale |
| 评论 | 6; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Doc]: Offline Inference Distributed

### Issue 正文摘录

### 📚 The doc issue Hi, I was just wondering why in the "Offline Inference Distributed" example, `ds.map_batches()` is used. I used this initially, but I am now splitting the dataset and using `ray.remote()` which has the advantage that I don't need to specify the batch_size and can use continuous batching per GPU. ### Suggest a potential alternative/fix If useful I could contribute with an example in the docs with ray.remote(), so both methods are available ### Before submitting a new issue... - [X] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: and using `ray.remote()` which has the advantage that I don't need to specify the batch_size and can use continuous batching per GPU. ### Suggest a potential alternative/fix If useful I could contribute with an example...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: ble ### Before submitting a new issue... - [X] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: [Doc]: Offline Inference Distributed documentation;ray;stale ### 📚 The doc issue Hi, I was just wondering why in the "Offline Inference Distributed" example, `ds.map_batches()` is used. I used this initially, but I am n...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
