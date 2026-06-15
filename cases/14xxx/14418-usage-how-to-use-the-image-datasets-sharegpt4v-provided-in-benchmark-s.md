# vllm-project/vllm#14418: [Usage]: How to use the image datasets sharegpt4v provided in benchmark_serving?

| 字段 | 值 |
| --- | --- |
| Issue | [#14418](https://github.com/vllm-project/vllm/issues/14418) |
| 状态 | closed |
| 标签 | usage;stale |
| 评论 | 6; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Usage]: How to use the image datasets sharegpt4v provided in benchmark_serving?

### Issue 正文摘录

### Your current environment ```text The output of `python collect_env.py` ``` ### How would you like to use vllm I want to run multi modal benchmark with vllm, first with image inputs. I download the dataset sharegpt4v as provide in README, but I found if I run benchmark_serving with: ``` dataset-name sharegpt ``` the program actually read the text prompt but no image input. How can we use benchmark_serving with the given dataset, to test the basic performance of dealing with images and prompt input? ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 2: [Usage]: How to use the image datasets sharegpt4v provided in benchmark_serving? usage;stale ### Your current environment ```text The output of `python collect_env.py` ``` ### How would you like to use vllm I want to ru...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: ut? ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: o use the image datasets sharegpt4v provided in benchmark_serving? usage;stale ### Your current environment ```text The output of `python collect_env.py` ``` ### How would you like to use vllm I want to run multi modal...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
