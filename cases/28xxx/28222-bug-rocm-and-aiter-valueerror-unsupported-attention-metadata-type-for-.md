# vllm-project/vllm#28222: [Bug]: ROCm and AITER ValueError: Unsupported attention metadata type for speculative decoding with num_speculative_tokens > 1

| 字段 | 值 |
| --- | --- |
| Issue | [#28222](https://github.com/vllm-project/vllm/issues/28222) |
| 状态 | closed |
| 标签 | bug;rocm;stale |
| 评论 | 6; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | attention_kv_cache;distributed_parallel;frontend_api;hardware_porting;model_support;speculative_decoding |
| 子分类 | kernel_eff |
| Operator 关键词 | attention |
| 症状 | build_error |
| 根因提示 | memory_layout |
| 硬件范围 | amd |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: ROCm and AITER ValueError: Unsupported attention metadata type for speculative decoding with num_speculative_tokens > 1

### Issue 正文摘录

### Your current environment I'm leveraging vLLM for DeepSeek V3 MTP serving on AMD MI300Xs. ### 🐛 Describe the bug Hi, I'm trying to enable MTP for DeepSeek V3 using AITER backend for a better performance running on AMD GPUs. However, there is a bug triggered when I set up the attention backend as aiter and num_speculative_tokens as 3, and the bug information is as below: > **ValueError: Unsupported attention metadata type for speculative decoding with num_speculative_tokens > 1:** The command for launching the server using vLLM is as below: ```text export VLLM_ATTENTION_BACKEND=ROCM_AITER vllm serve /models/DeepSeek-V3/ \ --tensor-parallel-size 8 \ --max-model-len 65536 \ --max-num-seqs 512 \ --max-num-batched-tokens 32768 \ --disable-log-requests \ --port 8001 \ --block-size 1 \ --compilation-config '{"full_cuda_graph":false,"cudagraph_mode":"PIECEWISE"}' \ --trust-remote-code \ --speculative_config '{"num_speculative_tokens": 2}' \ --gpu-memory-utilization 0.85 ``` The client command for benchmarking: ```text vllm bench serve \ --backend openai \ --model /models/DeepSeek-V3/ \ --tokenizer /models/DeepSeek-V3/ \ --dataset-name random \ --num-prompts 100 \ --save-result \ --trus...

## 候选优化模式

- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 5: [Bug]: ROCm and AITER ValueError: Unsupported attention metadata type for speculative decoding with num_speculative_tokens > 1 bug;rocm;stale ### Your current environment I'm leveraging vLLM for DeepSeek V3 MTP serving...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 4: [Bug]: ROCm and AITER ValueError: Unsupported attention metadata type for speculative decoding with num_speculative_tokens > 1 bug;rocm;stale ### Your current environment I'm leveraging vLLM for DeepSeek V3 MTP serving...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: ttention backend as aiter and num_speculative_tokens as 3, and the bug information is as below: > **ValueError: Unsupported attention metadata type for speculative decoding with num_speculative_tokens > 1:** The command...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 3: Bug]: ROCm and AITER ValueError: Unsupported attention metadata type for speculative decoding with num_speculative_tokens > 1 bug;rocm;stale ### Your current environment I'm leveraging vLLM for DeepSeek V3 MTP serving o...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 2: [Bug]: ROCm and AITER ValueError: Unsupported attention metadata type for speculative decoding with num_speculative_tokens > 1 bug;rocm;stale ### Your current environment I'm leveraging vLLM for DeepSeek V3 MTP serving...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
