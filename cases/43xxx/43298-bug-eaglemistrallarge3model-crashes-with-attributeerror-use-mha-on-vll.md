# vllm-project/vllm#43298: [Bug]: EagleMistralLarge3Model crashes with AttributeError: 'use_mha' on vLLM 0.21.0

| 字段 | 值 |
| --- | --- |
| Issue | [#43298](https://github.com/vllm-project/vllm/issues/43298) |
| 状态 | open |
| 标签 | bug |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | development |
| 工作域 | attention_kv_cache;distributed_parallel;model_support;quantization;speculative_decoding |
| 子分类 | env_compat |
| Operator 关键词 | attention |
| 症状 | crash |
| 根因提示 |  |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: EagleMistralLarge3Model crashes with AttributeError: 'use_mha' on vLLM 0.21.0

### Issue 正文摘录

### Your current environment ## Environment - **vLLM version:** 0.21.0 - **Model:** `mistralai/Mistral-Large-3-675B-Instruct-2512` with Eagle speculative decoding - **Hardware:** 8x H200 NVL, TP=8 ``` (APIServer pid=1) INFO 05-21 08:22:26 [utils.py:240] non-default args: {'model_tag': 'mistralai/Mistral-Large-3-675B-Instruct-2512-NVFP4', 'enable_auto_tool_choice': True, 'tool_call_parser': 'mistral', 'model': 'mistralai/Mistral-Large-3-675B-Instruct-2512-NVFP4', 'tokenizer_mode': 'mistral', 'served_model_name': ['mistral-large-3-675b-instruct-2512'], 'config_format': 'mistral', 'load_format': 'mistral', 'tensor_parallel_size': 8, 'speculative_config': {'model': 'mistralai/Mistral-Large-3-675B-Instruct-2512-Eagle', 'num_speculative_tokens': 3, 'method': 'eagle', 'max_model_len': '16384'}} ``` ### 🐛 Describe the bug ## Description `EagleMistralLarge3Model` fails during weight loading with: ``` File "/usr/local/lib/python3.12/dist-packages/vllm/model_executor/models/deepseek_v2.py", line 1355, in load_weights if self.use_mha: ^^^^^^^^^^^^ AttributeError: 'EagleMistralLarge3Model' object has no attribute 'use_mha' ``` This worked in vLLM 0.19.x / 0.20.2 and regressed in 0.21.0. ## Roo...

## 现有链接修复摘要

#43621 [Bugfix] Set use_mha=False in EagleMistralLarge3Model.__init__

## 候选优化模式

- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 3: efault args: {'model_tag': 'mistralai/Mistral-Large-3-675B-Instruct-2512-NVFP4', 'enable_auto_tool_choice': True, 'tool_call_parser': 'mistral', 'model': 'mistralai/Mistral-Large-3-675B-Instruct-2512-NVFP4', 'tokenizer_...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: [Bug]: EagleMistralLarge3Model crashes with AttributeError: 'use_mha' on vLLM 0.21.0 bug ### Your current environment ## Environment - **vLLM version:** 0.21.0 - **Model:** `mistralai/Mistral-Large-3-675B-Instruct-2512`...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 2: term, the bypassed `super().__init__()` pattern will keep causing these regressions whenever `DeepseekV2Model.__init__` gains new attributes. ### Before submitting a new issue... - [x] Make sure you already searched for...
- [Bitwise 确定性与数值等价](../patterns/bitwise_determinism_equivalence.md) - 分数 1: the parent `__init__` — was flagged by reviewers at the time. ## How to Reproduce ```bash vllm serve mistralai/Mistral-Large-3-675B-Instruct-2512 \ --speculative-config '{"model": "mistralai/Mistral-Large-3-675B-Instruc...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: n vLLM 0.21.0 bug ### Your current environment ## Environment - **vLLM version:** 0.21.0 - **Model:** `mistralai/Mistral-Large-3-675B-Instruct-2512` with Eagle speculative decoding - **Hardware:** 8x H200 NVL, TP=8 ```...

## 关联 PR 证据

| PR | 链接类型 | 置信度 | PR 标题 | 证据 |
| --- | --- | ---: | --- | --- |
| [#43621](https://github.com/vllm-project/vllm/pull/43621) | closes_keyword | 0.95 | [Bugfix] Set use_mha=False in EagleMistralLarge3Model.__init__ | fix shape that #37232 established for the same file. ## Test Plan The reporter (in #43298) has the only known SM-class hardware to run the model end-to-end (8×H200, Mistral-Large |

## Wiki 抽取状态

- 后续迭代应在可用时读取完整讨论评论。
