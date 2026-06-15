# vllm-project/vllm#9872: [Bug]: You are using a model of type qwen2_vl to instantiate a model of type . This is not supported for all configurations of models and can yield errors.

| 字段 | 值 |
| --- | --- |
| Issue | [#9872](https://github.com/vllm-project/vllm/issues/9872) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 17; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: You are using a model of type qwen2_vl to instantiate a model of type . This is not supported for all configurations of models and can yield errors.

### Issue 正文摘录

### Your current environment vllm=0.6.3 ### Model Input Dumps You are using a model of type qwen2_vl to instantiate a model of type . This is not supported for all configurations of models and can yield errors. ### 🐛 Describe the bug vllm of 0.6.3 supoorted Qwen2-vl Now ,but when inerence , it raise an warning,did't it result to some errors? You are using a model of type qwen2_vl to instantiate a model of type . This is not supported for all configurations of models and can yield errors. ### Before submitting a new issue... - [X] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: [Bug]: You are using a model of type qwen2_vl to instantiate a model of type . This is not supported for all configurations of models and can yield errors. bug;stale ### Your current environment vllm=0.6.3 ### Model Inp...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: rs. ### Before submitting a new issue... - [X] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: not supported for all configurations of models and can yield errors. bug;stale ### Your current environment vllm=0.6.3 ### Model Input Dumps You are using a model of type qwen2_vl to instantiate a model of type . This i...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
