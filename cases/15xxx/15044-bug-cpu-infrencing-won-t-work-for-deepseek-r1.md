# vllm-project/vllm#15044: [Bug]: CPU infrencing won't work for DeepSeek-R1

| 字段 | 值 |
| --- | --- |
| Issue | [#15044](https://github.com/vllm-project/vllm/issues/15044) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;frontend_api;gemm_linear;hardware_porting;model_support;quantization;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cuda;fp8;kernel;operator;quantization;sampling;triton |
| 症状 | build_error;crash;nan_inf |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: CPU infrencing won't work for DeepSeek-R1

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug During the call of the API, the inferencing server gived the following error messages: `ERROR 03-18 22:29:46 [serving_chat.py:677] Error in chat completion stream generator. ERROR 03-18 22:29:46 [serving_chat.py:677] Traceback (most recent call last): ERROR 03-18 22:29:46 [serving_chat.py:677] File "/home/sfever/anaconda3/envs/vllm-cpu/lib/python3.12/site-packages/vllm-0.8.0rc2.dev9+g6eaf1e5c.cpu-py3.12-linux-x86_64.egg/vllm/entrypoints/openai/serving_chat.py", line 373, in chat_completion_stream_generator ERROR 03-18 22:29:46 [serving_chat.py:677] async for res in result_generator: ERROR 03-18 22:29:46 [serving_chat.py:677] File "/home/sfever/anaconda3/envs/vllm-cpu/lib/python3.12/site-packages/vllm-0.8.0rc2.dev9+g6eaf1e5c.cpu-py3.12-linux-x86_64.egg/vllm/engine/multiprocessing/client.py", line 664, in _process_request ERROR 03-18 22:29:46 [serving_chat.py:677] raise request_output ERROR 03-18 22:29:46 [serving_chat.py:677] vllm.engine.multiprocessing.MQEngineDeadError: Engine loop is not running. Inspect the stacktrace to find the original error: NotImplementedError("Could not run 'vllm::apply_w8a8_block_fp8_linear' with argume...

## 候选优化模式

- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 4: ot run 'vllm::apply_w8a8_block_fp8_linear' with arguments from the 'CPU' backend. This could be because the operator doesn't exist for this backend, or was omitted during the selective/custom build process (if using cus...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: [Bug]: CPU infrencing won't work for DeepSeek-R1 bug;stale ### Your current environment ### 🐛 Describe the bug During the call of the API, the inferencing server gived the following error messages: `ERROR 03-18 22:29:46...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 4: [Bug]: CPU infrencing won't work for DeepSeek-R1 bug;stale ### Your current environment ### 🐛 Describe the bug During the call of the API, the inferencing server gived the following error messages: `ERROR 03-18 22:29:46...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 3: iginal error: NotImplementedError("Could not run 'vllm::apply_w8a8_block_fp8_linear' with arguments from the 'CPU' backend. This could be because the operator doesn't exist for this backend, or was omitted during the se...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: llm::apply_w8a8_block_fp8_linear' is only available for these backends: [CUDA, Meta, BackendSelect, Python, FuncTorchDynamicLayerBackMode, Functionalize, Named, Conjugate, Negative, ZeroTensor, ADInplaceOrView, Autograd...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
