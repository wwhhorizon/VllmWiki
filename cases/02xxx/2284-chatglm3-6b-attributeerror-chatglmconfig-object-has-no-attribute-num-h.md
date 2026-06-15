# vllm-project/vllm#2284: ChatGLM3-6B AttributeError: 'ChatGLMConfig' object has no attribute 'num_hidden_layers'

| 字段 | 值 |
| --- | --- |
| Issue | [#2284](https://github.com/vllm-project/vllm/issues/2284) |
| 状态 | closed |
| 标签 |  |
| 评论 | 4; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> ChatGLM3-6B AttributeError: 'ChatGLMConfig' object has no attribute 'num_hidden_layers'

### Issue 正文摘录

Traceback (most recent call last): File "vcheck.py", line 2014, in llm = LLM(model=model_path, trust_remote_code=True) # Name or path of your model File "/app/vllm/vllm/entrypoints/llm.py", line 66, in __init__ self.llm_engine = LLMEngine.from_engine_args(engine_args) File "/app/vllm/vllm/engine/llm_engine.py", line 157, in from_engine_args engine = cls(*engine_configs, File "/app/vllm/vllm/engine/llm_engine.py", line 79, in __init__ self._verify_args() File "/app/vllm/vllm/engine/llm_engine.py", line 114, in _verify_args self.model_config.verify_with_parallel_config(self.parallel_config) File "/app/vllm/vllm/config.py", line 81, in verify_with_parallel_config total_num_hidden_layers = self.hf_config.num_hidden_layers File "/usr/local/lib/python3.8/dist-packages/transformers/configuration_utils.py", line 265, in __getattribute__ return super().__getattribute__(key) AttributeError: 'ChatGLMConfig' object has no attribute 'num_hidden_layers' my vllm version is 0.2.6

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: ChatGLM3-6B AttributeError: 'ChatGLMConfig' object has no attribute 'num_hidden_layers' Traceback (most recent call last): File "vcheck.py", line 2014, in llm = LLM(model=model_path, trust_remote_code=True) # Name or pa...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: ror: 'ChatGLMConfig' object has no attribute 'num_hidden_layers' my vllm version is 0.2.6

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
