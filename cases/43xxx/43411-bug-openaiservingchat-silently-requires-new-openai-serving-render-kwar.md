# vllm-project/vllm#43411: [Bug]: OpenAIServingChat silently requires new openai_serving_render kwarg since v0.18

| 字段 | 值 |
| --- | --- |
| Issue | [#43411](https://github.com/vllm-project/vllm/issues/43411) |
| 状态 | open |
| 标签 | bug |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: OpenAIServingChat silently requires new openai_serving_render kwarg since v0.18

### Issue 正文摘录

### Your current environment Since v0.18.0 (#36483), `OpenAIServingChat.__init__` requires a new keyword-only argument `openai_serving_render: OpenAIServingRender`. This is a silent breaking change for anyone constructing `OpenAIServingChat` directly. We are using KubeRay + Ray Serve + FastAPI encounter this issue. ### Code that worked on v0.17.0: ```python from vllm.engine.async_llm_engine import AsyncLLMEngine from vllm.engine.arg_utils import AsyncEngineArgs from vllm.entrypoints.openai.chat_completion.serving import OpenAIServingChat from vllm.entrypoints.openai.models.serving import OpenAIServingModels from vllm.entrypoints.openai.models.protocol import BaseModelPath engine = AsyncLLMEngine.from_engine_args(AsyncEngineArgs(model="Qwen/Qwen3-4B-Instruct-2507")) serving_models = OpenAIServingModels( engine_client=engine, base_model_paths=[BaseModelPath(name="my-model", model_path="Qwen/Qwen3-4B-Instruct-2507")], lora_modules=[], ) OpenAIServingChat( engine, models=serving_models, response_role="assistant", request_logger=None, chat_template=None, chat_template_content_format="auto", ) ``` ### Error on v0.18.0+ ``` TypeError: OpenAIServingChat.__init__() missing 1 required keywo...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: mpletion.serving import OpenAIServingChat from vllm.entrypoints.openai.models.serving import OpenAIServingModels from vllm.entrypoints.openai.models.protocol import BaseModelPath engine = AsyncLLMEngine.from_engine_args...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: ving_render` should default to `None` with an internal auto-construction fallback so existing call sites keep working. ### 🐛 Describe the bug N/A ### Before submitting a new issue... - [x] Make sure you already searched...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: that worked on v0.17.0: ```python from vllm.engine.async_llm_engine import AsyncLLMEngine from vllm.engine.arg_utils import AsyncEngineArgs from vllm.entrypoints.openai.chat_completion.serving import OpenAIServingChat f...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: N/A ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: ine, models=serving_models, response_role="assistant", request_logger=None, chat_template=None, chat_template_content_format="auto", ) ``` ### Error on v0.18.0+ ``` TypeError: OpenAIServingChat.__init__() missing 1 requ...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
