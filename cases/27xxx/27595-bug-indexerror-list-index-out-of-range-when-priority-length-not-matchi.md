# vllm-project/vllm#27595: [Bug]: IndexError: list index out of range when priority length not matching length of prompts in LLM class

| 字段 | 值 |
| --- | --- |
| Issue | [#27595](https://github.com/vllm-project/vllm/issues/27595) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 0; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | development |
| 工作域 | distributed_parallel;model_support;sampling_logits |
| 子分类 | debug |
| Operator 关键词 | cuda;sampling |
| 症状 | crash |
| 根因提示 | env_dependency |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: IndexError: list index out of range when priority length not matching length of prompts in LLM class

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug Checked with chatbot that there is no issue or PR related to this. In the code at [llm.py#L1591](https://github.com/vllm-project/vllm/blob/main/vllm/entrypoints/llm.py#L1591), there is no explicit validation to ensure that the `priority` list matches the length of prompts. This could lead to unsafe behavior if their lengths differ. The code only checks lengths for `params` and `lora_request`, not for `priority`. ```python from vllm import LLM, SamplingParams prompts = [ "Hello, my name is", "The president of the United States is", "The capital of France is", "The future of AI is", ] sampling_params = SamplingParams(temperature=0.8, top_p=0.95) llm = LLM(model="facebook/opt-125m") outputs = llm.generate(prompts, sampling_params, priority=[0, 0, 0]) # Print the outputs. for output in outputs: prompt = output.prompt generated_text = output.outputs[0].text print(f"Prompt: {prompt!r}, Generated text: {generated_text!r}") ``` Output ``` Traceback (most recent call last): File "/home/ec2-user/inference_playground/vllm/bug.py", line 10, in outputs = llm.generate(promtps, priority=[0, 0, 0]) ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ File...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: -project/vllm/blob/main/vllm/entrypoints/llm.py#L1591), there is no explicit validation to ensure that the `priority` list matches the length of prompts. This could lead to unsafe behavior if their lengths differ. The c...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: ``` ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 1: 591, in _validate_and_add_requests priority=priority[i] if priority else 0, ~~~~~~~~^^^ IndexError: list index out of range ``` ### Before submitting a new issue... - [x] Make sure you already searched for relevant issu...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: sampling_params = SamplingParams(temperature=0.8, top_p=0.95) llm = LLM(model="facebook/opt-125m") outputs = llm.generate(prompts, sampling_params, priority=[0, 0, 0]) # Print the outputs. for output in outputs: prompt...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: heir lengths differ. The code only checks lengths for `params` and `lora_request`, not for `priority`. ```python from vllm import LLM, SamplingParams prompts = [ "Hello, my name is", "The president of the United States...

## Wiki 抽取状态

- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
