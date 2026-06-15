# vllm-project/vllm#29855: [Bug]: DSR1 fp8/nvfp4 MTP with spec num 3 load weight failure

| 字段 | 值 |
| --- | --- |
| Issue | [#29855](https://github.com/vllm-project/vllm/issues/29855) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | attention_kv_cache;distributed_parallel;frontend_api;model_support;moe;quantization;scheduler_memory |
| 子分类 | latency_reg |
| Operator 关键词 | fp8;moe |
| 症状 | slowdown |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: DSR1 fp8/nvfp4 MTP with spec num 3 load weight failure

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug B200 and GB200 have the same issue. Error message: [0;36m(Worker_TP2_EP2 pid=3559682)[0;0m ERROR 11-30 07:51:23 [multiproc_executor.py:750] File "/usr/local/lib/python3.12/dist-packages/vllm/model_executor/model_loader/base_loader.py", line 55, in load_model [0;36m(Worker_TP2_EP2 pid=3559682)[0;0m ERROR 11-30 07:51:23 [multiproc_executor.py:750] self.load_weights(model, model_config) [0;36m(Worker_TP2_EP2 pid=3559682)[0;0m ERROR 11-30 07:51:23 [multiproc_executor.py:750] File "/usr/local/lib/python3.12/dist-packages/vllm/model_executor/model_loader/default_loader.py", line 305, in load_weights [0;36m(Worker_TP2_EP2 pid=3559682)[0;0m ERROR 11-30 07:51:23 [multiproc_executor.py:750] loaded_weights = model.load_weights(self.get_all_weights(model_config, model)) [0;36m(Worker_TP2_EP2 pid=3559682)[0;0m ERROR 11-30 07:51:23 [multiproc_executor.py:750] ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ [0;36m(Worker_TP2_EP2 pid=3559682)[0;0m ERROR 11-30 07:51:23 [multiproc_executor.py:750] File "/usr/local/lib/python3.12/dist-packages/vllm/model_executor/models/deepseek_mtp.py", line 396, in load_weights [0;36m(W...

## 候选优化模式

- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 5: [Bug]: DSR1 fp8/nvfp4 MTP with spec num 3 load weight failure bug;stale ### Your current environment ### 🐛 Describe the bug B200 and GB200 have the same issue. Error message: [0;36m(Worker_TP2_EP2 pid=3559682)[0;0m ER...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 4: [Bug]: DSR1 fp8/nvfp4 MTP with spec num 3 load weight failure bug;stale ### Your current environment ### 🐛 Describe the bug B200 and GB200 have the same issue. Error message: [0;36m(Worker_TP2_EP2 pid=3559682)[0;0m ER...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: ilure bug;stale ### Your current environment ### 🐛 Describe the bug B200 and GB200 have the same issue. Error message: [0;36m(Worker_TP2_EP2 pid=3559682)[0;0m ERROR 11-30 07:51:23 [multiproc_executor.py:750] File "/us...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 2: 1 export VLLM_USE_TRTLLM_RAGGED_DEEPSEEK_PREFILL=1 export VLLM_ATTENTION_BACKEND=FLASHINFER_MLA export VLLM_FLASHINFER_MOE_BACKEND=latency export VLLM_USE_FLASHINFER_MOE_FP4=1 export VLLM_USE_FLASHINFER_MOE_FP8=1 FP8 se...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: oc_executor.py:750] File "/usr/local/lib/python3.12/dist-packages/vllm/model_executor/model_loader/base_loader.py", line 55, in load_model [0;36m(Worker_TP2_EP2 pid=3559682)[0;0m ERROR 11-30 07:51:23 [multiproc_execut...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
