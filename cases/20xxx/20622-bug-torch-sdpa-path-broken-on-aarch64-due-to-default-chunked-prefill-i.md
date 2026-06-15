# vllm-project/vllm#20622: [Bug]: Torch SDPA path broken on AArch64 due to default chunked_prefill in vLLM Engine V1

| 字段 | 值 |
| --- | --- |
| Issue | [#20622](https://github.com/vllm-project/vllm/issues/20622) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 4; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | attention_kv_cache;ci_build;frontend_api;hardware_porting;model_support;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | attention;cuda;operator;sampling |
| 症状 | build_error;nan_inf |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Torch SDPA path broken on AArch64 due to default chunked_prefill in vLLM Engine V1

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug Description: After rebasing PR #17112 on the mainline, We have encountered a new issue stemming from recent changes in the default engine behavior in vLLM. It appears that the vLLM Engine V1 is now used by default for the LLM.generate() API, and this engine enables chunked_prefill by default. Due to this updated behavior, the Torch SDPA path is currently broken on the AArch64 backend. **Issue Details:** • The condition in the following line evaluates to False on AArch64: 🔗 [torch_sdpa.py#L391](https://github.com/vllm-project/vllm/blob/923147b5e8551887fd64a0fc242c361d5216e1d7/vllm/attention/backends/torch_sdpa.py#L391) • As a result, the fallback path attempts to use Intel IPEX without checking the _use_ipex flag. • There is currently no valid chunked_prefill attention path enabled for AArch64. **Impact:** • Any LLM.generate() invocation under the V1 engine on AArch64 fails due to the lack of a valid attention backend. **How to Reproduce:** 1. Apply PR #17112: 2. Convert the model using the script shared in the comment here: https://github.com/vllm-project/vllm/pull/17112#issuecomment-2848271426 3. Run the model using the LLM.gene...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: nswer lots of frequently asked questions. correctness attention_kv_cache;ci_build;frontend_api;hardware_porting;model_support;sampling_logits;speculative_decoding attention;cuda;operator;sampling build_error;nan_inf dty...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 2: updated behavior, the Torch SDPA path is currently broken on the AArch64 backend. **Issue Details:** • The condition in the following line evaluates to False on AArch64: 🔗 [torch_sdpa.py#L391](https://github.com/vllm-pr...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 2: LLM.generate() API on an AArch64 machine: • Ensure the model is run in float32 (torch.float32) datatype. • Confirm that vLLM Engine V1 is active (default behavior as of recent commits). ### Before submitting a new issue...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: [Bug]: Torch SDPA path broken on AArch64 due to default chunked_prefill in vLLM Engine V1 bug ### Your current environment ### 🐛 Describe the bug Description: After rebasing PR #17112 on the mainline, We have encountere...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: [Bug]: Torch SDPA path broken on AArch64 due to default chunked_prefill in vLLM Engine V1 bug ### Your current environment ### 🐛 Describe the bug Description: After rebasing PR #17112 on the mainline, We have encountere...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
