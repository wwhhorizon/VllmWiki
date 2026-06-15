# vllm-project/vllm#3415: [Bug]: RuntimeError: invalid argument to reset_peak_memory_stats when offline sampling using neuron

| 字段 | 值 |
| --- | --- |
| Issue | [#3415](https://github.com/vllm-project/vllm/issues/3415) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | ci_build;sampling_logits |
| 子分类 |  |
| Operator 关键词 | cuda;sampling |
| 症状 | crash |
| 根因提示 | env_dependency |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: RuntimeError: invalid argument to reset_peak_memory_stats when offline sampling using neuron

### Issue 正文摘录

### Your current environment ```text The output of `python collect_env.py` ``` Root cause: liine 88 to 98 in model_runner in this [commit](https://github.com/vllm-project/vllm/commit/385da2dae2b90e5273da8dfce881727bd9c574a1) breaks the neuron behavior. Because there is no CUDA env on neuron. ### 🐛 Describe the bug ``` Traceback (most recent call last): File "/root/space/vllm-main/examples/offline_inference_neuron.py", line 14, in llm = LLM( File "/opt/conda/lib/python3.10/site-packages/vllm/entrypoints/llm.py", line 109, in __init__ self.llm_engine = LLMEngine.from_engine_args(engine_args) File "/opt/conda/lib/python3.10/site-packages/vllm/engine/llm_engine.py", line 136, in from_engine_args engine = cls(*engine_configs, File "/opt/conda/lib/python3.10/site-packages/vllm/engine/llm_engine.py", line 101, in __init__ self.model_executor = executor_class(model_config, cache_config, File "/opt/conda/lib/python3.10/site-packages/vllm/executor/gpu_executor.py", line 42, in __init__ self._init_worker() File "/opt/conda/lib/python3.10/site-packages/vllm/executor/gpu_executor.py", line 77, in _init_worker self.driver_worker.load_model() File "/opt/conda/lib/python3.10/site-packages/vllm/wo...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: untimeError: invalid argument to reset_peak_memory_stats ``` performance ci_build;sampling_logits cuda;sampling crash env_dependency Your current environment
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: he output of `python collect_env.py` ``` Root cause: liine 88 to 98 in model_runner in this [commit](https://github.com/vllm-project/vllm/commit/385da2dae2b90e5273da8dfce881727bd9c574a1) breaks the neuron behavior. Beca...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: 3da8dfce881727bd9c574a1) breaks the neuron behavior. Because there is no CUDA env on neuron. ### 🐛 Describe the bug ``` Traceback (most recent call last): File "/root/space/vllm-main/examples/offline_inference_neuron.py...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: gument to reset_peak_memory_stats when offline sampling using neuron bug;stale ### Your current environment ```text The output of `python collect_env.py` ``` Root cause: liine 88 to 98 in model_runner in this [commit](h...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
