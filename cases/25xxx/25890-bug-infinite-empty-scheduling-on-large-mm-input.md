# vllm-project/vllm#25890: [Bug]: infinite empty scheduling on large mm input

| 字段 | 值 |
| --- | --- |
| Issue | [#25890](https://github.com/vllm-project/vllm/issues/25890) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 5; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;quantization;sampling_logits;scheduler_memory;speculative_decoding |
| 子分类 | kernel_eff |
| Operator 关键词 | cuda;gemm;operator;quantization;sampling;triton |
| 症状 | build_error |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: infinite empty scheduling on large mm input

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug ## Serve ```shell vllm serve Qwen/Qwen2.5-VL-72B-Instruct-AWQ --port 8011 --host 0.0.0.0 --uvicorn-log-level info --cpu-offload-gb 0 --max-model-len 32768 --limit-mm-per-prompt {"image":5,"video":2} --allowed-local-media-path /home --skip-mm-profiling --gpu-memory-utilization 0.9 ``` ## Generate ```python { "messages": [ { "role": "system", "content": [ {"type": "text", "text": "describe the video"}, { "type": "video_url", "video_url": { "url": "file:///home/cache/ec8fdb302486a171fe3e41a90bd0176bc05e99b2.mp4" }, }, ], } ], "model": "Qwen/Qwen2.5-VL-72B-Instruct-AWQ", "seed": 42, "temperature": 0.2, "top_p": 0.1, } ``` ## Bug The sever gives no response when the video is large (~22272 tokens) but ok when it is small(~6093 tokens). When stuck, the worker process takes 100% cpu and 0% gpu, the stack dump from `py-spy` looks like: ``` Process 1829647: VLLM::EngineCore Python v3.12.9 (envs/vllm/bin/python3.12) Thread 1829647 (active+gil): "MainThread" get_num_common_prefix_blocks (vllm/v1/core/single_type_kv_cache_manager.py:288) get_num_common_prefix_blocks (vllm/v1/core/kv_cache_coordinator.py:138) get_num_common_prefix_blocks (vllm...

## 候选优化模式

- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 6: ocks (vllm/v1/core/kv_cache_manager.py:340) schedule (vllm/v1/core/sched/scheduler.py:540) step (vllm/v1/engine/core.py:287) _process_engine_step (vllm/v1/engine/core.py:745) run_busy_loop (vllm/v1/engine/core.py:720) r...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: test/), which can answer lots of frequently asked questions. performance ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;quantization;sampling_logits;scheduler_memory;speculative_decoding cuda;...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: es no response when the video is large (~22272 tokens) but ok when it is small(~6093 tokens). When stuck, the worker process takes 100% cpu and 0% gpu, the stack dump from `py-spy` looks like: ``` Process 1829647: VLLM:...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: nt environment ### 🐛 Describe the bug ## Serve ```shell vllm serve Qwen/Qwen2.5-VL-72B-Instruct-AWQ --port 8011 --host 0.0.0.0 --uvicorn-log-level info --cpu-offload-gb 0 --max-model-len 32768 --limit-mm-per-prompt {"im...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 2: ineCore_0 pid=2029978) WARNING 09-29 20:09:30 [topk_topp_sampler.py:102] FlashInfer 0.2.3+ does not support per-request generators. Falling back to PyTorch-native implementation. (EngineCore_0 pid=2029978) INFO 09-29 20...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
