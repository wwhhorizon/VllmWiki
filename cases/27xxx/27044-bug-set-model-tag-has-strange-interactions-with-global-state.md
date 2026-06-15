# vllm-project/vllm#27044: [Bug]: `set_model_tag` has strange interactions with global state

| 字段 | 值 |
| --- | --- |
| Issue | [#27044](https://github.com/vllm-project/vllm/issues/27044) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 4; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;frontend_api;gemm_linear;hardware_porting;model_support;multimodal_vlm;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cuda;operator;sampling;triton |
| 症状 | build_error;nan_inf |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: `set_model_tag` has strange interactions with global state

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug We would like to use `set_model_tag` to support compile usage in different ways (currently, it is only used for Eagle but we can in the future use it for multimodal compilation as well) However, the current implementation modifies a global `model-tag` here https://github.com/vllm-project/vllm/blob/7bb736d00e81c6cd893007323641dd974d921715/vllm/compilation/backends.py#L464 This means when importing `set_model_tag`, we initialize this state and may cause failures in Eagle model initializations/tests - see https://github.com/vllm-project/vllm/blob/7bb736d00e81c6cd893007323641dd974d921715/vllm/model_executor/models/gemma3n.py#L807 We should investigate fixing this integration in order to have set_model_tag not cause test failures ### Repro: Import `from vllm.compilation.backends import set_model_tag` at top level in either `qwen2_5_vl.py` or `gemma3n.py` and then run ``` pytest tests/models/test_initialization.py::test_can_initialize_large_subset ``` For instance, adding in qwen_2_5_vl then running ``` pytest tests/models/test_initialization.py::test_can_initialize_large_subset[Eagle3Qwen2_5vlForCausalLM] ``` Results in https://gist.g...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 5: ### 🐛 Describe the bug We would like to use `set_model_tag` to support compile usage in different ways (currently, it is only used for Eagle but we can in the future use it for multimodal compilation as well) However, t...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 5: [Bug]: `set_model_tag` has strange interactions with global state bug;stale ### Your current environment ### 🐛 Describe the bug We would like to use `set_model_tag` to support compile usage in different ways (currently,...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 2: ject/vllm/blob/7bb736d00e81c6cd893007323641dd974d921715/vllm/compilation/backends.py#L464 This means when importing `set_model_tag`, we initialize this state and may cause failures in Eagle model initializations/tests -...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: db1 ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: [Bug]: `set_model_tag` has strange interactions with global state bug;stale ### Your current environment ### 🐛 Describe the bug We would like to use `set_model_tag` to support compile usage in different ways (currently,...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
