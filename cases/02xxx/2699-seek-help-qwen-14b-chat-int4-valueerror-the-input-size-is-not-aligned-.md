# vllm-project/vllm#2699: Seek help, `Qwen-14B-Chat-Int4`ValueError: The input size is not aligned with the quantized weight shape. This can be caused by too large tensor parallel size.

| 字段 | 值 |
| --- | --- |
| Issue | [#2699](https://github.com/vllm-project/vllm/issues/2699) |
| 状态 | closed |
| 标签 |  |
| 评论 | 18; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | ci_build;distributed_parallel;frontend_api;gemm_linear;model_support;quantization |
| 子分类 | latency_reg |
| Operator 关键词 | quantization |
| 症状 | crash;slowdown |
| 根因提示 | dtype;env_dependency;shape |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> Seek help, `Qwen-14B-Chat-Int4`ValueError: The input size is not aligned with the quantized weight shape. This can be caused by too large tensor parallel size.

### Issue 正文摘录

* docker image`vllm/vllm-openai:v0.2.7`, startup command: ``` docker run -it -d -p 5003:8000 \ --name vllm-api \ -v $(pwd)/huggingface:/root/.cache/huggingface \ -v $(pwd)/Qwen-14B-Chat-Int4:/workspace/qwen \ --runtime nvidia --gpus all \ --ipc=host \ vllm/vllm-openai:v0.2.7 \ --trust-remote-code \ --dtype auto \ --tensor-parallel-size 2 \ --quantization gptq \ --model qwen ``` * The graphics card is `NVIDIA GeForce RTX 4090 24G`*2 * Use`Qwen-7B-Chat-Int4`works properly, Use`Qwen-14B-Chat-Int4`error: ``` INFO 02-01 01:41:59 api_server.py:727] args: Namespace(host=None, port=8000, allow_credentials=False, allowed_origins=['*'], allowed_methods=['*'], allowed_headers=['*'], served_model_name=None, chat_template=None, response_role='assistant', ssl_keyfile=None, ssl_certfile=None, model='qwen', tokenizer=None, revision=None, tokenizer_revision=None, tokenizer_mode='auto', trust_remote_code=True, download_dir=None, load_format='auto', dtype='auto', max_model_len=None, worker_use_ray=False, pipeline_parallel_size=1, tensor_parallel_size=2, max_parallel_loading_workers=None, block_size=16, seed=0, swap_space=4, gpu_memory_utilization=0.9, max_num_batched_tokens=None, max_num_seqs=256, m...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 6: Seek help, `Qwen-14B-Chat-Int4`ValueError: The input size is not aligned with the quantized weight shape. This can be caused by too large tensor parallel size. * docker image`vllm/vllm-openai:v0.2.7`, startup command: `...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: ed weight shape. This can be caused by too large tensor parallel size. * docker image`vllm/vllm-openai:v0.2.7`, startup command: ``` docker run -it -d -p 5003:8000 \ --name vllm-api \ -v $(pwd)/huggingface:/root/.cache/...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 4: Seek help, `Qwen-14B-Chat-Int4`ValueError: The input size is not aligned with the quantized weight shape. This can be caused by too large tensor parallel size. * docker image`vllm/vllm-openai:v0.2.7`, startup command: `...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 2: server.py:727] args: Namespace(host=None, port=8000, allow_credentials=False, allowed_origins=['*'], allowed_methods=['*'], allowed_headers=['*'], served_model_name=None, chat_template=None, response_role='assistant', s...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: ntization gptq \ --model qwen ``` * The graphics card is `NVIDIA GeForce RTX 4090 24G`*2 * Use`Qwen-7B-Chat-Int4`works properly, Use`Qwen-14B-Chat-Int4`error: ``` INFO 02-01 01:41:59 api_server.py:727] args: Namespace(h...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
