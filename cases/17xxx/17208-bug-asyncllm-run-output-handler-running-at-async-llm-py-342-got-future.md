# vllm-project/vllm#17208: [Bug]: AsyncLLM._run_output_handler running at async_llm.py:342 got Future <Future pending> attached to a different loop

| 字段 | 值 |
| --- | --- |
| Issue | [#17208](https://github.com/vllm-project/vllm/issues/17208) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;multimodal_vlm;sampling_logits |
| 子分类 | precision |
| Operator 关键词 | cuda;operator;sampling;triton |
| 症状 | build_error;crash;nan_inf |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: AsyncLLM._run_output_handler running at async_llm.py:342 got Future <Future pending> attached to a different loop

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug Code: ``` async def get_model_config(_engine): # Await and get the model configuration return await _engine.get_model_config() if __name__ == "__main__": stats_client = StatsClient() model_path = os.path.join("/", "/models/Phi-4-multimodal-instruct/") served_model_name = "phi-4" parser = FlexibleArgumentParser(description="vLLM OpenAI API server.") parser = make_arg_parser(parser) args = parser.parse_args() args.model = model_path args.served_model_name = served_model_name args.port = int(os.getenv("SERVER_PORT", "5001")) env_args = os.getenv("ENGINE_ARGS", None) engine_args = AsyncEngineArgs.from_cli_args(args) engine = AsyncLLMEngine.from_engine_args( engine_args, usage_context=UsageContext.API_SERVER ) model_config = asyncio.run(get_model_config(engine)) base_model_paths = [BaseModelPath(name=args.served_model_name, model_path=args.model)] serving_model = OpenAIServingModels( engine_client=engine, model_config=model_config, base_model_paths=base_model_paths, lora_modules=args.lora_modules, prompt_adapters=args.prompt_adapters, ) openai_serving_chat = OpenAIServingChat( engine, model_config, serving_model, args.response_role, r...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 5: current environment ### 🐛 Describe the bug Code: ``` async def get_model_config(_engine): # Await and get the model configuration return await _engine.get_model_config() if __name__ == "__main__": stats_client = StatsCl...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: rgs, usage_context=UsageContext.API_SERVER ) model_config = asyncio.run(get_model_config(engine)) base_model_paths = [BaseModelPath(name=args.served_model_name, model_path=args.model)] serving_model = OpenAIServingModel...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: ``` ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: model_config, serving_model, args.response_role, request_logger=None, chat_template=args.chat_template, chat_template_content_format=args.chat_template_content_format, ) openai_serving_completion = OpenAIServingCompleti...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: ting;model_support;multimodal_vlm;sampling_logits cuda;operator;sampling;triton build_error;crash;nan_inf env_dependency Your current environment

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
