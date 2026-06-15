# vllm-project/vllm#32925: [Bug]: tensorize_vllm_model double gpu

| 字段 | 值 |
| --- | --- |
| Issue | [#32925](https://github.com/vllm-project/vllm/issues/32925) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 4; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | attention_kv_cache;ci_build;distributed_parallel;frontend_api;model_support;moe;quantization;sampling_logits |
| 子分类 | memory |
| Operator 关键词 | attention;cuda;gemm;quantization;sampling |
| 症状 |  |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: tensorize_vllm_model double gpu

### Issue 正文摘录

### Your current environment v 0.14 or v0.9.2 ### 🐛 Describe the bug docker run --gpus '"device=3"' --shm-size=4g -p 38954:38954 --name tensorize-deploy -v /storage/leo/workspace/common-ie/asset_script/serialize_model/vllm/model/checkpoint-1350-merged:/storage/model -v /storage/leo/workspace/train_project/train_somefile/chat_template:/storage/chat_template vllm-openai-tensorizer:v0.9.2 --served-model-name K-GPT-V --model /storage/model --port 38954 --load-format tensorizer --model-loader-extra-config '{"tensorizer_uri": "/storage/model/model.tensors", "encryption_keyfile": "/storage/model/szkingdomai"}' --api-key EMPTY --tensor-parallel-size 1 --gpu_memory_utilization 0.25 --chat-template /storage/chat_template/chat_template.jinja --mm-processor-kwargs '{"min_pixels": 200704, "max_pixels": 1003520, "fps": 2.0}' --max_model_len 8192 When I used the "tensorize_vllm_model" script to serialize the qwen-2.5-vl -7b model, and then saved the model, after starting the service and initializing, the memory usage immediately soared to 32G, and finally dropped to 21G. INFO 01-23 00:39:38 [cli_args.py:325] non-default args: {'port': 38954, 'api_key': 'EMPTY', 'chat_template': '/storage/chat_te...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 7: ### Your current environment v 0.14 or v0.9.2 ### 🐛 Describe the bug docker run --gpus '"device=3"' --shm-size=4g -p 38954:38954 --name tensorize-deploy -v /storage/leo/workspace/common-ie/asset_script/serialize_model/v...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 5: [Bug]: tensorize_vllm_model double gpu bug;stale ### Your current environment v 0.14 or v0.9.2 ### 🐛 Describe the bug docker run --gpus '"device=3"' --shm-size=4g -p 38954:38954 --name tensorize-deploy -v /storage/leo/w...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 4: kv_cache_dtype=auto, device_config=cuda, decoding_config=DecodingConfig(backend='auto', disable_fallback=False, disable_any_whitespace=False, disable_additional_properties=False, reasoning_backend=''), observability_con...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 4: ride_neuron_config={}, tokenizer_revision=None, trust_remote_code=False, dtype=torch.bfloat16, max_seq_len=8192, download_dir=None, load_format=LoadFormat.TENSORIZER, tensor_parallel_size=1, pipeline_parallel_size=1, di...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: [Bug]: tensorize_vllm_model double gpu bug;stale ### Your current environment v 0.14 or v0.9.2 ### 🐛 Describe the bug docker run --gpus '"device=3"' --shm-size=4g -p 38954:38954 --name tensorize-deploy -v /storage/leo/w...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
