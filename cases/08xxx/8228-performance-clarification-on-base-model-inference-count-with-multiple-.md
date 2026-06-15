# vllm-project/vllm#8228: [Performance]: Clarification on Base Model Inference Count with Multiple LoRA Models in vLLM Deployment

| 字段 | 值 |
| --- | --- |
| Issue | [#8228](https://github.com/vllm-project/vllm/issues/8228) |
| 状态 | closed |
| 标签 | performance |
| 评论 | 4; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Performance]: Clarification on Base Model Inference Count with Multiple LoRA Models in vLLM Deployment

### Issue 正文摘录

### Proposal to improve performance _No response_ ### Report of performance regression _No response_ ### Misc discussion on performance Question: When deploying LoRA with vLLM, suppose I have 1000 different LoRA models, and each LoRA receives a separate request with a different input. In this scenario, how many times does the base model actually perform inference? Is it only once, or does it perform 1000 inferences? I understand that the LoRA part will run 1000 times, but its computational cost is relatively small. I'm mainly concerned about how many times the base model runs inference in this case. If the base model only runs once, that would be incredibly efficient, meaning that as the number of LoRA models increases, the overall efficiency would improve significantly. Is this possible? ### Your current environment (if you think it is necessary) _No response_ ### Before submitting a new issue... - [X] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: LoRA part will run 1000 times, but its computational cost is relatively small. I'm mainly concerned about how many times the base model runs inference in this case. If the base model only runs once, that would be incred...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 2: roposal to improve performance _No response_ ### Report of performance regression _No response_ ### Misc discussion on performance Question: When deploying LoRA with vLLM, suppose I have 1000 different LoRA models, and...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: his case. If the base model only runs once, that would be incredibly efficient, meaning that as the number of LoRA models increases, the overall efficiency would improve significantly. Is this possible? ### Your current...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: [Performance]: Clarification on Base Model Inference Count with Multiple LoRA Models in vLLM Deployment performance ### Proposal to improve performance _No response_ ### Report of performance regression _No response_ ##...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: ose I have 1000 different LoRA models, and each LoRA receives a separate request with a different input. In this scenario, how many times does the base model actually perform inference? Is it only once, or does it perfo...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
