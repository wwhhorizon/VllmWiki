# vllm-project/vllm#28273: [Bug]: IOProcessor `pre_process_async` return type not handled correctly in `serving_pooling.py`

| 字段 | 值 |
| --- | --- |
| Issue | [#28273](https://github.com/vllm-project/vllm/issues/28273) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | development |
| 工作域 | ci_build;distributed_parallel;frontend_api;hardware_porting;model_support |
| 子分类 | env_compat |
| Operator 关键词 | cuda;operator;triton |
| 症状 | build_error |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: IOProcessor `pre_process_async` return type not handled correctly in `serving_pooling.py`

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug ### Summary The `OpenAIServingPooling.create_pooling()` method does not correctly handle the `Union[PromptType, Sequence[PromptType]]` return type from `IOProcessor.pre_process_async()`. When a single `PromptType` is returned (instead of a sequence), the code attempts to enumerate over a `TypedDict`, causing unexpected behavior. ### The Issue The `IOProcessor` interface defines `pre_process_async()` with this return type: ```python async def pre_process_async( self, prompt: IOProcessorInput, request_id: Optional[str] = None, **kwargs, ) -> Union[PromptType, Sequence[PromptType]]: ``` **Source:** https://github.com/vllm-project/vllm/blob/v0.10.2/vllm/plugins/io_processors/interface.py#L31-L37 However, `serving_pooling.py` directly enumerates the result without checking whether it's a single object or a sequence: ```python # Line 129-130 engine_prompts = await self.io_processor.pre_process_async( prompt=validated_prompt, request_id=request_id) # Line 172 - No check for single vs sequence for i, engine_prompt in enumerate(engine_prompts): request_id_item = f"{request_id}-{i}" # ... ``` **Source:** - https://github.com/vllm-project/v...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 5: .) instead of treating it as a single prompt object. ### Minimal Reproducible Example ```python from vllm.plugins.io_processors import IOProcessor from vllm.inputs import TextPrompt from vllm.config import VllmConfig fr...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: for a text prompt.""" prompt: str multi_modal_data: NotRequired["MultiModalDataDict"] # ... ``` **Source:** https://github.com/vllm-project/vllm/blob/v0.10.2/vllm/inputs/data.py#L14-L24 When `pre_process_async()` return...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: wrapped in list ``` ## Before submitting a new issue... - [x] I have searched the existing issues and didn't find a similar one - [x] I have consulted the documentation ## Additional Context This bug affects anyone impl...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: buted_parallel;frontend_api;hardware_porting;model_support cuda;operator;triton build_error env_dependency Your current environment
- [Bitwise 确定性与数值等价](../patterns/bitwise_determinism_equivalence.md) - 分数 1: "`, etc.) instead of treating it as a single prompt object. ### Minimal Reproducible Example ```python from vllm.plugins.io_processors import IOProcessor from vllm.inputs import TextPrompt from vllm.config import VllmCo...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
