# vllm-project/vllm#6321: [Model]: Support for InternVL2

| 字段 | 值 |
| --- | --- |
| Issue | [#6321](https://github.com/vllm-project/vllm/issues/6321) |
| 状态 | closed |
| 标签 | new-model |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Model]: Support for InternVL2

### Issue 正文摘录

### 🚀 The feature, motivation and pitch InternVL2 is currently the most powerful open-source Multimodal Large Language Model (MLLM). The InternVL2 family includes models ranging from a 2B model, suitable for edge devices, to a 108B model, which is significantly more powerful. With larger-scale language models, InternVL2-Pro demonstrates outstanding multimodal understanding capabilities, matching the performance of commercial closed-source models across various benchmarks. Given the significant potential of InternVL2, we believe that integrating it with vLLM would greatly benefit both the vLLM community and users of this model. We kindly request your assistance in enabling the deployment of InternVL2 using the vLLM framework. We look forward to your positive response and are eager to collaborate on this exciting endeavor. ### Alternatives _No response_ ### Additional context Blog：https://internvl.github.io/blog/2024-07-02-InternVL-2.0/ Model Family：https://huggingface.co/collections/OpenGVLab/internvl-20-667d3961ab5eb12c7ed1463e

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: [Model]: Support for InternVL2 new-model ### 🚀 The feature, motivation and pitch InternVL2 is currently the most powerful open-source Multimodal Large Language Model (MLLM). The InternVL2 family includes models ranging f
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: multimodal understanding capabilities, matching the performance of commercial closed-source models across various benchmarks. Given the significant potential of InternVL2, we believe that integrating it with vLLM would...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 1: ices, to a 108B model, which is significantly more powerful. With larger-scale language models, InternVL2-Pro demonstrates outstanding multimodal understanding capabilities, matching the performance of commercial closed...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: eatly benefit both the vLLM community and users of this model. We kindly request your assistance in enabling the deployment of InternVL2 using the vLLM framework. We look forward to your positive response and are eager...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: tching the performance of commercial closed-source models across various benchmarks. Given the significant potential of InternVL2, we believe that integrating it with vLLM would greatly benefit both the vLLM community a...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
