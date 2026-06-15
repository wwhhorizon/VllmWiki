# vllm-project/vllm#8298: [Bug]: Missing code checking when using Encoder/Decoder models on CPU backend

| 字段 | 值 |
| --- | --- |
| Issue | [#8298](https://github.com/vllm-project/vllm/issues/8298) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 0; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | attention_kv_cache;ci_build;frontend_api;hardware_porting;model_support;quantization;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cuda;kernel;operator;quantization;sampling;triton |
| 症状 | build_error;crash;nan_inf |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Missing code checking when using Encoder/Decoder models on CPU backend

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug Greetings! I was collecting some combination of features and check the compatibility and then I tested encoder/decoder on CPU. I already knew that it should not work, I found the comment at the codebase in the test `test_bart.py`: ```python if not is_cpu(): # CPU backend is not currently supported with encoder/decoder models # skip test definitions entirely to avoid importing GPU kernel libs # (xFormers, etc.) ``` I tested the [encoder/decoder example](https://docs.vllm.ai/en/stable/getting_started/examples/offline_inference_encoder_decoder.html) from the documentation I got the following output: ``` INFO 09-08 00:46:05 importing.py:10] Triton not installed; certain GPU-related functions will not be available. config.json: 100%|████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████| 1.58k/1.58k [00:00 [rank0]: outputs = llm.generate(prompts, sampling_params) [rank0]: File "/usr/local/lib/python3.10/dist-packages/vllm/utils.py", line 1032, in inner [rank0]: return fn(...

## 现有链接修复摘要

#8355 [Misc] Raise error when using encoder/decoder model with cpu backend

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 5: ith encoder/decoder models # skip test definitions entirely to avoid importing GPU kernel libs # (xFormers, etc.) ``` I tested the [encoder/decoder example](https://docs.vllm.ai/en/stable/getting_started/examples/offlin...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 2: [Bug]: Missing code checking when using Encoder/Decoder models on CPU backend bug ### Your current environment ### 🐛 Describe the bug Greetings! I was collecting some combination of features and check the compatibility...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 2: attention_kv_cache;ci_build;frontend_api;hardware_porting;model_support;quantization;sampling_logits;speculative_decoding cuda;kernel;operator;quantization;sampling;triton build_error;crash;nan_inf dtype;env_dependency...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: em. ### Before submitting a new issue... - [X] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: [Bug]: Missing code checking when using Encoder/Decoder models on CPU backend bug ### Your current environment ### 🐛 Describe the bug Greetings! I was collecting some combination of features and check the compatibility...

## 关联 PR 证据

| PR | 链接类型 | 置信度 | PR 标题 | 证据 |
| --- | --- | ---: | --- | --- |
| [#8355](https://github.com/vllm-project/vllm/pull/8355) | closes_keyword | 0.95 | [Misc] Raise error when using encoder/decoder model with cpu backend | FIX #8298 **BEFORE SUBMITTING, PLEASE READ THE CHECKLIST BELOW AND FILL IN THE DESCRIPTION ABOVE** --- <details> <!-- inside this <details> section, markdown rendering do |

## Wiki 抽取状态

- 后续迭代应在可用时读取完整讨论评论。
