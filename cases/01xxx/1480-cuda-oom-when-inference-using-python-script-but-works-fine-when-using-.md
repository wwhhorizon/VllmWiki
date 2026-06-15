# vllm-project/vllm#1480: CUDA OOM when inference using python script but works fine when using online inference command

| 字段 | 值 |
| --- | --- |
| Issue | [#1480](https://github.com/vllm-project/vllm/issues/1480) |
| 状态 | closed |
| 标签 |  |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | model_support |
| 子分类 | memory |
| Operator 关键词 | cuda |
| 症状 | oom |
| 根因提示 | env_dependency;shape |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> CUDA OOM when inference using python script but works fine when using online inference command

### Issue 正文摘录

I bumped into a problem when using vllm to do llm generation. I use the same model Qwen-7B for offline inference and online inference, when using offline inference I followed the instruction in the documentation but I got cuda out of memory issue. However, when I use the same model to initialize a service and try using online inference to do the same generation task, it works fine. In my situation, I need to do batch offline inference, can you give me some advice on how to avoid the CUDA OOM problem? THANK YOU!

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: mped into a problem when using vllm to do llm generation. I use the same model Qwen-7B for offline inference and online inference, when using offline inference I followed the instruction in the documentation but I got c...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: the CUDA OOM problem? THANK YOU! performance model_support cuda oom env_dependency;shape I bumped into a problem when using vllm to do llm generation. I use the same model Qwen-7B for offline inference and online infere...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: CUDA OOM when inference using python script but works fine when using online inference command I bumped into a problem when using vllm to do llm generation. I use the same model Qwen-7B for offline inference and online i
- [KV Cache 容量、压缩与 Offload](../patterns/kv_cache_capacity_offload.md) - 分数 1: CUDA OOM when inference using python script but works fine when using online inference command I bumped into a problem when using vllm to do llm generation. I use the same model Qwen-7B for offline inference and online...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
