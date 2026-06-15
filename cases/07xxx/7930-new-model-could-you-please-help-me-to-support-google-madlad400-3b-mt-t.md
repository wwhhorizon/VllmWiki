# vllm-project/vllm#7930: [New Model]: Could you please help me to support google/madlad400-3b-mt translator model in vLLM?

| 字段 | 值 |
| --- | --- |
| Issue | [#7930](https://github.com/vllm-project/vllm/issues/7930) |
| 状态 | closed |
| 标签 | new-model;stale |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [New Model]: Could you please help me to support google/madlad400-3b-mt translator model in vLLM?

### Issue 正文摘录

### The model to consider. https://huggingface.co/google/madlad400-3b-mt ### The closest model vllm already supports. I was unable to find a model compatible with the Google model I want to implement for language translations. ### What's your difficulty of supporting the model you want? The architecture required to mount the model is T5ForConditionalGeneration and for Tokenizer is T5Tokenizer. This architecture is not listed among those supported in vLLM. The code I have implemented to mount the model and tokenizer is: from transformers import T5ForConditionalGeneration, T5Tokenizer import os import torch model = T5ForConditionalGeneration.from_pretrained(os.path.join(BASE_PATH,MODEL_NAME), torch_dtype=torch.bfloat16, device_map="auto") tokenizer = T5Tokenizer.from_pretrained(os.path.join(BASE_PATH,MODEL_NAME)) ### Before submitting a new issue... - [X] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 3: onalGeneration.from_pretrained(os.path.join(BASE_PATH,MODEL_NAME), torch_dtype=torch.bfloat16, device_map="auto") tokenizer = T5Tokenizer.from_pretrained(os.path.join(BASE_PATH,MODEL_NAME)) ### Before submitting a new i...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: [New Model]: Could you please help me to support google/madlad400-3b-mt translator model in vLLM? new-model;stale ### The model to consider. https://huggingface.co/google/madlad400-3b-mt ### The closest model vllm alrea...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: have implemented to mount the model and tokenizer is: from transformers import T5ForConditionalGeneration, T5Tokenizer import os import torch model = T5ForConditionalGeneration.from_pretrained(os.path.join(BASE_PATH,MOD...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: ions. ### What's your difficulty of supporting the model you want? The architecture required to mount the model is T5ForConditionalGeneration and for Tokenizer is T5Tokenizer. This architecture is not listed among those...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: me to support google/madlad400-3b-mt translator model in vLLM? new-model;stale ### The model to consider. https://huggingface.co/google/madlad400-3b-mt ### The closest model vllm already supports. I was unable to find a...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
