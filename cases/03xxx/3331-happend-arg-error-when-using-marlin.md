# vllm-project/vllm#3331: happend arg error when using marlin

| 字段 | 值 |
| --- | --- |
| Issue | [#3331](https://github.com/vllm-project/vllm/issues/3331) |
| 状态 | closed |
| 标签 |  |
| 评论 | 0; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> happend arg error when using marlin

### Issue 正文摘录

File "/usr/local/lib/python3.10/dist-packages/vllm/entrypoints/openai/api_server.py", line 258, in engine = AsyncLLMEngine.from_engine_args(engine_args) File "/usr/local/lib/python3.10/dist-packages/vllm/engine/async_llm_engine.py", line 619, in from_engine_args engine_configs = engine_args.create_engine_configs() File "/usr/local/lib/python3.10/dist-packages/vllm/engine/arg_utils.py", line 318, in create_engine_configs model_config = ModelConfig( File "/usr/local/lib/python3.10/dist-packages/vllm/config.py", line 130, in init self._verify_quantization() File "/usr/local/lib/python3.10/dist-packages/vllm/config.py", line 204, in _verify_quantization raise ValueError( ValueError: Quantization method specified in the model config (marlin) does not match the quantization method specified in the quantization argument (gptq). quantization arg has not marlin,if I use marlin kernel and marlin model,happend error

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: s/vllm/engine/async_llm_engine.py", line 619, in from_engine_args engine_configs = engine_args.create_engine_configs() File "/usr/local/lib/python3.10/dist-packages/vllm/engine/arg_utils.py", line 318, in create_engine_...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: verify_quantization raise ValueError( ValueError: Quantization method specified in the model config (marlin) does not match the quantization method specified in the quantization argument (gptq). quantization arg has not...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 1: python3.10/dist-packages/vllm/config.py", line 130, in init self._verify_quantization() File "/usr/local/lib/python3.10/dist-packages/vllm/config.py", line 204, in _verify_quantization raise ValueError( ValueError: Quan...

## Wiki 抽取状态

- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
