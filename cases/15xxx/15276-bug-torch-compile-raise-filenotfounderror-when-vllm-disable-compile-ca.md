# vllm-project/vllm#15276: [Bug]: torch.compile raise  FileNotFoundError when VLLM_DISABLE_COMPILE_CACHE=1

| 字段 | 值 |
| --- | --- |
| Issue | [#15276](https://github.com/vllm-project/vllm/issues/15276) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 0; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;quantization;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cuda;operator;quantization;sampling;triton |
| 症状 | build_error;crash;nan_inf |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: torch.compile raise  FileNotFoundError when VLLM_DISABLE_COMPILE_CACHE=1

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug When setting VLLM_DISABLE_COMPILE_CACHE=1, vLLM throws the following error: ```text ERROR 03-21 07:20:45 [core.py:330] EngineCore hit an exception: Traceback (most recent call last): ERROR 03-21 07:20:45 [core.py:330] File "/root/Code/vllm_dev/vllm/vllm/v1/engine/core.py", line 322, in run_engine_core ERROR 03-21 07:20:45 [core.py:330] engine_core = EngineCoreProc(*args, **kwargs) ERROR 03-21 07:20:45 [core.py:330] File "/root/Code/vllm_dev/vllm/vllm/v1/engine/core.py", line 277, in __init__ ERROR 03-21 07:20:45 [core.py:330] super().__init__(vllm_config, executor_class, log_stats) ERROR 03-21 07:20:45 [core.py:330] File "/root/Code/vllm_dev/vllm/vllm/v1/engine/core.py", line 62, in __init__ ERROR 03-21 07:20:45 [core.py:330] num_gpu_blocks, num_cpu_blocks = self._initialize_kv_caches( ERROR 03-21 07:20:45 [core.py:330] File "/root/Code/vllm_dev/vllm/vllm/v1/engine/core.py", line 121, in _initialize_kv_caches ERROR 03-21 07:20:45 [core.py:330] available_gpu_memory = self.model_executor.determine_available_memory() ERROR 03-21 07:20:45 [core.py:330] File "/root/Code/vllm_dev/vllm/vllm/v1/executor/abstract.py", line 66, in determin...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 5: [Bug]: torch.compile raise FileNotFoundError when VLLM_DISABLE_COMPILE_CACHE=1 bug ### Your current environment ### 🐛 Describe the bug When setting VLLM_DISABLE_COMPILE_CACHE=1, vLLM throws the following error: ```text...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: in __init__ ERROR 03-21 07:20:45 [core.py:330] super().__init__(vllm_config, executor_class, log_stats) ERROR 03-21 07:20:45 [core.py:330] File "/root/Code/vllm_dev/vllm/vllm/v1/engine/core.py", line 62, in __init__ ERR...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 3: nvert.py", line 962, in step ERROR 03-21 07:20:45 [core.py:330] self.dispatch_table[inst.opcode](self, inst) ERROR 03-21 07:20:45 [core.py:330] File "/root/anaconda3/envs/py310_vllm_dev/lib/python3.10/site-packages/torc...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 3: vailable_memory ERROR 03-21 07:20:45 [core.py:330] self.model_runner.profile_run() ERROR 03-21 07:20:45 [core.py:330] File "/root/Code/vllm_dev/vllm/vllm/v1/worker/gpu_model_runner.py", line 1468, in profile_run ERROR 0...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: ``` ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...

## Wiki 抽取状态

- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
