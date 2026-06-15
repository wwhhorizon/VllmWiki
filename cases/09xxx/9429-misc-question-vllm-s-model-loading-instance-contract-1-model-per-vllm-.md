# vllm-project/vllm#9429: [Misc]: [Question] vLLM's model loading & instance contract, 1 model per vLLM instance, or multiple models per vLLM instance

| 字段 | 值 |
| --- | --- |
| Issue | [#9429](https://github.com/vllm-project/vllm/issues/9429) |
| 状态 | closed |
| 标签 | stale |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Misc]: [Question] vLLM's model loading & instance contract, 1 model per vLLM instance, or multiple models per vLLM instance

### Issue 正文摘录

### Anything you want to discuss about vllm. Can vLLM consider support multiple models on the same vLLM instance? We are evaluating using vLLM for large scale LLM inference serving. But we are concerned by the limit of 1 model per vLLM instances, as we are serving small models on beefy GPUs (which are keep getting bigger). Managing multiple vLLM instances for each model on the same GPU is very challenging. ### Before submitting a new issue... - [X] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: concerned by the limit of 1 model per vLLM instances, as we are serving small models on beefy GPUs (which are keep getting bigger). Managing multiple vLLM instances for each model on the same GPU is very challenging. ##...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 2: vLLM consider support multiple models on the same vLLM instance? We are evaluating using vLLM for large scale LLM inference serving. But we are concerned by the limit of 1 model per vLLM instances, as we are serving sma...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 1: odels on the same vLLM instance? We are evaluating using vLLM for large scale LLM inference serving. But we are concerned by the limit of 1 model per vLLM instances, as we are serving small models on beefy GPUs (which a...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: [Misc]: [Question] vLLM's model loading & instance contract, 1 model per vLLM instance, or multiple models per vLLM instance stale ### Anything you want to discuss about vllm. Can vLLM consider support multiple models o...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: ontract, 1 model per vLLM instance, or multiple models per vLLM instance stale ### Anything you want to discuss about vllm. Can vLLM consider support multiple models on the same vLLM instance? We are evaluating using vL...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
