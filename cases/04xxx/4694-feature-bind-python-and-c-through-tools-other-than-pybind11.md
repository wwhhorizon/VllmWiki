# vllm-project/vllm#4694: [Feature]: bind python and c++ through tools other than pybind11

| 字段 | 值 |
| --- | --- |
| Issue | [#4694](https://github.com/vllm-project/vllm/issues/4694) |
| 状态 | closed |
| 标签 | help wanted;feature request;stale |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Feature]: bind python and c++ through tools other than pybind11

### Issue 正文摘录

### 🚀 The feature, motivation and pitch As vLLM goes into a fast release schedule (currently one release every two weeks), we will quickly hit the project-wide limit of pypi (around 5GB per project). One solution, as pointed out in https://github.com/pypi/support/issues/3792#issuecomment-2099941677 , is to build one wheel for all python versions (Python 3.8+). I have figured out the procedure https://github.com/pypi/support/issues/3792#issuecomment-2101360740 , but pybind11 does not support this Python Limited API protocol. One possible solution is to replace pybind11 with some other tools, so that the binding procedure can be used with Python Limited API. Possible solutions: - Nanobind (seems to support it starting from Python 3.12 only: https://github.com/wjakob/nanobind/pull/561 ) - register ops through pytorch directly https://pytorch.org/tutorials/advanced/torch_script_custom_ops.html ### Alternatives _No response_ ### Additional context _No response_

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: ps://github.com/pypi/support/issues/3792#issuecomment-2099941677 , is to build one wheel for all python versions (Python 3.8+). I have figured out the procedure https://github.com/pypi/support/issues/3792#issuecomment-2...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: ind python and c++ through tools other than pybind11 help wanted;feature request;stale ### 🚀 The feature, motivation and pitch As vLLM goes into a fast release schedule (currently one release every two weeks), we will q...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
