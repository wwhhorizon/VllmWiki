# vllm-project/vllm#10883: [Installation]: Installation Issue: vLLM 0.6.3 with CUDA 11.8 for Python 3.8

| 字段 | 值 |
| --- | --- |
| Issue | [#10883](https://github.com/vllm-project/vllm/issues/10883) |
| 状态 | closed |
| 标签 | installation |
| 评论 | 0; 本地原始数据只有评论数量，没有评论正文 |
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

> [Installation]: Installation Issue: vLLM 0.6.3 with CUDA 11.8 for Python 3.8

### Issue 正文摘录

### Your current environment ```text The output of `python collect_env.py` ``` ### How you are installing vllm ```sh pip install -vvv vllm ``` ### Before submitting a new issue... - [X] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: [Installation]: Installation Issue: vLLM 0.6.3 with CUDA 11.8 for Python 3.8 installation ### Your current environment ```text The output of `python collect_env.py` ``` ### How you are installing vllm ```sh pip install
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: [Installation]: Installation Issue: vLLM 0.6.3 with CUDA 11.8 for Python 3.8 installation ### Your current environment ```text The output of `python collect_env.py` ``` ### How you are installing vllm ```sh pip install...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions. development ci_build cuda env_dependency Your current environment

## Wiki 抽取状态

- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
