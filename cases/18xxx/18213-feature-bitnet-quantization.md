# vllm-project/vllm#18213: [Feature]: BitNet Quantization

| 字段 | 值 |
| --- | --- |
| Issue | [#18213](https://github.com/vllm-project/vllm/issues/18213) |
| 状态 | closed |
| 标签 | feature request;stale |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Feature]: BitNet Quantization

### Issue 正文摘录

### 🚀 The feature, motivation and pitch New model [falcon-E](https://huggingface.co/tiiuae/Falcon-E-3B-Instruct?s=09) has a LlamaForCausalLM architecture but a Bitnet Quantization. They also provide a [onebitllms](https://github.com/tiiuae/onebitllms) library. ### Alternatives There isn't really an optimized way to run bitnet models at scale. The closest being native transformers implementation, or bitnet.cpp. However there is some ongoing efforts [here](https://github.com/vllm-project/vllm/pull/17588) ### Additional context _No response_ ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: ation feature request;stale ### 🚀 The feature, motivation and pitch New model [falcon-E](https://huggingface.co/tiiuae/Falcon-E-3B-Instruct?s=09) has a LlamaForCausalLM architecture but a Bitnet Quantization. They also...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 2: [Feature]: BitNet Quantization feature request;stale ### 🚀 The feature, motivation and pitch New model [falcon-E](https://huggingface.co/tiiuae/Falcon-E-3B-Instruct?s=09) has a LlamaForCausalLM architecture but a Bitnet...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: [Feature]: BitNet Quantization feature request;stale ### 🚀 The feature, motivation and pitch New model [falcon-E](https://huggingface.co/tiiuae/Falcon-E-3B-Instruct?s=09) has a LlamaForCausalLM architecture but a Bitnet...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: huggingface.co/tiiuae/Falcon-E-3B-Instruct?s=09) has a LlamaForCausalLM architecture but a Bitnet Quantization. They also provide a [onebitllms](https://github.com/tiiuae/onebitllms) library. ### Alternatives There isn'...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
