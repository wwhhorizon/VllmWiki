# vllm-project/vllm#1980: latest version requires cuda >= 12.1?

| 字段 | 值 |
| --- | --- |
| Issue | [#1980](https://github.com/vllm-project/vllm/issues/1980) |
| 状态 | closed |
| 标签 |  |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | development |
| 工作域 | ci_build |
| 子分类 | env_compat |
| Operator 关键词 | cuda |
| 症状 | build_error |
| 根因提示 | env_dependency |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> latest version requires cuda >= 12.1?

### Issue 正文摘录

I have a problem getting the garbage outputs with version >= 0.2.2, but works fine with lower version e.g. 0.2.1.post1. Could it be related to cuda version? mine is 11.8. I also have a try with cu118 version, or build from source, but didn't work.

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: latest version requires cuda >= 12.1? I have a problem getting the garbage outputs with version >= 0.2.2, but works fine with lower version e.g. 0.2.1.post1. Could it be related to cuda version? mine is 11.8. I also hav...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: latest version requires cuda >= 12.1? I have a problem getting the garbage outputs with version >= 0.2.2, but works fine with lower version e.g. 0.2.1.post1. Could it be related to cuda version? mine is 11.8. I also hav...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: latest version requires cuda >= 12.1? I have a problem getting the garbage outputs with version >= 0.2.2, but works fine with lower version e.g. 0.2.1.post1. Could it be related to cuda version? mine is 11.8. I also hav...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
