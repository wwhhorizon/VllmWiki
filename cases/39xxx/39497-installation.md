# vllm-project/vllm#39497: [Installation]:

| 字段 | 值 |
| --- | --- |
| Issue | [#39497](https://github.com/vllm-project/vllm/issues/39497) |
| 状态 | closed |
| 标签 | installation |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |
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

> [Installation]:

### Issue 正文摘录

### Your current environment ```text I can't run this, because i can't install vllm, lol. Just gonna say it's latest Fedora with python 3.14 ``` ### How you are installing vllm ```sh uv pip install -U vllm --pre --extra-index-url https://wheels.vllm.ai/nightly/cu130 --extra-index-url https://download.pytorch.org/whl/cu130 --index-strategy unsafe-best-match ``` Error occurs both on nightly, stable and cuda 12/13 builds. I didn't find any similar issues so decided to make a new one. [vllm.error.log](https://github.com/user-attachments/files/26631899/vllm.error.log) ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 5: [Installation]: installation ### Your current environment ```text I can't run this, because i can't install vllm, lol. Just gonna say it's latest Fedora with python 3.14 ``` ### How you are installing vllm ```sh uv pip
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: -strategy unsafe-best-match ``` Error occurs both on nightly, stable and cuda 12/13 builds. I didn't find any similar issues so decided to make a new one. [vllm.error.log](https://github.com/user-attachments/files/26631...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: can't run this, because i can't install vllm, lol. Just gonna say it's latest Fedora with python 3.14 ``` ### How you are installing vllm ```sh uv pip install -U vllm --pre --extra-index-url https://wheels.vllm.ai/night...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
