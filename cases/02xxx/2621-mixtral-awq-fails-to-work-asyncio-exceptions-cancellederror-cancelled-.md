# vllm-project/vllm#2621: Mixtral AWQ fails to work: asyncio.exceptions.CancelledError: Cancelled by cancel scope 7fd214489990

| 字段 | 值 |
| --- | --- |
| Issue | [#2621](https://github.com/vllm-project/vllm/issues/2621) |
| 状态 | closed |
| 标签 |  |
| 评论 | 12; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | attention_kv_cache;ci_build;distributed_parallel;frontend_api;model_support;quantization;sampling_logits |
| 子分类 | throughput |
| Operator 关键词 | cache;cuda;quantization;sampling |
| 症状 | crash;oom;slowdown |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> Mixtral AWQ fails to work: asyncio.exceptions.CancelledError: Cancelled by cancel scope 7fd214489990

### Issue 正文摘录

``` export CUDA_HOME=/usr/local/cuda-12.3 export PIP_EXTRA_INDEX_URL="https://download.pytorch.org/whl/cu123" pip install git+https://github.com/vllm-project/vllm.git --upgrade export CUDA_VISIBLE_DEVICES=1 python -m vllm.entrypoints.openai.api_server --port=5002 --host=0.0.0.0 --model TheBloke/Mixtral-8x7B-Instruct-v0.1-AWQ --quantization awq --dtype auto --seed 1234 --tensor-parallel-size=1 --max-num-batched-tokens=66560 --max-log-len=100 ``` Any where, even simple, leads to: ``` INFO 01-27 01:15:31 api_server.py:209] args: Namespace(host='0.0.0.0', port=5002, allow_credentials=False, allowed_origins=['*'], allowed_methods=['*'], allowed_headers=['*'], api_key=None, served_model_name=None, chat_template=None, response_role='assistant', ssl_keyfile=None, ssl_certfile=None, root_path=None, middleware=[], model='TheBloke/Mixtral-8x7B-Instru> WARNING 01-27 01:15:31 config.py:176] awq quantization is not fully optimized yet. The speed can be slower than non-quantized models. INFO 01-27 01:15:31 llm_engine.py:72] Initializing an LLM engine with config: model='TheBloke/Mixtral-8x7B-Instruct-v0.1-AWQ', tokenizer='TheBloke/Mixtral-8x7B-Instruct-v0.1-AWQ', tokenizer_mode=auto, revision=No...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: Mixtral AWQ fails to work: asyncio.exceptions.CancelledError: Cancelled by cancel scope 7fd214489990 ``` export CUDA_HOME=/usr/local/cuda-12.3 export PIP_EXTRA_INDEX_URL="https://download.pytorch.org/whl/cu123" pip inst...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 3: rt=5002 --host=0.0.0.0 --model TheBloke/Mixtral-8x7B-Instruct-v0.1-AWQ --quantization awq --dtype auto --seed 1234 --tensor-parallel-size=1 --max-num-batched-tokens=66560 --max-log-len=100 ``` Any where, even simple, le...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: ython -m vllm.entrypoints.openai.api_server --port=5002 --host=0.0.0.0 --model TheBloke/Mixtral-8x7B-Instruct-v0.1-AWQ --quantization awq --dtype auto --seed 1234 --tensor-parallel-size=1 --max-num-batched-tokens=66560...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 2: , sender) File "/ephemeral/vllm/lib/python3.10/site-packages/starlette/routing.py", line 762, in __call__ await self.middleware_stack(scope, receive, send) File "/ephemeral/vllm/lib/python3.10/site-packages/starlette/ro...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: ptions.CancelledError: Cancelled by cancel scope 7fd214489990 ``` export CUDA_HOME=/usr/local/cuda-12.3 export PIP_EXTRA_INDEX_URL="https://download.pytorch.org/whl/cu123" pip install git+https://github.com/vllm-project...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
