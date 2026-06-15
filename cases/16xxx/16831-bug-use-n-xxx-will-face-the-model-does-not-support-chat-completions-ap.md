# vllm-project/vllm#16831: [Bug]: use n = xxx will face "the model does not support Chat Completions API" sometimes

| 字段 | 值 |
| --- | --- |
| Issue | [#16831](https://github.com/vllm-project/vllm/issues/16831) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: use n = xxx will face "the model does not support Chat Completions API" sometimes

### Issue 正文摘录

### Your current environment ``` resp = client.chat.completions.create( model= model, messages=messages, temperature = 1.3, n = 3, timeout = 6000 ) ``` ``` ChatCompletion(id=None, choices=None, created=None, model=None, object='error', service_tier=None, system_fingerprint=None, usage=None, message='The model does not support Chat Completions API', type='BadRequestError', param=None, code=400) ``` ### 🐛 Describe the bug 1 ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: 1 ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), whic...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: [Bug]: use n = xxx will face "the model does not support Chat Completions API" sometimes bug ### Your current environment ``` resp = client.chat.completions.create( model= model, messages=messages, temperature = 1.3, n...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: one, message='The model does not support Chat Completions API', type='BadRequestError', param=None, code=400) ``` ### 🐛 Describe the bug 1 ### Before submitting a new issue... - [x] Make sure you already searched for re...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
