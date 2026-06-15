# vllm-project/vllm#3786: [Feature]: cuda12.2 support 

| 字段 | 值 |
| --- | --- |
| Issue | [#3786](https://github.com/vllm-project/vllm/issues/3786) |
| 状态 | closed |
| 标签 | feature request |
| 评论 | 17; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | development |
| 工作域 | ci_build;frontend_api |
| 子分类 | install |
| Operator 关键词 | cuda |
| 症状 | build_error |
| 根因提示 | env_dependency |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Feature]: cuda12.2 support 

### Issue 正文摘录

### 🚀 The feature, motivation and pitch I use docker image based on `nvcr.io/nvidia/pytorch:23.10-py3` - Python 3.10 - cuda 12.2.2 - torch 2.1.0a0+32f93b1 after upgrade vllm to 0.4.0 from 0.3.3, vllm raise error. (0.3.3 works on same base image) Are there any plans to provide build packages for cuda12.2 ? ### Alternatives Build and install from source, it works. ### Additional context _No response_

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 5: support feature request ### 🚀 The feature, motivation and pitch I use docker image based on `nvcr.io/nvidia/pytorch:23.10-py3` - Python 3.10 - cuda 12.2.2 - torch 2.1.0a0+32f93b1 after upgrade vllm to 0.4.0 from 0.3.3,...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: [Feature]: cuda12.2 support feature request ### 🚀 The feature, motivation and pitch I use docker image based on `nvcr.io/nvidia/pytorch:23.10-py3` - Python 3.10 - cuda 12.2.2 - torch 2.1.0a0+32f93b1 after upgrade vllm t...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: [Feature]: cuda12.2 support feature request ### 🚀 The feature, motivation and pitch I use docker image based on `nvcr.io/nvidia/pytorch:23.10-py3` - Python 3.10 - cuda 12.2.2 - torch 2.1.0a0+32f93b1 after upgrade vllm t...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
