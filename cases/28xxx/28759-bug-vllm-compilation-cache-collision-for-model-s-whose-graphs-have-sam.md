# vllm-project/vllm#28759: [Bug]: VLLM compilation cache collision for model's whose graphs have same shape but different input

| 字段 | 值 |
| --- | --- |
| Issue | [#28759](https://github.com/vllm-project/vllm/issues/28759) |
| 状态 | closed |
| 标签 | bug;torch.compile;stale |
| 评论 | 11; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;frontend_api;gemm_linear;hardware_porting;model_support;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cuda;operator;sampling;triton |
| 症状 | build_error;nan_inf |
| 根因提示 | env_dependency;shape |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: VLLM compilation cache collision for model's whose graphs have same shape but different input

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug Using a model that has 2 instances of a model structured like llama's MLP [decoder](https://github.com/vllm-project/vllm/blob/main/vllm/model_executor/models/llama.py#L73) with one having bias weights and the other not having them causes a vllm cache collision. This cache collision results in an fx graph being used during a forward pass that causes an arity error due to expecting different inputs. fx/graph_module.py stacktrace snippet: ``` [rank0]: File "/home/ /.cache/vllm/torch_compile_cache/db51c87ae7/rank_0_0/inductor_cache/3w/c3wihxyfg33qoai6h63q43gxf4r2q7yihmvq3sy7y7tlv7sqcjun.py", line 154, in call [rank0]: arg0_1, arg1_1, arg2_1, arg3_1, arg4_1, arg5_1, arg6_1 = args [rank0]: ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ [rank0]: ValueError: not enough values to unpack (expected 7, got 6) ``` ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: n for model's whose graphs have same shape but different input bug;torch.compile;stale ### Your current environment ### 🐛 Describe the bug Using a model that has 2 instances of a model structured like llama's MLP [decod...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 3: del's whose graphs have same shape but different input bug;torch.compile;stale ### Your current environment ### 🐛 Describe the bug Using a model that has 2 instances of a model structured like llama's MLP [decoder](http...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: ``` ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: [Bug]: VLLM compilation cache collision for model's whose graphs have same shape but different input bug;torch.compile;stale ### Your current environment ### 🐛 Describe the bug Using a model that has 2 instances of a mo...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: odel_support;sampling_logits;speculative_decoding cuda;operator;sampling;triton build_error;nan_inf env_dependency;shape Your current environment

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
