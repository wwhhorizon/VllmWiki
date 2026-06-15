# vllm-project/vllm#16341: [Bug]: Gemma3 failed tool parser for AsyncLLMengine

| 字段 | 值 |
| --- | --- |
| Issue | [#16341](https://github.com/vllm-project/vllm/issues/16341) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 4; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: Gemma3 failed tool parser for AsyncLLMengine

### Issue 正文摘录

### Your current environment - VLLM `0.8.3` - `VLLM_USE_V1=0` ### 🐛 Describe the bug What is the problem if I start unicorn server and call the same endpoints from `vllm/entrypoints/openai/serving_chat.py` and use the same sampling params and turn on the tools and pass the parser: ``` self.engine = AsyncLLMEngine.from_engine_args(engine_args) base_model_paths = [BaseModelPath(name=self.model_path, model_path=self.model_path)] model_config = await self.engine.get_model_config() openai_serving_models = OpenAIServingModels( engine_client=self.engine, model_config=model_config, base_model_paths=base_model_paths, lora_modules=None, prompt_adapters=None, ) openai_serving_chat = OpenAIServingChat( engine_client=self.engine, model_config=model_config, models=openai_serving_models, chat_template="examples/tool_chat_template_llama3.1_json.jinja", enable_reasoning=self.enable_reasoning, reasoning_parser=self.reasoning_parser, enable_auto_tools=True, tool_parser="pythonic", chat_template_content_format="string", response_role="assistant", request_logger=None, ) ``` When I run it through [VLLM serve command ](https://github.com/vllm-project/vllm/issues/14734#issuecomment-2735270076) ``` VLLM_U...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 5: [Bug]: Gemma3 failed tool parser for AsyncLLMengine bug;stale ### Your current environment - VLLM `0.8.3` - `VLLM_USE_V1=0` ### 🐛 Describe the bug What is the problem if I start unicorn server and call the same endpoint...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: [Bug]: Gemma3 failed tool parser for AsyncLLMengine bug;stale ### Your current environment - VLLM `0.8.3` - `VLLM_USE_V1=0` ### 🐛 Describe the bug What is the problem if I start unicorn server and call the same endpoint...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: emory-utilization 0.90 --tensor-parallel-size 2 --distributed-executor-backend ray --enable-auto-tool-choice --tool-call-parser pythonic --chat-template examples/tool_chat_template_gemma3_pythonic.jinja ``` - the output...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: METHOD: CompletionOutput(index=0, text="[get_weather(location='San Francisco, CA', unit='celsius')]", token_ids=(236840, 828, 236779, 19323, 236769, 7125, 2507, 23243, 14322, 236764, 8253, 963, 4360, 2507, 236755, 42024...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 1: ment-2735270076) ``` VLLM_USE_V1=0 vllm serve gaunernst/gemma-3-27b-it-int4-awq --max-model-len 4096 --gpu-memory-utilization 0.90 --tensor-parallel-size 2 --distributed-executor-backend ray --enable-auto-tool-choice --...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
