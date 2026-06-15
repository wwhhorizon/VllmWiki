# vllm-project/vllm#12263: [Usage]: Automated Tool Calling for OLMoForCausalLM

| 字段 | 值 |
| --- | --- |
| Issue | [#12263](https://github.com/vllm-project/vllm/issues/12263) |
| 状态 | closed |
| 标签 | usage;stale;tool-calling |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Usage]: Automated Tool Calling for OLMoForCausalLM

### Issue 正文摘录

### Your current environment - Version: 0.6.4.post1 - Python 3.12.0 ### How would you like to use vllm I would like to use `allenai/OLMo-7B-hf`with tool calling. I read in [supported_models](https://docs.vllm.ai/en/latest/models/supported_models.html) that OLMo is supported. However, in [Tool Calling](https://docs.vllm.ai/en/latest/features/tool_calling.html) I can't find the required tool parser. Is there a tool parser for OLMo models available? Thanks! ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: ### How would you like to use vllm I would like to use `allenai/OLMo-7B-hf`with tool calling. I read in [supported_models](https://docs.vllm.ai/en/latest/models/supported_models.html) that OLMo is supported. However, in...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: OLMoForCausalLM usage;stale;tool-calling ### Your current environment - Version: 0.6.4.post1 - Python 3.12.0 ### How would you like to use vllm I would like to use `allenai/OLMo-7B-hf`with tool calling. I read in [suppo...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: ks! ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: [Usage]: Automated Tool Calling for OLMoForCausalLM usage;stale;tool-calling ### Your current environment - Version: 0.6.4.post1 - Python 3.12.0 ### How would you like to use vllm I would like to use `allenai/OLMo-7B-hf...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ith tool calling. I read in [supported_models](https://docs.vllm.ai/en/latest/models/supported_models.html) that OLMo is supported. However, in [Tool Calling](https://docs.vllm.ai/en/latest/features/tool_calling.html) I...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
