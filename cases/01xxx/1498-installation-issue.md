# vllm-project/vllm#1498: Installation Issue

| 字段 | 值 |
| --- | --- |
| Issue | [#1498](https://github.com/vllm-project/vllm/issues/1498) |
| 状态 | closed |
| 标签 |  |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | development |
| 工作域 | ci_build |
| 子分类 | env_compat |
| Operator 关键词 | cuda |
| 症状 |  |
| 根因提示 | env_dependency |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> Installation Issue

### Issue 正文摘录

How to install in ubuntu 22.04, cuda 11.8, torch 2.1.0+cu118 python 3.10? I found that `pip install vllm` will re-install torch-2.01 and update cuda version. How to install vllm, but based on my cuda env? thanks in advance!!!

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 5: Installation Issue How to install in ubuntu 22.04, cuda 11.8, torch 2.1.0+cu118 python 3.10? I found that `pip install vllm` will re-install torch-2.01 and update cuda version. How to install vllm, but based on my cuda
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: Installation Issue How to install in ubuntu 22.04, cuda 11.8, torch 2.1.0+cu118 python 3.10? I found that `pip install vllm` will re-install torch-2.01 and update cuda version. How to install vllm, but based on my cuda...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
