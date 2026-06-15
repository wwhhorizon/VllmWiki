# vllm-project/vllm#32545: [Bug]: Gemma3/SiglipVisionEmbeddings embedding output is different to transformers implementation due to custom Conv2d

| 字段 | 值 |
| --- | --- |
| Issue | [#32545](https://github.com/vllm-project/vllm/issues/32545) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 8; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: Gemma3/SiglipVisionEmbeddings embedding output is different to transformers implementation due to custom Conv2d

### Issue 正文摘录

### Your current environment vLLM main branch (v0.13.0) ### 🐛 Describe the bug Due to custom `enable_linear` in Conv2d in vLLM, the output of this layer used in SiglipVisionEmbeddings is different to SiglipVisionEmbeddings in transformers which uses vanilla Conv2d When I run inference of [Gemma3-4b-it](https://huggingface.co/google/gemma-3-4b-it) model, I notice that the vision part of vLLM implementation and transformer are different. Particularly, tracing down to the [patch_embedding](https://github.com/vllm-project/vllm/blob/main/vllm/model_executor/models/siglip.py#L289) layer which is basically a custom Conv2dLayer. When enable_linear = True (which is the case of Gemma3 model), the flow goes to [custom implementation of Conv2d](https://github.com/vllm-project/vllm/blob/main/vllm/model_executor/layers/conv.py#L117-L130) 1- Why do we need a custom implementation of Conv2d? 2- Is it expected that Gemma3-4b-it should use this custom implemetation? ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots o...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: [Bug]: Gemma3/SiglipVisionEmbeddings embedding output is different to transformers implementation due to custom Conv2d bug;stale ### Your current environment vLLM main branch (v0.13.0) ### 🐛 Describe the bug Due to cust...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: t of vLLM implementation and transformer are different. Particularly, tracing down to the [patch_embedding](https://github.com/vllm-project/vllm/blob/main/vllm/model_executor/models/siglip.py#L289) layer which is basica...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: on? ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [MoE、GEMM 与 Expert Routing](../patterns/moe_gemm_routing.md) - 分数 1: [Bug]: Gemma3/SiglipVisionEmbeddings embedding output is different to transformers implementation due to custom Conv2d bug;stale ### Your current environment vLLM main branch (v0.13.0) ### 🐛 Describe the bug Due to cust...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: put is different to transformers implementation due to custom Conv2d bug;stale ### Your current environment vLLM main branch (v0.13.0) ### 🐛 Describe the bug Due to custom `enable_linear` in Conv2d in vLLM, the output o...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
