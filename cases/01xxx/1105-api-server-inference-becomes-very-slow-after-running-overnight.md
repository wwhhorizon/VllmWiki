# vllm-project/vllm#1105: API-Server inference becomes very slow after running overnight

| 字段 | 值 |
| --- | --- |
| Issue | [#1105](https://github.com/vllm-project/vllm/issues/1105) |
| 状态 | closed |
| 标签 |  |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | ci_build;frontend_api;moe |
| 子分类 |  |
| Operator 关键词 | moe |
| 症状 | slowdown |
| 根因提示 |  |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> API-Server inference becomes very slow after running overnight

### Issue 正文摘录

My api-server becomes very slow after running overnight, even if I restart the api-server. It only returns to normal after restarting the VM. However, it becomes slow again after a while. Is there any expert who can help? Thank you very much. My environment involves creating a virtual machine (VM) on a Hyper Converge Infrastructure machine, and within the VM, setting up a Conda environment. And using an A100 80g GPU.

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: , setting up a Conda environment. And using an A100 80g GPU. performance ci_build;frontend_api;moe moe slowdown My api-server becomes very slow after running overnight, even if I restart the api-server. It only returns...
- [MoE、GEMM 与 Expert Routing](../patterns/moe_gemm_routing.md) - 分数 2: rting the VM. However, it becomes slow again after a while. Is there any expert who can help? Thank you very much. My environment involves creating a virtual machine (VM) on a Hyper Converge Infrastructure machine, and...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: machine, and within the VM, setting up a Conda environment. And using an A100 80g GPU. performance ci_build;frontend_api;moe moe slowdown My api-server becomes very slow after running overnight, even if I restart the ap...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
