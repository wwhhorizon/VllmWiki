# vllm-project/vllm#12791: [Bug]: Reward model usage

| 字段 | 值 |
| --- | --- |
| Issue | [#12791](https://github.com/vllm-project/vllm/issues/12791) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 20; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: Reward model usage

### Issue 正文摘录

### Your current environment I am recently trying to use the new feature to serve reward model with vLLM, but I note that the sequential classifier type RM is not supported well (I am using `0.7.1`), I checked #8976 #10444 seems it is been resolved already, I am not sure if it is a bug or not ### 🐛 Describe the bug for example (adapted from [this](https://docs.vllm.ai/en/latest/models/pooling_models.html#llm-encode) ) ``` from vllm import LLM llm = LLM(model="Skywork/Skywork-Reward-Llama-3.1-8B-v0.2", task="reward") (output,) = llm.encode("Hello, my name is") data = output.outputs.data print(f"Data: {data!r}") ``` And I got `ValueError: Model architectures ['LlamaForSequenceClassification'] are not supported for now. ` Similarly, `Gemma2ForSequenceClassification` is not supported. I wonder if there will be support for these models ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: [Bug]: Reward model usage bug;stale ### Your current environment I am recently trying to use the new feature to serve reward model with vLLM, but I note that the sequential classifier type RM is not supported well (I am...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: llm.ai/en/latest/models/pooling_models.html#llm-encode) ) ``` from vllm import LLM llm = LLM(model="Skywork/Skywork-Reward-Llama-3.1-8B-v0.2", task="reward") (output,) = llm.encode("Hello, my name is") data = output.out...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: .outputs.data print(f"Data: {data!r}") ``` And I got `ValueError: Model architectures ['LlamaForSequenceClassification'] are not supported for now. ` Similarly, `Gemma2ForSequenceClassification` is not supported. I wond...
- [MoE、GEMM 与 Expert Routing](../patterns/moe_gemm_routing.md) - 分数 1: lamaForSequenceClassification'] are not supported for now. ` Similarly, `Gemma2ForSequenceClassification` is not supported. I wonder if there will be support for these models ### Before submitting a new issue... - [x] M...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: [Bug]: Reward model usage bug;stale ### Your current environment I am recently trying to use the new feature to serve reward model with vLLM, but I note that the sequential classifier type RM is not supported well (I am...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
