# vllm-project/vllm#11175: [Bug]: Nonsensical Sentences Generated When Inferencing INT8 Quantized Qwen2.5-72B Model

| 字段 | 值 |
| --- | --- |
| Issue | [#11175](https://github.com/vllm-project/vllm/issues/11175) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 17; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | activation_norm;attention_kv_cache;ci_build;distributed_parallel;frontend_api;gemm_linear;hardware_porting;model_support;quantization;sampling_logits |
| 子分类 | memory |
| Operator 关键词 | activation;cuda;operator;quantization;sampling;triton |
| 症状 | build_error;crash;oom |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Nonsensical Sentences Generated When Inferencing INT8 Quantized Qwen2.5-72B Model

### Issue 正文摘录

### Your current environment ### Model Input Dumps _No response_ ### 🐛 Describe the bug When I attempt to deploy the model with `Quantize FFN Only`, I encounter the following issues: 1. `SmoothQuant`: The inference works correctly with `Transformers`, but VLLM outputs are either all zeros or nonsensical sentences. 2. `GPTQ-w8a16-onlyFFN`: The inference works correctly with `Transformers`, but when deploying with VLLM, I get the following error: `KeyError: 'layers.10.self_attn.qkv_proj.weight'` 3. `GPTQ-w8a16`: The inference works correctly with `Transformers`, but VLLM outputs are all `!`. Additionally, all parameters of this model have been quantized. a minimal example： ```python import os os.environ["CUDA_VISIBLE_DEVICES"]= "1,2" os.environ["VLLM_LOGGING_LEVEL"]="DEBUG" from typing import Optional, Union, List from transformers import AutoTokenizer, AutoModelForCausalLM from vllm import LLM, SamplingParams import torch class ModelInference: def __init__( self, model_name: str, use_vllm: bool = False, max_tokens: int = 512 ): self.model_name = model_name self.use_vllm = use_vllm self.max_tokens = max_tokens if use_vllm: self.model = LLM( model=model_name, trust_remote_code=True,...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: [Bug]: Nonsensical Sentences Generated When Inferencing INT8 Quantized Qwen2.5-72B Model bug;stale ### Your current environment ### Model Input Dumps _No response_ ### 🐛 Describe the bug When I attempt to deploy the mod...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: [Bug]: Nonsensical Sentences Generated When Inferencing INT8 Quantized Qwen2.5-72B Model bug;stale ### Your current environment ### Model Input Dumps _No response_ ### 🐛 Describe the bug When I attempt to deploy the mod...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 3: [Bug]: Nonsensical Sentences Generated When Inferencing INT8 Quantized Qwen2.5-72B Model bug;stale ### Your current environment ### Model Input Dumps _No response_ ### 🐛 Describe the bug When I attempt to deploy the mod...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: e model with `Quantize FFN Only`, I encounter the following issues: 1. `SmoothQuant`: The inference works correctly with `Transformers`, but VLLM outputs are either all zeros or nonsensical sentences. 2. `GPTQ-w8a16-onl...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: entences Generated When Inferencing INT8 Quantized Qwen2.5-72B Model bug;stale ### Your current environment ### Model Input Dumps _No response_ ### 🐛 Describe the bug When I attempt to deploy the model with `Quantize FF...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
