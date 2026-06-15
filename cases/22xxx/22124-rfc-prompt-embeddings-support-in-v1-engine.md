# vllm-project/vllm#22124: [RFC]: Prompt Embeddings Support in v1 Engine

| 字段 | 值 |
| --- | --- |
| Issue | [#22124](https://github.com/vllm-project/vllm/issues/22124) |
| 状态 | closed |
| 标签 | RFC |
| 评论 | 5; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [RFC]: Prompt Embeddings Support in v1 Engine

### Issue 正文摘录

### Motivation. Prompt Embedding inputs are a niche, but frequently asked for feature in vLLM. https://github.com/vllm-project/vllm/pull/15428 introduced them in the v0 engine, but they have not yet been ported to the v1 engine. Prompt embedding users will be stuck on older versions of vLLM unless the feature is also introduced into the v1 engine. Related historical issues/PRs: v0 Support: - https://github.com/vllm-project/vllm/pull/15428 - https://github.com/vllm-project/vllm/pull/17607 - https://github.com/vllm-project/vllm/pull/17590 - https://github.com/vllm-project/vllm/pull/17615 - https://github.com/vllm-project/vllm/pull/18171 - https://github.com/vllm-project/vllm/pull/21390 - https://github.com/vllm-project/vllm/pull/21612 Open Issues that would require v1 support to fix: - https://github.com/vllm-project/vllm/issues/20757 (Although this issue is closed because the user's original issue was resolved, it revealed a more fundamental incompatibility between the v0 implementation and multi-modal models in that engine which was not resolved). - https://github.com/vllm-project/vllm/issues/19746 ### Proposed Change. ### Input processing #### Input pre-processing https://github....

## 候选优化模式

- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 5: length of prompt embeds OR prompt_token_ids. Additional the v1 EngineCoreRequest requires a new prompt_embeds field to pass in the prompt_embeds to the engine. There are several other places between the input processing...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: n ported to the v1 engine. Prompt embedding users will be stuck on older versions of vLLM unless the feature is also introduced into the v1 engine. Related historical issues/PRs: v0 Support: - https://github.com/vllm-pr...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: undamental incompatibility between the v0 implementation and multi-modal models in that engine which was not resolved). - https://github.com/vllm-project/vllm/issues/19746 ### Proposed Change. ### Input processing ####...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: is sufficiently different from v0, that not much can be reused. The new architecture, which handles multimodal inputs by generating the appropriate inputs_embeds already has much of the support needed to take raw inputs...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 2: abled (or batch does not contain prompt_embeds) to avoid the performance regression in https://github.com/vllm-project/vllm/pull/11032. input_ids = self.input_ids[:num_input_tokens] inputs_embeds = None ``` This could b...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
