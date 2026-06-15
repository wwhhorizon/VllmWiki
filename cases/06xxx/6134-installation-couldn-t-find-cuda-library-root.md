# vllm-project/vllm#6134: [Installation]: Couldn't find CUDA library root.

| 字段 | 值 |
| --- | --- |
| Issue | [#6134](https://github.com/vllm-project/vllm/issues/6134) |
| 状态 | closed |
| 标签 | installation;stale |
| 评论 | 5; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | development |
| 工作域 | ci_build |
| 子分类 | install |
| Operator 关键词 | cuda |
| 症状 |  |
| 根因提示 | env_dependency |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Installation]: Couldn't find CUDA library root.

### Issue 正文摘录

### Your current environment ```text The output of `python collect_env.py` ``` ### How you are installing vllm I install vLLM using Souce code. ```python pip install -e . ``` but encounter an error: Couldn't find CUDA library root. which is likely caused by the cuda environment.

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: [Installation]: Couldn't find CUDA library root. installation;stale ### Your current environment ```text The output of `python collect_env.py` ``` ### How you are installing vllm I install vLLM using Souce code. ```py
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: [Installation]: Couldn't find CUDA library root. installation;stale ### Your current environment ```text The output of `python collect_env.py` ``` ### How you are installing vllm I install vLLM using Souce code. ```pyth...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: [Installation]: Couldn't find CUDA library root. installation;stale ### Your current environment ```text The output of `python collect_env.py` ``` ### How you are installing vllm I install vLLM using Souce code. ```pyth...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
