# vllm-project/vllm#27866: [RFC]: Internal Process-level Fault Tolerance for vLLM

| 字段 | 值 |
| --- | --- |
| Issue | [#27866](https://github.com/vllm-project/vllm/issues/27866) |
| 状态 | closed |
| 标签 | RFC;stale |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [RFC]: Internal Process-level Fault Tolerance for vLLM

### Issue 正文摘录

### Motivation. Modern sparse Mixture-of-Experts (MoE) model service like DeepSeek use hybrid parallelism (e.g., DP+EP) across multiple GPUs and nodes for high-throughput inference, but this tight coupling makes them highly fault-sensitive — a single GPU or network failure can halt the entire instance. **vLLM currently follows a fail-stop recovery model**, where any fault terminates the whole instance, causing minute-long recovery delays and request interruptions — **an overly rigid approach for transient or localized issues such as short communication drops or single-GPU errors**. To address these challenges, we propose to introduce internal process-level fault tolerance mechanisms. These mechanisms aim to handle local faults efficiently while minimizing service interruption from minutes to seconds. Based on publicly reported hardware failure statistics[[1](https://arxiv.org/abs/2407.21783),[2](https://arxiv.org/pdf/2505.09343v1),[3](https://arxiv.org/pdf/2509.16293)], we estimate that approximately 70% of failures can be mitigated by the proposed process-level fault tolerance mechanism. ![Image](https://github.com/user-attachments/assets/cf2161ae-d037-4066-9dba-b1651aa41c37) ###...

## 候选优化模式

- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 3: [RFC]: Internal Process-level Fault Tolerance for vLLM RFC;stale ### Motivation. Modern sparse Mixture-of-Experts (MoE) model service like DeepSeek use hybrid parallelism (e.g., DP+EP) across multiple GPUs and nodes for...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: lt tolerance mechanisms. These mechanisms aim to handle local faults efficiently while minimizing service interruption from minutes to seconds. Based on publicly reported hardware failure statistics[[1](https://arxiv.or...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: Mixture-of-Experts (MoE) model service like DeepSeek use hybrid parallelism (e.g., DP+EP) across multiple GPUs and nodes for high-throughput inference, but this tight coupling makes them highly fault-sensitive — a singl...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: r vLLM RFC;stale ### Motivation. Modern sparse Mixture-of-Experts (MoE) model service like DeepSeek use hybrid parallelism (e.g., DP+EP) across multiple GPUs and nodes for high-throughput inference, but this tight coupl...
- [MoE、GEMM 与 Expert Routing](../patterns/moe_gemm_routing.md) - 分数 2: t Tolerance for vLLM RFC;stale ### Motivation. Modern sparse Mixture-of-Experts (MoE) model service like DeepSeek use hybrid parallelism (e.g., DP+EP) across multiple GPUs and nodes for high-throughput inference, but th...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
