# vllm-project/vllm#42047: [Bug] Gemma4ToolParser streams incorrect float values (e.g., 108.2 → 108.02)

| 字段 | 值 |
| --- | --- |
| Issue | [#42047](https://github.com/vllm-project/vllm/issues/42047) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;sampling_logits |
| 子分类 | race_cond |
| Operator 关键词 | cuda;sampling |
| 症状 | build_error;mismatch |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug] Gemma4ToolParser streams incorrect float values (e.g., 108.2 → 108.02)

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug ### Bug Summary In vLLM 0.19.1, the `Gemma4ToolParser` produces **incorrect floating-point argument values in streaming mode**. A number like `108.2` is incorrectly streamed as `108.02`, and `22.8` becomes `22.08`. String-typed arguments and non-streaming responses are unaffected. ### Launch Command ```bash vllm serve /llm-models/gemma-4-26B-A4B-it \ --served-model-name gemma4-26b-a4b-it \ --host=0.0.0.0 \ --port 9999 \ --gpu_memory_utilization 0.9 \ --tensor-parallel-size 2 \ --max-model-len 262144 \ --enable-prefix-caching \ --enable-auto-tool-choice \ --reasoning-parser gemma4 \ --tool-call-parser gemma4 ``` ### Minimal Reproduction ```python # pip install openai==1.76.1 from openai import OpenAI client = OpenAI(base_url="http://127.0.0.1:9999/v1", api_key="EMPTY") response = client.chat.completions.create( ​ model="gemma4-26b-a4b-it", ​ messages=[{ ​ "role": "user", ​ "content": [{"type": "text", "text": "Calculate the sum of 108.2 and 22.8"}] ​ }], ​ tools=[{ ​ "type": "function", ​ "function": { ​ "name": "add", ​ "description": "Calculate the sum of two numbers", ​ "parameters": { ​ "type": "object", ​ "properties": { ​ "l...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 5: --tool-call-parser gemma4 ``` ### Minimal Reproduction ```python # pip install openai==1.76.1 from openai import OpenAI client = OpenAI(base_url="http://127.0.0.1:9999/v1", api_key="EMPTY") response = client.chat.comple...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: 08} ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: [Bug] Gemma4ToolParser streams incorrect float values (e.g., 108.2 → 108.02) bug ### Your current environment ### 🐛 Describe the bug ### Bug Summary In vLLM 0.19.1, the `Gemma4ToolParser` produces **incorrect floating-po
- [Bitwise 确定性与数值等价](../patterns/bitwise_determinism_equivalence.md) - 分数 1: hardware_porting;model_support;sampling_logits cuda;sampling build_error;mismatch env_dependency Your current environment
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 1: "top_k": 20, ​ "chat_template_kwargs": {"enable_thinking": False}, ​ }, ) arguments = "" for chunk in response: ​ tc = chunk.choices[0].delta.tool_calls ​ if tc and len(tc) == 1: ​ arguments += tc[0].function.arguments...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
