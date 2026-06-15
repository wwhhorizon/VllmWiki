# vllm-project/vllm#20634: [Bug]: TypeError: FlashAttentionImpl.__init__() got an unexpected keyword argument 'layer_idx' while loading a fine-tuned qwen2.5 model

| 字段 | 值 |
| --- | --- |
| Issue | [#20634](https://github.com/vllm-project/vllm/issues/20634) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 7; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | attention_kv_cache;ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;moe;quantization;sampling_logits |
| 子分类 | memory |
| Operator 关键词 | attention;cuda;operator;quantization;sampling;triton |
| 症状 | build_error;crash |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: TypeError: FlashAttentionImpl.__init__() got an unexpected keyword argument 'layer_idx' while loading a fine-tuned qwen2.5 model

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug I am deploying my fine tuned model and encountered flashAttention problem. However it works well when I run command `vllm serve /root/.cache/huggingface/Qwen/Qwen2.5-7B-Instruct-GPTQ-Int8 --quantization gptq` ```bash vllm serve /usr/rag ``` Here is my error message ```bash INFO 07-08 14:54:38 [__init__.py:244] Automatically detected platform cuda. INFO 07-08 14:54:43 [api_server.py:1287] vLLM API server version 0.9.1 INFO 07-08 14:54:44 [cli_args.py:309] non-default args: {'model': '/usr/rag'} INFO 07-08 14:54:51 [config.py:823] This model supports multiple tasks: {'score', 'embed', 'reward', 'generate', 'classify'}. Defaulting to 'generate'. INFO 07-08 14:54:51 [config.py:3268] Downcasting torch.float32 to torch.bfloat16. INFO 07-08 14:54:51 [config.py:2195] Chunked prefill is enabled with max_num_batched_tokens=2048. WARNING 07-08 14:54:53 [env_override.py:17] NCCL_CUMEM_ENABLE is set to 0, skipping override. This may increase memory overhead with cudagraph+allreduce: https://github.com/NVIDIA/nccl/issues/1234 INFO 07-08 14:54:55 [__init__.py:244] Automatically detected platform cuda. INFO 07-08 14:54:58 [core.py:455] Waiting f...

## 候选优化模式

- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 6: [Bug]: TypeError: FlashAttentionImpl.__init__() got an unexpected keyword argument 'layer_idx' while loading a fine-tuned qwen2.5 model bug ### Your current environment ### 🐛 Describe the bug I am deploying my fine tune...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 6: platform cuda. INFO 07-08 14:54:43 [api_server.py:1287] vLLM API server version 0.9.1 INFO 07-08 14:54:44 [cli_args.py:309] non-default args: {'model': '/usr/rag'} INFO 07-08 14:54:51 [config.py:823] This model supports...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 6: vllm serve /root/.cache/huggingface/Qwen/Qwen2.5-7B-Instruct-GPTQ-Int8 --quantization gptq` ```bash vllm serve /usr/rag ``` Here is my error message ```bash INFO 07-08 14:54:38 [__init__.py:244] Automatically detected p...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 5: ot an unexpected keyword argument 'layer_idx' while loading a fine-tuned qwen2.5 model bug ### Your current environment ### 🐛 Describe the bug I am deploying my fine tuned model and encountered flashAttention problem. H...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 5: .float32 to torch.bfloat16. INFO 07-08 14:54:51 [config.py:2195] Chunked prefill is enabled with max_num_batched_tokens=2048. WARNING 07-08 14:54:53 [env_override.py:17] NCCL_CUMEM_ENABLE is set to 0, skipping override....

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
