# vllm-project/vllm#1308: v0.2.0 KeyError: 'base_lrs' 

| 字段 | 值 |
| --- | --- |
| Issue | [#1308](https://github.com/vllm-project/vllm/issues/1308) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> v0.2.0 KeyError: 'base_lrs' 

### Issue 正文摘录

Hi, when switching from 0.1.7. to 0.2.0 I encountered this error seen below. When switching back to 0.1.7 it works again. I run a Llama 13B model inside a Docker container. Any idea how to fix this error? ``` Traceback (most recent call last): File "/usr/lib/python3.10/runpy.py", line 196, in _run_module_as_main return _run_code(code, main_globals, None, File "/usr/lib/python3.10/runpy.py", line 86, in _run_code exec(code, run_globals) File "/project/vllm_app/run.py", line 33, in vllm_single() File "/project/vllm_app/run.py", line 14, in vllm_single single_test.run_vllm_single() File "/project/vllm_app/vllm_samples/single_test.py", line 12, in run_vllm_single llm = LLM(model="data/models/llama/") File "/usr/local/lib/python3.10/dist-packages/vllm/entrypoints/llm.py", line 89, in __init__ self.llm_engine = LLMEngine.from_engine_args(engine_args) File "/usr/local/lib/python3.10/dist-packages/vllm/engine/llm_engine.py", line 229, in from_engine_args engine = cls(*engine_configs, File "/usr/local/lib/python3.10/dist-packages/vllm/engine/llm_engine.py", line 108, in __init__ self._init_workers(distributed_init_method) File "/usr/local/lib/python3.10/dist-packages/vllm/engine/llm_engine...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: error seen below. When switching back to 0.1.7 it works again. I run a Llama 13B model inside a Docker container. Any idea how to fix this error? ``` Traceback (most recent call last): File "/usr/lib/python3.10/runpy.py...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: witching back to 0.1.7 it works again. I run a Llama 13B model inside a Docker container. Any idea how to fix this error? ``` Traceback (most recent call last): File "/usr/lib/python3.10/runpy.py", line 196, in _run_mod...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: () File "/project/vllm_app/run.py", line 14, in vllm_single single_test.run_vllm_single() File "/project/vllm_app/vllm_samples/single_test.py", line 12, in run_vllm_single llm = LLM(model="data/models/llama/") File "/us...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
