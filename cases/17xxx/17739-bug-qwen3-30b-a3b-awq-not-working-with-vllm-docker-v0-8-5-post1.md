# vllm-project/vllm#17739: [Bug]: Qwen3 30b a3b awq not working with vllm docker v0.8.5.post1

| 字段 | 值 |
| --- | --- |
| Issue | [#17739](https://github.com/vllm-project/vllm/issues/17739) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 6; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | attention_kv_cache;ci_build;distributed_parallel;frontend_api;model_support;moe;quantization;scheduler_memory |
| 子分类 | precision |
| Operator 关键词 | attention;cuda;moe;operator;quantization |
| 症状 | build_error;crash;mismatch;slowdown |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Qwen3 30b a3b awq not working with vllm docker v0.8.5.post1

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug sudo docker run --ipc=host --log-opt max-size=10m --log-opt max-file=1 --rm -it --gpus '"device=0"' --env "VLLM_USE_MODELSCOPE=True" --env "VLLM_USE_V1=0" -p 8000:8000 --mount type=bind,source=/home/me/.cache,target=/root/.cache vllm/vllm-openai:v0.8.5 --model swift/Qwen3-30B-A3B-AWQ --max-model-len 4000 --dtype half --gpu-memory-utilization 0.92 --disable-log-requests --no-enable-prefix-caching -q awq --tensor-parallel-size 1 me@am5:~$ sudo docker run --ipc=host --log-opt max-size=10m --log-opt max-file=1 --rm -it --gpus '"device=0"' --env "VLLM_USE_MODELSCOPE=True" --env "VLLM_USE_V1=0" -p 8000:8000 --mount type=bind,source=/home/m e/.cache,target=/root/.cache vllm/vllm-openai:v0.8.5.post1 --model swift/Qwen3-30B-A3B-AWQ --max-model-len 4000 --dtype half --gpu-memory-utilization 0.92 --disable-log-requests --no-enable-prefix-caching -q aw q --tensor-parallel-size 1 [sudo] password for me: INFO 05-06 12:20:53 [__init__.py:239] Automatically detected platform cuda. INFO 05-06 12:20:55 [api_server.py:1043] vLLM API server version 0.8.5.post1 INFO 05-06 12:20:55 [api_server.py:1044] args: Namespace(host=None, port=8000, uvicorn_log...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 6: [Bug]: Qwen3 30b a3b awq not working with vllm docker v0.8.5.post1 bug;stale ### Your current environment ### 🐛 Describe the bug sudo docker run --ipc=host --log-opt max-size=10m --log-opt max-file=1 --rm -it --gpus '"d...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 6: [Bug]: Qwen3 30b a3b awq not working with vllm docker v0.8.5.post1 bug;stale ### Your current environment ### 🐛 Describe the bug sudo docker run --ipc=host --log-opt max-size=10m --log-opt max-file=1 --rm -it --gpus '"d...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 5: [Bug]: Qwen3 30b a3b awq not working with vllm docker v0.8.5.post1 bug;stale ### Your current environment ### 🐛 Describe the bug sudo docker run --ipc=host --log-opt max-size=10m --log-opt max-file=1 --rm -it --gpus '"d...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 4: llm-openai:v0.8.5 --model swift/Qwen3-30B-A3B-AWQ --max-model-len 4000 --dtype half --gpu-memory-utilization 0.92 --disable-log-requests --no-enable-prefix-caching -q awq --tensor-parallel-size 1 me@am5:~$ sudo docker r...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 4: =None, port=8000, uvicorn_log_level='info', disable_uvicorn_access_log=False, allow_credentials=False, allowed_origins=['*'], allowed_methods=['*'], allowed_headers=['*'], api_key=None, lora_modules=None, prompt_adapter...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
