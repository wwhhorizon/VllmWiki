# vllm-project/vllm#18044: [Bug]: Serve Qwen3 MOE GPTQ models raise `torch._dynamo.exc.Unsupported` error

| 字段 | 值 |
| --- | --- |
| Issue | [#18044](https://github.com/vllm-project/vllm/issues/18044) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 7; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;hardware_porting;model_support;moe;quantization;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cuda;moe;operator;quantization;sampling;triton |
| 症状 | build_error;nan_inf |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Serve Qwen3 MOE GPTQ models raise `torch._dynamo.exc.Unsupported` error

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug Attempt to `vllm serve Qwen/Qwen3-30B-A3B-GPTQ-Int4` raises `torch._dynamo.exc.Unsupported: Observed exception`. Not sure if it is a vllm or pytorch compile bug tho. Log file **without** VLLM_LOGGING_LEVEL=DEBUG, VLLM_TRACE_FUNCTION=1 and TORCHDYNAMO_VERBOSE=1: [vllm_qwen3moe_gptq_error.log](https://github.com/user-attachments/files/20180658/vllm_qwen3moe_gptq_error.log) Log file **with** VLLM_LOGGING_LEVEL=DEBUG, VLLM_TRACE_FUNCTION=1 and TORCHDYNAMO_VERBOSE=1: [vllm_qwen3moe_gptq_error_long.log](https://github.com/user-attachments/files/20180713/vllm_qwen3moe_gptq_error_long.log) ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: xc.Unsupported: Observed exception`. Not sure if it is a vllm or pytorch compile bug tho. Log file **without** VLLM_LOGGING_LEVEL=DEBUG, VLLM_TRACE_FUNCTION=1 and TORCHDYNAMO_VERBOSE=1: [vllm_qwen3moe_gptq_error.log](ht...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 3: ### 🐛 Describe the bug Attempt to `vllm serve Qwen/Qwen3-30B-A3B-GPTQ-Int4` raises `torch._dynamo.exc.Unsupported: Observed exception`. Not sure if it is a vllm or pytorch compile bug tho. Log file **without** VLLM_LOGG...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: og) ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: [Bug]: Serve Qwen3 MOE GPTQ models raise `torch._dynamo.exc.Unsupported` error bug;stale ### Your current environment ### 🐛 Describe the bug Attempt to `vllm serve Qwen/Qwen3-30B-A3B-GPTQ-Int4` raises `torch._dynamo.exc...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: ve Qwen3 MOE GPTQ models raise `torch._dynamo.exc.Unsupported` error bug;stale ### Your current environment ### 🐛 Describe the bug Attempt to `vllm serve Qwen/Qwen3-30B-A3B-GPTQ-Int4` raises `torch._dynamo.exc.Unsupport...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
