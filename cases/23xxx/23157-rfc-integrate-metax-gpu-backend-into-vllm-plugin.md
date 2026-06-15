# vllm-project/vllm#23157: [RFC]: Integrate MetaX GPU Backend into vLLM Plugin

| 字段 | 值 |
| --- | --- |
| Issue | [#23157](https://github.com/vllm-project/vllm/issues/23157) |
| 状态 | closed |
| 标签 | RFC;stale |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | ci_build;distributed_parallel;frontend_api;hardware_porting;model_support |
| 子分类 | cold_start |
| Operator 关键词 | cuda;kernel;operator |
| 症状 | build_error |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [RFC]: Integrate MetaX GPU Backend into vLLM Plugin

### Issue 正文摘录

# Integrate MetaX GPU into vLLM Plugin ## Background MetaX is dedicated to delivering full-stack GPU chips and solutions for heterogeneous computing, which are widely applicable in cutting-edge domains such as Intelligent Computing, Cloud Computing, Autonomous Vehicles. These solutions provide robust computational support for the advancement of the digital economy. MetaX develops full-stack GPU chips and will launch the MetaX N-series GPUs for inference, MetaX [C-series GPUs](https://www.metax-tech.com/en/goods/prod.html?cid=2) for general-purpose computing, and MetaX G-series GPUs for graphics. All MetaX products are based on proprietary GPU IP, featuring a fully independent instruction set and architecture, as well as a comprehensive software stack (*MXMACA*) that maintains compatibility with mainstream GPU ecosystems. ### i. MXMACA MXMACA (hereinafter referred to as *maca*) is a heterogeneous computing platform introduced by MetaX, utilizing a general-purpose parallel computing architecture. It incorporates a self-developed Instruction Set Architecture (ISA) and a parallel computing engine within the GPU. This platform provides a user-friendly, C-like programming language for d...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 7: nce, MetaX [C-series GPUs](https://www.metax-tech.com/en/goods/prod.html?cid=2) for general-purpose computing, and MetaX G-series GPUs for graphics. All MetaX products are based on proprietary GPU IP, featuring a fully...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 5: ugin ## Background MetaX is dedicated to delivering full-stack GPU chips and solutions for heterogeneous computing, which are widely applicable in cutting-edge domains such as Intelligent Computing, Cloud Computing, Aut...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: ainstream C/C++ heterogeneous computing languages, such as CUDA. More information is available at [MetaX](https://www.metax-tech.com/en/about/about.html). ## Motivation. Since version 0.6.6, [MetaX](https://www.metax-te...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: [RFC]: Integrate MetaX GPU Backend into vLLM Plugin RFC;stale # Integrate MetaX GPU into vLLM Plugin ## Background MetaX is dedicated to delivering full-stack GPU chips and solutions for heterogeneous computing, which a...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 1: ugin. This can be easily addressed in vLLM(non-plugin) by adding an if-else branch to redirect `forward_maca` to `forward_cuda`. Other related limitations are discussed in [issue 19161](https://github.com/vllm-project/v...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
