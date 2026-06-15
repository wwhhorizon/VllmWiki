# vllm-project/vllm#2026: vLLM Docker container fails with Mixtral 8x7b

| 字段 | 值 |
| --- | --- |
| Issue | [#2026](https://github.com/vllm-project/vllm/issues/2026) |
| 状态 | closed |
| 标签 |  |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> vLLM Docker container fails with Mixtral 8x7b

### Issue 正文摘录

I built the `Dockerfile` in the root of the repo, on commit `https://github.com/vllm-project/vllm/commit/4ff0203987ff100eaaad69f0a8abf7ed821e3a0a`, then pushed the container and tried to run it using the following args: ``` - --host - 0.0.0.0 - --model - mistralai/Mixtral-8x7B-Instruct-v0.1 - --tensor-parallel-size - "2" ``` When I run the container, this is what I see ``` INFO 12-11 17:57:51 api_server.py:719] args: Namespace(host='0.0.0.0', port=8000, allow_credentials=False, allowed_origins=['*'], allowed_methods=['*'], allowed_headers=['*'], served_model_name=None, chat_template=None, response_role='assistant', model='mistralai/Mixtral-8x7B-Instruct-v0.1', tokenizer=None, revision=None, tokenizer_revision=None, tokenizer_mode='auto', trust_remote_code=False, download_dir=None, load_format='auto', dtype='auto', max_model_len=None, worker_use_ray=False, pipeline_parallel_size=1, tensor_parallel_size=2, max_parallel_loading_workers=None, block_size=16, seed=0, swap_space=4, gpu_memory_utilization=0.9, max_num_batched_tokens=None, max_num_seqs=256, max_paddings=256, disable_log_stats=False, quantization=None, engine_use_ray=False, disable_log_requests=False, max_log_len=None) conf...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: run it using the following args: ``` - --host - 0.0.0.0 - --model - mistralai/Mixtral-8x7B-Instruct-v0.1 - --tensor-parallel-size - "2" ``` When I run the container, this is what I see ``` INFO 12-11 17:57:51 api_server...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: vLLM Docker container fails with Mixtral 8x7b I built the `Dockerfile` in the root of the repo, on commit `https://github.com/vllm-project/vllm/commit/4ff0203987ff100eaaad69f0a8abf7ed821e3a0a`, then pushed the container...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 2: ='auto', trust_remote_code=False, download_dir=None, load_format='auto', dtype='auto', max_model_len=None, worker_use_ray=False, pipeline_parallel_size=1, tensor_parallel_size=2, max_parallel_loading_workers=None, block...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 2: r.py:719] args: Namespace(host='0.0.0.0', port=8000, allow_credentials=False, allowed_origins=['*'], allowed_methods=['*'], allowed_headers=['*'], served_model_name=None, chat_template=None, response_role='assistant', m...
- [MoE、GEMM 与 Expert Routing](../patterns/moe_gemm_routing.md) - 分数 1: m/model_executor/models/mixtral.py", line 151, in class BlockSparseMoE(nn.Module): File "/workspace/vllm/model_executor/models/mixtral.py", line 254, in BlockSparseMoE padded_bins: torch.Tensor) -> stk.Matrix: NameError...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
