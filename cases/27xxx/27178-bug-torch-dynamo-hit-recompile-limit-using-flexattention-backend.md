# vllm-project/vllm#27178: [Bug]: torch._dynamo hit recompile_limit using FlexAttention backend

| 字段 | 值 |
| --- | --- |
| Issue | [#27178](https://github.com/vllm-project/vllm/issues/27178) |
| 状态 | open |
| 标签 | bug;torch.compile;unstale |
| 评论 | 7; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | attention_kv_cache;ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | attention;cuda;operator;sampling;triton |
| 症状 | build_error;nan_inf |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: torch._dynamo hit recompile_limit using FlexAttention backend

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug I'm serving Phi 3.5 at fp32 (debugging some numerical issues): ``` vllm serve microsoft/Phi-3.5-mini-instruct --dtype float32 --max-model-len 16000 -tp 4 ``` and hitting it with guidellm: ``` guidellm benchmark --target "URL" --rate-type concurrent --rate 64 --data "prompt_tokens=3677,prompt_tokens_stdev=1687,prompt_tokens_min=999,prompt_tokens_max=9689,output_tokens=584,output_tokens_stdev=267,output_tokens_min=1,output_tokens_max=1024" --max-requests 1000 ``` I'm seeing the following: ``` (Worker_TP0 pid=10585) [rank0]:W1018 04:27:34.433000 10585 torch/_dynamo/convert_frame.py:1016] [1/8] torch._dynamo hit config.recompile_limit (8) (Worker_TP0 pid=10585) [rank0]:W1018 04:27:34.433000 10585 torch/_dynamo/convert_frame.py:1016] [1/8] function: 'create_block_mask' (/usr/local/lib/python3.12/dist-packages/torch/nn/attention/flex_attention.py:832) (Worker_TP0 pid=10585) [rank0]:W1018 04:27:34.433000 10585 torch/_dynamo/convert_frame.py:1016] [1/8] last reason: 1/3: ___check_obj_id(mask_mod.__code__, 140030620899312) (Worker_TP0 pid=10585) [rank0]:W1018 04:27:34.433000 10585 torch/_dynamo/convert_frame.py:1016] [1/8] To log all reco...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: [Bug]: torch._dynamo hit recompile_limit using FlexAttention backend bug;torch.compile;unstale ### Your current environment ### 🐛 Describe the bug I'm serving Phi 3.5 at fp32 (debugging some numerical issues): ``` vllm...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 3: namo hit recompile_limit using FlexAttention backend bug;torch.compile;unstale ### Your current environment ### 🐛 Describe the bug I'm serving Phi 3.5 at fp32 (debugging some numerical issues): ``` vllm serve microsoft/...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 2: [Bug]: torch._dynamo hit recompile_limit using FlexAttention backend bug;torch.compile;unstale ### Your current environment ### 🐛 Describe the bug I'm serving Phi 3.5 at fp32 (debugging some numerical issues): ``` vllm...
- [Bitwise 确定性与数值等价](../patterns/bitwise_determinism_equivalence.md) - 分数 2: ### 🐛 Describe the bug I'm serving Phi 3.5 at fp32 (debugging some numerical issues): ``` vllm serve microsoft/Phi-3.5-mini-instruct --dtype float32 --max-model-len 16000 -tp 4 ``` and hitting it with guidellm: ``` guid...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 2: some numerical issues): ``` vllm serve microsoft/Phi-3.5-mini-instruct --dtype float32 --max-model-len 16000 -tp 4 ``` and hitting it with guidellm: ``` guidellm benchmark --target "URL" --rate-type concurrent --rate 64...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
