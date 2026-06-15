# vllm-project/vllm#12977: [RFC]: copy pynvml code into vllm codebase

| 字段 | 值 |
| --- | --- |
| Issue | [#12977](https://github.com/vllm-project/vllm/issues/12977) |
| 状态 | closed |
| 标签 | RFC |
| 评论 | 4; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | development |
| 工作域 | distributed_parallel |
| 子分类 | install |
| Operator 关键词 | cuda |
| 症状 |  |
| 根因提示 | env_dependency |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [RFC]: copy pynvml code into vllm codebase

### Issue 正文摘录

### Motivation. We have suffered a lot from the module `pynvml` recently, see https://github.com/vllm-project/vllm/issues/12847 for example. libnvml.so is the library behind nvidia-smi, and pynvml is a Python wrapper around it. We use it to get GPU status without initializing CUDA context in the current process. Historically, there are two packages that provide a module named `pynvml`: - `nvidia-ml-py` (https://pypi.org/project/nvidia-ml-py/): The official wrapper. It is a dependency of vLLM, and is installed when users install vLLM. It provides a Python module named `pynvml`. - `pynvml` (https://pypi.org/project/pynvml/): An unofficial wrapper. Prior to version 12.0, it also provides a Python module `pynvml`, and therefore conflicts with the official one. What's worse, the module is a Python package, and has higher priority than the official one which is a standalone Python file. This causes errors when both of them are installed. Starting from version 12.0, it migrates to a new module named `pynvml_utils` to avoid the conflict. To make vLLM work, we have to make sure, there's no `pynvml` package, or the `pynvml` package has version 12.0 or higher. However, neither of them is a d...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 6: vml`: - `nvidia-ml-py` (https://pypi.org/project/nvidia-ml-py/): The official wrapper. It is a dependency of vLLM, and is installed when users install vLLM. It provides a Python module named `pynvml`. - `pynvml` (https:...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: /vllm/issues/12847 for example. libnvml.so is the library behind nvidia-smi, and pynvml is a Python wrapper around it. We use it to get GPU status without initializing CUDA context in the current process. Historically,...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions. development distributed_parallel cuda env_dependency Motivation.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
