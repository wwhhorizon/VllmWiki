# vllm-project/vllm#2272: mixtral fails to load, pytorch cuda errror

| 字段 | 值 |
| --- | --- |
| Issue | [#2272](https://github.com/vllm-project/vllm/issues/2272) |
| 状态 | closed |
| 标签 |  |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | development |
| 工作域 | frontend_api;model_support;quantization |
| 子分类 | runtime_err |
| Operator 关键词 | cuda;quantization |
| 症状 | crash |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> mixtral fails to load, pytorch cuda errror

### Issue 正文摘录

It says report to pytorch but I can't help thinking it's either user error or incompat with mixtral somehow Error: ``` File "/usr/local/lib/python3.10/dist-packages/vllm/model_executor/models/mixtral.py", line 182, in __init__ torch.empty(self.ffn_dim_per_partition * self.num_experts, File "/usr/local/lib/python3.10/dist-packages/torch/utils/_device.py", line 77, in __torch_function__ return func(*args, **kwargs) RuntimeError: NVML_SUCCESS == r INTERNAL ASSERT FAILED at "../c10/cuda/CUDACachingAllocator.cpp":1154, please report a bug to PyTorch. ``` Full error: ``` INFO 12-26 15:52:49 api_server.py:719] args: Namespace(host='0.0.0.0', port=8000, allow_credentials=False, allowed_origins=['*'], allowed_methods=['*'], allowed_headers=['*'], served_model_name=None, chat_template=None, response_role='assistant', model='mistralai/Mixtral-8x7B-Instruct-v0.1', tokenizer=None, revision=None, tokenizer_revision=None, tokenizer_mode='auto', trust_remote_code=False, download_dir='/.cache/huggingface/hub', load_format='pt', dtype='auto', max_model_len=None, worker_use_ray=False, pipeline_parallel_size=1, tensor_parallel_size=1, max_parallel_loading_workers=None, block_size=16, seed=0, swap_spa...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 5: l somehow Error: ``` File "/usr/local/lib/python3.10/dist-packages/vllm/model_executor/models/mixtral.py", line 182, in __init__ torch.empty(self.ffn_dim_per_partition * self.num_experts, File "/usr/local/lib/python3.10...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 2: te_code=False, download_dir='/.cache/huggingface/hub', load_format='pt', dtype='auto', max_model_len=None, worker_use_ray=False, pipeline_parallel_size=1, tensor_parallel_size=1, max_parallel_loading_workers=None, block...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 2: r.py:719] args: Namespace(host='0.0.0.0', port=8000, allow_credentials=False, allowed_origins=['*'], allowed_methods=['*'], allowed_headers=['*'], served_model_name=None, chat_template=None, response_role='assistant', m...
- [MoE、GEMM 与 Expert Routing](../patterns/moe_gemm_routing.md) - 分数 2: line 182, in __init__ torch.empty(self.ffn_dim_per_partition * self.num_experts, File "/usr/local/lib/python3.10/dist-packages/torch/utils/_device.py", line 77, in __torch_function__ return func(*args, **kwargs) Runtime...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: le_log_stats=False, quantization=None, engine_use_ray=False, disable_log_requests=False, max_log_len=None) config.json: 0%| | 0.00/720 [00:00 engine = AsyncLLMEngine.from_engine_args(engine_args) File "/usr/local/lib/py...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
