# vllm-project/vllm#9586: [Usage]:Quality issues with the internvl2-8b-vllm-server 

| 字段 | 值 |
| --- | --- |
| Issue | [#9586](https://github.com/vllm-project/vllm/issues/9586) |
| 状态 | closed |
| 标签 | usage |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Usage]:Quality issues with the internvl2-8b-vllm-server 

### Issue 正文摘录

### Your current environment ```text The output of `python collect_env.py` ``` ### How would you like to use vllm I want to run inference of a [specific model](put link here). I don't know how to integrate it with vllm. I started an interpl2-8b service using VLLM on a10 GPU for summarizing image information, but encountered the following problem: 1. The output quality of the service is poor, accompanied by irrelevant content, garbled content, and mixed Chinese and English output 2. If the max tokens parameter is set, the instruction following ability of the model deteriorates. For example, if max tokens is set to 512 and the instruction prompt outputs 30 words, the model will still output long text I don't know if these issues are due to problems with the way my service is started or the support of the VLLM framework for this model. My command is as follows: python - m VLLM. entrypoints. openai. api_user -- model/ internvl2-8b --dtype auto --tensor-parallel-size 1 --max-model-len 8096 --served-model-name internvl2-8b --trust-remote-code ### Before submitting a new issue... - [X] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right co...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: [Usage]:Quality issues with the internvl2-8b-vllm-server usage ### Your current environment ```text The output of `python collect_env.py` ``` ### How would you like to use vllm I want to run inference of a [specific mod...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: `` ### How would you like to use vllm I want to run inference of a [specific model](put link here). I don't know how to integrate it with vllm. I started an interpl2-8b service using VLLM on a10 GPU for summarizing imag...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 1: python - m VLLM. entrypoints. openai. api_user -- model/ internvl2-8b --dtype auto --tensor-parallel-size 1 --max-model-len 8096 --served-model-name internvl2-8b --trust-remote-code ### Before submitting a new issue......
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: ode ### Before submitting a new issue... - [X] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
