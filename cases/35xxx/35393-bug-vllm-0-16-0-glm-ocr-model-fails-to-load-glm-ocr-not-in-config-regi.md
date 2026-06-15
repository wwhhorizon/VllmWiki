# vllm-project/vllm#35393: [Bug]: vllm 0.16.0 GLM-OCR model fails to load - glm_ocr not in _CONFIG_REGISTRY, requires transformers >= 5.1

| 字段 | 值 |
| --- | --- |
| Issue | [#35393](https://github.com/vllm-project/vllm/issues/35393) |
| 状态 | open |
| 标签 | bug;stale |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: vllm 0.16.0 GLM-OCR model fails to load - glm_ocr not in _CONFIG_REGISTRY, requires transformers >= 5.1

### Issue 正文摘录

### Your current environment - vLLM: `v0.16.0` (also reproducible on main) - transformers: `4.56.x` (as pinned by vllm requirements: >= 4.56.0, = 4.56.0, = 5.1.0, the config lookup fails Additionally, the model code imports from transformers at type-check time: ```python if TYPE_CHECKING: from transformers.models.glm_ocr.configuration_glm_ocr import GlmOcrVisionConfig ``` This module path does not exist in transformers < 5. ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: 1 bug;stale ### Your current environment - vLLM: `v0.16.0` (also reproducible on main) - transformers: `4.56.x` (as pinned by vllm requirements: >= 4.56.0, = 4.56.0, = 5.1.0, the config lookup fails Additionally, the mo...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: [Bug]: vllm 0.16.0 GLM-OCR model fails to load - glm_ocr not in _CONFIG_REGISTRY, requires transformers >= 5.1 bug;stale ### Your current environment - vLLM: `v0.16.0` (also reproducible on main) - transformers: `4.56.x...
- [Bitwise 确定性与数值等价](../patterns/bitwise_determinism_equivalence.md) - 分数 1: s >= 5.1 bug;stale ### Your current environment - vLLM: `v0.16.0` (also reproducible on main) - transformers: `4.56.x` (as pinned by vllm requirements: >= 4.56.0, = 4.56.0, = 5.1.0, the config lookup fails Additionally,...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: 5. ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), whi...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: load - glm_ocr not in _CONFIG_REGISTRY, requires transformers >= 5.1 bug;stale ### Your current environment - vLLM: `v0.16.0` (also reproducible on main) - transformers: `4.56.x` (as pinned by vllm requirements: >= 4.56...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
