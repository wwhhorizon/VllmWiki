# vllm-project/vllm#16268: [RFC]: TPU V1 Sampler planning

| 字段 | 值 |
| --- | --- |
| Issue | [#16268](https://github.com/vllm-project/vllm/issues/16268) |
| 状态 | closed |
| 标签 | RFC;stale |
| 评论 | 8; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | ci_build;frontend_api;hardware_porting;model_support;sampling_logits |
| 子分类 | latency_reg |
| Operator 关键词 | cuda;operator;sampling |
| 症状 | build_error;slowdown |
| 根因提示 | env_dependency;shape |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [RFC]: TPU V1 Sampler planning

### Issue 正文摘录

### Motivation. I'd like to gather some input on how to move forward with sampling support, and also provide a brief recap of the current state+planned support. At a high level, the current design splits model forward and sampling into two separate graphs. As of now (`f2ebb6f54`) only the `temperature` and `min_p` have been intentionally enabled. As more techniques will be added, the sampling graph will grow in size (vertically, sequential ops) and performance may need monitoring, as we're simply evaluating more operations at runtime. To clarify, even when one option is not enabled, we still evaluate a no-op version that undergoes the same ops in the graph (eg top-p with p=1). ### Proposed Change. Following https://github.com/vllm-project/vllm/pull/15489 a few concerns that have been raised regarding performance while enabling topk, hence adding the **very first** op to the initial sampling graph, I'd like to re-evaluate the current approach. Looking at the opposite side of the spectrum one could ideally provide a sampling graph for each combination of parameters. While this is unfeasible due to the number of parameters that sampling needs to support, one approach "in the middle"...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 5: clarify, even when one option is not enabled, we still evaluate a no-op version that undergoes the same ops in the graph (eg top-p with p=1). ### Proposed Change. Following https://github.com/vllm-project/vllm/pull/1548...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 4: ly, sequential ops) and performance may need monitoring, as we're simply evaluating more operations at runtime. To clarify, even when one option is not enabled, we still evaluate a no-op version that undergoes the same...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: , current interface needs to be rethought because it can introduce dynamism. We could create a BxV matrix (B padded+precompiled) to pack the preferences from the list[dicts]. This would work but obviously the factor of...
- [MoE、GEMM 与 Expert Routing](../patterns/moe_gemm_routing.md) - 分数 2: few concerns that have been raised regarding performance while enabling topk, hence adding the **very first** op to the initial sampling graph, I'd like to re-evaluate the current approach. Looking at the opposite side...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: [RFC]: TPU V1 Sampler planning RFC;stale ### Motivation. I'd like to gather some input on how to move forward with sampling support, and also provide a brief recap of the current state+planned support. At a high level,...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
