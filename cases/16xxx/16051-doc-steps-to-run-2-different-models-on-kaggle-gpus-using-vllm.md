# vllm-project/vllm#16051: [Doc]: Steps to run 2 different models on Kaggle GPUs using vllm

| 字段 | 值 |
| --- | --- |
| Issue | [#16051](https://github.com/vllm-project/vllm/issues/16051) |
| 状态 | closed |
| 标签 | documentation;stale |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | frontend_api;model_support;quantization |
| 子分类 | memory |
| Operator 关键词 | cuda;quantization |
| 症状 | oom |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Doc]: Steps to run 2 different models on Kaggle GPUs using vllm

### Issue 正文摘录

### 📚 The doc issue I'm trying to deploy two Hugging Face LLM models using the vLLM library, but due to VRAM limitations, I want to assign each model to a different GPU on Kaggle (Kaggle provides free 2xT4 GPUs). However, no matter what I try, vLLM keeps loading the second model onto the first GPU as well, leading to CUDA OUT OF MEMORY errors. I did manage to get them assigned to different GPUs with this approach: ``` from vllm import LLM device_1 = torch.device("cuda:0") device_2 = torch.device("cuda:1") self.llm = LLM(model=model_1, dtype=torch.float16, device=device_1) self.llm = LLM(model=model_2, dtype=torch.float16, device=device_2) ``` But this breaks the responses—the LLM starts outputting garbage, like repeated one-word answers or "seems like your input got cut short..." Could you please provide me the correct approach to specify each gpu for each model? Would really appreciate any insights! Full code below: ``` from transformers import AutoTokenizer from vllm import LLM, SamplingParams import torch import os class Qwen2Model: def __init__(self, model_name="Qwen/Qwen2.5-7B-Instruct-AWQ"): # Initialize tokenizer and model only once self.tokenizer = AutoTokenizer.from_pretr...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: o get them assigned to different GPUs with this approach: ``` from vllm import LLM device_1 = torch.device("cuda:0") device_2 = torch.device("cuda:1") self.llm = LLM(model=model_1, dtype=torch.float16, device=device_1)...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 3: 0") device_2 = torch.device("cuda:1") self.llm = LLM(model=model_1, dtype=torch.float16, device=device_1) self.llm = LLM(model=model_2, dtype=torch.float16, device=device_2) ``` But this breaks the responses—the LLM sta...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: LM keeps loading the second model onto the first GPU as well, leading to CUDA OUT OF MEMORY errors. I did manage to get them assigned to different GPUs with this approach: ``` from vllm import LLM device_1 = torch.devic...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: [Doc]: Steps to run 2 different models on Kaggle GPUs using vllm documentation;stale ### 📚 The doc issue I'm trying to deploy two Hugging Face LLM models using the vLLM library, but due to VRAM limitations, I want to as...
- [KV Cache 容量、压缩与 Offload](../patterns/kv_cache_capacity_offload.md) - 分数 1: s. performance frontend_api;model_support;quantization cuda;quantization oom dtype;env_dependency 📚 The doc issue

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
