# vllm-project/vllm#17212: [Installation]: torch 2.6.0 unavailable for intel mac

| 字段 | 值 |
| --- | --- |
| Issue | [#17212](https://github.com/vllm-project/vllm/issues/17212) |
| 状态 | closed |
| 标签 | installation |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Installation]: torch 2.6.0 unavailable for intel mac

### Issue 正文摘录

### Your current environment ```text ModuleNotFoundError: No module named 'vllm.envs' ``` Probably because I cannot install vllm ### How you are installing vllm I am installing vllm on intel cpu using these steps in my pyenv ``` pip install --upgrade pip pip install "cmake>=3.26" wheel packaging ninja "setuptools-scm>=8" numpy pip install -v -r requirements/cpu.txt --extra-index-url https://download.pytorch.org/whl/cpu ``` Seems like torch 2.6.0+cpu / torch 2.6.0 is unavailable from the list of available versions. ``` ERROR: Could not find a version that satisfies the requirement torch==2.6.0 (from versions: 2.0.0, 2.0.1, 2.1.0, 2.1.1, 2.1.2, 2.2.0, 2.2.1, 2.2.2) ERROR: No matching distribution found for torch==2.6.0 ``` I am not sure how to install torch 2.6.0. I also tried installing it from the official pytorch website docs but it seems like no version is supported beyond 2.2.2. Not sure how to fix this or what version to use instead. Will appreciate any help! ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which ca...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 5: [Installation]: torch 2.6.0 unavailable for intel mac installation ### Your current environment ```text ModuleNotFoundError: No module named 'vllm.envs' ``` Probably because I cannot install vllm ### How you are install
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
