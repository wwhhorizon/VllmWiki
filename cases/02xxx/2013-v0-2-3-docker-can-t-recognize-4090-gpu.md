# vllm-project/vllm#2013: v0.2.3 docker can't recognize 4090 gpu

| 字段 | 值 |
| --- | --- |
| Issue | [#2013](https://github.com/vllm-project/vllm/issues/2013) |
| 状态 | closed |
| 标签 |  |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | ci_build;frontend_api;model_support;quantization |
| 子分类 | latency_reg |
| Operator 关键词 | cuda;quantization |
| 症状 | crash;slowdown |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> v0.2.3 docker can't recognize 4090 gpu

### Issue 正文摘录

Hi, I'm trying the official image with config ```bash vllm: 0 docker-vllm-1 | Traceback (most recent call last): docker-vllm-1 | File "/usr/lib/python3.10/runpy.py", line 196, in _run_module_as_main docker-vllm-1 | return _run_code(code, main_globals, None, docker-vllm-1 | File "/usr/lib/python3.10/runpy.py", line 86, in _run_code docker-vllm-1 | exec(code, run_globals) docker-vllm-1 | File "/workspace/vllm/entrypoints/openai/api_server.py", line 646, in docker-vllm-1 | engine = AsyncLLMEngine.from_engine_args(engine_args) docker-vllm-1 | File "/workspace/vllm/engine/async_llm_engine.py", line 486, in from_engine_args docker-vllm-1 | engine = cls(parallel_config.worker_use_ray, docker-vllm-1 | File "/workspace/vllm/engine/async_llm_engine.py", line 269, in __init__ docker-vllm-1 | self.engine = self._init_engine(*args, **kwargs) docker-vllm-1 | File "/workspace/vllm/engine/async_llm_engine.py", line 305, in _init_engine docker-vllm-1 | return engine_class(*args, **kwargs) docker-vllm-1 | File "/workspace/vllm/engine/llm_engine.py", line 110, in __init__ docker-vllm-1 | self._init_workers(distributed_init_method) docker-vllm-1 | File "/workspace/vllm/engine/llm_engine.py", line 142...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 5: v0.2.3 docker can't recognize 4090 gpu Hi, I'm trying the official image with config ```bash vllm: 0 docker-vllm-1 | Traceback (most recent call last): docker-vllm-1 | File "/usr/lib/python3.10/runpy.py", line 196,
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: llm/worker/worker.py", line 60, in init_model docker-vllm-1 | torch.cuda.set_device(self.device) docker-vllm-1 | File "/usr/local/lib/python3.10/dist-packages/torch/cuda/__init__.py", line 404, in set_device docker-vllm...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 2: ething for vllm to work? performance ci_build;frontend_api;model_support;quantization cuda;quantization crash;slowdown dtype;env_dependency Hi, I'm trying the official image with config
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: 3 docker can't recognize 4090 gpu Hi, I'm trying the official image with config ```bash vllm: 0 docker-vllm-1 | Traceback (most recent call last): docker-vllm-1 | File "/usr/lib/python3.10/runpy.py", line 196, in _run_m...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
