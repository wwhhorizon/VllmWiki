# vllm-project/vllm#22479: [Bug]: --tensor-parallel-size 2 seems broken for Blackwell 6000 pro since version 10

| 字段 | 值 |
| --- | --- |
| Issue | [#22479](https://github.com/vllm-project/vllm/issues/22479) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 5; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | attention_kv_cache;distributed_parallel;frontend_api;hardware_porting;model_support;quantization;sampling_logits;scheduler_memory |
| 子分类 | cold_start |
| Operator 关键词 | cache;cuda;quantization;sampling |
| 症状 | crash |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: --tensor-parallel-size 2 seems broken for Blackwell 6000 pro since version 10

### Issue 正文摘录

### Your current environment --tensor-parallel-size 2 seems broken for Blackwell 6000 pro since version 10. I can run with -tp 2 in version 9.2 with two rtx 6000 pro blackwell but it doesnt support newer models like GLM-4.5 etc ```text Version: 0.10.1.dev446+g7e3a8dc90.d20250808.cu129 ``` ### 🐛 Describe the bug tensor parallel is broken for rtx 6000 pro's ``` (EngineCore_0 pid=1422484) INFO 08-07 19:06:21 [kv_cache_utils.py:833] Maximum concurrency for 40,960 tokens per request: 11.46x Capturing CUDA graph shapes: 100%|███████████████████████████████████████████| 67/67 [00:07<00:00, 8.75it/s] (VllmWorker TP0 pid=1422634) INFO 08-07 19:06:29 [custom_all_reduce.py:196] Registering 8643 cuda graph addresses (VllmWorker TP1 pid=1422635) INFO 08-07 19:06:30 [custom_all_reduce.py:196] Registering 8643 cuda graph addresses (VllmWorker TP1 pid=1422635) INFO 08-07 19:06:31 [gpu_model_runner.py:2537] Graph capturing finished in 9 secs, took 1.21 GiB (VllmWorker TP0 pid=1422634) INFO 08-07 19:06:31 [gpu_model_runner.py:2537] Graph capturing finished in 9 secs, took 1.21 GiB (EngineCore_0 pid=1422484) INFO 08-07 19:06:31 [core.py:198] init engine (profile, create kv cache, warmup model) took...

## 候选优化模式

- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 8: parallel-size 2 seems broken for Blackwell 6000 pro since version 10 bug;stale ### Your current environment --tensor-parallel-size 2 seems broken for Blackwell 6000 pro since version 10. I can run with -tp 2 in version...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 5: Bug]: --tensor-parallel-size 2 seems broken for Blackwell 6000 pro since version 10 bug;stale ### Your current environment --tensor-parallel-size 2 seems broken for Blackwell 6000 pro since version 10. I can run with -t...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 5: OST (APIServer pid=1422128) INFO 08-07 19:06:32 [launcher.py:37] Route: /scale_elastic_ep, Methods: POST (APIServer pid=1422128) INFO 08-07 19:06:32 [launcher.py:37] Route: /is_scaling_elastic_ep, Methods: POST (APIServ...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 4: [Bug]: --tensor-parallel-size 2 seems broken for Blackwell 6000 pro since version 10 bug;stale ### Your current environment --tensor-parallel-size 2 seems broken for Blackwell 6000 pro since version 10. I can run with -...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: version 9.2 with two rtx 6000 pro blackwell but it doesnt support newer models like GLM-4.5 etc ```text Version: 0.10.1.dev446+g7e3a8dc90.d20250808.cu129 ``` ### 🐛 Describe the bug tensor parallel is broken for rtx 6000...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
