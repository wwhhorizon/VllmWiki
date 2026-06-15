# vllm-project/vllm#21372: [Bug]: Tool call argument value of type `integer` may break things when `stream=True`

| 字段 | 值 |
| --- | --- |
| Issue | [#21372](https://github.com/vllm-project/vllm/issues/21372) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 6; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | distributed_parallel;frontend_api;hardware_porting;model_support;quantization;sampling_logits |
| 子分类 | kernel_eff |
| Operator 关键词 | fp8;sampling |
| 症状 |  |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Tool call argument value of type `integer` may break things when `stream=True`

### Issue 正文摘录

### Your current environment 2 * RTX A6000 48G (Ampere) vLLM 0.9.1 (OpenAI compatible API server) + Qwen3 series (FP8 official weight, W8A16) ``` vllm serve ./models/Qwen3/Qwen3-30B-A3B-FP8/ --served-model-name Qwen3-30B-A3B --host 0.0.0.0 --port 8888 --gpu-memory-utilization 0.6 --disable-log-stats --enable-auto-tool-choice --tool-call-parser hermes --reasoning-parser qwen3 --rope-scaling {"rope_type":"yarn","factor":2.0,"original_max_position_embeddings":32768} --max-model-len 65536 -tp 2 ``` ### 🐛 Describe the bug I think it's just Qwen3 because Qwen2.5 worked fine before. Or maybe it's W8A16's doing? It would be great if anyone could test it out. Many thanks. Minimal test code below, should just work after changing the key and url, pardon the janky code. ```python import json from openai import OpenAI openai_api_key = "abc" openai_api_base = "http://1.2.3.4:8888/v1" client = OpenAI( api_key=openai_api_key, base_url=openai_api_base, ) messages = [ { "role": "system", "content": "You are an artificial intelligence assistant who will call tools everytime when responding.", }, { "role": "user", "content": "Hi! Do you have any detailed information about the product id 7355608?", },...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: mpere) vLLM 0.9.1 (OpenAI compatible API server) + Qwen3 series (FP8 official weight, W8A16) ``` vllm serve ./models/Qwen3/Qwen3-30B-A3B-FP8/ --served-model-name Qwen3-30B-A3B --host 0.0.0.0 --port 8888 --gpu-memory-uti...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 3: 0 48G (Ampere) vLLM 0.9.1 (OpenAI compatible API server) + Qwen3 series (FP8 official weight, W8A16) ``` vllm serve ./models/Qwen3/Qwen3-30B-A3B-FP8/ --served-model-name Qwen3-30B-A3B --host 0.0.0.0 --port 8888 --gpu-me...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: ay break things when `stream=True` bug ### Your current environment 2 * RTX A6000 48G (Ampere) vLLM 0.9.1 (OpenAI compatible API server) + Qwen3 series (FP8 official weight, W8A16) ``` vllm serve ./models/Qwen3/Qwen3-30...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: 2 * RTX A6000 48G (Ampere) vLLM 0.9.1 (OpenAI compatible API server) + Qwen3 series (FP8 official weight, W8A16) ``` vllm serve ./models/Qwen3/Qwen3-30B-A3B-FP8/ --served-model-name Qwen3-30B-A3B --host 0.0.0.0 --port 8...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 1: ed": ["product_name"], }, }, }, ] use_stream = False tool_calls = 0 while tool_calls The "None" is expected. If we ask "Hi! Do you know the ID of the product named 123456789?" the tool call argument is correct. If we as...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
