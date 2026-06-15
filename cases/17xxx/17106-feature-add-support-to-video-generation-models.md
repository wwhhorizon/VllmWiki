# vllm-project/vllm#17106: [Feature]: Add Support to Video Generation Models

| 字段 | 值 |
| --- | --- |
| Issue | [#17106](https://github.com/vllm-project/vllm/issues/17106) |
| 状态 | closed |
| 标签 | feature request;stale |
| 评论 | 6; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Feature]: Add Support to Video Generation Models

### Issue 正文摘录

## 🚀 Feature Request: Add Support for Video Generation Models Please consider adding support for the following **video generation** models, which are currently not supported by `vLLM`: - [CogVideoX-5b by THUDM](https://huggingface.co/THUDM/CogVideoX-5b) - [Mochi-1 (Preview) by Genmo](https://huggingface.co/genmo/mochi-1-preview) - [Allegro by Rhymes AI](https://huggingface.co/rhymes-ai/Allegro) - [LTX-Video by Lightricks](https://huggingface.co/Lightricks/LTX-Video) These models represent the latest advancements in **text-to-video** generation, and support for them would significantly enhance vLLM's capabilities in the multimodal AI space. --- ## 🔄 Alternatives _No known alternatives for video generation support in vLLM at the moment._ --- ## 💡 Additional Context These models are gaining popularity in generative AI workflows for creating high-quality video content from text prompts. Integration with vLLM would enable more efficient inference and unlock a range of creative and industrial use cases. --- ## ✅ Pre-Submission Checklist - [x] I have searched for existing issues related to this request. - [x] I have consulted the chatbot available at the bottom-right of the [vLLM documen...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: [Feature]: Add Support to Video Generation Models feature request;stale ## 🚀 Feature Request: Add Support for Video Generation Models Please consider adding support for the following **video generation** models, which a...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: [Feature]: Add Support to Video Generation Models feature request;stale ## 🚀 Feature Request: Add Support for Video Generation Models Please consider adding support for the following **video generation** models, which a...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: o content from text prompts. Integration with vLLM would enable more efficient inference and unlock a range of creative and industrial use cases. --- ## ✅ Pre-Submission Checklist - [x] I have searched for existing issu...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: ndustrial use cases. --- ## ✅ Pre-Submission Checklist - [x] I have searched for existing issues related to this request. - [x] I have consulted the chatbot available at the bottom-right of the [vLLM documentation](http...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: tps://huggingface.co/Lightricks/LTX-Video) These models represent the latest advancements in **text-to-video** generation, and support for them would significantly enhance vLLM's capabilities in the multimodal AI space....

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
