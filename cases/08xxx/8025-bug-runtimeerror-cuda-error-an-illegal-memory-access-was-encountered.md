# vllm-project/vllm#8025: [Bug]: RuntimeError: CUDA error: an illegal memory access was encountered

| 字段 | 值 |
| --- | --- |
| Issue | [#8025](https://github.com/vllm-project/vllm/issues/8025) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 10; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | attention_kv_cache;ci_build;frontend_api;model_support;quantization |
| 子分类 |  |
| Operator 关键词 | attention;cuda;quantization |
| 症状 | build_error;crash |
| 根因提示 | env_dependency |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: RuntimeError: CUDA error: an illegal memory access was encountered

### Issue 正文摘录

### Your current environment VLLM image: v0.5.4 hardware: RTX4090 gpu driver: 550.78 model: qwen1.5-14b-chat-awq launch cmd: enable-prefix-caching ### 🐛 Describe the bug ``` 2024-08-30T15:30:57.763092820+08:00 INFO 08-30 15:30:57 async_llm_engine.py:175] Added request chat-1b1cbff0e55642b5a6823f983103f9fd. 2024-08-30T15:30:57.881850637+08:00 ERROR 08-30 15:30:57 async_llm_engine.py:58] Engine background task failed 2024-08-30T15:30:57.881886624+08:00 ERROR 08-30 15:30:57 async_llm_engine.py:58] Traceback (most recent call last): 2024-08-30T15:30:57.881901781+08:00 ERROR 08-30 15:30:57 async_llm_engine.py:58] File "/usr/local/lib/python3.10/dist-packages/vllm/engine/async_llm_engine.py", line 48, in _log_task_completion 2024-08-30T15:30:57.881912691+08:00 ERROR 08-30 15:30:57 async_llm_engine.py:58] return_value = task.result() 2024-08-30T15:30:57.881922782+08:00 ERROR 08-30 15:30:57 async_llm_engine.py:58] File "/usr/local/lib/python3.10/dist-packages/vllm/engine/async_llm_engine.py", line 648, in run_engine_loop 2024-08-30T15:30:57.881933110+08:00 ERROR 08-30 15:30:57 async_llm_engine.py:58] result = task.result() 2024-08-30T15:30:57.881943849+08:00 ERROR 08-30 15:30:57 async_llm...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: 30T15:30:57.882572543+08:00 ERROR 08-30 15:30:57 async_llm_engine.py:58] Compile with `TORCH_USE_CUDA_DSA` to enable device-side assertions. 2024-08-30T15:30:57.882582869+08:00 ERROR 08-30 15:30:57 async_llm_engine.py:5...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: [Bug]: RuntimeError: CUDA error: an illegal memory access was encountered bug ### Your current environment VLLM image: v0.5.4 hardware: RTX4090 gpu driver: 550.78 model: qwen1.5-14b-chat-awq launch cmd: enable-prefix-ca...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 2: nc_llm_engine.py:58] attn_output = self.attn(q, k, v, kv_cache, attn_metadata) 2024-08-30T15:30:57.882389814+08:00 ERROR 08-30 15:30:57 async_llm_engine.py:58] File "/usr/local/lib/python3.10/dist-packages/torch/nn/modu...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: ent environment VLLM image: v0.5.4 hardware: RTX4090 gpu driver: 550.78 model: qwen1.5-14b-chat-awq launch cmd: enable-prefix-caching ### 🐛 Describe the bug ``` 2024-08-30T15:30:57.763092820+08:00 INFO 08-30 15:30:57 as...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: 30:57.763092820+08:00 INFO 08-30 15:30:57 async_llm_engine.py:175] Added request chat-1b1cbff0e55642b5a6823f983103f9fd. 2024-08-30T15:30:57.881850637+08:00 ERROR 08-30 15:30:57 async_llm_engine.py:58] Engine background...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
