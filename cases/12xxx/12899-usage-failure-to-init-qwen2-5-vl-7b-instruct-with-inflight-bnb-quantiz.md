# vllm-project/vllm#12899: [Usage]: Failure to Init Qwen2.5-VL-7B-Instruct with inflight bnb quantization

| 字段 | 值 |
| --- | --- |
| Issue | [#12899](https://github.com/vllm-project/vllm/issues/12899) |
| 状态 | closed |
| 标签 | usage |
| 评论 | 0; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | attention_kv_cache;ci_build;distributed_parallel;frontend_api;gemm_linear;model_support;multimodal_vlm;quantization |
| 子分类 | precision |
| Operator 关键词 | attention;cuda;quantization |
| 症状 | crash;slowdown |
| 根因提示 | dtype;env_dependency;shape |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Usage]: Failure to Init Qwen2.5-VL-7B-Instruct with inflight bnb quantization

### Issue 正文摘录

### Your current environment ```text docker vllm-openai:v0.7.2 with latest transformers installed ``` ### How would you like to use vllm Hi and I'm trying to launch qwen2.5-vl-7b-instruct in bnb inflight quanization but got error ``` (AssertionError: param_data.shape == loaded_weight.shape) ``` I was able to run this model at full precision with docker. Below is how I init the full precision one: ``` sudo docker run --runtime nvidia --gpus '"device=0,1"' --ipc=host -p 18434:8000 \ -v hf_cache:/root/.cache/huggingface -d \ --name qwen2.5-vl-7b \ --entrypoint "python3" qwen-vl-fixed \ # I installed new transformer and commited into a new image. -m vllm.entrypoints.openai.api_server --model Qwen/Qwen2.5-VL-7B-Instruct \ --tensor-parallel-size 2 --trust-remote-code --max-model-len 18000 --dtype half ``` When I added `--quantization bitsandbytes --load-format bitsandbytes` into the docker command, the launch of the model in bnb 4bit inflight quantization failed. Below is the full error log: ``` INFO 02-07 05:08:11 __init__.py:190] Automatically detected platform cuda. INFO 02-07 05:08:13 api_server.py:840] vLLM API server version 0.7.2  uINFO 02-07 05:08:13 api_server.py:841] args: Na...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 8: [Usage]: Failure to Init Qwen2.5-VL-7B-Instruct with inflight bnb quantization usage ### Your current environment ```text docker vllm-openai:v0.7.2 with latest transformers installed ``` ### How would you like to use vl...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 7: th inflight bnb quantization usage ### Your current environment ```text docker vllm-openai:v0.7.2 with latest transformers installed ``` ### How would you like to use vllm Hi and I'm trying to launch qwen2.5-vl-7b-instr...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 5: [Usage]: Failure to Init Qwen2.5-VL-7B-Instruct with inflight bnb quantization usage ### Your current environment ```text docker vllm-openai:v0.7.2 with latest transformers installed ``` ### How would you like to use vl...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 5: okens_as_token_ids=False, disable_frontend_multiprocessing=False, enable_request_id_headers=False, enable_auto_tool_choice=False, enable_reasoning=False, reasoning_parser=None, tool_call_parser=None, tool_parser_plugin=...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 3: pace(host=None, port=8000, uvicorn_log_level='info', allow_credentials=False, allowed_origins=['*'], allowed_methods=['*'], allowed_headers=['*'], api_key=None, lora_modules=None, prompt_adapters=None, chat_template=Non...

## Wiki 抽取状态

- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
