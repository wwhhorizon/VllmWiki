# vllm-project/vllm#17924: [Bug]: Usage of VLLM_ALLOW_LONG_MAX_MODEL_LEN=1 in V1 likely to cause a crash

| 字段 | 值 |
| --- | --- |
| Issue | [#17924](https://github.com/vllm-project/vllm/issues/17924) |
| 状态 | open |
| 标签 | bug |
| 评论 | 8; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | development |
| 工作域 | ci_build;frontend_api;model_support;scheduler_memory |
| 子分类 | runtime_err |
| Operator 关键词 | cuda |
| 症状 | build_error;crash |
| 根因提示 | env_dependency;memory_layout |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Usage of VLLM_ALLOW_LONG_MAX_MODEL_LEN=1 in V1 likely to cause a crash

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug Using `VLLM_ALLOW_LONG_MAX_MODEL_LEN=1` allows setting `--max-model-len` to be greater than what is found from the model configurtion. However, this only affect the scheduler's knowledge of the max context; the model configuration is not changed. In V1 with torch compilation, I've found that extending the context with `--max-model-len` causes a CUDA crash when a long-context request is processed (at least for models with `max_position_embeddings`): ``` ... /workspace/my-vllm/lib64/python3.12/site-packages/torch/_inductor/runtime/compile_tasks.py:45: : block: [337,0,0], thread: [112,0,0] Assertion `index out of bounds: 0 : block: [337,0,0], thread: [113,0,0] Assertion `index out of bounds: 0 : block: [337,0,0], thread: [114,0,0] Assertion `index out of bounds: 0 : block: [337,0,0], thread: [115,0,0] Assertion `index out of bounds: 0 <= tl.broadcast_to(tmp10, [XBLOCK]) < 4096` failed. ... ERROR 05-09 22:28:50 core.py:291] File "/workspace/my-vllm/lib64/python3.12/site-packages/vllm/v1/worker/gpu_worker.py", line 227, in execute_model ERROR 05-09 22:28:50 core.py:291] output = self.model_runner.execute_model(scheduler_output) ERROR...

## 现有链接修复摘要

#20904 [Frontend] Update the warning log when using VLLM_ALLOW_LONG_MAX_MODEL_LEN | #44286 [Bugfix] Fail fast or extend RoPE cache when VLLM_ALLOW_LONG_MAX_MODEL_LEN exceeds model positions

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: workspace/my-vllm/lib64/python3.12/site-packages/torch/_inductor/runtime/compile_tasks.py:45: : block: [337,0,0], thread: [112,0,0] Assertion `index out of bounds: 0 : block: [337,0,0], thread: [113,0,0] Assertion `inde...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: [Bug]: Usage of VLLM_ALLOW_LONG_MAX_MODEL_LEN=1 in V1 likely to cause a crash bug ### Your current environment ### 🐛 Describe the bug Using `VLLM_ALLOW_LONG_MAX_MODEL_LEN=1` allows setting `--max-model-len` to be greate...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: n, I've found that extending the context with `--max-model-len` causes a CUDA crash when a long-context request is processed (at least for models with `max_position_embeddings`): ``` ... /workspace/my-vllm/lib64/python3...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 2: python3.12/site-packages/torch/_inductor/runtime/compile_tasks.py:45: : block: [337,0,0], thread: [112,0,0] Assertion `index out of bounds: 0 : block: [337,0,0], thread: [113,0,0] Assertion `index out of bounds: 0 : blo...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: what is found from the model configurtion. However, this only affect the scheduler's knowledge of the max context; the model configuration is not changed. In V1 with torch compilation, I've found that extending the cont...

## 关联 PR 证据

| PR | 链接类型 | 置信度 | PR 标题 | 证据 |
| --- | --- | ---: | --- | --- |
| [#20904](https://github.com/vllm-project/vllm/pull/20904) | mentioned | 0.6 | [Frontend] Update the warning log when using VLLM_ALLOW_LONG_MAX_MODEL_LEN | t's Remove VLLM_ALLOW_LONG_MAX_MODEL_LEN~~ related to #20828 #20837 #17924 ......... ## updated warning & error - Error: Remove the content encouraging users to use VLLM_ALLOW_LON… |
| [#44286](https://github.com/vllm-project/vllm/pull/44286) | closes_keyword | 0.95 | [Bugfix] Fail fast or extend RoPE cache when VLLM_ALLOW_LONG_MAX_MODEL_LEN exceeds model positions | Fixes #17924. When `VLLM_ALLOW_LONG_MAX_MODEL_LEN=1` is set, vLLM lets the user pick a `--max-model-len` larger than the length derived from the model config, but it only skips |

## Wiki 抽取状态

- 后续迭代应在可用时读取完整讨论评论。
