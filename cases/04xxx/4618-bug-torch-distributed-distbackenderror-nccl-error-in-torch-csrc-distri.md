# vllm-project/vllm#4618: [Bug]: torch.distributed.DistBackendError: NCCL error in: ../torch/csrc/distributed/c10d/ProcessGroupNCCL.cpp:1970, unhandled system error (run with NCCL_DEBUG=INFO for details), NCCL version 2.20.5

| 字段 | 值 |
| --- | --- |
| Issue | [#4618](https://github.com/vllm-project/vllm/issues/4618) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | attention_kv_cache;ci_build;distributed_parallel;frontend_api;model_support;quantization |
| 子分类 |  |
| Operator 关键词 | attention;cuda;quantization |
| 症状 | crash |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: torch.distributed.DistBackendError: NCCL error in: ../torch/csrc/distributed/c10d/ProcessGroupNCCL.cpp:1970, unhandled system error (run with NCCL_DEBUG=INFO for details), NCCL version 2.20.5

### Issue 正文摘录

### Your current environment ```text docker exec: python3 api_server.py --served-model-name qwen-7b-chat --model /data/models/qwen1.5-110B-Chat-GPTQ-Int4/ --quantization gptq --max-model-len 16384 --tensor-parallel-size 2 ``` ### 🐛 Describe the bug ```tex INFO 05-06 08:55:09 llm_engine.py:100] Initializing an LLM engine (v0.4.2) with config: model='/data/models/qwen1.5-110B-Chat-GPTQ-Int4/', speculative_config=None, tokenizer='/data/models/qwen1.5-110B-Chat-GPTQ-Int4/', skip_tokenizer_init=False, tokenizer_mode=auto, revision=None, tokenizer_revision=None, trust_remote_code=False, dtype=torch.float16, max_seq_len=16384, download_dir=None, load_format=LoadFormat.AUTO, tensor_parallel_size=2, disable_custom_all_reduce=False, quantization=gptq, enforce_eager=False, kv_cache_dtype=auto, quantization_param_path=None, device_config=cuda, decoding_config=DecodingConfig(guided_decoding_backend='outlines'), seed=0, served_model_name=qwen-7b-chat) Special tokens have been added in the vocabulary, make sure the associated word embeddings are fine-tuned or trained. INFO 05-06 08:55:14 utils.py:660] Found nccl from library /root/.config/vllm/nccl/cu12/libnccl.so.2.18.1 (RayWorkerWrapper pid=54...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 6: 970, unhandled system error (run with NCCL_DEBUG=INFO for details), NCCL version 2.20.5 bug ### Your current environment ```text docker exec: python3 api_server.py --served-model-name qwen-7b-chat --model /data/models/q...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 4: rved-model-name qwen-7b-chat --model /data/models/qwen1.5-110B-Chat-GPTQ-Int4/ --quantization gptq --max-model-len 16384 --tensor-parallel-size 2 ``` ### 🐛 Describe the bug ```tex INFO 05-06 08:55:09 llm_engine.py:100]...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: urrent environment ```text docker exec: python3 api_server.py --served-model-name qwen-7b-chat --model /data/models/qwen1.5-110B-Chat-GPTQ-Int4/ --quantization gptq --max-model-len 16384 --tensor-parallel-size 2 ``` ###...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 2: [Bug]: torch.distributed.DistBackendError: NCCL error in: ../torch/csrc/distributed/c10d/ProcessGroupNCCL.cpp:1970, unhandled system error (run with NCCL_DEBUG=INFO for details), NCCL version 2.20.5 bug ### Your current...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: (v0.4.2) with config: model='/data/models/qwen1.5-110B-Chat-GPTQ-Int4/', speculative_config=None, tokenizer='/data/models/qwen1.5-110B-Chat-GPTQ-Int4/', skip_tokenizer_init=False, tokenizer_mode=auto, revision=None, tok...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
