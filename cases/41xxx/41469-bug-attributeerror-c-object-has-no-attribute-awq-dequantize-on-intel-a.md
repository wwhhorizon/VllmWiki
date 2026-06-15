# vllm-project/vllm#41469: [Bug]: AttributeError: '_C' object has no attribute 'awq_dequantize' on Intel Arc B580 XPU (AWQ inference fails)

| 字段 | 值 |
| --- | --- |
| Issue | [#41469](https://github.com/vllm-project/vllm/issues/41469) |
| 状态 | open |
| 标签 | bug;intel-gpu |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | attention_kv_cache;ci_build;hardware_porting;model_support;quantization;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | attention;cuda;kernel;operator;quantization;sampling;triton |
| 症状 | build_error;crash;nan_inf |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: AttributeError: '_C' object has no attribute 'awq_dequantize' on Intel Arc B580 XPU (AWQ inference fails)

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug I am trying to run an AWQ-quantized model (Chunity/gemma-4-E4B-it-AWQ-4bit) on an Intel Arc B580 GPU using the vLLM XPU backend. While standard unquantized models (like opt-125m) run fine, attempting to serve the AWQ model crashes with an AttributeError, indicating that the awq_dequantize C++ kernel is missing or not compiled for the Intel XPU backend. Reproduction: ```bash vllm serve Chunity/gemma-4-E4B-it-AWQ-4bit \ --max-model-len 4k \ --enable-auto-tool-choice \ --tool-call-parser gemma4 \ --port 8000 \ --enforce-eager \ --attention-backend TRITON_ATTN ``` Error log: ``` ERROR [core.py:1136] File "/home/_/vllm/.venv/lib/python3.12/site-packages/torch/_ops.py", line 1379, in __getattr__ ERROR [core.py:1136] raise AttributeError ERROR [core.py:1136] AttributeError: '_OpNamespace' '_C' object has no attribute 'awq_dequantize' ``` ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 现有链接修复摘要

#42727 fix(quantization): Fix AWQ dequantize on Intel XPU and refactor AutoAWQ config

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: teError, indicating that the awq_dequantize C++ kernel is missing or not compiled for the Intel XPU backend. Reproduction: ```bash vllm serve Chunity/gemma-4-E4B-it-AWQ-4bit \ --max-model-len 4k \ --enable-auto-tool-cho...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: ironment ### 🐛 Describe the bug I am trying to run an AWQ-quantized model (Chunity/gemma-4-E4B-it-AWQ-4bit) on an Intel Arc B580 GPU using the vLLM XPU backend. While standard unquantized models (like opt-125m) run fine...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 2: ity/gemma-4-E4B-it-AWQ-4bit) on an Intel Arc B580 GPU using the vLLM XPU backend. While standard unquantized models (like opt-125m) run fine, attempting to serve the AWQ model crashes with an AttributeError, indicating...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 2: [Bug]: AttributeError: '_C' object has no attribute 'awq_dequantize' on Intel Arc B580 XPU (AWQ inference fails) bug;intel-gpu ### Your current environment ### 🐛 Describe the bug I am trying to run an AWQ-quantized mode...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: ``` ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...

## 关联 PR 证据

| PR | 链接类型 | 置信度 | PR 标题 | 证据 |
| --- | --- | ---: | --- | --- |
| [#42727](https://github.com/vllm-project/vllm/pull/42727) | closes_keyword | 0.95 | fix(quantization): Fix AWQ dequantize on Intel XPU and refactor AutoAWQ config | fixes the AWQ dequantize issue on Intel XPU (#41469) and refactors the AutoAWQ config for better XPU performance support. The refactoring approach is inspired by #38288 (consolidat |

## Wiki 抽取状态

- 后续迭代应在可用时读取完整讨论评论。
