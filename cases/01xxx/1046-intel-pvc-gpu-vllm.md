# vllm-project/vllm#1046: Intel PVC GPU + vLLM

| 字段 | 值 |
| --- | --- |
| Issue | [#1046](https://github.com/vllm-project/vllm/issues/1046) |
| 状态 | closed |
| 标签 |  |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> Intel PVC GPU + vLLM

### Issue 正文摘录

I currently see a prerequisite of CUDA for vLLM models. We currently have a cluster with Intel PVC GPUs. I would like to know if there are plans on abstracting vllm to use our pre-trained models so that it can run without CUDA.

## 候选优化模式

- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: Intel PVC GPU + vLLM I currently see a prerequisite of CUDA for vLLM models. We currently have a cluster with Intel PVC GPUs. I would like to know if there are plans on abstracting vllm to use our pre-trained models so...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: Intel PVC GPU + vLLM I currently see a prerequisite of CUDA for vLLM models. We currently have a cluster with Intel PVC GPUs. I would like to know if there are plans on abstracting vllm to use our pre-trained models so...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
