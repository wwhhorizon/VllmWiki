# vllm-project/vllm#5086: [Installation]: Error when importing LLM from vllm

| 字段 | 值 |
| --- | --- |
| Issue | [#5086](https://github.com/vllm-project/vllm/issues/5086) |
| 状态 | closed |
| 标签 | installation;stale |
| 评论 | 19; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | development |
| 工作域 | ci_build |
| 子分类 | env_compat |
| Operator 关键词 | cuda |
| 症状 | import_error |
| 根因提示 | env_dependency |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Installation]: Error when importing LLM from vllm

### Issue 正文摘录

### My current environment i am using linux system, rtx 4080, cuda version: 12.1, python version - 3.9 ``` from vllm import LLM ImportError: cannot import name 'LLM' from 'vllm' (unknown location) ``` ### How you are installing vllm ```sh pip install vllm ```

## 现有链接修复摘要

#14891 [Kernel] vLLM Windows CUDA support

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 6: [Installation]: Error when importing LLM from vllm installation;stale ### My current environment i am using linux system, rtx 4080, cuda version: 12.1, python version - 3.9 ``` from vllm import LLM ImportError: cannot
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: m installation;stale ### My current environment i am using linux system, rtx 4080, cuda version: 12.1, python version - 3.9 ``` from vllm import LLM ImportError: cannot import name 'LLM' from 'vllm' (unknown location) `...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: [Installation]: Error when importing LLM from vllm installation;stale ### My current environment i am using linux system, rtx 4080, cuda version: 12.1, python version - 3.9 ``` from vllm import LLM ImportError: cannot i...

## 关联 PR 证据

| PR | 链接类型 | 置信度 | PR 标题 | 证据 |
| --- | --- | ---: | --- | --- |
| [#14891](https://github.com/vllm-project/vllm/pull/14891) | closes_keyword | 0.95 | [Kernel] vLLM Windows CUDA support | FIX #5086 FIX #5631 FIX #1685 FIX #179 FIX #2309 |

## Wiki 抽取状态

- 后续迭代应在可用时读取完整讨论评论。
