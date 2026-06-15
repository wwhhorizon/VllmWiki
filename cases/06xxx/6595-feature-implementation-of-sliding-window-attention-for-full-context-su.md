# vllm-project/vllm#6595: [Feature]: Implementation of Sliding Window Attention for Full Context Support with Gemma-2

| 字段 | 值 |
| --- | --- |
| Issue | [#6595](https://github.com/vllm-project/vllm/issues/6595) |
| 状态 | closed |
| 标签 | feature request;stale |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Feature]: Implementation of Sliding Window Attention for Full Context Support with Gemma-2

### Issue 正文摘录

### 🚀 The feature, motivation and pitch The state-of-the-art language model Gemma-2-9b has proven to be a powerful SLM for various natural language processing tasks. It is the best model of its size. In some cases, it outperforms Meta-Llama-3-70-B in multi-agent systems. Its ability to translate and accurately follow multistep instructions is impressive. Therefore, there should be significant interest in fully supporting Gemma-2-9b with an 8K token context, rather than being limited to its current 4K sliding window. For LMStudio, the model already works with its full context size. However, we want this model to run on our Nvidia GH200, which currently uses vllm. We would greatly appreciate an implementation that supports this, as it would help accelerate our progress in developing fully local agent systems. :) ### Alternatives _No response_ ### Additional context _No response_

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: Implementation of Sliding Window Attention for Full Context Support with Gemma-2 feature request;stale ### 🚀 The feature, motivation and pitch The state-of-the-art language model Gemma-2-9b has proven to be a powerful S...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: f Sliding Window Attention for Full Context Support with Gemma-2 feature request;stale ### 🚀 The feature, motivation and pitch The state-of-the-art language model Gemma-2-9b has proven to be a powerful SLM for various n...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: n on our Nvidia GH200, which currently uses vllm. We would greatly appreciate an implementation that supports this, as it would help accelerate our progress in developing fully local agent systems. :) ### Alternatives _...
- [MoE、GEMM 与 Expert Routing](../patterns/moe_gemm_routing.md) - 分数 1: Implementation of Sliding Window Attention for Full Context Support with Gemma-2 feature request;stale ### 🚀 The feature, motivation and pitch The state-of-the-art language model Gemma-2-9b has proven to be a powerful S...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
