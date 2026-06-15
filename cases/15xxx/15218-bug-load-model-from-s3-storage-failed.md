# vllm-project/vllm#15218: [Bug]: load model from s3 storage failed

| 字段 | 值 |
| --- | --- |
| Issue | [#15218](https://github.com/vllm-project/vllm/issues/15218) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 4; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | development |
| 工作域 | ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;quantization;sampling_logits;speculative_decoding |
| 子分类 | env_compat |
| Operator 关键词 | cuda;operator;quantization;sampling;triton |
| 症状 | build_error |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: load model from s3 storage failed

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug I want to load model from s3 storage, the model stored in the s3 bucket is as following: ![Image](https://github.com/user-attachments/assets/d7cae8bb-b6a3-498f-8709-81f6ec538b20) the demo code is: ```python import json from vllm import LLM, SamplingParams prompts = [ "Hello, my name is", "The future of AI is", ] sampling_params = SamplingParams(temperature=0.8, top_p=0.95) bucket_name="mynewbucket" llm = LLM( model=f"s3://{bucket_name}/Qwen2.5-7B-Instruct" ) outputs = llm.generate(prompts, sampling_params) # Print the outputs. for output in outputs: prompt = output.prompt generated_text = output.outputs[0].text print(f"Prompt: {prompt!r}, Generated text: {generated_text!r}") ``` ![Image](https://github.com/user-attachments/assets/4191272e-b9fa-4b6d-88e8-c8930c118cf2) ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: ssets/d7cae8bb-b6a3-498f-8709-81f6ec538b20) the demo code is: ```python import json from vllm import LLM, SamplingParams prompts = [ "Hello, my name is", "The future of AI is", ] sampling_params = SamplingParams(tempera...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: f2) ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: [Bug]: load model from s3 storage failed bug;stale ### Your current environment ### 🐛 Describe the bug I want to load model from s3 storage, the model stored in the s3 bucket is as following: ![Image](https://github.com...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: [Bug]: load model from s3 storage failed bug;stale ### Your current environment ### 🐛 Describe the bug I want to load model from s3 storage, the model stored in the s3 bucket is as following: ![Image](https://github.com...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: sampling_logits;speculative_decoding cuda;operator;quantization;sampling;triton build_error env_dependency Your current environment

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
