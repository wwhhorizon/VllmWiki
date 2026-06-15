# vllm-project/vllm#8983: [Bug]: Distributed inference fails on certain multimodal models

| 字段 | 值 |
| --- | --- |
| Issue | [#8983](https://github.com/vllm-project/vllm/issues/8983) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;hardware_porting;model_support;multimodal_vlm;sampling_logits;speculative_decoding |
| 子分类 | shape_align |
| Operator 关键词 | cuda;operator;sampling;triton |
| 症状 | build_error;mismatch;nan_inf |
| 根因提示 | env_dependency;shape |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Distributed inference fails on certain multimodal models

### Issue 正文摘录

### Your current environment ### Model Input Dumps [err_execute_model_input_20240930-213352.pkl.zip](https://github.com/user-attachments/files/17198766/err_execute_model_input_20240930-213352.pkl.zip) ### 🐛 Describe the bug Sampel code: from vllm import LLM, SamplingParams llm = LLM(model="adept/fuyu-8b", tensor_parallel_size=4, pipeline_parallel_size=1) This sample code throws the following error on an instance with 4 A10G GPUs. RuntimeError: Error in model execution (input dumped to /tmp/err_execute_model_input_20240930-231823.pkl): shape mismatch: value tensor of shape [16128, 1024] cannot be broadcast to indexing result of shape [16128, 4096] ### Before submitting a new issue... - [X] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 现有链接修复摘要

#8986 [Bugfix] Fix Fuyu tensor parallel inference

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: 0240930-213352.pkl.zip) ### 🐛 Describe the bug Sampel code: from vllm import LLM, SamplingParams llm = LLM(model="adept/fuyu-8b", tensor_parallel_size=4, pipeline_parallel_size=1) This sample code throws the following e...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: put dumped to /tmp/err_execute_model_input_20240930-231823.pkl): shape mismatch: value tensor of shape [16128, 1024] cannot be broadcast to indexing result of shape [16128, 4096] ### Before submitting a new issue... - [...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: [Bug]: Distributed inference fails on certain multimodal models bug ### Your current environment ### Model Input Dumps [err_execute_model_input_20240930-213352.pkl.zip](https://github.com/user-attachments/files/17198766...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: ltimodal_vlm;sampling_logits;speculative_decoding cuda;operator;sampling;triton build_error;mismatch;nan_inf env_dependency;shape #8986 [Bugfix] Fix Fuyu tensor parallel inference Your current environment
- [Bitwise 确定性与数值等价](../patterns/bitwise_determinism_equivalence.md) - 分数 1: input dumped to /tmp/err_execute_model_input_20240930-231823.pkl): shape mismatch: value tensor of shape [16128, 1024] cannot be broadcast to indexing result of shape [16128, 4096] ### Before submitting a new issue... -...

## 关联 PR 证据

| PR | 链接类型 | 置信度 | PR 标题 | 证据 |
| --- | --- | ---: | --- | --- |
| [#8986](https://github.com/vllm-project/vllm/pull/8986) | closes_keyword | 0.95 | [Bugfix] Fix Fuyu tensor parallel inference | FIX #8983 (*link existing issues this PR will resolve*) **BEFORE SUBMITTING, PLEASE READ THE CHECKLIST BELOW AND FILL IN THE DESCRIPTION ABOVE** --- <details> <!-- inside |

## Wiki 抽取状态

- 后续迭代应在可用时读取完整讨论评论。
