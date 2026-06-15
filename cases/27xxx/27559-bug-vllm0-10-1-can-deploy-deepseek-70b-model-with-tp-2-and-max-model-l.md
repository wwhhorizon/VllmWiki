# vllm-project/vllm#27559: [Bug]: vllm0.10.1 can deploy deepseek-70b model with tp=2 and max-model-len 20000 on the machine with two NVIDIA A800(80GiB)  , But vllm 0.11.0 failed

| 字段 | 值 |
| --- | --- |
| Issue | [#27559](https://github.com/vllm-project/vllm/issues/27559) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | attention_kv_cache;ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;moe;quantization;sampling_logits;scheduler_memory;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | attention;cache;cuda;operator;quantization;sampling;triton |
| 症状 | build_error;crash;nan_inf |
| 根因提示 | dtype;env_dependency;memory_layout;shape |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: vllm0.10.1 can deploy deepseek-70b model with tp=2 and max-model-len 20000 on the machine with two NVIDIA A800(80GiB)  , But vllm 0.11.0 failed

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug In above machine, I update the vllm **0.10.1** to **0.11.0**. However, I use the same start_vllm.sh which will show later had succed in 0.10.1, **but in 0.11.0 failed**. The log file said that the memory is not enough. More details will show on the down file. The model i use is which deepseek-70b downloaded from huggingface. In summary, i use the same start_vllm.sh in 0.10.1, it can successfully run and do inference, but in 0.11.1 it failed. Thanks! ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: nswer lots of frequently asked questions. correctness attention_kv_cache;ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;moe;quantization;sampling_logits;scheduler_memory;speculative_decoding a...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 3: on the machine with two NVIDIA A800(80GiB) , But vllm 0.11.0 failed bug;stale ### Your current environment ### 🐛 Describe the bug In above machine, I update the vllm **0.10.1** to **0.11.0**. However, I use the same sta...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 2: ild;distributed_parallel;frontend_api;hardware_porting;model_support;moe;quantization;sampling_logits;scheduler_memory;speculative_decoding attention;cache;cuda;operator;quantization;sampling;triton build_error;crash;na...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: ks! ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: [Bug]: vllm0.10.1 can deploy deepseek-70b model with tp=2 and max-model-len 20000 on the machine with two NVIDIA A800(80GiB) , But vllm 0.11.0 failed bug;stale ### Your current environment ### 🐛 Describe the bug In abov...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
