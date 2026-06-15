# vllm-project/vllm#2665: Setting Different CUDA Devices for LLM and Helper Models

| 字段 | 值 |
| --- | --- |
| Issue | [#2665](https://github.com/vllm-project/vllm/issues/2665) |
| 状态 | closed |
| 标签 |  |
| 评论 | 0; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 |  |
| 子分类 |  |
| Operator 关键词 | cuda |
| 症状 |  |
| 根因提示 |  |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> Setting Different CUDA Devices for LLM and Helper Models

### Issue 正文摘录

I'm currently working on a project where I'm integrating an LLM alongside several auxiliary models to enhance performance. Due to hardware constraints, I need to allocate the LLM to cuda:1 and the helper models to cuda:0. However, I'm facing challenges in achieving this configuration using CUDA_VISIBLE_DEVICES. Has anyone else encountered a similar issue or can offer insights into how to correctly set different CUDA devices for distinct models? Any guidance or suggestions would be greatly appreciated. Thank you in advance for your assistance!

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: Setting Different CUDA Devices for LLM and Helper Models I'm currently working on a project where I'm integrating an LLM alongside several auxiliary models to enhance performance. Due to hardware constraints, I need to...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: locate the LLM to cuda:1 and the helper models to cuda:0. However, I'm facing challenges in achieving this configuration using CUDA_VISIBLE_DEVICES. Has anyone else encountered a similar issue or can offer insights into...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: Setting Different CUDA Devices for LLM and Helper Models I'm currently working on a project where I'm integrating an LLM alongside several auxiliary models to enhance performance. Due to hardware constraints, I need to...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 1: in achieving this configuration using CUDA_VISIBLE_DEVICES. Has anyone else encountered a similar issue or can offer insights into how to correctly set different CUDA devices for distinct models? Any guidance or suggest...

## Wiki 抽取状态

- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
