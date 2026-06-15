# vllm-project/vllm#1931: Support loading Int8-quantified (smoothquant) Codellama-13B ?

| 字段 | 值 |
| --- | --- |
| Issue | [#1931](https://github.com/vllm-project/vllm/issues/1931) |
| 状态 | closed |
| 标签 |  |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> Support loading Int8-quantified (smoothquant) Codellama-13B ?

### Issue 正文摘录

Hi, dear: I have completed the conversion and export of the model format by smoothquant, but when I use vllm to load the model and do inference, the error is as follows: INFO 12-05 09:00:58 tokenizer.py:32] For some LLaMA V1 models, initializing the fast tokenizer may take a long time. To reduce the initialization time, consider using 'hf-internal-testing/llama-tokenizer' instead of the original tokenizer. Traceback (most recent call last): File "./vllm/entrypoints/api_server.py", line 80, in engine = AsyncLLMEngine.from_engine_args(engine_args) File "/home/miniconda3/envs/vllm/lib/python3.8/site-packages/vllm/engine/async_llm_engine.py", line 495, in from_engine_args engine = cls(parallel_config.worker_use_ray, File "/home/miniconda3/envs/vllm/lib/python3.8/site-packages/vllm/engine/async_llm_engine.py", line 269, in __init__ self.engine = self._init_engine(*args, **kwargs) File "/home/miniconda3/envs/vllm/lib/python3.8/site-packages/vllm/engine/async_llm_engine.py", line 314, in _init_engine return engine_class(*args, **kwargs) File "/home/miniconda3/envs/vllm/lib/python3.8/site-packages/vllm/engine/llm_engine.py", line 109, in __init__ self._init_workers(distributed_init_method...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 5: Support loading Int8-quantified (smoothquant) Codellama-13B ? Hi, dear: I have completed the conversion and export of the model format by smoothquant, but when I use vllm to load the model and do inference, the error is...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: ntified (smoothquant) Codellama-13B ? Hi, dear: I have completed the conversion and export of the model format by smoothquant, but when I use vllm to load the model and do inference, the error is as follows: INFO 12-05...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 1: Support loading Int8-quantified (smoothquant) Codellama-13B ? Hi, dear: I have completed the conversion and export of the model format by smoothquant, but when I use vllm to load the model and do inference, the error is...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: Support loading Int8-quantified (smoothquant) Codellama-13B ? Hi, dear: I have completed the conversion and export of the model format by smoothquant, but when I use vllm to load the model and do inference, the error is...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ong time. To reduce the initialization time, consider using 'hf-internal-testing/llama-tokenizer' instead of the original tokenizer. Traceback (most recent call last): File "./vllm/entrypoints/api_server.py", line 80, i...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
