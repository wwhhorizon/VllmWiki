# vllm-project/vllm#32434: [Bug]: gpt-oss no output with TRITON_ATTN backend with spec decode on ROCm

| 字段 | 值 |
| --- | --- |
| Issue | [#32434](https://github.com/vllm-project/vllm/issues/32434) |
| 状态 | open |
| 标签 | bug;rocm |
| 评论 | 11; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cuda;kernel;operator;sampling;triton |
| 症状 | build_error;nan_inf;slowdown |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: gpt-oss no output with TRITON_ATTN backend with spec decode on ROCm

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug The following test fails on ROCm when using the `TRITON_ATTN` backend. ``` pytest -v -s tests/entrypoints/openai/test_serving_chat.py::TestGPTOSSSpeculativeChat::test_gpt_oss_speculative_reasoning_leakage[with_tool_parser-exclude_tools_when_tool_choice_none] ``` It passes when you use `ROCM_AITER_UNIFIED_ATTN`, as proposed in https://github.com/vllm-project/vllm/pull/32431. The test runs without error until the assertion `assert len(reasoning_content) > 0, "No reasoning was generated."`. Indeed, no output is generated. ``` (APIServer pid=1393219) INFO 01-15 23:04:33 [metrics.py:100] SpecDecoding metrics: Mean acceptance length: 1.00, Accepted throughput: 0.00 tokens/s, Drafted throughput: 146.39 tokens/s, Accepted: 0 tokens, Drafted: 1464 tokens, Per-position acceptance rate: 0.000, 0.000, 0.000, Avg Draft acceptance rate: 0.0% (APIServer pid=1393219) INFO 01-15 23:04:33 [launcher.py:110] Shutting down FastAPI HTTP server. [rank0]:[W115 23:04:33.593767203 ProcessGroupNCCL.cpp:1524] Warning: WARNING: destroy_process_group() was not called before program exit, which can leak resources. For more info, please see https://pytorch.org/...

## 候选优化模式

- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 5: [Bug]: gpt-oss no output with TRITON_ATTN backend with spec decode on ROCm bug;rocm ### Your current environment ### 🐛 Describe the bug The following test fails on ROCm when using the `TRITON_ATTN` backend. ``` pytest -...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: oss_speculative_client = with_tool_parser = True @pytest.mark.asyncio async def test_gpt_oss_speculative_reasoning_leakage( self, gptoss_speculative_client: OpenAI, with_tool_parser: bool, ): if not with_tool_parser: py...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 3: [Bug]: gpt-oss no output with TRITON_ATTN backend with spec decode on ROCm bug;rocm ### Your current environment ### 🐛 Describe the bug The following test fails on ROCm when using the `TRITON_ATTN` backend. ``` pytest -...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: [Bug]: gpt-oss no output with TRITON_ATTN backend with spec decode on ROCm bug;rocm ### Your current environment ### 🐛 Describe the bug The following test fails on ROCm when using the `TRITON_ATTN` backend. ``` pytest -...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: [Bug]: gpt-oss no output with TRITON_ATTN backend with spec decode on ROCm bug;rocm ### Your current environment ### 🐛 Describe the bug The following test fails on ROCm when using the `TRITON_ATTN` backend. ``` pytest -v

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
