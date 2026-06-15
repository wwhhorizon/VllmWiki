# vllm-project/vllm#20664: [Installation]: verl + editable vllm installation does not work

| 字段 | 值 |
| --- | --- |
| Issue | [#20664](https://github.com/vllm-project/vllm/issues/20664) |
| 状态 | closed |
| 标签 | installation;rl |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Installation]: verl + editable vllm installation does not work

### Issue 正文摘录

### Your current environment ```text The output of `python collect_env.py` ``` ### How you are installing vllm ```sh git clone git@github.com:vllm-project/vllm.git cd vllm pip install -e . ``` Now check the `vllm/_version.py`, the version always remains 0.1 ``` __version__ = version = '0.1.dev7557+g977180c' __version_tuple__ = version_tuple = (0, 1, 'dev7557', 'g977180c') ``` This will cause a problem with some third party libraries such as [verl](https://github.com/volcengine/verl/blob/cccc2ef2c94e747578b75b58eb69625a0dd2f9bf/verl/third_party/vllm/__init__.py#L44) Wondering how this is controlled? Possible to increment this to be latest released version? ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: [Installation]: verl + editable vllm installation does not work installation;rl ### Your current environment ```text The output of `python collect_env.py` ``` ### How you are installing vllm ```sh git clone git@github.
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: on? ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: 4) Wondering how this is controlled? Possible to increment this to be latest released version? ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
