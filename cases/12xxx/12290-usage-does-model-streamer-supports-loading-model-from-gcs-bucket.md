# vllm-project/vllm#12290: [Usage]: Does model streamer supports loading model from GCS bucket?

| 字段 | 值 |
| --- | --- |
| Issue | [#12290](https://github.com/vllm-project/vllm/issues/12290) |
| 状态 | closed |
| 标签 | usage;stale |
| 评论 | 10; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Usage]: Does model streamer supports loading model from GCS bucket?

### Issue 正文摘录

### Your current environment ```text The output of `python collect_env.py` ``` ### How would you like to use vllm Hi, I am looking into use [Run:ai Model Streamer](https://docs.vllm.ai/en/stable/serving/runai_model_streamer.html#loading-models-with-run-ai-model-streamer), and from the document, it says it only supports loading from remove `AWS S3 object store`, so I want to ask does it support loading from Google Cloud Storage bucket (a.k.a GCS)? Thanks! ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: ks! ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: [Usage]: Does model streamer supports loading model from GCS bucket? usage;stale ### Your current environment ```text The output of `python collect_env.py` ``` ### How would you like to use vllm Hi, I am looking into us...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: sage]: Does model streamer supports loading model from GCS bucket? usage;stale ### Your current environment ```text The output of `python collect_env.py` ``` ### How would you like to use vllm Hi, I am looking into use...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
