# vllm-project/vllm#29485: [RFC]: Detailed Usage Guide for AFD Support in vLLM

| 字段 | 值 |
| --- | --- |
| Issue | [#29485](https://github.com/vllm-project/vllm/issues/29485) |
| 状态 | closed |
| 标签 | RFC;stale |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [RFC]: Detailed Usage Guide for AFD Support in vLLM

### Issue 正文摘录

### Motivation. First, we would like to express our gratitude to the engineers of vLLM. They have brought tremendous surprises to the community and driven significant progress in both science and industry. However, AFD (Attention-FFN Disaggregation), which has garnered substantial attention within the community recently, is not yet supported by vLLM. ### Proposed Change. I have carefully reviewed the vLLM documentation and paid particular attention to relevant issues, arriving at the following conclusions: The vLLM framework does not yet fully support a mature and usable AFD (Attention-FFN Disaggregation) feature. However, experimental implementations for specific models already exist and are in the development and iteration phase. Key issues still need to be addressed before its official deployment. > [[Feature]: AFD support load customer connect model from local path. · Issue #27872 · vllm-project/vllm](https://github.com/vllm-project/vllm/issues/27872) > [RFC]: ATTN-FFN Disaggregation for MoE Models > [GitHub vllm-project/vllm ](https://github.com/vllm-project/vllm/issues/27584) > [draft AFD implementation for step3 by Oliver-ss · Pull Request #25162 · vllm-project/vllm](https:...

## 候选优化模式

- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 3: [RFC]: Detailed Usage Guide for AFD Support in vLLM RFC;stale ### Motivation. First, we would like to express our gratitude to the engineers of vLLM. They have brought tremendous surprises to the community and driven si...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: cess relevant resources. Finally, we wish the developers good health and smooth work. ### Feedback Period. _No response_ ### CC List. _No response_ ### Any Other Things. _No response_ ### Before submitting a new issue.....
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: dous surprises to the community and driven significant progress in both science and industry. However, AFD (Attention-FFN Disaggregation), which has garnered substantial attention within the community recently, is not y...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: aggregation) feature. However, experimental implementations for specific models already exist and are in the development and iteration phase. Key issues still need to be addressed before its official deployment. > [[Fea...
- [MoE、GEMM 与 Expert Routing](../patterns/moe_gemm_routing.md) - 分数 1: com/vllm-project/vllm/issues/27872) > [RFC]: ATTN-FFN Disaggregation for MoE Models > [GitHub vllm-project/vllm ](https://github.com/vllm-project/vllm/issues/27584) > [draft AFD implementation for step3 by Oliver-ss · P...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
