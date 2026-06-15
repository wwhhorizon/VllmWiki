# vllm-project/vllm#2251: Load Mixtral 8x7b AWQ model failed

| 字段 | 值 |
| --- | --- |
| Issue | [#2251](https://github.com/vllm-project/vllm/issues/2251) |
| 状态 | closed |
| 标签 | stale |
| 评论 | 30; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> Load Mixtral 8x7b AWQ model failed

### Issue 正文摘录

I am using the latest vllm docker image, trying to run Mixtral 8x7b model quantized in AWQ format. I got error message as below: ``` INFO 12-24 09:22:55 llm_engine.py:73] Initializing an LLM engine with config: model='/models/openbuddy-mixtral-8x7b-v15.2-AWQ', tokenizer='/models/openbuddy-mixtral-8x7b-v15.2-AWQ', tokenizer_mode=auto, revision=None, tokenizer_revision=None, trust_remote_code=True, dtype=torch.float16, max_seq_len=32768, download_dir=None, load_format=auto, tensor_parallel_size=2, quantization=awq, enforce_eager=False, seed=0) (RayWorkerVllm pid=2491) /usr/local/lib/python3.10/dist-packages/torch/nn/init.py:412: UserWarning: Initializing zero-element tensors is a no-op (RayWorkerVllm pid=2491) warnings.warn("Initializing zero-element tensors is a no-op") Traceback (most recent call last): File "/usr/lib/python3.10/runpy.py", line 196, in _run_module_as_main return _run_code(code, main_globals, None, File "/usr/lib/python3.10/runpy.py", line 86, in _run_code exec(code, run_globals) File "/workspace/vllm/entrypoints/openai/api_server.py", line 729, in engine = AsyncLLMEngine.from_engine_args(engine_args) File "/workspace/vllm/engine/async_llm_engine.py", line 496, in...

## 候选优化模式

- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 3: am using the latest vllm docker image, trying to run Mixtral 8x7b model quantized in AWQ format. I got error message as below: ``` INFO 12-24 09:22:55 llm_engine.py:73] Initializing an LLM engine with config: model='/mo...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: Load Mixtral 8x7b AWQ model failed stale I am using the latest vllm docker image, trying to run Mixtral 8x7b model quantized in AWQ format. I got error message as below: ``` INFO 12-24 09:22:55 llm_engine.py:73] Initial...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 2: d_format=auto, tensor_parallel_size=2, quantization=awq, enforce_eager=False, seed=0) (RayWorkerVllm pid=2491) /usr/local/lib/python3.10/dist-packages/torch/nn/init.py:412: UserWarning: Initializing zero-element tensors...
- [MoE、GEMM 与 Expert Routing](../patterns/moe_gemm_routing.md) - 分数 2: ts param = params_dict[name] KeyError: 'model.layers.26.block_sparse_moe.experts.0.w2.qweight' ```
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: Load Mixtral 8x7b AWQ model failed stale I am using the latest vllm docker image, trying to run Mixtral 8x7b model quantized in AWQ format. I got error message as below: ``` INFO 12-24 09:22:55 llm_engine.py:73] Initial...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
