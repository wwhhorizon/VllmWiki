# vllm-project/vllm#2714: Output Garbage Text in Mixtral 8x7b Post Upgrade to 0.3.0

| 字段 | 值 |
| --- | --- |
| Issue | [#2714](https://github.com/vllm-project/vllm/issues/2714) |
| 状态 | closed |
| 标签 | stale |
| 评论 | 10; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> Output Garbage Text in Mixtral 8x7b Post Upgrade to 0.3.0

### Issue 正文摘录

I recently upgraded my deployment from version 0.2.7 to 0.3.0 for a mixtral-8x7b architecture model and have encountered a significant issue where the model outputs completely garbled data post-upgrade. Upon conducting tests, I found that the commit [ea8489fce266d69f2fbe314c1385956b1a342e12](https://github.com/vllm-project/vllm/commit/ea8489fce266d69f2fbe314c1385956b1a342e12) produces expected and normal outputs. However, starting from commit [ab406446691f289ef51d1abd8d1ff66760eda36f](https://github.com/vllm-project/vllm/commit/ab406446691f289ef51d1abd8d1ff66760eda36f), the output becomes entirely garbage. This leads me to suspect that the issue may be related to the introduction of fused kernel. ### Environment Details: - **PyTorch Version:** 2.2.0 - **CUDA Version:** 12.1 - **Hardware:** NVIDIA V100 - Enforce_eager = True, TP=4 Thank you for addressing this matter.

## 候选优化模式

- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: ly upgraded my deployment from version 0.2.7 to 0.3.0 for a mixtral-8x7b architecture model and have encountered a significant issue where the model outputs completely garbled data post-upgrade. Upon conducting tests, I...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: 8x7b Post Upgrade to 0.3.0 stale I recently upgraded my deployment from version 0.2.7 to 0.3.0 for a mixtral-8x7b architecture model and have encountered a significant issue where the model outputs completely garbled da...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: y deployment from version 0.2.7 to 0.3.0 for a mixtral-8x7b architecture model and have encountered a significant issue where the model outputs completely garbled data post-upgrade. Upon conducting tests, I found that t...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: Output Garbage Text in Mixtral 8x7b Post Upgrade to 0.3.0 stale I recently upgraded my deployment from version 0.2.7 to 0.3.0 for a mixtral-8x7b architecture model and have encountered a significant issue where the mode...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: the model outputs completely garbled data post-upgrade. Upon conducting tests, I found that the commit [ea8489fce266d69f2fbe314c1385956b1a342e12](https://github.com/vllm-project/vllm/commit/ea8489fce266d69f2fbe314c13859...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
