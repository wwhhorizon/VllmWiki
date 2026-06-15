# vllm-project/vllm#7984: [New Model]: LlavaQwen2ForCausalLM

| 字段 | 值 |
| --- | --- |
| Issue | [#7984](https://github.com/vllm-project/vllm/issues/7984) |
| 状态 | closed |
| 标签 | new-model |
| 评论 | 21; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [New Model]: LlavaQwen2ForCausalLM

### Issue 正文摘录

### The model to consider. I am interested in deploying the HuatuoGPT-Vision 7B model, as detailed in the repository [HuatuoGPT-Vision](https://github.com/FreedomIntelligence/HuatuoGPT-Vision). However, I noticed that the model architecture LlavaQwen2ForCausalLM used by [HuatuoGPT-Vision-7B](https://huggingface.co/FreedomIntelligence/HuatuoGPT-Vision-7B) is not currently supported by vLLM. As this model is a multimodal model, it's hard to add it to vllm framework by myself. Could you please consider adding support for this model? If there are any specific challenges or requirements needed to enable this support, I would be happy to assist or provide more information. Thank you for your attention to this request. ### The closest model vllm already supports. LlavaQwenForCausalLM ### What's your difficulty of supporting the model you want? _No response_ ### Before submitting a new issue... - [X] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 5: [New Model]: LlavaQwen2ForCausalLM new-model ### The model to consider. I am interested in deploying the HuatuoGPT-Vision 7B model, as detailed in the repository [HuatuoGPT-Vision](https://github.com/FreedomIntelligence...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: d you please consider adding support for this model? If there are any specific challenges or requirements needed to enable this support, I would be happy to assist or provide more information. Thank you for your attenti...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: FreedomIntelligence/HuatuoGPT-Vision). However, I noticed that the model architecture LlavaQwen2ForCausalLM used by [HuatuoGPT-Vision-7B](https://huggingface.co/FreedomIntelligence/HuatuoGPT-Vision-7B) is not currently...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: ssist or provide more information. Thank you for your attention to this request. ### The closest model vllm already supports. LlavaQwenForCausalLM ### What's your difficulty of supporting the model you want? _No respons...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
