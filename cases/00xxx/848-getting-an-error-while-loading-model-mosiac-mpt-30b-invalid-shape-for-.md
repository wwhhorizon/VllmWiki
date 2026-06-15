# vllm-project/vllm#848: Getting an error while loading model mosiac/mpt-30b, Invalid shape for attention bias

| 字段 | 值 |
| --- | --- |
| Issue | [#848](https://github.com/vllm-project/vllm/issues/848) |
| 状态 | closed |
| 标签 |  |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> Getting an error while loading model mosiac/mpt-30b, Invalid shape for attention bias

### Issue 正文摘录

Hi , while running the following code: `model= LLM(model="mosaicml/mpt-30b", tokenizer = "mosaicml/mpt-30b", tensor_parallel_size=4, pipeline_parallel_size=1, gpu_memory_utilization=0.90 dtype='bfloat16')` I am getting an error while loading the mpt model. Below is the call stack ``` Traceback (most recent call last): File "inference.py", line 207, in vllm_inference_provider.load_model(model_args, inference_args, vllm_args) File "inference.py", line 175, in load_model self.model = LLM(model=self.model_args.model_path, tensor_parallel_size=self.vllm_args.tensor_parallel_size, File "/opt/conda/envs/vllm/lib/python3.8/site-packages/vllm/entrypoints/llm.py", line 62, in __init__ self.llm_engine = LLMEngine.from_engine_args(engine_args) File "/opt/conda/envs/vllm/lib/python3.8/site-packages/vllm/engine/llm_engine.py", line 154, in from_engine_args engine = cls(*engine_configs, File "/opt/conda/envs/vllm/lib/python3.8/site-packages/vllm/engine/llm_engine.py", line 105, in __init__ self._init_cache() File "/opt/conda/envs/vllm/lib/python3.8/site-packages/vllm/engine/llm_engine.py", line 117, in _init_cache num_blocks = self._run_workers( File "/opt/conda/envs/vllm/lib/python3.8/site-pack...

## 候选优化模式

- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 3: gpu_memory_utilization=0.90 dtype='bfloat16')` I am getting an error while loading the mpt model. Below is the call stack ``` Traceback (most recent call last): File "inference.py", line 207, in vllm_inference_provider....
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: ion.py", line 352, in multi_query_kv_attention out = xops.memory_efficient_attention_forward( File "/opt/conda/envs/vllm/lib/python3.8/site-packages/xformers/ops/fmha/__init__.py", line 214, in memory_efficient_attentio...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 2: te-packages/vllm/engine/llm_engine.py", line 117, in _init_cache num_blocks = self._run_workers( File "/opt/conda/envs/vllm/lib/python3.8/site-packages/vllm/engine/llm_engine.py", line 334, in _run_workers all_outputs =...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: Getting an error while loading model mosiac/mpt-30b, Invalid shape for attention bias Hi , while running the following code: `model= LLM(model="mosaicml/mpt-30b", tokenizer = "mosaicml/mpt-30b", tensor_parallel_size=4
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: _instanceof_cause() ray.exceptions.RayTaskError(ValueError): ray::Worker.profile_num_available_blocks() (pid=28130, ip=172.31.46.1, actor_id=2959eb28c8ba6c028ee5032301000000, repr= ) File "/opt/conda/envs/vllm/lib/pytho...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
