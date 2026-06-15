# vllm-project/vllm#44219: [RFC]: hardware agnostic model definitions in vLLM

| 字段 | 值 |
| --- | --- |
| Issue | [#44219](https://github.com/vllm-project/vllm/issues/44219) |
| 状态 | open |
| 标签 | RFC |
| 评论 | 4; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | ci_build;hardware_porting;model_support |
| 子分类 |  |
| Operator 关键词 | cuda;kernel;operator |
| 症状 | build_error |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [RFC]: hardware agnostic model definitions in vLLM

### Issue 正文摘录

### Motivation. This is a direct follow up to https://github.com/vllm-project/vllm/issues/42770, which proposes removing full model torch.compile from vLLM and proposes separating model definitions by hardware type in vLLM. While the [vLLM models proposal](https://github.com/vllm-project/vllm/issues/42770) addresses a lot of the concerns related to achieving maximum performance for the most popular models on the most popular hardware (specifically measured as how many GW of power is expected to be used for inference overall for the next of couple months) it makes supporting a wide set of models and hardwares more challenging. In this follow up, we argue that this proposal doesn’t completely serve the whole userbase. In particular: - There is significant interest in the community for alternative hardwares. We think giving users more choice is good for the community in the long-term. - Supporting many hardwares across many models is a challenging task; we think sharing parts of the stack between hardware is the simplest and most reliable way to do this. We propose to embrace this view of the world while setting appropriate boundaries to ensure this will not get in the way of the top...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: vllm-project/vllm/issues/42770, which proposes removing full model torch.compile from vLLM and proposes separating model definitions by hardware type in vLLM. While the [vLLM models proposal](https://github.com/vllm-pro...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: [RFC]: hardware agnostic model definitions in vLLM RFC ### Motivation. This is a direct follow up to https://github.com/vllm-project/vllm/issues/42770, which proposes removing full model torch.compile from vLLM and prop...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: xisting vLLM hardware-agnostic model definitions and the CustomOp mechanism in vLLM. For head models: this is accepting a hardware-agnostic model definition and PRs to CustomOp-ify it. There are some options for how we...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 2: hat is maintained by the community in the core vLLM repository. Hardware backends can choose to use this model definition or they can choose to create their own model definition (as per [the vLLM models proposal](https:...
- [MoE、GEMM 与 Expert Routing](../patterns/moe_gemm_routing.md) - 分数 1: sure ### CC List. @WoosukKwon @tlrmchlsmth @mgoin @LucasWilkinson @ProExpertProg @ZJY0516 @albanD, @tdoublep, @raghukiran1224, @xuechendi, @claudio1212 ### Any Other Things. Thanks to @albanD, @tdoublep, @raghukiran1224...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
