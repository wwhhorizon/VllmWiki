# vllm-project/vllm#3019: No CUDA GPUs are available

| 字段 | 值 |
| --- | --- |
| Issue | [#3019](https://github.com/vllm-project/vllm/issues/3019) |
| 状态 | closed |
| 标签 |  |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | development |
| 工作域 |  |
| 子分类 | install |
| Operator 关键词 | cuda |
| 症状 |  |
| 根因提示 |  |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> No CUDA GPUs are available

### Issue 正文摘录

I am trying to run this on Kubernetes which has GPU available The image I am using: ``` image: nvidia/cuda:12.3.1-devel-ubi8 ``` When I attempt to run code form https://github.com/vllm-project/vllm/blob/main/examples/offline_inference.py#L2 I get that error. I have ensured pod is running on the node with the GPU.

## 候选优化模式

- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: No CUDA GPUs are available I am trying to run this on Kubernetes which has GPU available The image I am using: ``` image: nvidia/cuda:12.3.1-devel-ubi8 ``` When I attempt to run code form https://github.com/vllm-

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
