# vllm-project/vllm#2211: Mixtral weight loading with manually downloaded weights does not work

| 字段 | 值 |
| --- | --- |
| Issue | [#2211](https://github.com/vllm-project/vllm/issues/2211) |
| 状态 | closed |
| 标签 |  |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | distributed_parallel;frontend_api;model_support;quantization |
| 子分类 | latency_reg |
| Operator 关键词 | cuda;quantization |
| 症状 | crash;slowdown |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> Mixtral weight loading with manually downloaded weights does not work

### Issue 正文摘录

Hi, I downloaded this model manually with `git lfs`. https://huggingface.co/TheBloke/Mixtral-8x7B-Instruct-v0.1-GPTQ I tried to start an OpenAI server pointing to this directory ```bash python3 -m vllm.entrypoints.openai.api_server \ --model /models/Mixtral-8x7B-Instruct-v0.1-GPTQ -tp 2 --dtype float16 ``` Error: ```bash INFO 12-20 03:39:53 api_server.py:727] args: Namespace(host=None, port=8000, allow_credentials=False, allowed_origins=['*'], allowed_methods=['*'], allowed_headers=['*'], served_model_name=None, chat_template=None, response_role='assistant', ssl_keyfile=None, ssl_certfile=None, model='/models/Mixtral-8x7B-Instruct-v0.1-GPTQ', tokenizer=None, revision=None, tokenizer_revision=None, tokenizer_mode='auto', trust_remote_code=False, download_dir=None, load_format='auto', dtype='float16', max_model_len=None, worker_use_ray=False, pipeline_parallel_size=1, tensor_parallel_size=2, max_parallel_loading_workers=None, block_size=16, seed=0, swap_space=4, gpu_memory_utilization=0.9, max_num_batched_tokens=None, max_num_seqs=256, max_paddings=256, disable_log_stats=False, quantization=None, enforce_eager=False, max_context_len_to_capture=8192, engine_use_ray=False, disable_log...

## 候选优化模式

- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 4: --model /models/Mixtral-8x7B-Instruct-v0.1-GPTQ -tp 2 --dtype float16 ``` Error: ```bash INFO 12-20 03:39:53 api_server.py:727] args: Namespace(host=None, port=8000, allow_credentials=False, allowed_origins=['*'], allow...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: ing with manually downloaded weights does not work Hi, I downloaded this model manually with `git lfs`. https://huggingface.co/TheBloke/Mixtral-8x7B-Instruct-v0.1-GPTQ I tried to start an OpenAI server pointing to this...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: ize() == loaded_weight.size() AssertionError ``` However, when I run specifying a name, and let vLLM do the downloading, it works. ```bash python3 -m vllm.entrypoints.openai.api_server \
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 2: server.py:727] args: Namespace(host=None, port=8000, allow_credentials=False, allowed_origins=['*'], allowed_methods=['*'], allowed_headers=['*'], served_model_name=None, chat_template=None, response_role='assistant', s...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: ized models. WARNING 12-20 03:39:53 config.py:187] gptq does not support CUDA graph yet. Disabling CUDA graph. 2023-12-20 03:39:54,822 INFO worker.py:1673 -- Started a local Ray instance. INFO 12-20 03:39:55 llm_engine....

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
