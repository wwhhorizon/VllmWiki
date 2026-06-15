# vllm-project/vllm#2074: error when inferencing Mixtral AWQ

| 字段 | 值 |
| --- | --- |
| Issue | [#2074](https://github.com/vllm-project/vllm/issues/2074) |
| 状态 | closed |
| 标签 |  |
| 评论 | 30; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> error when inferencing Mixtral AWQ

### Issue 正文摘录

When I try to run a AsyncEngine with ybelkada/Mixtral-8x7B-Instruct-v0.1-AWQ I get Traceback (most recent call last): File "/home/marco/Scrivania/TESI/serving/vllm_server.py", line 91, in engine = AsyncLLMEngine.from_engine_args(engine_args) File "/home/marco/miniconda3/envs/serving/lib/python3.10/site-packages/vllm/engine/async_llm_engine.py", line 495, in from_engine_args engine = cls(parallel_config.worker_use_ray, File "/home/marco/miniconda3/envs/serving/lib/python3.10/site-packages/vllm/engine/async_llm_engine.py", line 269, in __init__ self.engine = self._init_engine(*args, **kwargs) File "/home/marco/miniconda3/envs/serving/lib/python3.10/site-packages/vllm/engine/async_llm_engine.py", line 314, in _init_engine return engine_class(*args, **kwargs) File "/home/marco/miniconda3/envs/serving/lib/python3.10/site-packages/vllm/engine/llm_engine.py", line 107, in __init__ self._init_workers_ray(placement_group) File "/home/marco/miniconda3/envs/serving/lib/python3.10/site-packages/vllm/engine/llm_engine.py", line 194, in _init_workers_ray self._run_workers( File "/home/marco/miniconda3/envs/serving/lib/python3.10/site-packages/vllm/engine/llm_engine.py", line 750, in _run_worker...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: _llm_engine.py", line 495, in from_engine_args engine = cls(parallel_config.worker_use_ray, File "/home/marco/miniconda3/envs/serving/lib/python3.10/site-packages/vllm/engine/async_llm_engine.py", line 269, in __init__...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: error when inferencing Mixtral AWQ When I try to run a AsyncEngine with ybelkada/Mixtral-8x7B-Instruct-v0.1-AWQ I get Traceback (most recent call last): File "/home/marco/Scrivania/TESI/serving/vllm_server.py", line 91,...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
