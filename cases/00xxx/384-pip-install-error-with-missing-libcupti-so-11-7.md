# vllm-project/vllm#384: pip install error with missing libcupti.so.11.7

| 字段 | 值 |
| --- | --- |
| Issue | [#384](https://github.com/vllm-project/vllm/issues/384) |
| 状态 | closed |
| 标签 | installation |
| 评论 | 7; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | development |
| 工作域 | ci_build |
| 子分类 | install |
| Operator 关键词 | cuda |
| 症状 |  |
| 根因提示 |  |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> pip install error with missing libcupti.so.11.7

### Issue 正文摘录

Hi, My environment has cuda 11.8 (linux), but the pip installation gives the following error while building the wheel: `libcupti.so.11.7: cannot open shared object file: No such file or directory` It seems that the installation is looking for cuda 11.7 specifically for some reason. Any insight on this one? Many thanks

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: pip install error with missing libcupti.so.11.7 installation Hi, My environment has cuda 11.8 (linux), but the pip installation gives the following error while building the wheel: `libcupti.so.11.7: cannot open shared o...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: rror with missing libcupti.so.11.7 installation Hi, My environment has cuda 11.8 (linux), but the pip installation gives the following error while building the wheel: `libcupti.so.11.7: cannot open shared object file: N...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
