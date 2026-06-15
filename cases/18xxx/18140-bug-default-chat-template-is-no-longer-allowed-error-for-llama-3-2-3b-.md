# vllm-project/vllm#18140: [Bug]: "Default chat template is no longer allowed" error for llama-3.2-3B instruct model

| 字段 | 值 |
| --- | --- |
| Issue | [#18140](https://github.com/vllm-project/vllm/issues/18140) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: "Default chat template is no longer allowed" error for llama-3.2-3B instruct model

### Issue 正文摘录

### Your current environment if not self.openai_serving_chat: model_config = await self.engine.get_model_config() # Determine the name of the served model for the OpenAI client. if self.engine_args.served_model_name is not None: served_model_names = self.engine_args.served_model_name else: served_model_names = [self.engine_args.model] base_model_paths = [ BaseModelPath(name=name, model_path=self.engine_args.model) for name in served_model_names ] models = OpenAIServingModels( self.engine, model_config, base_model_paths, ) self.openai_serving_chat = OpenAIServingChat( self.engine, model_config, models, response_role=self.response_role, chat_template=self.chat_template, request_logger=None, chat_template_content_format="auto", ) logger.info(f"Request: {request}") generator = await self.openai_serving_chat.create_chat_completion( request, raw_request ) if isinstance(generator, ErrorResponse): return JSONResponse( content=generator.model_dump(), status_code=generator.code ) if request.stream: return StreamingResponse(content=generator, media_type="text/event-stream") else: assert isinstance(generator, ChatCompletionResponse) return JSONResponse(content=generator.model_dump()) ### 🐛 De...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 5: [Bug]: "Default chat template is no longer allowed" error for llama-3.2-3B instruct model bug ### Your current environment if not self.openai_serving_chat: model_config = await self.engine.get_model_config() # Determine...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: ne. ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 1: served_model_names = self.engine_args.served_model_name else: served_model_names = [self.engine_args.model] base_model_paths = [ BaseModelPath(name=name, model_path=self.engine_args.model) for name in served_model_nam
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: _role, chat_template=self.chat_template, request_logger=None, chat_template_content_format="auto", ) logger.info(f"Request: {request}") generator = await self.openai_serving_chat.create_chat_completion( re
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
