# vllm-project/vllm#14008: [Bug]: (vllm0.7.3 & v1) ValueError: signal only works in main thread of the main interpreter

| 字段 | 值 |
| --- | --- |
| Issue | [#14008](https://github.com/vllm-project/vllm/issues/14008) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 4; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;frontend_api;hardware_porting;model_support |
| 子分类 | precision |
| Operator 关键词 | cuda;operator;triton |
| 症状 | build_error;crash;nan_inf |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: (vllm0.7.3 & v1) ValueError: signal only works in main thread of the main interpreter

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug I attempted to use the vLLM's v1 engine to run DeepSeek1, and I wrapped the script with Ray's Serve deployment. The serving job was submitted in the form of a Ray job. The script is as follows: ```python @serve.deployment(name=config["model_name"],max_ongoing_requests=config["max_ongoing_requests"]) @serve.ingress(app) class VLLMDeployment: def __init__( self, config: Dict[str, str], engine_args: AsyncEngineArgs, response_role: str = "assistant", lora_modules: Optional[List[LoRAModulePath]] = None, prompt_adapters: Optional[List[PromptAdapterPath]] = None, request_logger: Optional[RequestLogger] = None, chat_template: Optional[str] = None, ): logger.info(f"Starting with engine args: {engine_args}") self.openai_serving_chat = None self.config=config self.engine_args = engine_args self.response_role = response_role self.lora_modules = lora_modules self.prompt_adapters = prompt_adapters self.request_logger = request_logger self.chat_template = chat_template del os.environ['CUDA_VISIBLE_DEVICES'] self.engine = AsyncLLMEngine.from_engine_args(engine_args) ``` However, after submitting the job, I encountered the following error. Notabl...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: ServeController pid=281666) self._user_callable_asgi_app = await asyncio.wrap_future( (ServeController pid=281666) ^^^^^^^^^^^^^^^^^^^^^^^^^^ (ServeController pid=281666) File "/home/ray/anaconda3/lib/python3.11/site-pa...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: f a Ray job. The script is as follows: ```python @serve.deployment(name=config["model_name"],max_ongoing_requests=config["max_ongoing_requests"]) @serve.ingress(app) class VLLMDeployment: def __init__( self, config: Dic...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: ogger self.chat_template = chat_template del os.environ['CUDA_VISIBLE_DEVICES'] self.engine = AsyncLLMEngine.from_engine_args(engine_args) ``` However, after submitting the job, I encountered the following error. Notabl...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: ValueError: signal only works in main thread of the main interpreter bug;stale ### Your current environment ### 🐛 Describe the bug I attempted to use the vLLM's v1 engine to run DeepSeek1, and I wrapped the script with...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: buted_parallel;frontend_api;hardware_porting;model_support cuda;operator;triton build_error;crash;nan_inf env_dependency Your current environment

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
