# vllm-project/vllm#4323: [Bug]: phi-3 (microsoft/Phi-3-mini-128k-instruct) fails with assert "factor" in rope_scaling

| 字段 | 值 |
| --- | --- |
| Issue | [#4323](https://github.com/vllm-project/vllm/issues/4323) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 16; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | development |
| 工作域 | ci_build;distributed_parallel;frontend_api;model_support;quantization |
| 子分类 | env_compat |
| Operator 关键词 | quantization;triton |
| 症状 | crash |
| 根因提示 | dtype |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: phi-3 (microsoft/Phi-3-mini-128k-instruct) fails with assert "factor" in rope_scaling

### Issue 正文摘录

### Your current environment docker 0.4.0.post1 ### 🐛 Describe the bug ``` docker run -d --runtime=nvidia --gpus '"device=1"' --shm-size=10.24gb -p 5001:5001 -e NCCL_IGNORE_DISABLED_P2P=1 -e HUGGING_FACE_HUB_TOKEN=$HUGGING_FACE_HUB_TOKEN -v /etc/passwd:/etc/passwd:ro -v /etc/group:/etc/group:ro -u `id -u`:`id -g` -v "${HOME}"/.cache:$HOME/.cache/ -v "${HOME}"/.config:$HOME/.config/ -v "${HOME}"/.triton:$HOME/.triton/ --network host vllm/vllm-openai:latest --port=5001 --host=0.0.0.0 --model=microsoft/Phi-3-mini-128k-instruct --seed 1234 --trust-remote-code --tensor-parallel-size=1 --max-num-batched-tokens=131072 --max-log-len=100 --download-dir=$HOME/.cache/huggingface/hub &>> logs.vllm_server.phi3.txt ``` gives: ``` (h2ogpt) fsuser@e2e-77-235:~/h2ogpt_ops$ docker logs d7b0c7e07f4d6055cce27ba8e7244860463d89ad36aa7bf2e0e9e13ea7941843 INFO 04-24 06:29:08 api_server.py:149] vLLM API server version 0.4.0.post1 INFO 04-24 06:29:08 api_server.py:150] args: Namespace(host='0.0.0.0', port=5001, uvicorn_log_level='info', allow_credentials=False, allowed_origins=['*'], allowed_methods=['*'], allowed_headers=['*'], api_key=None, served_model_name=None, lora_modules=None, chat_template=None, r...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 5: -u `id -u`:`id -g` -v "${HOME}"/.cache:$HOME/.cache/ -v "${HOME}"/.config:$HOME/.config/ -v "${HOME}"/.triton:$HOME/.triton/ --network host vllm/vllm-openai:latest --port=5001 --host=0.0.0.0 --model=microsoft/Phi-3-mini...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: s with assert "factor" in rope_scaling bug ### Your current environment docker 0.4.0.post1 ### 🐛 Describe the bug ``` docker run -d --runtime=nvidia --gpus '"device=1"' --shm-size=10.24gb -p 5001:5001 -e NCCL_IGNORE_DIS...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 4: e, image_token_id=None, image_input_shape=None, image_feature_size=None, scheduler_delay_factor=0.0, enable_chunked_prefill=False, speculative_model=None, num_speculative_tokens=None, engine_use_ray=False, disable_log_r...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 3: host='0.0.0.0', port=5001, uvicorn_log_level='info', allow_credentials=False, allowed_origins=['*'], allowed_methods=['*'], allowed_headers=['*'], api_key=None, served_model_name=None, lora_modules=None, chat_template=N...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 2: download_dir='/home/fsuser/.cache/huggingface/hub', load_format='auto', dtype='auto', kv_cache_dtype='auto', max_model_len=None, worker_use_ray=False, pipeline_parallel_size=1, tensor_parallel_size=1, max_parallel_loadi...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
