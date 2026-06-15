# vllm-project/vllm#16607: [Bug]: `llm.llm_engine.model_executor.driver_worker.model_runner.model` is not accessible when using vLLM v1 engine

| 字段 | 值 |
| --- | --- |
| Issue | [#16607](https://github.com/vllm-project/vllm/issues/16607) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 10; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: `llm.llm_engine.model_executor.driver_worker.model_runner.model` is not accessible when using vLLM v1 engine

### Issue 正文摘录

Hi vLLM team, I noticed an inconsistency in the behavior of the `LLM` object between v0 and v1 engines when trying to access the underlying model. In vLLM v0 (`VLLM_USE_V1=0`), the following code correctly retrieves the model instance: ```python llm = LLM(**engine_args) print(llm.llm_engine.model_executor.driver_worker.model_runner.model) ``` However, when using v1 (`VLLM_USE_V1=1`), this same code fails with an `AttributeError` because `.model_executor` no longer exists on `llm.llm_engine`. I understand the architecture has changed in v1 (now using `EngineCore`), but it would be extremely useful to have a public and stable way to access the underlying model instance for inspection or manipulation (e.g., for debugging or weight loading). --- **Feature Request / Bug?** - ❓ Is there an officially supported way in v1 to access the underlying model instance like we could in v0? - 🙏 If not, could you consider adding an API like `llm.get_model()` or expose a similar field? - 🧪 For context, this is from a script used for audio-language inference using models like `Qwen2.5-Omni`. --- Command to reproduce: ```bash VLLM_USE_V1=1 python examples/offline_inference/audio_language.py --model-ty...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: [Bug]: `llm.llm_engine.model_executor.driver_worker.model_runner.model` is not accessible when using vLLM v1 engine bug Hi vLLM team, I noticed an inconsistency in the behavior of the `LLM` object between v0 and v1 engi...
- [Bitwise 确定性与数值等价](../patterns/bitwise_determinism_equivalence.md) - 分数 1: dio-language inference using models like `Qwen2.5-Omni`. --- Command to reproduce: ```bash VLLM_USE_V1=1 python examples/offline_inference/audio_language.py --model-type qwen2_5_omni ``` Thanks for the great work on vLL...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: r weight loading). --- **Feature Request / Bug?** - ❓ Is there an officially supported way in v1 to access the underlying model instance like we could in v0? - 🙏 If not, could you consider adding an API like `llm.get_mo...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: .model_executor` no longer exists on `llm.llm_engine`. I understand the architecture has changed in v1 (now using `EngineCore`), but it would be extremely useful to have a public and stable way to access the underlying...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: or manipulation (e.g., for debugging or weight loading). --- **Feature Request / Bug?** - ❓ Is there an officially supported way in v1 to access the underlying model instance like we could in v0? - 🙏 If not, could you c...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
