# vllm-project/vllm#9918: [Bug]: illegal memory access error when using prefix caching

| 字段 | 值 |
| --- | --- |
| Issue | [#9918](https://github.com/vllm-project/vllm/issues/9918) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 7; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;quantization;sampling_logits;speculative_decoding |
| 子分类 |  |
| Operator 关键词 | cuda;operator;quantization;triton |
| 症状 | build_error |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: illegal memory access error when using prefix caching

### Issue 正文摘录

### Your current environment ### Model Input Dumps _No response_ ### 🐛 Describe the bug As discussed in https://github.com/vllm-project/vllm/pull/9532, setting `enable_prefix_caching=True` leads to illegal memory access error when using 8 H100 GPUs. This is the code to reproduce the error: ```python import torch from vllm import LLM, SamplingParams sampling_params = SamplingParams(temperature=0, max_tokens=8192, seed=1234) llm = LLM(model='Qwen/Qwen2.5-72B-Instruct', enable_prefix_caching=True, tensor_parallel_size=8, enable_chunked_prefill=False) prompts = torch.load('test.id') outputs = llm.generate(prompts, sampling_params=sampling_params, use_tqdm=False) ``` [test.id.zip](https://github.com/user-attachments/files/17600817/test.id.zip) Please unzip the file to get `test.id` ### Before submitting a new issue... - [X] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: n using 8 H100 GPUs. This is the code to reproduce the error: ```python import torch from vllm import LLM, SamplingParams sampling_params = SamplingParams(temperature=0, max_tokens=8192, seed=1234) llm = LLM(model='Qwen...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: e_prefix_caching=True` leads to illegal memory access error when using 8 H100 GPUs. This is the code to reproduce the error: ```python import torch from vllm import LLM, SamplingParams sampling_params = SamplingParams(t...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 3: [Bug]: illegal memory access error when using prefix caching bug;stale ### Your current environment ### Model Input Dumps _No response_ ### 🐛 Describe the bug As discussed in https://github.com/vllm-project/vllm/pull/95...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: when using prefix caching bug;stale ### Your current environment ### Model Input Dumps _No response_ ### 🐛 Describe the bug As discussed in https://github.com/vllm-project/vllm/pull/9532, setting `enable_prefix_caching=...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: tization;sampling_logits;speculative_decoding cuda;operator;quantization;triton build_error env_dependency Your current environment

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
