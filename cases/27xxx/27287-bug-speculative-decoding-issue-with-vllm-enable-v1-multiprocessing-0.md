# vllm-project/vllm#27287: [Bug]: Speculative Decoding Issue with VLLM_ENABLE_V1_MULTIPROCESSING=0

| 字段 | 值 |
| --- | --- |
| Issue | [#27287](https://github.com/vllm-project/vllm/issues/27287) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;sampling_logits;scheduler_memory;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cuda;operator;sampling;triton |
| 症状 | build_error;nan_inf |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Speculative Decoding Issue with VLLM_ENABLE_V1_MULTIPROCESSING=0

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug ### Description of the Issue The speculative decoding doesn't seem to work properly when setting `VLLM_ENABLE_V1_MULTIPROCESSING=0` + Example commands with multi_proc disabled (spec doesn't work) ``` VLLM_ENABLE_V1_MULTIPROCESSING=0 python examples/offline_inference/spec_decode.py --method ngram ``` Output ==> ``` ------------------------------------------------- total_num_output_tokens: 247573 num_drafts: 0 num_draft_tokens: 0 num_accepted_tokens: 0 mean acceptance length: 1.00 -------------------------------------------------- acceptance at token 0: 0.00 acceptance at token 1: 0.00 ``` + Example commands with multi_proc enabled (default) (**spec work properly**) ``` python examples/offline_inference/spec_decode.py --method ngram ``` Output ==> ``` -------------------------------------------------- total_num_output_tokens: 248291 num_drafts: 74097 num_draft_tokens: 147899 num_accepted_tokens: 141162 mean acceptance length: 2.91 -------------------------------------------------- acceptance at token 0: 0.96 acceptance at token 1: 0.94 ``` ### Possible Reason It appears that the [`post_step()`](https://github.com/vllm-project/vllm/...

## 候选优化模式

- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 5: [Bug]: Speculative Decoding Issue with VLLM_ENABLE_V1_MULTIPROCESSING=0 bug;stale ### Your current environment ### 🐛 Describe the bug ### Description of the Issue The speculative decoding doesn't seem to work properly w...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: test/), which can answer lots of frequently asked questions. correctness ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;sampling_logits;scheduler_memory;speculative_decoding cuda;operator;samp...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: 041 ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: ling_logits;scheduler_memory;speculative_decoding cuda;operator;sampling;triton build_error;nan_inf env_dependency Your current environment
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: puts: - outputs, _ = self.engine_core.step_fn() + outputs, model_executed = self.engine_core.step_fn() + self.engine_core.post_step(model_executed) return outputs and outputs.get(0) or EngineCoreOutputs() ``` ### Refere...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
