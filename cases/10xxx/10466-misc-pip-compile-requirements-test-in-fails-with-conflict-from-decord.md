# vllm-project/vllm#10466: [Misc]: `pip-compile requirements-test.in` fails with conflict from "decord"

| 字段 | 值 |
| --- | --- |
| Issue | [#10466](https://github.com/vllm-project/vllm/issues/10466) |
| 状态 | closed |
| 标签 |  |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Misc]: `pip-compile requirements-test.in` fails with conflict from "decord"

### Issue 正文摘录

### Anything you want to discuss about vllm. TL;DR: don't pip-compile on arm-chip macbook as of 2024Q4 ----------------------original post------------------- `decord` was introduced in #10020, now `pip-compile` is failing for both python3.9 and python3.12 with error ``` ERROR: Cannot install decord because these package versions have conflicting dependencies. Discarding decord==0.6.0 (from -r requirements-test.txt (line 96)) to proceed the resolution ERROR: Could not find a version that satisfies the requirement decord (from versions: none) ``` test python3.12 using mac (m3 pro) ``` conda create --name py312 -c conda-forge python=3.12 conda activate py312 pip install pip-tools pip-compile --output-file=requirements-test.txt requirements-test.in ``` cc @litianjian ### Before submitting a new issue... - [X] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: [Misc]: `pip-compile requirements-test.in` fails with conflict from "decord" ### Anything you want to discuss about vllm. TL;DR: don't pip-compile on arm-chip macbook as of 2024Q4 ----------------------original post----...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: ything you want to discuss about vllm. TL;DR: don't pip-compile on arm-chip macbook as of 2024Q4 ----------------------original post------------------- `decord` was introduced in #10020, now `pip-compile` is failing for...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: [Misc]: `pip-compile requirements-test.in` fails with conflict from "decord" ### Anything you want to discuss about vllm. TL;DR: don't pip-compile on arm-chip macbook as of 2024Q4 ----------------------original post----...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
