# vllm-project/vllm#33804: [RFC]: [compile] Rollout strategy for AOT Compilation.

| 字段 | 值 |
| --- | --- |
| Issue | [#33804](https://github.com/vllm-project/vllm/issues/33804) |
| 状态 | closed |
| 标签 | RFC;torch.compile |
| 评论 | 4; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [RFC]: [compile] Rollout strategy for AOT Compilation.

### Issue 正文摘录

### Motivation. After some discussion offline with @zou3519, we want to ensure the rollout of AOT compilation doesn't churn vLLM users in general with torch 2.10 in the next vLLM release. Why we think it might cause churn: In the umbrella task for torch 2.10 release, 4 out of 18 launch blocking vLLM test failures was related to AOT compilation: https://github.com/pytorch/pytorch/issues/170433 We had the fixes merged for all of the above issues so far, so we think in general AOT should be well tested against important features we want to cover in the current CI, but just want to request for feedback whether we want to further safeguard the rollout of AOT compilation feature. Context: When VLLM_USE_AOT_COMPILE=1 (currently by default =1 for torch 2.10+), we will serialize both Dynamo and Inductor artifacts on disk, meaning instead of rerunning Dynamo analysis from scratch, we will cache the analysis result when the model code doesn't change in the next vLLM run. (original PR: https://github.com/vllm-project/vllm/pull/24274) ### Proposed Change. **Option 1**: Do nothing, yolo AOT compilation in the next vLLM release, as we currently planned to do. Risk: May cause churn for some users...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: [RFC]: [compile] Rollout strategy for AOT Compilation. RFC;torch.compile ### Motivation. After some discussion offline with @zou3519, we want to ensure the rollout of AOT compilation doesn't churn vLLM users in general...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: 's CI. If we take this path and some user report issues related AOT, the fallback solution is to tell user to use VLLM_USE_AOT_COMPILE=0 for mitigation and triage this to be fixed in the next vLLM release. **Option 2**:...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: se_ ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 1: e churn: In the umbrella task for torch 2.10 release, 4 out of 18 launch blocking vLLM test failures was related to AOT compilation: https://github.com/pytorch/pytorch/issues/170433 We had the fixes merged for all of th...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: Dynamo analysis from scratch, we will cache the analysis result when the model code doesn't change in the next vLLM run. (original PR: https://github.com/vllm-project/vllm/pull/24274) ### Proposed Change. **Option 1**:...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
