# vllm-project/vllm#10258: [Usage]:Qwen2-VL not support Lora

| 字段 | 值 |
| --- | --- |
| Issue | [#10258](https://github.com/vllm-project/vllm/issues/10258) |
| 状态 | closed |
| 标签 | usage |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Usage]:Qwen2-VL not support Lora

### Issue 正文摘录

### Your current environment ```text The output of `python collect_env.py` ``` File "/home/mlr/.local/lib/python3.10/site-packages/vllm/engine/async_llm_engine.py", line 265, in __init__ super().__init__(*args, **kwargs) File "/home/mlr/.local/lib/python3.10/site-packages/vllm/engine/llm_engine.py", line 335, in __init__ self.model_executor = executor_class( File "/home/mlr/.local/lib/python3.10/site-packages/vllm/executor/executor_base.py", line 47, in __init__ self._init_executor() File "/home/mlr/.local/lib/python3.10/site-packages/vllm/executor/gpu_executor.py", line 40, in _init_executor self.driver_worker.load_model() File "/home/mlr/.local/lib/python3.10/site-packages/vllm/worker/worker.py", line 183, in load_model self.model_runner.load_model() File "/home/mlr/.local/lib/python3.10/site-packages/vllm/worker/model_runner.py", line 1062, in load_model self.model = get_model(model_config=self.model_config, File "/home/mlr/.local/lib/python3.10/site-packages/vllm/model_executor/model_loader/__init__.py", line 19, in get_model return loader.load_model(model_config=model_config, File "/home/mlr/.local/lib/python3.10/site-packages/vllm/model_executor/model_loader/loader.py", line...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: cutor/model_loader/loader.py", line 175, in _initialize_model return build_model( File "/home/mlr/.local/lib/python3.10/site-packages/vllm/model_executor/model_loader/loader.py", line 156, in build_model extra_kwargs =...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: [Usage]:Qwen2-VL not support Lora usage ### Your current environment ```text The output of `python collect_env.py` ``` File "/home/mlr/.local/lib/python3.10/site-packages/vllm/engine/async_llm_engine.py", line 265, in _...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: lm. ### Before submitting a new issue... - [X] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
