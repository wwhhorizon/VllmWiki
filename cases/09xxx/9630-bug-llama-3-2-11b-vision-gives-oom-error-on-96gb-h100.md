# vllm-project/vllm#9630: [Bug]: Llama-3.2-11B-Vision gives OOM error on 96GB H100

| 字段 | 值 |
| --- | --- |
| Issue | [#9630](https://github.com/vllm-project/vllm/issues/9630) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 8; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | activation_norm;ci_build;frontend_api;hardware_porting;model_support;multimodal_vlm;sampling_logits;scheduler_memory;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | activation;cuda;operator;sampling;triton |
| 症状 | build_error;crash;nan_inf;oom |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Llama-3.2-11B-Vision gives OOM error on 96GB H100

### Issue 正文摘录

### Your current environment ### Model Input Dumps _No response_ ### 🐛 Describe the bug vllm serve fails with OOM error. ``` INFO 10-23 19:55:16 model_runner.py:1067] Loading model weights took 19.8557 GB INFO 10-23 19:55:16 enc_dec_model_runner.py:301] Starting profile run for multi-modal models. Process SpawnProcess-1: Traceback (most recent call last): File "/usr/lib/python3.10/multiprocessing/process.py", line 314, in _bootstrap self.run() File "/usr/lib/python3.10/multiprocessing/process.py", line 108, in run self._target(*self._args, **self._kwargs) File "/usr/local/lib/python3.10/dist-packages/vllm/engine/multiprocessing/engine.py", line 390, in run_mp_engine engine = MQLLMEngine.from_engine_args(engine_args=engine_args, File "/usr/local/lib/python3.10/dist-packages/vllm/engine/multiprocessing/engine.py", line 139, in from_engine_args return cls( File "/usr/local/lib/python3.10/dist-packages/vllm/engine/multiprocessing/engine.py", line 78, in __init__ self.engine = LLMEngine(*args, **kwargs) File "/usr/local/lib/python3.10/dist-packages/vllm/engine/llm_engine.py", line 348, in __init__ self._initialize_kv_caches() File "/usr/local/lib/python3.10/dist-packages/vllm/engine/ll...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: : CUDA out of memory. Tried to allocate 10.08 GiB. GPU 0 has a total capacity of 94.50 GiB of which 10.06 GiB is free. Including non-PyTorch memory, this process has 0 bytes memory in use. Of the allocated memory 80.48...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: [Bug]: Llama-3.2-11B-Vision gives OOM error on 96GB H100 bug;stale ### Your current environment ### Model Input Dumps _No response_ ### 🐛 Describe the bug vllm serve fails with OOM error. ``` INFO 10-23 19:55:16 model_r
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 4: [Bug]: Llama-3.2-11B-Vision gives OOM error on 96GB H100 bug;stale ### Your current environment ### Model Input Dumps _No response_ ### 🐛 Describe the bug vllm serve fails with OOM error. ``` INFO 10-23 19:55:16 model_r...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: [Bug]: Llama-3.2-11B-Vision gives OOM error on 96GB H100 bug;stale ### Your current environment ### Model Input Dumps _No response_ ### 🐛 Describe the bug vllm serve fails with OOM error. ``` INFO 10-23 19:55:16 model_r...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 2: ib/python3.10/dist-packages/vllm/scripts.py", line 195, in main args.dispatch_function(args) File "/usr/local/lib/python3.10/dist-packages/vllm/scripts.py", line 41, in serve uvloop.run(run_server(args)) File "/usr/loca...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
