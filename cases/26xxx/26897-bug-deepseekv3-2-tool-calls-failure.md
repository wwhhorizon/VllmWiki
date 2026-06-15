# vllm-project/vllm#26897: [Bug]: deepseekv3.2 tool_calls failure

| 字段 | 值 |
| --- | --- |
| Issue | [#26897](https://github.com/vllm-project/vllm/issues/26897) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 14; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;moe |
| 子分类 | race_cond |
| Operator 关键词 | cuda;kernel;moe;triton |
| 症状 | build_error;crash;mismatch |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: deepseekv3.2 tool_calls failure

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug pip install vllm --extra-index-url https://wheels.vllm.ai/nightly pip install https://wheels.vllm.ai/dsv32/deep_gemm-2.1.0%2B594953a-cp312-cp312-linux_x86_64.whl server: `vllm serve deepseek-ai/DeepSeek-V3.2-Exp --served-model-name DeepSeek-V3.2-Exp --trust-remote-code --data-parallel-size 8 --enable-expert-parallel --enable-auto-tool-choice --tool-call-parser deepseek_v31 --chat-template ./deepseek_v31.jinjia ` Follow the code here，https://github.com/vllm-project/vllm/pull/23454 https://github.com/vllm-project/vllm/pull/23454#:~:text=Test-,Script,-(Non%2DStreaming)%3A Test Script (Non-Streaming): Result ``` root@pytorch-job-20251015152714476386g2zcyrl9qvtf:/# python3 test_tool_calls.py Traceback (most recent call last): File "//test_tool_calls.py", line 65, in response = client.chat.completions.create( ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ File "/usr/local/lib/python3.12/dist-packages/openai/_utils/_utils.py", line 286, in wrapper return func(*args, **kwargs) ^^^^^^^^^^^^^^^^^^^^^ File "/usr/local/lib/python3.12/dist-packages/openai/resources/chat/completions/completions.py", line 1156, in create return self._post( ^^^^^^^^^^^ File "/...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 6: e bug;stale ### Your current environment ### 🐛 Describe the bug pip install vllm --extra-index-url https://wheels.vllm.ai/nightly pip install https://wheels.vllm.ai/dsv32/deep_gemm-2.1.0%2B594953a-cp312-cp312-linux_x86_...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: _DP5 pid=826) ERROR 10-15 16:18:24 [core.py:710] torch.AcceleratorError: CUDA error: an illegal memory access was encountered (EngineCore_DP5 pid=826) ERROR 10-15 16:18:24 [core.py:710] CUDA kernel errors might be async...
- [MoE、GEMM 与 Expert Routing](../patterns/moe_gemm_routing.md) - 分数 3: s://wheels.vllm.ai/nightly pip install https://wheels.vllm.ai/dsv32/deep_gemm-2.1.0%2B594953a-cp312-cp312-linux_x86_64.whl server: `vllm serve deepseek-ai/DeepSeek-V3.2-Exp --served-model-name DeepSeek-V3.2-Exp --trust-...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 3: [Bug]: deepseekv3.2 tool_calls failure bug;stale ### Your current environment ### 🐛 Describe the bug pip install vllm --extra-index-url https://wheels.vllm.ai/nightly pip install https://wheels.vllm.ai/dsv32/deep_gemm-2...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 2: f._make_status_error_from_response(err.response) from None openai.InternalServerError: Error code: 500 - {'error': {'message': 'EngineCore encountered an issue. See stack trace (above) for the root cause.', 'type': 'Int...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
