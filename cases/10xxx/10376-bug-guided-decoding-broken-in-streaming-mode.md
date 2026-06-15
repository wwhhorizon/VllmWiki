# vllm-project/vllm#10376: [Bug]: Guided Decoding Broken in Streaming mode

| 字段 | 值 |
| --- | --- |
| Issue | [#10376](https://github.com/vllm-project/vllm/issues/10376) |
| 状态 | closed |
| 标签 | bug;structured-output;stale |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;quantization;sampling_logits |
| 子分类 | precision |
| Operator 关键词 | cuda;operator;quantization;sampling;triton |
| 症状 | build_error;nan_inf |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Guided Decoding Broken in Streaming mode

### Issue 正文摘录

### Your current environment ### Model Input Dumps _No response_ ### 🐛 Describe the bug Guided decoding broken in streaming mode after this commit https://github.com/vllm-project/vllm/commit/04cef2c6ab0ea47bb1dfa73d3343985499fe1c4b Previous commits are working fine. Non-streaming mode works fine as well. Dataset to test: https://raw.githubusercontent.com/JC1DA/SharedData/refs/heads/main/gsm8k_luca_input_prompts/dataset.json Test script: ``` import json from openai import OpenAI from concurrent.futures import ThreadPoolExecutor from tqdm import tqdm json_schema = """ { "$schema": "http://json-schema.org/draft-07/schema#", "type": "object", "properties": { "thoughts": { "type": "array", "items": { "type": "object", "properties": { "action": { "type": "string", "description": "Description of the step in the thought process" }, "calculation": { "type": "string", "description": "Calculation performed in this step" }, "result": { "type": "integer", "description": "Result of the calculation" } }, "required": ["action", "calculation", "result"], "additionalProperties": false } }, "answer": { "type": "integer", "description": "Final answer calculated from the thoughts" } }, "required": ["t...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: /refs/heads/main/gsm8k_luca_input_prompts/dataset.json Test script: ``` import json from openai import OpenAI from concurrent.futures import ThreadPoolExecutor from tqdm import tqdm json_schema = """ { "$schema": "http:...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 3: Properties": false } """.strip() model = "Qwen/Qwen2.5-7B-Instruct-GPTQ-Int4" client = OpenAI( base_url="http://localhost:5006/v1", api_key="NOKEY", ) data = json.load(open("dataset.json", "r", encoding="utf-8")) def ge...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: est: https://raw.githubusercontent.com/JC1DA/SharedData/refs/heads/main/gsm8k_luca_input_prompts/dataset.json Test script: ``` import json from openai import OpenAI from concurrent.futures import ThreadPoolExecutor from...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: ng mode bug;structured-output;stale ### Your current environment ### Model Input Dumps _No response_ ### 🐛 Describe the bug Guided decoding broken in streaming mode after this commit https://github.com/vllm-project/vllm...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 2: extra_body={"guided_json": json.loads(json_schema), "guided_decoding_backend": "outlines"}, ) _data = "" for chunk in stream: if chunk.choices[0].delta.content is not None: _data += chunk.choices[0].delta.content return...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
