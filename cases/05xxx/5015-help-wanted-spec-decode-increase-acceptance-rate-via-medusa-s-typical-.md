# vllm-project/vllm#5015: [Help wanted] [Spec decode]: Increase acceptance rate via Medusa's typical acceptance

| 字段 | 值 |
| --- | --- |
| Issue | [#5015](https://github.com/vllm-project/vllm/issues/5015) |
| 状态 | closed |
| 标签 | feature request;speculative-decoding |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Help wanted] [Spec decode]: Increase acceptance rate via Medusa's typical acceptance

### Issue 正文摘录

### 🚀 The feature, motivation and pitch Speculative decoding allows emitting multiple tokens per sequence by speculating future tokens, scoring their likelihood using the LLM, and then accepting each speculative token based on its likelihood. This process is laid out in the following diagram: ![Screenshot 2024-05-23 at 1 45 16 PM](https://github.com/vllm-project/vllm/assets/950914/52d21c58-1a0e-4a8f-b1f8-4abe79651588) The problem with rejection sampling is that it holds a very high bar for quality: it is lossless and guarantees the distribution of the target model, even if it means rejecting plausible speculative tokens. This issue is a request to implement Medusa's typical acceptance routing in vLLM. Typical acceptance trades off output quality to increase the acceptance rate. See "Choice of threshold in typical acceptance" in the [Medusa blogpost](https://sites.google.com/view/medusa-llm) for more information. vLLM users should be able to toggle between different acceptance routines; they can use rejection sampling for tasks that require higher quality, or typical acceptance when speedup is more important. NOTE: This acceptance routine should work with other proposal types (Eagl...

## 候选优化模式

- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 5: [Help wanted] [Spec decode]: Increase acceptance rate via Medusa's typical acceptance feature request;speculative-decoding ### 🚀 The feature, motivation and pitch Speculative decoding allows emitting multiple tokens per...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: or quality: it is lossless and guarantees the distribution of the target model, even if it means rejecting plausible speculative tokens. This issue is a request to implement Medusa's typical acceptance routing in vLLM....
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: okens. This issue is a request to implement Medusa's typical acceptance routing in vLLM. Typical acceptance trades off output quality to increase the acceptance rate. See "Choice of threshold in typical acceptance" in t...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: that require higher quality, or typical acceptance when speedup is more important. NOTE: This acceptance routine should work with other proposal types (Eagle, draft, ngram, other), not just Medusa. The speculative decod...
- [MoE、GEMM 与 Expert Routing](../patterns/moe_gemm_routing.md) - 分数 1: okens. This issue is a request to implement Medusa's typical acceptance routing in vLLM. Typical acceptance trades off output quality to increase the acceptance rate. See "Choice of threshold in typical acceptance" in t...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
