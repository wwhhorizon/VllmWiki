# vllm-project/vllm#695: Request for creation of a wheel for vllm

| 字段 | 值 |
| --- | --- |
| Issue | [#695](https://github.com/vllm-project/vllm/issues/695) |
| 状态 | closed |
| 标签 |  |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |
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

> Request for creation of a wheel for vllm

### Issue 正文摘录

Hi vllm team, We are looking to use vllm. One of the issues we are facing is that pip install for the project fails if CUDA is not installed on the build host. Can we have a wheel for vllm ? From the installation page I understand that "vLLM is a Python library that also contains some C++ and CUDA code. This additional code requires compilation on the user’s machine.". But can we not have platform specific wheels like for CentOS, macOS etc ? Looking forward to hear from you. Thanks, Dhritiman

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 5: Request for creation of a wheel for vllm Hi vllm team, We are looking to use vllm. One of the issues we are facing is that pip install for the project fails if CUDA is not installed on the build host. Can we have a whee...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: of the issues we are facing is that pip install for the project fails if CUDA is not installed on the build host. Can we have a wheel for vllm ? From the installation page I understand that "vLLM is a Python library tha...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: Request for creation of a wheel for vllm Hi vllm team, We are looking to use vllm. One of the issues we are facing is that pip install for the project fails if CUDA is not installed on the build host. Can we have a whee

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
