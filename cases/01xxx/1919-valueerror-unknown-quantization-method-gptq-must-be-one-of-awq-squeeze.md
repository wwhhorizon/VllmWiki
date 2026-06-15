# vllm-project/vllm#1919: ValueError: Unknown quantization method: gptq. Must be one of ['awq', 'squeezellm'].

| 字段 | 值 |
| --- | --- |
| Issue | [#1919](https://github.com/vllm-project/vllm/issues/1919) |
| 状态 | closed |
| 标签 |  |
| 评论 | 6; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> ValueError: Unknown quantization method: gptq. Must be one of ['awq', 'squeezellm'].

### Issue 正文摘录

``` Traceback (most recent call last): File "/workspace/api/server.py", line 2, in from api.models import app, EMBEDDED_MODEL, GENERATE_ENGINE File "/workspace/api/models.py", line 144, in GENERATE_ENGINE = create_vllm_engine() File "/workspace/api/models.py", line 89, in create_vllm_engine engine = AsyncLLMEngine.from_engine_args(engine_args) File "/workspace/vllm/engine/async_llm_engine.py", line 480, in from_engine_args engine_configs = engine_args.create_engine_configs() File "/workspace/vllm/engine/arg_utils.py", line 187, in create_engine_configs model_config = ModelConfig(self.model, self.tokenizer, File "/workspace/vllm/config.py", line 97, in __init__ self._verify_quantization() File "/workspace/vllm/config.py", line 137, in _verify_quantization raise ValueError( ValueError: Unknown quantization method: gptq. Must be one of ['awq', 'squeezellm']. ```

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: call last): File "/workspace/api/server.py", line 2, in from api.models import app, EMBEDDED_MODEL, GENERATE_ENGINE File "/workspace/api/models.py", line 144, in GENERATE_ENGINE = create_vllm_engine() File "/workspace/a...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: st): File "/workspace/api/server.py", line 2, in from api.models import app, EMBEDDED_MODEL, GENERATE_ENGINE File "/workspace/api/models.py", line 144, in GENERATE_ENGINE = create_vllm_engine() File "/workspace/api/mode...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 1: ValueError: Unknown quantization method: gptq. Must be one of ['awq', 'squeezellm']. ``` Traceback (most recent call last): File "/workspace/api/server.py", line 2, in from api.models import app, EMBEDDED_MODEL, GENERAT...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
