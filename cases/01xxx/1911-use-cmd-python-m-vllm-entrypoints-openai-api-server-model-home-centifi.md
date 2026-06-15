# vllm-project/vllm#1911: use cmd : python -m vllm.entrypoints.openai.api_server --model /home/centific/hua-project/models/01ai/Yi-34B-Chat-4bits , RuntimeError: CUDA error: CUBLAS_STATUS_NOT_INITIALIZED when calling `cublasCreate(handle)`

| 字段 | 值 |
| --- | --- |
| Issue | [#1911](https://github.com/vllm-project/vllm/issues/1911) |
| 状态 | closed |
| 标签 |  |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | frontend_api;gemm_linear;model_support;quantization;sampling_logits |
| 子分类 | latency_reg |
| Operator 关键词 | cuda;gemm;quantization |
| 症状 | crash;slowdown |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> use cmd : python -m vllm.entrypoints.openai.api_server --model /home/centific/hua-project/models/01ai/Yi-34B-Chat-4bits , RuntimeError: CUDA error: CUBLAS_STATUS_NOT_INITIALIZED when calling `cublasCreate(handle)`

### Issue 正文摘录

(vllm) centific@centific-System-Product-Name:~/hua-project/vllm$ python -m vllm.entrypoints.openai.api_server --model /home/centific/hua-project/models/01ai/Yi-34B-Chat-4bits INFO 12-04 10:05:22 api_server.py:704] args: Namespace(host=None, port=8000, allow_credentials=False, allowed_origins=['*'], allowed_methods=['*'], allowed_headers=['*'], served_model_name=None, chat_template=None, response_role='assistant', model='/home/centific/hua-project/models/01ai/Yi-34B-Chat-4bits', tokenizer=None, revision=None, tokenizer_revision=None, tokenizer_mode='auto', trust_remote_code=False, download_dir=None, load_format='auto', dtype='auto', max_model_len=None, worker_use_ray=False, pipeline_parallel_size=1, tensor_parallel_size=1, max_parallel_loading_workers=None, block_size=16, seed=0, swap_space=4, gpu_memory_utilization=0.9, max_num_batched_tokens=None, max_num_seqs=256, max_paddings=256, disable_log_stats=False, quantization=None, engine_use_ray=False, disable_log_requests=False, max_log_len=None) WARNING 12-04 10:05:22 config.py:140] awq quantization is not fully optimized yet. The speed can be slower than non-quantized models. INFO 12-04 10:05:22 llm_engine.py:72] Initializing an LL...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: use cmd : python -m vllm.entrypoints.openai.api_server --model /home/centific/hua-project/models/01ai/Yi-34B-Chat-4bits , RuntimeError: CUDA error: CUBLAS_STATUS_NOT_INITIALIZED when calling `cublasCreate(handle)` (vllm...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 3: ='auto', trust_remote_code=False, download_dir=None, load_format='auto', dtype='auto', max_model_len=None, worker_use_ray=False, pipeline_parallel_size=1, tensor_parallel_size=1, max_parallel_loading_workers=None, block...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 2: server.py:704] args: Namespace(host=None, port=8000, allow_credentials=False, allowed_origins=['*'], allowed_methods=['*'], allowed_headers=['*'], served_model_name=None, chat_template=None, response_role='assistant', m...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: tization;sampling_logits cuda;gemm;quantization crash;slowdown dtype;env_dependency (vllm) centific@centific-System-Product-Name:~/hua-project/vllm$ python -m vllm.entrypoints.openai.api_server --model /home/centific/hu...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: /home/centific/hua-project/models/01ai/Yi-34B-Chat-4bits , RuntimeError: CUDA error: CUBLAS_STATUS_NOT_INITIALIZED when calling `cublasCreate(handle)` (vllm) centific@centific-System-Product-Name:~/hua-project/vllm$ pyt...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
