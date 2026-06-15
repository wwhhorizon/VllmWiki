# vllm-project/vllm#41637: [Installation]: RIXL not available

| 字段 | 值 |
| --- | --- |
| Issue | [#41637](https://github.com/vllm-project/vllm/issues/41637) |
| 状态 | closed |
| 标签 | installation |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Installation]: RIXL not available

### Issue 正文摘录

### Your current environment ```text The output of `python collect_env.py` ``` ### How you are installing vllm ```sh docker pull vllm/vllm-openai-rocm:v0.20.1 ``` I want to run PD disaggregation on AMD with NixlConnector, but RIXL is not shipped with the official vllm-openai-rocm image: ```bash $ docker run --rm --entrypoint python3 vllm/vllm-openai-rocm:v0.20.1 -c "from rixl._api import nixl_agent; print('RIXL OK')" Traceback (most recent call last): File " ", line 1, in ModuleNotFoundError: No module named 'rixl' ``` Would be great to understand if we can make the behavior more similar to MoRI that's not shipped OOB with the image. This would make adoption easier. In contrast, on NV NIXL is included OOB: ```shell $ docker run --rm --entrypoint python3 vllm/vllm-openai:v0.20.1 -c "from nixl._api import nixl_agent; print('NIXL OK')" NIXL OK ``` ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: [Installation]: RIXL not available installation ### Your current environment ```text The output of `python collect_env.py` ``` ### How you are installing vllm ```sh docker pull vllm/vllm-openai-rocm:v0.20.1 ``` I want
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: ``` ### How you are installing vllm ```sh docker pull vllm/vllm-openai-rocm:v0.20.1 ``` I want to run PD disaggregation on AMD with NixlConnector, but RIXL is not shipped with the official vllm-openai-rocm image: ```bas...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
