# vllm-project/vllm#16360: [Bug]: Bad result when serving extracted Gemma-3-4b-it-language model in vLLM

| 字段 | 值 |
| --- | --- |
| Issue | [#16360](https://github.com/vllm-project/vllm/issues/16360) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 5; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: Bad result when serving extracted Gemma-3-4b-it-language model in vLLM

### Issue 正文摘录

### Your current environment ### Environment Docker image: hiyouga/verl:ngc-th2.6.0-cu120-vllm0.8.2-verl0.3.0.post1 ### 🐛 Describe the bug ### Problem Description I've encountered an issue when using vLLM to serve the language model component extracted from gemma-3-4b-it. While the original gemma-3-4b-it model generates normal results with vLLM, the extracted language model (gemma-3-4b-it-language) produces abnormal outputs. ### Steps to reproduce 1. Extract the language model from Gemma-3-4b-it: 2. Verify the extracted model works with Transformers: This works correctly, producing the expected response（" user\n Who are you? \n \n model\nI'm Gemma, a large language model created by the Gemma team at Google DeepMind. I’m an open-weights model, which means I’m widely available for public use! \n\nI take text and images as inputs and generate text as output. \n\nYou can learn more about me on the Gemma project page: https://ai.google.dev/gemma "）. 3. Serve the original model with vLLM, test with curl, and it works well: response text: I'm Gemma, a large language model created by the Gemma team at Google DeepMind. I’m an open-weights model, which means I’m widely available for public...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: ge model in vLLM bug;stale ### Your current environment ### Environment Docker image: hiyouga/verl:ngc-th2.6.0-cu120-vllm0.8.2-verl0.3.0.post1 ### 🐛 Describe the bug ### Problem Description I've encountered an issue whe...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: [Bug]: Bad result when serving extracted Gemma-3-4b-it-language model in vLLM bug;stale ### Your current environment ### Environment Docker image: hiyouga/verl:ngc-th2.6.0-cu120-vllm0.8.2-verl0.3.0.post1 ### 🐛 Describe...
- [Bitwise 确定性与数值等价](../patterns/bitwise_determinism_equivalence.md) - 分数 1: del (gemma-3-4b-it-language) produces abnormal outputs. ### Steps to reproduce 1. Extract the language model from Gemma-3-4b-it: 2. Verify the extracted model works with Transformers: This works correctly, producing the...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which...
- [MoE、GEMM 与 Expert Routing](../patterns/moe_gemm_routing.md) - 分数 1: [Bug]: Bad result when serving extracted Gemma-3-4b-it-language model in vLLM bug;stale ### Your current environment ### Environment Docker image: hiyouga/verl:ngc-th2.6.0-cu120-vllm0.8.2-verl0.3.0.post1 ### 🐛 Describe...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
