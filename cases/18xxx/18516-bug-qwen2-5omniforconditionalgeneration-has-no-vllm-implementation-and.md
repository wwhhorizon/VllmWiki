# vllm-project/vllm#18516: [Bug]:Qwen2_5OmniForConditionalGeneration has no vLLM implementation and the Transformers implementation is not compatible with vLLM. Try setting VLLM_USE_V1=0.

| 字段 | 值 |
| --- | --- |
| Issue | [#18516](https://github.com/vllm-project/vllm/issues/18516) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 4; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | attention_kv_cache;ci_build;distributed_parallel;frontend_api;model_support;quantization;scheduler_memory |
| 子分类 | kernel_eff |
| Operator 关键词 | attention;cuda;kernel;quantization |
| 症状 | crash |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]:Qwen2_5OmniForConditionalGeneration has no vLLM implementation and the Transformers implementation is not compatible with vLLM. Try setting VLLM_USE_V1=0.

### Issue 正文摘录

### Your current environment **Qwen2.5-Omni-7B works normally, but Qwen2.5-Omni-7B-AWQ gives an error.** https://modelscope.cn/models/Qwen/Qwen2.5-Omni-7B-AWQ/summary https://github.com/vllm-project/vllm/issues/18450 root@node37:/disk1/Qwen2.5-Omni-7B-AWQ# vi docker-compose.yml #version: '3.3' services: # vllm vllm-openai: image: vllm/vllm-openai:v0.8.5 container_name: Qwen2.5-Omni-7B-AWQ environment: - VLLM_USE_V1=0 - NCCL_CUMEM_ENABLE=0 restart: unless-stopped runtime: nvidia ports: - 8007:8000 volumes: - /disk1:/models command: > --model /models/Qwen2.5-Omni-7B-AWQ --enable-auto-tool-choice --tool-call-parser hermes --tokenizer_mode="auto" --trust-remote-code --dtype=bfloat16 --max_num_seqs=256 --tensor_parallel_size=1 --gpu-memory-utilization=0.95 --max-model-len=32768 --served-model-name=Qwen2.5-Omni-7B-AWQ deploy: resources: reservations: devices: - driver: nvidia capabilities: [gpu] device_ids: [ "0" ] ipc: host networks: vllm: ~ "docker-compose.yml" [dos] 37L, 922C written root@node37:/disk1/Qwen2.5-Omni-7B-AWQ# docker compose -f docker-compose.yml down root@node37:/disk1/Qwen2.5-Omni-7B-AWQ# docker compose -f docker-compose.yml up -d [+] Running 2/2 ? Network qwen25-omni-...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 6: lm-project/vllm/issues/18450 root@node37:/disk1/Qwen2.5-Omni-7B-AWQ# vi docker-compose.yml #version: '3.3' services: # vllm vllm-openai: image: vllm/vllm-openai:v0.8.5 container_name: Qwen2.5-Omni-7B-AWQ environment: -...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 6: r hermes --tokenizer_mode="auto" --trust-remote-code --dtype=bfloat16 --max_num_seqs=256 --tensor_parallel_size=1 --gpu-memory-utilization=0.95 --max-model-len=32768 --served-model-name=Qwen2.5-Omni-7B-AWQ deploy: resou...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 5: [Bug]:Qwen2_5OmniForConditionalGeneration has no vLLM implementation and the Transformers implementation is not compatible with vLLM. Try setting VLLM_USE_V1=0. bug;stale ### Your current environment **Qwen2.5-Omni-7B w...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 5: plementation is not compatible with vLLM. Try setting VLLM_USE_V1=0. bug;stale ### Your current environment **Qwen2.5-Omni-7B works normally, but Qwen2.5-Omni-7B-AWQ gives an error.** https://modelscope.cn/models/Qwen/Q...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 3: =None, port=8000, uvicorn_log_level='info', disable_uvicorn_access_log=False, allow_credentials=False, allowed_origins=['*'], allowed_methods=['*'], allowed_headers=['*'], api_key=None, lora_modules=None, prompt_adapter...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
