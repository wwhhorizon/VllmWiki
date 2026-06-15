# vllm-project/vllm#15251: [Bug]: `VLLM_USE_V1` + `TORCH_SDPA` regression in v0.8

| 字段 | 值 |
| --- | --- |
| Issue | [#15251](https://github.com/vllm-project/vllm/issues/15251) |
| 状态 | closed |
| 标签 | bug;stale |
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

> [Bug]: `VLLM_USE_V1` + `TORCH_SDPA` regression in v0.8

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug With `vllm==0.7.3` the below works: ```none VLLM_USE_V1=1 VLLM_ATTENTION_BACKEND=TORCH_SDPA vllm serve \ /path/to/ckpt-123 --max-model-len 2816 --tensor-parallel-size 8 --tokenizer /path/to/ckpt-123 ``` However, with `vllm==0.8.1`, the same command gives the below ``` NotImplementedError: VLLM_USE_V1=1 is not supported with VLLM_ATTENTION_BACKEND=TORCH_SDPA. ``` This seems to have been a regression from https://github.com/vllm-project/vllm/pull/13726 ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: test/), which can answer lots of frequently asked questions. correctness ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;sampling_logits;speculative_decoding cuda;operator;sampling;triton build...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 2: ith `vllm==0.7.3` the below works: ```none VLLM_USE_V1=1 VLLM_ATTENTION_BACKEND=TORCH_SDPA vllm serve \ /path/to/ckpt-123 --max-model-len 2816 --tensor-parallel-size 8 --tokenizer /path/to/ckpt-123 ``` However, with `vl...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: 726 ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: [Bug]: `VLLM_USE_V1` + `TORCH_SDPA` regression in v0.8 bug;stale ### Your current environment ### 🐛 Describe the bug With `vllm==0.7.3` the below works: ```none VLLM_USE_V1=1 VLLM_ATTENTION_BACKEND=TORCH_SDPA vllm serve...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 2: [Bug]: `VLLM_USE_V1` + `TORCH_SDPA` regression in v0.8 bug;stale ### Your current environment ### 🐛 Describe the bug With `vllm==0.7.3` the below works: ```none VLLM_USE_V1=1 VLLM_ATTENTION_BACKEND=TORCH_SDPA vllm serve...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
