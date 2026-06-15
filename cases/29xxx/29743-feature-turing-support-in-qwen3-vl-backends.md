# vllm-project/vllm#29743: [Feature]: Turing support in Qwen3-VL backends

| 字段 | 值 |
| --- | --- |
| Issue | [#29743](https://github.com/vllm-project/vllm/issues/29743) |
| 状态 | closed |
| 标签 | feature request;stale |
| 评论 | 7; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | attention_kv_cache;ci_build;distributed_parallel;frontend_api;gemm_linear;hardware_porting;model_support;moe;quantization;sampling_logits;scheduler_memory;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | attention;cuda;operator;quantization;sampling;triton |
| 症状 | build_error;crash;nan_inf;slowdown |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Feature]: Turing support in Qwen3-VL backends

### Issue 正文摘录

### 🚀 The feature, motivation and pitch According to the current Qwen3-VL dense implementation, there is no supported backend for Turing GPUs (SM75, e.g., T4 and T4G). https://github.com/vllm-project/vllm/blob/2afcec4decbbd64cf8da20d49281f828dd136c27/vllm/model_executor/models/qwen3_vl.py#L379-L386 `FLASH_ATTN` is only supported for >= Ampere (sm80). `XFORMERS` does not work with FA2 in the same way, according to https://github.com/facebookresearch/xformers/issues/795. Other attentions, such as FlashInfer and Triton Attention, do not work, since there is no condition to calculate `context_layer`. https://github.com/vllm-project/vllm/blob/2afcec4decbbd64cf8da20d49281f828dd136c27/vllm/model_executor/models/qwen2_5_vl.py#L397-L425 Additionally, `TORCH_SDPA` is no longer functional, as it is no longer registered. https://github.com/vllm-project/vllm/blob/2afcec4decbbd64cf8da20d49281f828dd136c27/vllm/attention/backends/registry.py#L57 There is a similar issue at https://discuss.vllm.ai/t/build-issues-when-serving-gpt-oss-20b-on-tesla-t4-gpus-with-vllm/ for GPT-OSS. I would appreciate it if there were at least one backend that runs on Turing GPUs. Command: ```bash vllm serve "Qwen/Qwen3...

## 候选优化模式

- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 4: -VL dense implementation, there is no supported backend for Turing GPUs (SM75, e.g., T4 and T4G). https://github.com/vllm-project/vllm/blob/2afcec4decbbd64cf8da20d49281f828dd136c27/vllm/model_executor/models/qwen3_vl.py...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 4: [Feature]: Turing support in Qwen3-VL backends feature request;stale ### 🚀 The feature, motivation and pitch According to the current Qwen3-VL dense implementation, there is no supported backend for Turing GPUs (SM75, e...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 3: [Feature]: Turing support in Qwen3-VL backends feature request;stale ### 🚀 The feature, motivation and pitch According to the current Qwen3-VL dense implementation, there is no supported backend for Turing GPUs (SM75, e...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: s/registry.py#L57 There is a similar issue at https://discuss.vllm.ai/t/build-issues-when-serving-gpt-oss-20b-on-tesla-t4-gpus-with-vllm/ for GPT-OSS. I would appreciate it if there were at least one backend that runs o...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: [Feature]: Turing support in Qwen3-VL backends feature request;stale ### 🚀 The feature, motivation and pitch According to the current Qwen3-VL dense implementation, there is no supported backend for Turing GPUs (SM75, e...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
