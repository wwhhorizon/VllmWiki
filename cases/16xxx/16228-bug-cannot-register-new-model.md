# vllm-project/vllm#16228: [Bug]: Cannot register new model

| 字段 | 值 |
| --- | --- |
| Issue | [#16228](https://github.com/vllm-project/vllm/issues/16228) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 8; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: Cannot register new model

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug I am trying to register a new model architecture that is currently not support in vLLM. ```python AutoConfig.register("model_name", MyModelConfig, exist_ok=True) ModelRegistry.register_model("MyModelForCausalLM", MyModelForCausalLM) llm = LLM(model=model_path) llm.generate("Hello") ``` But this fails with ``` ValueError: MyModelForCausalLM has no vLLM implementation and the Transformers implementation is not compatible with vLLM. Try setting VLLM_USE_V1=0. ``` Seems that the issue is that when I register my model architecture on the driver side, the `ModelRegistry` dict gets updated. But when loading the model on the worker side, if I print out `ModelRegistry` in the `vllm.model_executor.model_loader.utils.get_model_architecture` function, the registry does not show the new model architecture that I added. I believe the `ModelRegistry` on the driver side has to be serialized and explicitly passed to the workers? ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which ca...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: [Bug]: Cannot register new model bug ### Your current environment ### 🐛 Describe the bug I am trying to register a new model architecture that is currently not support in vLLM. ```python AutoConfig.register("model_name"...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: eve the `ModelRegistry` on the driver side has to be serialized and explicitly passed to the workers? ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: ironment ### 🐛 Describe the bug I am trying to register a new model architecture that is currently not support in vLLM. ```python AutoConfig.register("model_name", MyModelConfig, exist_ok=True) ModelRegistry.register_mo...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
