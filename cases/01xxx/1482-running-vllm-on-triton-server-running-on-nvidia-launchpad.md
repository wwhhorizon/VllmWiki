# vllm-project/vllm#1482: Running vllm on Triton server running on Nvidia launchpad

| 字段 | 值 |
| --- | --- |
| Issue | [#1482](https://github.com/vllm-project/vllm/issues/1482) |
| 状态 | closed |
| 标签 |  |
| 评论 | 0; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> Running vllm on Triton server running on Nvidia launchpad

### Issue 正文摘录

Can I run vllm on nvidia launchpad? It has cuda version 12.2. Has vllm started supporting cuda version 12.x? Since we can deploy vllm on [triton server ](https://vllm.readthedocs.io/en/latest/serving/deploying_with_triton.html), I wonder if I can run it on NVIDIA Launchpad as well. Thanks!

## 候选优化模式

- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: Running vllm on Triton server running on Nvidia launchpad Can I run vllm on nvidia launchpad? It has cuda version 12.2. Has vllm started supporting cuda version 12.x? Since we can deploy vllm on [triton server ](https:/...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: ning on Nvidia launchpad Can I run vllm on nvidia launchpad? It has cuda version 12.2. Has vllm started supporting cuda version 12.x? Since we can deploy vllm on [triton server ](https://vllm.readthedocs.io/en/latest/se...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: r running on Nvidia launchpad Can I run vllm on nvidia launchpad? It has cuda version 12.2. Has vllm started supporting cuda version 12.x? Since we can deploy vllm on [triton server ](https://vllm.readthedocs.io/en/late...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: we can deploy vllm on [triton server ](https://vllm.readthedocs.io/en/latest/serving/deploying_with_triton.html), I wonder if I can run it on NVIDIA Launchpad as well. Thanks!

## Wiki 抽取状态

- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
