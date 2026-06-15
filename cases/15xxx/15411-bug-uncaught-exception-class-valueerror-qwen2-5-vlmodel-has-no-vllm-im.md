# vllm-project/vllm#15411: [Bug]: Uncaught exception | <class 'ValueError'>; Qwen2_5_VLModel has no vLLM implementation and the Transformers implementation is not compatible with vLLM

| 字段 | 值 |
| --- | --- |
| Issue | [#15411](https://github.com/vllm-project/vllm/issues/15411) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 15; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | development |
| 工作域 | attention_kv_cache;distributed_parallel;frontend_api;model_support;quantization;scheduler_memory |
| 子分类 | runtime_err |
| Operator 关键词 | attention;cuda;operator;quantization |
| 症状 | crash |
| 根因提示 | dtype;env_dependency;memory_layout |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Uncaught exception \| <class 'ValueError'>; Qwen2_5_VLModel has no vLLM implementation and the Transformers implementation is not compatible with vLLM

### Issue 正文摘录

### Your current environment I just know it's hosted on runpod serverless vLLM latest (today). ### 🐛 Describe the bug When trying to host my finetuned Qwen2.5 VL 7b 4bit dynamic quantization using unsloth, and after I have saved the trained model it as bf16, when I try to host the model, it gives me this error: ```python worker exited with exit code 1 j6zswihe185nfq[warning][rank0]:[W324 18:13:29.115599288 ProcessGroupNCCL.cpp:1250] Warning: WARNING: process group has NOT been destroyed before we destruct ProcessGroupNCCL. On normal program exit, the application should call destroy_process_group to ensure that any pending NCCL operations have finished in this process. In rare cases this process can exit before this point and block the progress of another member of the process group. This constraint has always been present, but this warning has only been added since PyTorch 2.4 (function operator())\n j6zswihe185nfq[info]engine.py :116 2025-03-24 18:13:28,839 Error initializing vLLM engine: Qwen2_5_VLModel has no vLLM implementation and the Transformers implementation is not compatible with vLLM.\n j6zswihe185nfq[error]Uncaught exception | ; Qwen2_5_VLModel has no vLLM implementati...

## 候选优化模式

- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 6: ibe the bug When trying to host my finetuned Qwen2.5 VL 7b 4bit dynamic quantization using unsloth, and after I have saved the trained model it as bf16, when I try to host the model, it gives me this error: ```python wo...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 6: [Bug]: Uncaught exception | <class 'ValueError'>; Qwen2_5_VLModel has no vLLM implementation and the Transformers implementation is not compatible with vLLM bug ### Your current environment I just know it's hosted on ru...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 5: pu_memory_utilization=0.95, max_num_batched_tokens=None, max_num_partial_prefills=1, max_long_partial_prefills=1, long_prefill_token_threshold=0, max_num_seqs=256, max_logprobs=20, disable_log_stats=False, revision=None...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 4: ing to host my finetuned Qwen2.5 VL 7b 4bit dynamic quantization using unsloth, and after I have saved the trained model it as bf16, when I try to host the model, it gives me this error: ```python worker exited with exi...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 2: trun-1.0...\n j6zswihe185nfq[info]INFO 03-24 18:13:28 cuda.py:229] Using Flash Attention backend.\n j6zswihe185nfq[info] j6zswihe185nfq[info]INFO 03-24 18:13:27 config.py:549] This model supports multiple tasks: {'score...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
