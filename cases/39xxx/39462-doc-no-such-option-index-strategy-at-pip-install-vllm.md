# vllm-project/vllm#39462: [Doc]: no such option: --index-strategy at pip install vllm

| 字段 | 值 |
| --- | --- |
| Issue | [#39462](https://github.com/vllm-project/vllm/issues/39462) |
| 状态 | open |
| 标签 | documentation |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |
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

> [Doc]: no such option: --index-strategy at pip install vllm

### Issue 正文摘录

### 📚 The doc issue I looked at Quickstart and executed the command. https://vllm.ai/ There is no option called --index-strategy in Python3.12. I looked for an option with a similar name starting with index, but it doesn't seem to be there. Which option should I specify? By the way, Do you support CUDA 13.1 and 13.2? ``` (.venv) $ pip install vllm --extra-index-url https://wheels.vllm.ai/0.19.0/cu130 --extra-index-url https://download.pytorch.org/whl/cu130 --index-strategy unsafe-best-match Usage: pip install [options] [package-index-options] ... pip install [options] -r [package-index-options] ... pip install [options] [-e] ... pip install [options] [-e] ... pip install [options] ... no such option: --index-strategy ``` ### Suggest a potential alternative/fix I can't think of an alternative, but I think the only way is to make pip install vllm without options with CUDA 13.1 and 13.2. ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 现有链接修复摘要

#39467 [Doc] Add pip equivalent for CUDA-specific wheel installation

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: [Doc]: no such option: --index-strategy at pip install vllm documentation ### 📚 The doc issue I looked at Quickstart and executed the command. https://vllm.ai/ There is no option called --index-strategy in Python3.12. I...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: to be there. Which option should I specify? By the way, Do you support CUDA 13.1 and 13.2? ``` (.venv) $ pip install vllm --extra-index-url https://wheels.vllm.ai/0.19.0/cu130 --extra-index-url https://download.pytorch....
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions. development ci_build cuda #39467 [Doc] Add pip equivalent for CUDA-specific wheel ins...

## 关联 PR 证据

| PR | 链接类型 | 置信度 | PR 标题 | 证据 |
| --- | --- | ---: | --- | --- |
| [#39467](https://github.com/vllm-project/vllm/pull/39467) | mentioned | 0.6 | [Doc] Add pip equivalent for CUDA-specific wheel installation | ## Testing Documentation-only change. No code changes. Relates to #39462 |

## Wiki 抽取状态

- 后续迭代应在可用时读取完整讨论评论。
