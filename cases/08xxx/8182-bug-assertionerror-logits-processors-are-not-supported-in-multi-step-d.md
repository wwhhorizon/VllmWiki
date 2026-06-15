# vllm-project/vllm#8182: [Bug]: AssertionError: Logits Processors are not supported in multi-step decoding

| 字段 | 值 |
| --- | --- |
| Issue | [#8182](https://github.com/vllm-project/vllm/issues/8182) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 4; 本地原始数据只有评论数量，没有评论正文 |
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

> [Bug]: AssertionError: Logits Processors are not supported in multi-step decoding

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug I pulled the latest version and added `--num-scheduler-steps 8` to my command. Then I got the above error. Here is my full command. ```shell > --host 0.0.0.0 --port ${PORT} --api-key ${API_KEY} --max-model-len ${MAX_MODEL_LEN} --tensor-parallel-size ${TP} --gpu-memory-utilization ${GMU} --served-model-name ${SERVED_MODEL_NAME} --seed 42 --disable-log-requests --enable-prefix-caching --model ${MODEL} --num-scheduler-steps 8 ``` ### Before submitting a new issue... - [X] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: Your current environment ### 🐛 Describe the bug I pulled the latest version and added `--num-scheduler-steps 8` to my command. Then I got the above error. Here is my full command. ```shell > --host 0.0.0.0 --port ${PORT...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 4: ionError: Logits Processors are not supported in multi-step decoding bug;stale ### Your current environment ### 🐛 Describe the bug I pulled the latest version and added `--num-scheduler-steps 8` to my command. Then I go...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: ``` ### Before submitting a new issue... - [X] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: ling_logits;scheduler_memory;speculative_decoding cuda;operator;sampling;triton build_error;nan_inf env_dependency Your current environment
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: host 0.0.0.0 --port ${PORT} --api-key ${API_KEY} --max-model-len ${MAX_MODEL_LEN} --tensor-parallel-size ${TP} --gpu-memory-utilization ${GMU} --served-model-name ${SERVED_MODEL_NAME} --seed 42 --disable-log-requests --...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
