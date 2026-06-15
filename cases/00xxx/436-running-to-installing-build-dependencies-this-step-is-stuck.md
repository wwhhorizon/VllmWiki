# vllm-project/vllm#436: Running to (Installing build dependencies ) this step is stuck

| 字段 | 值 |
| --- | --- |
| Issue | [#436](https://github.com/vllm-project/vllm/issues/436) |
| 状态 | closed |
| 标签 | installation |
| 评论 | 5; 本地原始数据只有评论数量，没有评论正文 |
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

> Running to (Installing build dependencies ) this step is stuck

### Issue 正文摘录

![image](https://github.com/vllm-project/vllm/assets/54533917/99997cfa-f6f6-4de1-9641-0e4c90884256) system： ubuntu 20.04 Nvidia driver 515 cuda 11.7 rtx3090 python 3.8 vllm 0.1.2

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: Running to (Installing build dependencies ) this step is stuck installation ![image](https://github.com/vllm-project/vllm/assets/54533917/99997cfa-f6f6-4de1-9641-0e4c90884256) system： ubuntu 20.04 Nvidia driver 515 cuda...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: cfa-f6f6-4de1-9641-0e4c90884256) system： ubuntu 20.04 Nvidia driver 515 cuda 11.7 rtx3090 python 3.8 vllm 0.1.2 development ci_build cuda build_error env_dependency ![image](https://github.com/vllm-project/vllm/assets/5...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
