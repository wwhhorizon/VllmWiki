# vllm-project/vllm#22475: [Bug]: Major issues with transformers version causing rubbish generations with Gemma3 family using vllm

| 字段 | 值 |
| --- | --- |
| Issue | [#22475](https://github.com/vllm-project/vllm/issues/22475) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 6; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: Major issues with transformers version causing rubbish generations with Gemma3 family using vllm

### Issue 正文摘录

### Your current environment . ### 🐛 Describe the bug Major issues with transformers version when used with Gemma3 family models on vllm. The output generations are incorrect and not usable—appears to be due to incompatibility or regression in transformers. Please advise on compatible versions or fixes. Example: Generations are rubbish or meaningless compared to expected outputs. Tested with latest vllm and Gemma3 models. ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: Major issues with transformers version causing rubbish generations with Gemma3 family using vllm bug ### Your current environment . ### 🐛 Describe the bug Major issues with transformers version when used with Gemma3 fam...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 2: ons are incorrect and not usable—appears to be due to incompatibility or regression in transformers. Please advise on compatible versions or fixes. Example: Generations are rubbish or meaningless compared to expected ou...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: [Bug]: Major issues with transformers version causing rubbish generations with Gemma3 family using vllm bug ### Your current environment . ### 🐛 Describe the bug Major issues with transformers version when used with Gem...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: ls. ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [MoE、GEMM 与 Expert Routing](../patterns/moe_gemm_routing.md) - 分数 1: Major issues with transformers version causing rubbish generations with Gemma3 family using vllm bug ### Your current environment . ### 🐛 Describe the bug Major issues with transformers version when used with Gemma3 fam...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
