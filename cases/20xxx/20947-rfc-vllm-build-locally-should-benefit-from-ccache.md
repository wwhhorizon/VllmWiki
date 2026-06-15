# vllm-project/vllm#20947: [RFC]: vLLM build locally should benefit from ccache

| 字段 | 值 |
| --- | --- |
| Issue | [#20947](https://github.com/vllm-project/vllm/issues/20947) |
| 状态 | closed |
| 标签 | RFC |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [RFC]: vLLM build locally should benefit from ccache

### Issue 正文摘录

### Motivation. ccache is a compiler cache that lets you build things faster locally, especially if you build the same things often. Each build of vLLM takes me 20 minutes; I probably built vLLM 10s of times in the last week. My local vLLM builds don't work with ccache; they do not cache hit. I don't know why. The going hypothesis is that `pip install -e . --no-build-isolation` picks a random tmp directory to build artifacts, and this causes ccache to cache miss. ### Proposed Change. I think we have two options. #### Option 1: Go back to python setup.py develop The default build instructions for vLLM recommends `pip install -e .` However, it looks like vLLM used to use `python setup.py install`/`python setup.py develop`. These commands both work with ccache for me; I experimented with the following: ``` python setup.py develop python setup.py clean ccache --zero-stats python setup.py develop ccache -s ``` resulting in a lot of cache hits: ``` Summary: Hits: 323 / 345 (93.62 %) Direct: 321 / 345 (93.04 %) Preprocessed: 2 / 24 (8.33 %) Misses: 22 Direct: 24 Preprocessed: 22 Uncacheable: 70 Primary storage: Hits: 644 / 690 (93.33 %) Misses: 46 Cache size (GB): 45.66 / 50.00 (91.31 %)...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: [RFC]: vLLM build locally should benefit from ccache RFC ### Motivation. ccache is a compiler cache that lets you build things faster locally, especially if you build the same things often. Each build of vLLM takes me 2...
- [Bitwise 确定性与数值等价](../patterns/bitwise_determinism_equivalence.md) - 分数 2: he last week. My local vLLM builds don't work with ccache; they do not cache hit. I don't know why. The going hypothesis is that `pip install -e . --no-build-isolation` picks a random tmp directory to build artifacts, a...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: you ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
