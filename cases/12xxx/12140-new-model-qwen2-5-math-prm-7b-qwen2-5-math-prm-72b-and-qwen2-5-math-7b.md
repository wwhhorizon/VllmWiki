# vllm-project/vllm#12140: [New Model]: Qwen2.5-Math-PRM-7B,  Qwen2.5-Math-PRM-72B,  and Qwen2.5-Math-7B-PRM800K

| 字段 | 值 |
| --- | --- |
| Issue | [#12140](https://github.com/vllm-project/vllm/issues/12140) |
| 状态 | closed |
| 标签 | new-model |
| 评论 | 5; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [New Model]: Qwen2.5-Math-PRM-7B,  Qwen2.5-Math-PRM-72B,  and Qwen2.5-Math-7B-PRM800K

### Issue 正文摘录

### The model to consider. https://huggingface.co/Qwen/Qwen2.5-Math-PRM-7B https://huggingface.co/Qwen/Qwen2.5-Math-PRM-72B https://huggingface.co/Qwen/Qwen2.5-Math-7B-PRM800K ### The closest model vllm already supports. vllm/model_executor/models/qwen2_rm.py ### What's your difficulty of supporting the model you want? Hi Team, A few days ago, the Qwen team released a new model class called `Process Reward Model (PRM)`. When attempting to load this new model using vLLM, I encountered the following error: ``` ValueError: Unrecognized configuration class for this kind of AutoModel: AutoModelForCausalLM. ``` I believe this issue arises because the PRM introduces a new configuration class, `Qwen2RMConfig`, which is not currently supported by vLLM. I came across an implementation of `Qwen2RMConfig` in this [GitHub repository](https://github.com/tzteyang/OpenRLHF/blob/bb40a8b5bd49c952deab9f61a66abb00ff9ab9a7/openrlhf/utils/support_models/configuration_qwen2_rm.py#L24). However, I’m unsure how to integrate this into the codebase to resolve the issue. Could you please provide guidance or add support for the new `Qwen2RMConfig` in vLLM? Any assistance would be greatly appreciated. Thank yo...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 5: [New Model]: Qwen2.5-Math-PRM-7B, Qwen2.5-Math-PRM-72B, and Qwen2.5-Math-7B-PRM800K new-model ### The model to consider. https://huggingface.co/Qwen/Qwen2.5-Math-PRM-7B https://huggingface.co/Qwen/Qwen2.5-Math-PRM-72B h...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: or the new `Qwen2RMConfig` in vLLM? Any assistance would be greatly appreciated. Thank you! ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: ! ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), whic...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
