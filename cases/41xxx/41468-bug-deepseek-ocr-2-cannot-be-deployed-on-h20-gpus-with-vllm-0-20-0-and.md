# vllm-project/vllm#41468: [Bug]: Deepseek-OCR-2 cannot be deployed on H20 GPUs with vllm[0.20.0] and vllm-docker.

| 字段 | 值 |
| --- | --- |
| Issue | [#41468](https://github.com/vllm-project/vllm/issues/41468) |
| 状态 | open |
| 标签 | bug |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | attention_kv_cache;ci_build;distributed_parallel;frontend_api;gemm_linear;hardware_porting;model_support;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cuda;operator;sampling;triton |
| 症状 | build_error;crash;nan_inf |
| 根因提示 | env_dependency;shape |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Deepseek-OCR-2 cannot be deployed on H20 GPUs with vllm[0.20.0] and vllm-docker.

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug When I launch vllm to serve DeepSeek-OCR-2, it always gets the following error even the message is only: ``` "messages": [{"role": "user", "content": "Hello"}] ``` The error: ``` (EngineCore pid=2699768) DEBUG 05-01 14:40:30 [v1/engine/core.py:1198] EngineCore loop active. (EngineCore pid=2699768) DEBUG 05-01 14:40:30 [v1/worker/gpu_model_runner.py:3905] Running batch with cudagraph_mode: NONE, batch_descriptor: BatchDescriptor(num_tokens=8, num_reqs=None, uniform=False, has_lora=False, num_active_loras=0), should_ubatch: False, num_tokens_across_dp: None (EngineCore pid=2699768) DEBUG 05-01 14:40:30 [v1/worker/gpu_model_runner.py:3926] ubatch_slices: None, ubatch_slices_padded: None (APIServer pid=2698734) ERROR 05-01 14:40:30 [v1/engine/async_llm.py:699] AsyncLLM output_handler failed. (APIServer pid=2698734) ERROR 05-01 14:40:30 [v1/engine/async_llm.py:699] Traceback (most recent call last): (APIServer pid=2698734) ERROR 05-01 14:40:30 [v1/engine/async_llm.py:699] File "/mnt/nvme3/zwx/.venv/lib/python3.13/site-packages/vllm/v1/engine/async_llm.py", line 655, in output_handler (APIServer pid=2698734) ERROR 05-01 14:40:30 [v1/en...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: Deepseek-OCR-2 cannot be deployed on H20 GPUs with vllm[0.20.0] and vllm-docker. bug ### Your current environment ### 🐛 Describe the bug When I launch vllm to serve DeepSeek-OCR-2, it always gets the following error eve...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 3: DEBUG CUDA_LAUNCH_BLOCKING=1 TORCH_USE_CUDA_DSA=1 VLLM_USE_V1=0 VLLM_USE_FLASHINFER=0 VLLM_ATTENTION_BACKEND=FLASH_ATTN CUDA_VISIBLE_DEVICES=0 vllm serve /modelremote/deepseek-ai_DeepSeek-OCR-2/ --trust-remote-code --ap...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: G 05-01 14:40:30 [v1/worker/gpu_model_runner.py:3905] Running batch with cudagraph_mode: NONE, batch_descriptor: BatchDescriptor(num_tokens=8, num_reqs=None, uniform=False, has_lora=False, num_active_loras=0), should_ub...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 2: batch_descriptor: BatchDescriptor(num_tokens=8, num_reqs=None, uniform=False, has_lora=False, num_active_loras=0), should_ubatch: False, num_tokens_across_dp: None (EngineCore pid=2699768) DEBUG 05-01 14:40:30 [v1/worke...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: oop active. (EngineCore pid=2699768) DEBUG 05-01 14:40:30 [v1/worker/gpu_model_runner.py:3905] Running batch with cudagraph_mode: NONE, batch_descriptor: BatchDescriptor(num_tokens=8, num_reqs=None, uniform=False, has_l...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
