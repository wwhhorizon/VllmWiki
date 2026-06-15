# vllm-project/vllm#26224: [Bug]: reasoning_parser parameter not working in run_batch.py

| 字段 | 值 |
| --- | --- |
| Issue | [#26224](https://github.com/vllm-project/vllm/issues/26224) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 0; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | development |
| 工作域 | ci_build;distributed_parallel;hardware_porting;model_support |
| 子分类 | env_compat |
| Operator 关键词 | cuda;operator;triton |
| 症状 | build_error |
| 根因提示 | env_dependency;shape |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: reasoning_parser parameter not working in run_batch.py

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug The reasoning_parser parameter from structured outputs configuration is not being passed to the `OpenAIServingChat` object in `run_batch.py`. It causing reasoning parser functionality to fail silently during batch processing. This creates inconsistent behavior between regular serving and batch processing modes. ```python # run_batch.py openai_serving_chat = OpenAIServingChat( engine_client, model_config, openai_serving_models, args.response_role, request_logger=request_logger, chat_template=None, chat_template_content_format="auto", enable_prompt_tokens_details=args.enable_prompt_tokens_details, ) if "generate" in supported_tasks else None ``` ### command ``` python3 -m vllm.entrypoints.openai.run_batch \ -i data/input.txt \ -o data/qwen3_output.txt \ --model ./model/qwen3-8b \ --trust_remote_code \ --reasoning-parser qwen3 ``` ### output data ``` "message": { "role": "assistant", "content": " \nOkay, let's tackle this. ... \n\nmain_content: ...", "refusal": null, "annotations": null, "audio": null, "function_call": null, "tool_calls": [], "reasoning_content": null }, ``` ### Before submitting a new issue... - [x] Make sure you a...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: Describe the bug The reasoning_parser parameter from structured outputs configuration is not being passed to the `OpenAIServingChat` object in `run_batch.py`. It causing reasoning parser functionality to fail silently d...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: test/), which can answer lots of frequently asked questions. development ci_build;distributed_parallel;hardware_porting;model_support cuda;operator;triton build_error env_dependency;shape Your current environment
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: ``` ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: _build;distributed_parallel;hardware_porting;model_support cuda;operator;triton build_error env_dependency;shape Your current environment
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 1: gs.enable_prompt_tokens_details, ) if "generate" in supported_tasks else None ``` ### command ``` python3 -m vllm.entrypoints.openai.run_batch \ -i data/input.txt \ -o data/qwen3_output.txt \ --model ./model/qwen3-8b \...

## Wiki 抽取状态

- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
