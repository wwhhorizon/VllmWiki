# vllm-project/vllm#11139: [Bug]: vllm using ray in eks hangs when using --pipeline_parallel_size > 1

| 字段 | 值 |
| --- | --- |
| Issue | [#11139](https://github.com/vllm-project/vllm/issues/11139) |
| 状态 | closed |
| 标签 | bug;ray;stale |
| 评论 | 10; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | development |
| 工作域 | attention_kv_cache;ci_build;distributed_parallel;frontend_api;model_support;quantization;scheduler_memory |
| 子分类 | env_compat |
| Operator 关键词 | attention;cuda;quantization |
| 症状 | build_error |
| 根因提示 | dtype;env_dependency;memory_layout |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: vllm using ray in eks hangs when using --pipeline_parallel_size > 1

### Issue 正文摘录

### Your current environment running on a pod in g6.12xlarge (allocated by lws). Pod is initializing ray before running vllm (using the proposed lws image https://github.com/kubernetes-sigs/lws/blob/main/docs/examples/vllm/build/Dockerfile.GPU) ### Model Input Dumps _No response_ ### 🐛 Describe the bug Vllm is stuck on this meesage: INFO 12-12 05:28:31 pynccl.py:69] vLLM is using nccl==2.21.5 full log: [2024-12-12 05:27:53,632 W 8 8] global_state_accessor.cc:463: Retrying to get node with node ID 9c36d691ad808fe6b12015dc3c0c4ba0432917a72547d5450434659c 2024-12-12 05:27:52,822 INFO usage_lib.py:467 -- Usage stats collection is enabled by default without user confirmation because this terminal is detected t o be non-interactive. To disable this, add `--disable-usage-stats` to the command that starts the cluster, or run the following command: `ray disable-usage -stats` before starting the cluster. See https://docs.ray.io/en/master/cluster/usage-stats.html for more details. 2024-12-12 05:27:52,822 INFO scripts.py:822 -- Local node IP: 10.0.143.175 2024-12-12 05:27:54,657 SUCC scripts.py:859 -- -------------------- 2024-12-12 05:27:54,657 SUCC scripts.py:860 -- Ray runtime started. 202...

## 候选优化模式

- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 7: m using ray in eks hangs when using --pipeline_parallel_size > 1 bug;ray;stale ### Your current environment running on a pod in g6.12xlarge (allocated by lws). Pod is initializing ray before running vllm (using the prop...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 6: mage https://github.com/kubernetes-sigs/lws/blob/main/docs/examples/vllm/build/Dockerfile.GPU) ### Model Input Dumps _No response_ ### 🐛 Describe the bug Vllm is stuck on this meesage: INFO 12-12 05:28:31 pynccl.py:69]...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 5: ernetes-sigs/lws/blob/main/docs/examples/vllm/build/Dockerfile.GPU) ### Model Input Dumps _No response_ ### 🐛 Describe the bug Vllm is stuck on this meesage: INFO 12-12 05:28:31 pynccl.py:69] vLLM is using nccl==2.21.5...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 4: media_path=None, download_dir=None, load_format='auto', config_format= , dtype='auto', kv_cach e_dtype='auto', quantization_param_path=None, max_model_len=None, guided_decoding_backend='outlines', distributed_executor_b...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 4: pace(host=None, port=8080, uvicorn_log_level='info', allow_credentials=False, allowed_origins=['*'], allo wed_methods=['*'], allowed_headers=['*'], api_key=None, lora_modules=None, prompt_adapters=None, chat_template=No...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
