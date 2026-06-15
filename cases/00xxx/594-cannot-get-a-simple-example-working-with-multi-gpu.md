# vllm-project/vllm#594: Cannot get a simple example working with multi-GPU

| 字段 | 值 |
| --- | --- |
| Issue | [#594](https://github.com/vllm-project/vllm/issues/594) |
| 状态 | closed |
| 标签 | installation |
| 评论 | 9; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> Cannot get a simple example working with multi-GPU

### Issue 正文摘录

I was trying to do a simple example script: ``` from vllm import LLM llm = LLM("facebook/opt-13b", tensor_parallel_size=4) output = llm.generate("San Franciso is a") ``` I installed vllm and ray in a virtual env, on a g5.12xlarge instance. At first, I install vllm using `pip install vllm`, and got the same IPV6 error as in [this bug](https://github.com/vllm-project/vllm/issues/570). Then I tried to install from the repo using `pip install -e .` and had trouble importing LLM. >>> from vllm import LLM Traceback (most recent call last): File " ", line 1, in ImportError: cannot import name 'LLM' from 'vllm' (unknown location) Anyone knows why this happens?

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: Cannot get a simple example working with multi-GPU installation I was trying to do a simple example script: ``` from vllm import LLM llm = LLM("facebook/opt-13b", tensor_parallel_size=4) output = llm.generate("San Franc...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
