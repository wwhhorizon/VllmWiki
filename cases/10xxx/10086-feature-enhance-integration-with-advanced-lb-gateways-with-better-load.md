# vllm-project/vllm#10086: [Feature]: Enhance integration with advanced LB/gateways with better load/cost reporting and LoRA management

| 字段 | 值 |
| --- | --- |
| Issue | [#10086](https://github.com/vllm-project/vllm/issues/10086) |
| 状态 | closed |
| 标签 | feature request;stale |
| 评论 | 8; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Feature]: Enhance integration with advanced LB/gateways with better load/cost reporting and LoRA management

### Issue 正文摘录

### 🚀 The feature, motivation and pitch There are huge potential in more advanced load balancing strategies tailored for the unique characteristics of AI inference, compared to basic strategies such as round robin. [llm instance gateway](https://github.com/kubernetes-sigs/llm-instance-gateway) is one of such efforts and is demonstrating huge [performance wins](https://docs.google.com/document/d/11ALHEF-9yOaLdbHbDjBoTY6fzejoEKiSYHzWpWqe8ZY/edit?tab=t.0). vLLM can demonstrate leadership in this space by providing better integration with advanced LBs/gateways. [This doc](https://docs.google.com/document/d/18VRJ2ufZmAwBZ2jArfvGjQGaWtsQtAP6_yF2Xn6zcms/edit?tab=t.0#heading=h.sw2xdf66jh6) captures the overall requirements for model servers to better support the llm instance gateway. Luckily vLLM already has lots of features/metrics that enable more efficient load balancing such as exposing the KVCacheUtilization metric. This is a high level breakdown of the feature requests: ### Dynamic LoRA Load/unload - [x] Done in https://github.com/vllm-project/vllm/issues/6275 ### Load/cost reporting in metrics - [x] Many useful metrics are already available https://docs.vllm.ai/en/latest/serving/me...

## 候选优化模式

- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 3: LB/gateways with better load/cost reporting and LoRA management feature request;stale ### 🚀 The feature, motivation and pitch There are huge potential in more advanced load balancing strategies tailored for the unique c...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: bDjBoTY6fzejoEKiSYHzWpWqe8ZY/edit?tab=t.0). vLLM can demonstrate leadership in this space by providing better integration with advanced LBs/gateways. [This doc](https://docs.google.com/document/d/18VRJ2ufZmAwBZ2jArfvGjQ...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: dit?tab=t.0#heading=h.sw2xdf66jh6) captures the overall requirements for model servers to better support the llm instance gateway. Luckily vLLM already has lots of features/metrics that enable more efficient load balanc...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: otivation and pitch There are huge potential in more advanced load balancing strategies tailored for the unique characteristics of AI inference, compared to basic strategies such as round robin. [llm instance gateway](h...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: [x] Many useful metrics are already available https://docs.vllm.ai/en/latest/serving/metrics.html - [x] Add LoRA serving metrics (max loras, active loras). Done in https://github.com/vllm-project/vllm/pull/9477 - [ ] Ad...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
