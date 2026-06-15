# vllm-project/vllm#19473: 安装最新的vllm0.9.1，还需要额外安装 flash-attn 或者 vllm-flash-attn 吗

| 字段 | 值 |
| --- | --- |
| Issue | [#19473](https://github.com/vllm-project/vllm/issues/19473) |
| 状态 | closed |
| 标签 | usage |
| 评论 | 8; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> 安装最新的vllm0.9.1，还需要额外安装 flash-attn 或者 vllm-flash-attn 吗

### Issue 正文摘录

### Your current environment ```text The output of `python collect_env.py` ``` ### How would you like to use vllm 如题，安装之后 pip show vllm-flash-attn 没有输出，说明并没有自动安装 vllm-flash-attn。但如果我手动 pip install vllm-flash-attn，会导致我的torch从2.7降级到2.4 ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: 装之后 pip show vllm-flash-attn 没有输出，说明并没有自动安装 vllm-flash-attn。但如果我手动 pip install vllm-flash-attn，会导致我的torch从2.7降级到2.4 ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and aske...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: 2.4 ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
