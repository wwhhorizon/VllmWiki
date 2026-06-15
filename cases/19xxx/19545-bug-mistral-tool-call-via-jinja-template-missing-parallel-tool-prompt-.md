# vllm-project/vllm#19545: [Bug] Mistral Tool-Call via Jinja Template: Missing `parallel_tool_prompt` Injection and Incorrect tool_response Handling

| 字段 | 值 |
| --- | --- |
| Issue | [#19545](https://github.com/vllm-project/vllm/issues/19545) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | attention_kv_cache;ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;moe;quantization;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | attention;cache;cuda;operator;quantization;sampling;triton |
| 症状 | build_error;mismatch;nan_inf |
| 根因提示 | dtype;env_dependency;shape |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug] Mistral Tool-Call via Jinja Template: Missing `parallel_tool_prompt` Injection and Incorrect tool_response Handling

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug ```python pip list | grep vllm # vllm 0.9.1 ``` #### Start vllm server ```python vllm serve models/Mistral-Small-24B-Instruct-2501 \ --tensor-parallel-size 8 \ --served_model_name Mistral-Small-24B-Instruct-2501 \ --port 8002 \ --tool-call-parser mistral \ --chat-template vllm/examples/tool_chat_template_mistral3.jinja \ --enable-auto-tool-choice \ --tokenizer-mode mistral \ --config_format mistral \ --load_format mistral ``` ### Basic setup ```python from openai import OpenAI from transformers import AutoTokenizer import json tools = [ { "type": "function", "function": { "name": "get_weather", "description": "Get the current weather in a given location", "parameters": { "type": "object", "properties": { "location": { "type": "string", "description": "Country or city name, e.g., 'Taipei', 'Japan'" }, "unit": { "type": "string", "description": "Temperature unit. Use Celsius for Asian cities; use Fahrenheit for European and American cities", "enum": ["celsius", "fahrenheit"] } }, "required": ["location", "unit"] } } }, { "type": "function", "function": { "name": "search", "description": "A search engine similar to Google. Use it to...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: al \ --load_format mistral ``` ### Basic setup ```python from openai import OpenAI from transformers import AutoTokenizer import json tools = [ { "type": "function", "function": { "name": "get_weather", "description": "...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: 0.9.1 ``` #### Start vllm server ```python vllm serve models/Mistral-Small-24B-Instruct-2501 \ --tensor-parallel-size 8 \ --served_model_name Mistral-Small-24B-Instruct-2501 \ --port 8002 \ --tool-call-parser mistral \...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: 0.9.1 ``` #### Start vllm server ```python vllm serve models/Mistral-Small-24B-Instruct-2501 \ --tensor-parallel-size 8 \ --served_model_name Mistral-Small-24B-Instruct-2501 \ --port 8002 \ --tool-call-parser mistral \...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 3: = AutoTokenizer.from_pretrained(model_path, local_files_only=True) def decode_ids(token_ids): decoded_text = tokenizer.decode(token_ids, skip_special_tokens=False) return decoded_text ``` #### #1 Client Query (Tool call...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 2: ild;distributed_parallel;frontend_api;hardware_porting;model_support;moe;quantization;sampling_logits;speculative_decoding attention;cache;cuda;operator;quantization;sampling;triton build_error;mismatch;nan_inf dtype;en...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
