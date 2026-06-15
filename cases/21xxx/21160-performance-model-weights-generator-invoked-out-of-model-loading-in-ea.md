# vllm-project/vllm#21160: [Performance]: `model_weights` generator invoked out of Model loading in EAGLE series models.

| 字段 | 值 |
| --- | --- |
| Issue | [#21160](https://github.com/vllm-project/vllm/issues/21160) |
| 状态 | closed |
| 标签 | performance |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Performance]: `model_weights` generator invoked out of Model loading in EAGLE series models.

### Issue 正文摘录

### Proposal to improve performance In EAGLE series models, `vllm/model_executor/models/eagle.py` `vllm/model_executor/models/llama_eagle.py` ..., model_weights is a dict(), WeightGenerator generate weight as tensor, and model_weights collects them, it pass `model_weights.items()` as Iterable to Loader. It evals all Tensor in python, may led to a increase in memory. Why not pass a `generator` to Loader? ### Report of performance regression _No response_ ### Misc discussion on performance _No response_ ### Your current environment (if you think it is necessary) ```text The output of `python collect_env.py` ``` ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 3: ects them, it pass `model_weights.items()` as Iterable to Loader. It evals all Tensor in python, may led to a increase in memory. Why not pass a `generator` to Loader? ### Report of performance regression _No response_...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: [Performance]: `model_weights` generator invoked out of Model loading in EAGLE series models. performance ### Proposal to improve performance In EAGLE series models, `vllm/model_executor/models/eagle.py` `vllm/model_exe...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: ``` ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
