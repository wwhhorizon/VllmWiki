# vllm-project/vllm#9172: [Bug]: Port binding keep failing due to unnecessary code

| 字段 | 值 |
| --- | --- |
| Issue | [#9172](https://github.com/vllm-project/vllm/issues/9172) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 4; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;quantization;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cuda;quantization;sampling;triton |
| 症状 | build_error;nan_inf |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Port binding keep failing due to unnecessary code

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug The code relevant to this issue is at: `vllm/entrypoints/openai/api_server.py` If you run any model with or without `--disable-frontend-multiprocessing`, you would get `Address already in use` no matter what the host or port is. ```bash MODEL_PATH= QUANTIZATION_METHOD=awq MODEL_NAME=wizardlm2 HOST=0.0.0.0 PORT=8000 conda run --no-capture-output -n vllm python -m vllm.entrypoints.openai.api_server --load-format safetensors --model $MODEL_PATH --tensor-parallel-size 2 --served-model-name=$MODEL_NAME --host=$HOST --port=$PORT --response-role=assistant --quantization $QUANTIZATION_METHOD --chat-template prompt.j2 --trust-remote-code --enforce-eager --disable-frontend-multiprocessing ``` By removing some useless code this bug can be fixed. ```python async def run_server(args, **uvicorn_kwargs) -> None: logger.info("vLLM API server version %s", VLLM_VERSION) logger.info("args: %s", args) # temp_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # temp_socket.bind(("", args.port)) def signal_handler(*_) -> None: # Interrupt server on sigterm while initializing raise KeyboardInterrupt("terminated") signal.signal(signal.SIGTERM, s...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: server(args, **uvicorn_kwargs) -> None: logger.info("vLLM API server version %s", VLLM_VERSION) logger.info("args: %s", args) # temp_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # temp_socket.bind(("", arg...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: his issue is at: `vllm/entrypoints/openai/api_server.py` If you run any model with or without `--disable-frontend-multiprocessing`, you would get `Address already in use` no matter what the host or port is. ```bash MODE...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 3: [Bug]: Port binding keep failing due to unnecessary code bug;stale ### Your current environment ### 🐛 Describe the bug The code relevant to this issue is at: `vllm/entrypoints/openai/api_server.py` If you run any model...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 2: vicorn_kwargs, ) # NB: Await server shutdown only after the backend context is exited await shutdown_task ``` Relevant pull request: #4513 (I wonder why this patch is not merged, cause currently `vllm` has no builtin fe...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: y.) ### Before submitting a new issue... - [X] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
