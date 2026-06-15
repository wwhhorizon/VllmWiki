# vllm-project/vllm#476: Installation errors

| 字段 | 值 |
| --- | --- |
| Issue | [#476](https://github.com/vllm-project/vllm/issues/476) |
| 状态 | closed |
| 标签 |  |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |
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

> Installation errors

### Issue 正文摘录

I'm seriously struggling with installing this package, i have tried the pip install, and docker as well. I'm getting wheel errors all the time. I have downgraded cuda to 11.8, and python version is 3.10. Why is the installation so hard? is it something you guys are working on? You have such a wonderful product, i hope the installation will be smooth in the future.

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 7: Installation errors I'm seriously struggling with installing this package, i have tried the pip install, and docker as well. I'm getting wheel errors all the time. I have downgraded cuda to 11.8, and python version is 3
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: ocker as well. I'm getting wheel errors all the time. I have downgraded cuda to 11.8, and python version is 3.10. Why is the installation so hard? is it something you guys are working on? You have such a wonderful produ...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
