# vllm-project/vllm#20986: [Bug]: 0.9.2: Qwen2.5-VL GPTQ MacheteLinearKernel for GPTQMarlinLinearMethod: torch._dynamo.exc.Unsupported

| 字段 | 值 |
| --- | --- |
| Issue | [#20986](https://github.com/vllm-project/vllm/issues/20986) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 4; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | attention_kv_cache;ci_build;distributed_parallel;frontend_api;gemm_linear;hardware_porting;model_support;moe;multimodal_vlm;quantization;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | attention;cache;cuda;kernel;operator;quantization;sampling;triton |
| 症状 | build_error;crash;nan_inf;slowdown |
| 根因提示 | dtype;env_dependency;shape |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: 0.9.2: Qwen2.5-VL GPTQ MacheteLinearKernel for GPTQMarlinLinearMethod: torch._dynamo.exc.Unsupported

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug Models quantized with GPTQModel https://github.com/ModelCloud/GPTQModel/ , whether the latest published version on Pypi (2.2.0) or compiling from source (this commit 5d2911a4b2a709afb0941d53c3882d0cd80b9649 ) (4.0.0-dev) cannot be load in vllm 0.9.2 (but could be loaded on vllm 0.9.1) I tried Qwen2.5-VL-3B-Instruct and Qwen2.5-VL-32B-Instruct. I assume it would replicate on the 7B and other versions. Command to start vllm (both 0.9.1 and 0.9.2): ```bash python3 -m vllm.entrypoints.openai.api_server --model 3B --generation-config vllm --max-model-len 32768 -tp 1 --limit_mm_per_prompt '{"images": 6, "videos": 0}' ``` For convenience, I have uploaded the quantized model here: https://huggingface.co/NM-dev/Qwen2.5-VL-3B-Instruct-GPTQModel-W4A16-G128 If you want to reproduce the model and quantize it yourself: ```python #!/usr/bin/env python # coding: utf-8 import os import random import json import io import base64 import types from datasets import load_dataset from qwen_vl_utils import process_vision_info from gptqmodel import GPTQModel, QuantizeConfig from gptqmodel.models.base import BaseGPTQModel from transformers import AutoProc...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 6: [Bug]: 0.9.2: Qwen2.5-VL GPTQ MacheteLinearKernel for GPTQMarlinLinearMethod: torch._dynamo.exc.Unsupported bug ### Your current environment ### 🐛 Describe the bug Models quantized with GPTQModel https://github.com/Mode...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 5: https://github.com/ModelCloud/GPTQModel/ , whether the latest published version on Pypi (2.2.0) or compiling from source (this commit 5d2911a4b2a709afb0941d53c3882d0cd80b9649 ) (4.0.0-dev) cannot be load in vllm 0.9.2 (...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 2: rted bug ### Your current environment ### 🐛 Describe the bug Models quantized with GPTQModel https://github.com/ModelCloud/GPTQModel/ , whether the latest published version on Pypi (2.2.0) or compiling from source (this...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: ``` ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [MoE、GEMM 与 Expert Routing](../patterns/moe_gemm_routing.md) - 分数 2: orrectness attention_kv_cache;ci_build;distributed_parallel;frontend_api;gemm_linear;hardware_porting;model_support;moe;multimodal_vlm;quantization;sampling_logits;speculative_decoding attention;cache;cuda;kernel;operat...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
