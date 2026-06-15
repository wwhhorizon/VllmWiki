# vllm-project/vllm#30798: [Usage]:  vllm offline server lora model

| 字段 | 值 |
| --- | --- |
| Issue | [#30798](https://github.com/vllm-project/vllm/issues/30798) |
| 状态 | closed |
| 标签 | usage;stale |
| 评论 | 6; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Usage]:  vllm offline server lora model

### Issue 正文摘录

### Your current environment Hi team, I have a question about deploying LoRA models with a vLLM offline server. Currently, we have a base model **A**. After LoRA training, we obtain adapter parameters **P**. When we serve model A with vLLM (offline server) and enable LoRA, we can select either the **base model A** or **A + P** (LoRA adapter) from the `/v1/models` list for inference. Based on this, suppose we **merge A and P** into a new merged model **B = A + P**, and then continue LoRA training on top of **B** to obtain another LoRA adapter **Q**. Is there a way to deploy on a single vLLM server such that the models list allows choosing among these three options for inference? 1. **A** 2. **A + P** 3. **A + P + Q** If vLLM cannot directly stack LoRA adapters (P then Q) at runtime, is there a recommended approach to **combine P and Q** into a new equivalent adapter (e.g., a single LoRA adapter **R**) that is functionally equivalent to **A + P + Q**, ideally in a way that is **equivalent to training a LoRA adapter directly on base A**? Thanks a lot for your help! --- ### How would you like to use vllm I want to run inference of a [specific model](put link here). I don't know how to...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: -- ### How would you like to use vllm I want to run inference of a [specific model](put link here). I don't know how to integrate it with vllm. ### Before submitting a new issue... - [x] Make sure you already searched f...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: lm. ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: [Usage]: vllm offline server lora model usage;stale ### Your current environment Hi team, I have a question about deploying LoRA models with a vLLM offline server. Currently, we have a base model **A**. After LoRA train...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: [Usage]: vllm offline server lora model usage;stale ### Your current environment Hi team, I have a question about deploying LoRA models with a vLLM offline server. Currently, we have a base model **A**. After LoRA train...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
