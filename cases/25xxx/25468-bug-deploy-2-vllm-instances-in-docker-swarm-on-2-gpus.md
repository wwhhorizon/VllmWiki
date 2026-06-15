# vllm-project/vllm#25468: [Bug]: deploy 2 vllm instances in docker swarm on 2 gpus

| 字段 | 值 |
| --- | --- |
| Issue | [#25468](https://github.com/vllm-project/vllm/issues/25468) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | attention_kv_cache;ci_build;distributed_parallel;frontend_api;model_support;moe;multimodal_vlm;quantization;sampling_logits |
| 子分类 | memory |
| Operator 关键词 | attention;cuda;quantization;sampling |
| 症状 | slowdown |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: deploy 2 vllm instances in docker swarm on 2 gpus

### Issue 正文摘录

### Your current environment llm-openai-v0.9.1 ### 🐛 Describe the bug I have defined 2 docker swarm services, set to deploy on the 2 gpus of the same server. ``` services: vllm-server-gpu0: image: rednotehilab/dots.ocr:vllm-openai-v0.9.1 networks: [doc-net] ports: - target: 30024 published: 30024 protocol: tcp mode: ingress environment: HF_MODEL_PATH: /models/DotsOCR PYTHONPATH: /models TRANSFORMERS_OFFLINE: "1" HF_DATASETS_OFFLINE: "1" CUDA_VISIBLE_DEVICES: "0" VLLM_IMAGE_FEATURE_SIZE: "576" # Reduce from default VLLM_MM_CACHE_PREPROCESSOR: "false" # Disable preprocessor caching volumes: - models:/models entrypoint: /bin/sh command: - -c - | VLLM_CLI=$$(which vllm) if [ -f "$$VLLM_CLI" ] && ! grep -q "from DotsOCR import modeling_dots_ocr_vllm" "$$VLLM_CLI"; then sed -i '/^from vllm\.entrypoints\.cli\.main import main$$/a from DotsOCR import modeling_dots_ocr_vllm' "$$VLLM_CLI" fi exec vllm serve /models/DotsOCR --tensor-parallel-size 1 --gpu-memory-utilization 0.95 --chat-template-content-format string --served-model-name model --trust-remote-code --host 0.0.0.0 --port 30024 --dtype auto --max-model-len 8192 deploy: replicas: 1 placement: constraints: - node.labels.gpu==true vll...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 8: [Bug]: deploy 2 vllm instances in docker swarm on 2 gpus bug ### Your current environment llm-openai-v0.9.1 ### 🐛 Describe the bug I have defined 2 docker swarm services, set to deploy on the 2 gpus of the same server....
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 6: 30024 protocol: tcp mode: ingress environment: HF_MODEL_PATH: /models/DotsOCR PYTHONPATH: /models TRANSFORMERS_OFFLINE: "1" HF_DATASETS_OFFLINE: "1" CUDA_VISIBLE_DEVICES: "0" VLLM_IMAGE_FEATURE_SIZE: "576" # Reduce from...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 4: kv_cache_dtype=auto, device_config=cuda, decoding_config=DecodingConfig(backend='auto', disable_fallback=False, disable_any_whitespace=False, disable_additional_properties=False, reasoning_backend=''), observability_con...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 4: erved-model-name model --trust-remote-code --host 0.0.0.0 --port 30024 --dtype auto --max-model-len 8192 deploy: replicas: 1 placement: constraints: - node.labels.gpu==true vllm-server-gpu1: image: rednotehilab/dots.ocr...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 4: 5-09-23T09:09:40.158161045Z INFO 09-23 02:09:40 [config.py:2195] Chunked prefill is enabled with max_num_batched_tokens=2048. 2025-09-23T09:09:41.617499759Z WARNING 09-23 02:09:41 [env_override.py:17] NCCL_CUMEM_ENABLE...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
