# vllm-project/vllm#26002: [Bug]: `eos_token_id` from `generation_config.json` ignored when `n>1` in V1 engine

| 字段 | 值 |
| --- | --- |
| Issue | [#26002](https://github.com/vllm-project/vllm/issues/26002) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cuda;operator;sampling;triton |
| 症状 | build_error;nan_inf |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: `eos_token_id` from `generation_config.json` ignored when `n>1` in V1 engine

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug Currently, vLLM seems to be applying different sampling parameters between `n=1` and `n>1` cases. In `n=1` case, `request.sampling_params` is generated in `self.processor.process_inputs`, which takes care of `generation_config.json` by [calling `sampling_params.update_from_generation_config`](https://github.com/vllm-project/vllm/blob/99028fda449d920237561da163daf2e908e25535/vllm/v1/engine/processor.py#L416): https://github.com/vllm-project/vllm/blob/99028fda449d920237561da163daf2e908e25535/vllm/v1/engine/async_llm.py#L283-L290 However, in `n>1` case, `sampling_params` of each child request are overwritten with the one from parent request (`child_request.sampling_params = params`), where `params` do not reflect `generation_config.json`: https://github.com/vllm-project/vllm/blob/99028fda449d920237561da163daf2e908e25535/vllm/v1/engine/async_llm.py#L292-L300 This is causing different sampling options being applied between `n=1` and `n>1` cases. This issue can easily be confirmed by adding lines like `print('n=1', f'{request.sampling_params.stop_token_ids=}')` and `print('n>1:', f'{child_request.sampling_params.stop_token_ids=}')`. ``...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: test/), which can answer lots of frequently asked questions. correctness ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;sampling_logits;speculative_decoding cuda;operator;sampling;triton build...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: [Bug]: `eos_token_id` from `generation_config.json` ignored when `n>1` in V1 engine bug ### Your current environment ### 🐛 Describe the bug Currently, vLLM seems to be applying different sampling parameters between `n=1...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: ``` ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: rent sampling parameters between `n=1` and `n>1` cases. In `n=1` case, `request.sampling_params` is generated in `self.processor.process_inputs`, which takes care of `generation_config.json` by [calling `sampling_params...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: odel_support;sampling_logits;speculative_decoding cuda;operator;sampling;triton build_error;nan_inf env_dependency Your current environment

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
