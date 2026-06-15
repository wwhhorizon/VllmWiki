# vllm-project/vllm#8186: [Bug]: Phi-3.5-MoE-Instruct on vLLM produces weird strings

| 字段 | 值 |
| --- | --- |
| Issue | [#8186](https://github.com/vllm-project/vllm/issues/8186) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 4; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | development |
| 工作域 | ci_build;distributed_parallel;hardware_porting;model_support;moe;sampling_logits;speculative_decoding |
| 子分类 | env_compat |
| Operator 关键词 | cuda;moe;operator;sampling;triton |
| 症状 | build_error |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | True |

## 源证据

### Issue 标题

> [Bug]: Phi-3.5-MoE-Instruct on vLLM produces weird strings

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug Hello, Phi-3.5-MoE-Instruct on vLLM produces weird strings. There is [a similar report in the comment of #7729](https://github.com/vllm-project/vllm/pull/7729#issuecomment-2326436109). Here is an example code to reproduce this issue: ```python from vllm import LLM, SamplingParams prompts = [" \nHello. Who are you? \n \n"] sampling_params = SamplingParams(temperature=0.5, top_p=1.0) llm = LLM( model="microsoft/Phi-3.5-MoE-instruct", dtype="bfloat16", trust_remote_code=True, tensor_parallel_size=8, ) outputs = llm.generate(prompts, sampling_params) for output in outputs: print(f"generated: {output.outputs[0].text}") ``` Here is the output of above code: ``` generated: or the or to and and the a and in a, and and,, ``` ### Before submitting a new issue... - [X] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 现有链接修复摘要

#7729 [Model] Adding support for MSFT Phi-3.5-MoE

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: 9). Here is an example code to reproduce this issue: ```python from vllm import LLM, SamplingParams prompts = [" \nHello. Who are you? \n \n"] sampling_params = SamplingParams(temperature=0.5, top_p=1.0) llm = LLM( mode...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 3: , top_p=1.0) llm = LLM( model="microsoft/Phi-3.5-MoE-instruct", dtype="bfloat16", trust_remote_code=True, tensor_parallel_size=8, ) outputs = llm.generate(prompts, sampling_params) for output in outputs: print(f"generat...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: ``` ### Before submitting a new issue... - [X] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: port;moe;sampling_logits;speculative_decoding cuda;moe;operator;sampling;triton build_error dtype;env_dependency #7729 [Model] Adding support for MSFT Phi-3.5-MoE Your current environment
- [Bitwise 确定性与数值等价](../patterns/bitwise_determinism_equivalence.md) - 分数 1: ject/vllm/pull/7729#issuecomment-2326436109). Here is an example code to reproduce this issue: ```python from vllm import LLM, SamplingParams prompts = [" \nHello. Who are you? \n \n"] sampling_params = SamplingParams(t...

## 关联 PR 证据

| PR | 链接类型 | 置信度 | PR 标题 | 证据 |
| --- | --- | ---: | --- | --- |
| [#7729](https://github.com/vllm-project/vllm/pull/7729) | mentioned | 0.45 | [Model] Adding support for MSFT Phi-3.5-MoE | produces weird strings. there is [a similar report in the comment of #7729](https://github.com/vllm-project/vllm/pull/7729#issuecomment-2326436109). here is an example code to rep… |

## Wiki 抽取状态

- 后续迭代应在可用时读取完整讨论评论。
