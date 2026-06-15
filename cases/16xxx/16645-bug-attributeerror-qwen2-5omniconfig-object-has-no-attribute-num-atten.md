# vllm-project/vllm#16645: [Bug]: AttributeError: 'Qwen2_5OmniConfig' object has no attribute 'num_attention_heads'

| 字段 | 值 |
| --- | --- |
| Issue | [#16645](https://github.com/vllm-project/vllm/issues/16645) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;quantization;scheduler_memory |
| 子分类 | kernel_eff |
| Operator 关键词 | cuda;quantization |
| 症状 | crash |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: AttributeError: 'Qwen2_5OmniConfig' object has no attribute 'num_attention_heads'

### Issue 正文摘录

### Your current environment just look here: [https://github.com/huggingface/transformers/issues/37515#issuecomment-2804126324](url) ### 🐛 Describe the bug `System Info root@445d74596699:/vllm-workspace# transformers-cli env Copy-and-paste the text below in your GitHub issue and FILL OUT the two last points. transformers version: 4.52.0.dev0 Platform: Linux-5.15.0-43-generic-x86_64-with-glibc2.35 Python version: 3.12.9 Huggingface_hub version: 0.30.2 Safetensors version: 0.5.3 Accelerate version: 1.5.2 Accelerate config: not found DeepSpeed version: not installed PyTorch version (GPU?): 2.6.0+cu124 (True) Tensorflow version (GPU?): not installed (NA) Flax version (CPU?/GPU?/TPU?): not installed (NA) Jax version: not installed JaxLib version: not installed Using distributed or parallel set-up in script?: Using GPU in script?: GPU type: NVIDIA L20 `(base) root@node15:/disk2/Qwen2.5-Omni-7B# more docker-compose.yml #version: '3.3' services: vllm vllm-openai: image: vllm/vllm-openai:v0.8.2 container_name: Qwen2.5-Omni-7B restart: unless-stopped runtime: nvidia ports: - 8007:8000 volumes: - /disk2:/models command: > --model /models/Qwen2.5-Omni-7B --tokenizer_mode="auto" --trust-remote...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 8: low in your GitHub issue and FILL OUT the two last points. transformers version: 4.52.0.dev0 Platform: Linux-5.15.0-43-generic-x86_64-with-glibc2.35 Python version: 3.12.9 Huggingface_hub version: 0.30.2 Safetensors ver...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 6: [Bug]: AttributeError: 'Qwen2_5OmniConfig' object has no attribute 'num_attention_heads' bug;stale ### Your current environment just look here: [https://github.com/huggingface/transformers/issues/37515#issuecomment-2804...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 6: r: 'Qwen2_5OmniConfig' object has no attribute 'num_attention_heads' bug;stale ### Your current environment just look here: [https://github.com/huggingface/transformers/issues/37515#issuecomment-2804126324](url) ### 🐛 D...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 5: el /models/Qwen2.5-Omni-7B --tokenizer_mode="auto" --trust-remote-code --dtype=bfloat16 --max_num_seqs=256 --tensor_parallel_size=1 --gpu-memory-utilization=0.9 --max-model-len=65536 --served-model-name=Qwen2.5-Omni-7B...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 3: =None, port=8000, uvicorn_log_level='info', disable_uvicorn_access_log=False, allow_credentials=False, allowed_origins=[''], allowed_methods=[''], allowed_headers=['*'], api_key=None, lora_modules=None, prompt_adapters=...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
