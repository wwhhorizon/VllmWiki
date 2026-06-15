# vllm-project/vllm#1713: ChatGLM3-6B  AttributeError: 'ChatGLMConfig' object has no attribute 'num_hidden_layers'

| 字段 | 值 |
| --- | --- |
| Issue | [#1713](https://github.com/vllm-project/vllm/issues/1713) |
| 状态 | closed |
| 标签 |  |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> ChatGLM3-6B  AttributeError: 'ChatGLMConfig' object has no attribute 'num_hidden_layers'

### Issue 正文摘录

Traceback (most recent call last): File "/home/imcp/ChatGlm3/vllm_test.py", line 11, in llm = LLM(model="./model", trust_remote_code=True) File "/home/imcp/anaconda3/envs/glm/lib/python3.10/site-packages/vllm/entrypoints/llm.py", line 93, in __init__ self.llm_engine = LLMEngine.from_engine_args(engine_args) File "/home/imcp/anaconda3/envs/glm/lib/python3.10/site-packages/vllm/engine/llm_engine.py", line 231, in from_engine_args engine = cls(*engine_configs, File "/home/imcp/anaconda3/envs/glm/lib/python3.10/site-packages/vllm/engine/llm_engine.py", line 96, in __init__ self._verify_args() File "/home/imcp/anaconda3/envs/glm/lib/python3.10/site-packages/vllm/engine/llm_engine.py", line 187, in _verify_args self.model_config.verify_with_parallel_config(self.parallel_config) File "/home/imcp/anaconda3/envs/glm/lib/python3.10/site-packages/vllm/config.py", line 128, in verify_with_parallel_config total_num_hidden_layers = self.hf_config.num_hidden_layers File "/home/imcp/anaconda3/envs/glm/lib/python3.10/site-packages/transformers/configuration_utils.py", line 262, in __getattribute__ return super().__getattribute__(key) AttributeError: 'ChatGLMConfig' object has no attribute 'num_hid...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: ChatGLM3-6B AttributeError: 'ChatGLMConfig' object has no attribute 'num_hidden_layers' Traceback (most recent call last): File "/home/imcp/ChatGlm3/vllm_test.py", line 11, in llm = LLM(model="./model", trust_remote_cod...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ers' Traceback (most recent call last): File "/home/imcp/ChatGlm3/vllm_test.py", line 11, in llm = LLM(model="./model", trust_remote_code=True) File "/home/imcp/anaconda3/envs/glm/lib/python3.10/site-packages/vllm/entry...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
