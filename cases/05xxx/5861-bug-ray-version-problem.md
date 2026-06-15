# vllm-project/vllm#5861: [Bug]: ray version problem

| 字段 | 值 |
| --- | --- |
| Issue | [#5861](https://github.com/vllm-project/vllm/issues/5861) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | development |
| 工作域 | distributed_parallel;model_support |
| 子分类 | env_compat |
| Operator 关键词 | cuda |
| 症状 |  |
| 根因提示 |  |
| 硬件范围 | nvidia |
| 需要人工复核 | True |

## 源证据

### Issue 标题

> [Bug]: ray version problem

### Issue 正文摘录

### Your current environment ray= 2.10.0 ### 🐛 Describe the bug New additions in #5748 from ray.exceptions import ActorDiedError, but only in ray>=2.11.0, Now ray =2.9 in the requirements-cuda.txt file, loading the model will fail after the source code is compiled

## 现有链接修复摘要

#5748 [Core] Add fault tolerance for `RayTokenizerGroupPool`

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: [Bug]: ray version problem bug ### Your current environment ray= 2.10.0 ### 🐛 Describe the bug New additions in #5748 from ray.exceptions import ActorDiedError, but only in ray>=2.11.0, Now ray =2.9 in the requirements-...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: ctorDiedError, but only in ray>=2.11.0, Now ray =2.9 in the requirements-cuda.txt file, loading the model will fail after the source code is compiled development distributed_parallel;model_support cuda #5748 [Core] Add...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: ray>=2.11.0, Now ray =2.9 in the requirements-cuda.txt file, loading the model will fail after the source code is compiled development distributed_parallel;model_support cuda #5748 [Core] Add fault tolerance for `RayTok...

## 关联 PR 证据

| PR | 链接类型 | 置信度 | PR 标题 | 证据 |
| --- | --- | ---: | --- | --- |
| [#5748](https://github.com/vllm-project/vllm/pull/5748) | mentioned | 0.45 | [Core] Add fault tolerance for `RayTokenizerGroupPool` | nt environment ray= 2.10.0 ### 🐛 describe the bug new additions in #5748 from ray.exceptions import actordiederror, but only in ray>=2.11.0, now ray =2.9 in the requirements-cuda.… |

## Wiki 抽取状态

- 后续迭代应在可用时读取完整讨论评论。
