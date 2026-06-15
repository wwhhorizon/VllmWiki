# vllm-project/vllm#20035: [Bug]: Error when loading Mistral3.2 Small in 4bit bnb quantization with HF format.

| 字段 | 值 |
| --- | --- |
| Issue | [#20035](https://github.com/vllm-project/vllm/issues/20035) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | attention_kv_cache;ci_build;distributed_parallel;frontend_api;gemm_linear;model_support;moe;multimodal_vlm;quantization;sampling_logits |
| 子分类 | latency_reg |
| Operator 关键词 | attention;cuda;fp8;gemm;operator;quantization;sampling |
| 症状 | crash;slowdown |
| 根因提示 | dtype;env_dependency;shape |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Error when loading Mistral3.2 Small in 4bit bnb quantization with HF format.

### Issue 正文摘录

### Your current environment I've had sucess in gettting the FP8 version (unsloth/Mistral-Small-3.2-24B-Instruct-2506-FP8) to work (it uses Mistral file format), but when trying to run the 4 bit version that uses HF Format it just fails loading the model with no meaningfull message. ``` export MODEL_ID=unsloth/Mistral-Small-3.2-24B-Instruct-2506-unsloth-bnb-4bit docker run \ --runtime nvidia \ -e VLLM_USE_V1=1 \ --gpus all \ --ipc=host \ -p "${MODEL_PORT}:8000" \ --env "HUGGING_FACE_HUB_TOKEN=${HUGGING_FACE_HUB_TOKEN}" \ --env "HF_HUB_OFFLINE=0" \ -v "${HF_HOME}:/root/.cache/huggingface" \ -v ~/.cache/vllm/torch_compile_cache:/root/.cache/vllm/torch_compile_cache \ vllm/vllm-openai:latest \ --model ${MODEL_ID} \ --tool-call-parser mistral \ --enable-auto-tool-choice \ --limit-mm-per-prompt 'image=1' \ --max-model-len 32000 \ --gpu-memory-utilization 0.95 \ --trust-remote-code \ --quantization bitsandbytes \ --dtype bfloat16 ``` I get this error: ``` INFO 06-24 11:38:42 [__init__.py:244] Automatically detected platform cuda. INFO 06-24 11:38:47 [api_server.py:1287] vLLM API server version 0.9.1 INFO 06-24 11:38:48 [cli_args.py:309] non-default args: {'enable_auto_tool_choice': True...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 7: [Bug]: Error when loading Mistral3.2 Small in 4bit bnb quantization with HF format. bug ### Your current environment I've had sucess in gettting the FP8 version (unsloth/Mistral-Small-3.2-24B-Instruct-2506-FP8) to work...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 6: t. bug ### Your current environment I've had sucess in gettting the FP8 version (unsloth/Mistral-Small-3.2-24B-Instruct-2506-FP8) to work (it uses Mistral file format), but when trying to run the 4 bit version that uses...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 5: [Bug]: Error when loading Mistral3.2 Small in 4bit bnb quantization with HF format. bug ### Your current environment I've had sucess in gettting the FP8 version (unsloth/Mistral-Small-3.2-24B-Instruct-2506-FP8) to work...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 4: kv_cache_dtype=auto, device_config=cuda, decoding_config=DecodingConfig(backend='auto', disable_fallback=False, disable_any_whitespace=False, disable_additional_properties=False, reasoning_backend=''), observability_con...
- [MoE、GEMM 与 Expert Routing](../patterns/moe_gemm_routing.md) - 分数 4: igned as DP rank 0, PP rank 0, TP rank 0, EP rank 0 INFO 06-24 11:39:07 [topk_topp_sampler.py:49] Using FlashInfer for top-p & top-k sampling. INFO 06-24 11:39:07 [gpu_model_runner.py:1595] Starting to load model unslot...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
