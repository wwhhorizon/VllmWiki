# vllm-project/vllm#21176: [Bug]: ValueError: There is no module or parameter named 'mm_whisper_embeddings' in LlamaForCausalLM

| 字段 | 值 |
| --- | --- |
| Issue | [#21176](https://github.com/vllm-project/vllm/issues/21176) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 8; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | development |
| 工作域 | attention_kv_cache;ci_build;distributed_parallel;frontend_api;model_support;moe;quantization;sampling_logits |
| 子分类 | install |
| Operator 关键词 | attention;cuda;operator;quantization;sampling |
| 症状 | crash |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: ValueError: There is no module or parameter named 'mm_whisper_embeddings' in LlamaForCausalLM

### Issue 正文摘录

### Your current environment FROM pytorch/pytorch:2.5.1-cuda12.1-cudnn9-devel RUN apt update && apt install -y git screen RUN pip install flashinfer-python RUN pip install -U "vllm[audio]" --extra-index-url https://wheels.vllm.ai/nightly ENTRYPOINT ["sleep", "999999999"] # For now: exec into container and run vllm serve from there ### 🐛 Describe the bug $ vllm serve mistralai/Voxtral-Mini-3B-2507 --tokenizer_mode mistral --config_format mistral --load_format mistral INFO 07-18 10:28:51 [__init__.py:244] Automatically detected platform cuda. INFO 07-18 10:28:55 [api_server.py:1395] vLLM API server version 0.9.2 INFO 07-18 10:28:55 [cli_args.py:325] non-default args: {'model': 'mistralai/Voxtral-Mini-3B-2507', 'tokenizer_mode': 'mistral', 'config_format': 'mistral', 'load_format': 'mistral'} INFO 07-18 10:29:03 [config.py:841] This model supports multiple tasks: {'generate', 'reward', 'embed', 'classify'}. Defaulting to 'generate'. ERROR 07-18 10:29:03 [config.py:130] Error retrieving safetensors: 'mistralai/Voxtral-Mini-3B-2507' is not a safetensors repo. Couldn't find 'model.safetensors.index.json' or 'model.safetensors' files., retrying 1 of 2 ERROR 07-18 10:29:06 [config.py:128]...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 7: FROM pytorch/pytorch:2.5.1-cuda12.1-cudnn9-devel RUN apt update && apt install -y git screen RUN pip install flashinfer-python RUN pip install -U "vllm[audio]" --extra-index-url https://wheels.vllm.ai/nightly ENTRYPOINT...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 5: dnn9-devel RUN apt update && apt install -y git screen RUN pip install flashinfer-python RUN pip install -U "vllm[audio]" --extra-index-url https://wheels.vllm.ai/nightly ENTRYPOINT ["sleep", "999999999"] # For now: exe...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 5: fetensors' files. INFO 07-18 10:29:06 [config.py:3368] Downcasting torch.float32 to torch.bfloat16. INFO 07-18 10:29:06 [config.py:1472] Using max model len 32768 INFO 07-18 10:29:06 [config.py:2285] Chunked prefill is...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 5: odule or parameter named 'mm_whisper_embeddings' in LlamaForCausalLM bug;stale ### Your current environment FROM pytorch/pytorch:2.5.1-cuda12.1-cudnn9-devel RUN apt update && apt install -y git screen RUN pip install fl...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: eError: There is no module or parameter named 'mm_whisper_embeddings' in LlamaForCausalLM bug;stale ### Your current environment FROM pytorch/pytorch:2.5.1-cuda12.1-cudnn9-devel RUN apt update && apt install -y git scre...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
