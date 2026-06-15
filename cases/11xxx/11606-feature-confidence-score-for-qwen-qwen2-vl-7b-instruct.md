# vllm-project/vllm#11606: [Feature]: Confidence score for Qwen/Qwen2-VL-7B-Instruct

| 字段 | 值 |
| --- | --- |
| Issue | [#11606](https://github.com/vllm-project/vllm/issues/11606) |
| 状态 | closed |
| 标签 | feature request;stale |
| 评论 | 16; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Feature]: Confidence score for Qwen/Qwen2-VL-7B-Instruct

### Issue 正文摘录

### 🚀 The feature, motivation and pitch I have served a model Qwen/Qwen2-VL-2B-Instruct using vLLM. I need to decode the confidence score for the model extracted output from the image using logprobs. Is that is possible for this model. Give me some ideas on this. I got empty list logprobs results so the confidence is 0 for the correct answers also. ### Alternatives Reference from Huggingface import vllm import torch import numpy as np from vllm import LLM, SamplingParams sampling_params = SamplingParams( logprobs=20, prompt_logprobs=20, ) llm = LLM(model='/root/huggingface/math-shepherd-mistral-7b-prm', dtype='float32', tensor_parallel_size=1, gpu_memory_utilization=0.9, max_model_len=4096) question = """Janet\u2019s ducks lay 16 eggs per day. She eats three for breakfast every morning and bakes muffins for her friends every day with four. She sells the remainder at the farmers' market daily for $2 per fresh duck egg. How much in dollars does she make every day at the farmers' market?""" output1 = """Step 1: Janet's ducks lay 16 eggs per day. ки\nStep 2: She eats three for breakfast every morning, so she has 16 - 3 = 13 eggs left. ки\nStep 3: She bakes muffins for her friends ever...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: [Feature]: Confidence score for Qwen/Qwen2-VL-7B-Instruct feature request;stale ### 🚀 The feature, motivation and pitch I have served a model Qwen/Qwen2-VL-2B-Instruct using vLLM. I need to decode the confidence score f...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 3: [Feature]: Confidence score for Qwen/Qwen2-VL-7B-Instruct feature request;stale ### 🚀 The feature, motivation and pitch I have served a model Qwen/Qwen2-VL-2B-Instruct using vLLM. I need to decode the confidence score f...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 2: 20, ) llm = LLM(model='/root/huggingface/math-shepherd-mistral-7b-prm', dtype='float32', tensor_parallel_size=1, gpu_memory_utilization=0.9, max_model_len=4096) question = """Janet\u2019s ducks lay 16 eggs per day. She...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: the correct answers also. ### Alternatives Reference from Huggingface import vllm import torch import numpy as np from vllm import LLM, SamplingParams sampling_params = SamplingParams( logprobs=20, prompt_logprobs=20, )...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: ces ### Before submitting a new issue... - [X] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
