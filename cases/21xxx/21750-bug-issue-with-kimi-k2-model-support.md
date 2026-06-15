# vllm-project/vllm#21750: [Bug]: Issue with Kimi K2 Model Support

| 字段 | 值 |
| --- | --- |
| Issue | [#21750](https://github.com/vllm-project/vllm/issues/21750) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 7; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | development |
| 工作域 | ci_build;distributed_parallel;frontend_api;model_support |
| 子分类 | install |
| Operator 关键词 | cuda |
| 症状 | crash;import_error |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Issue with Kimi K2 Model Support

### Issue 正文摘录

### Issue with Kimi K2 Model Support Issue on running moonshotai/Kimi-K2-Instruct model using vLLM v0.10.0. We're using the latest vllm docker image ### Deployment ``` vllm: container_name: vllm image: vllm/vllm-openai:v0.10.0 environment: - HUGGING_FACE_HUB_TOKEN=hf_XXXXXXXXX command: - "--served-model-name=moonshotai/Kimi-K2-Instruct" - "--dtype=auto" - "--max-model-len=8192" - "--tensor-parallel-size=8" - "--trust-remote-code" volumes: - /mnt/models:/root/.cache/huggingface ports: - 8000:8000 deploy: resources: reservations: devices: - driver: nvidia capabilities: [gpu] ``` ### Error ``` vllm | INFO 07-28 03:34:26 [__init__.py:235] Automatically detected platform cuda. vllm | INFO 07-28 03:34:28 [api_server.py:1755] vLLM API server version 0.10.0 vllm | INFO 07-28 03:34:28 [cli_args.py:261] non-default args: {'model': 'moonshotai/Kimi-K2-Instruct', 'trust_remote_code': True, 'max_model_len': 8192, 'tensor_parallel_size': 8} vllm | You are using a model of type kimi_k2 to instantiate a model of type deepseek_v3. This is not supported for all configurations of models and can yield errors. vllm | INFO 07-28 03:34:28 [config.py:243] Replacing legacy 'type' key with 'rope_type' vllm...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 7: i/Kimi-K2-Instruct model using vLLM v0.10.0. We're using the latest vllm docker image ### Deployment ``` vllm: container_name: vllm image: vllm/vllm-openai:v0.10.0 environment: - HUGGING_FACE_HUB_TOKEN=hf_XXXXXXXXX comm...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: [Bug]: Issue with Kimi K2 Model Support bug;stale ### Issue with Kimi K2 Model Support Issue on running moonshotai/Kimi-K2-Instruct model using vLLM v0.10.0. We're using the latest vllm docker image ### Deployment ``` v...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: | INFO 07-28 03:34:26 [__init__.py:235] Automatically detected platform cuda. vllm | INFO 07-28 03:34:28 [api_server.py:1755] vLLM API server version 0.10.0 vllm | INFO 07-28 03:34:28 [cli_args.py:261] non-default args:...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: [Bug]: Issue with Kimi K2 Model Support bug;stale ### Issue with Kimi K2 Model Support Issue on running moonshotai/Kimi-K2-Instruct model using vLLM v0.10.0. We're using the latest vllm docker image ### Deployment ``` v...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 1: nd: - "--served-model-name=moonshotai/Kimi-K2-Instruct" - "--dtype=auto" - "--max-model-len=8192" - "--tensor-parallel-size=8" - "--trust-remote-code" volumes: - /mnt/models:/root/.cache/huggingface ports: - 8000:8000 d...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
