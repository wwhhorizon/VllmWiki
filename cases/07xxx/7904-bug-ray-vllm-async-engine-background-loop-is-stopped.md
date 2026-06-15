# vllm-project/vllm#7904: [Bug]: ray + vllm async engine: Background loop is stopped

| 字段 | 值 |
| --- | --- |
| Issue | [#7904](https://github.com/vllm-project/vllm/issues/7904) |
| 状态 | closed |
| 标签 | bug;ray |
| 评论 | 15; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | development |
| 工作域 | ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;quantization;sampling_logits;speculative_decoding |
| 子分类 | env_compat |
| Operator 关键词 | cuda;operator;quantization;triton |
| 症状 | build_error;crash |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: ray + vllm async engine: Background loop is stopped

### Issue 正文摘录

### 🐛 Describe the bug this code is slighly modified from [async llm engine test](https://github.com/vllm-project/vllm/blob/4cf256ae7f8b0be8f06f6b85821e55d4f5bdaa13/tests/async_engine/test_async_llm_engine.py#L115) ``` def test_asyncio_run(): wait_for_gpu_memory_to_clear( devices=list(range(torch.cuda.device_count())), threshold_bytes=2 * 2**30, timeout_s=60, ) engine = AsyncLLMEngine.from_engine_args( AsyncEngineArgs(model="facebook/opt-125m")) async def run(prompt: str): sampling_params = SamplingParams( temperature=0, max_tokens=32, ) async for output in engine.generate(prompt, sampling_params, request_id=prompt): final_output = output return final_output async def generate(): return await asyncio.gather( run("test0"), run("test1"), ) results = asyncio.run(generate()) results = asyncio.run(generate()) # called it twice, this will met error assert len(results) == 2 ``` This works perfect, but when it's run under ray, the 2th ` results = asyncio.run(generate()) ` will get the error message: ``` [[36m(VLLMActor pid=50643) [[0m INFO 08-17 14:18:16 async_llm_engine.py:140] Finished request ed5d5c0f908a4a478793db4a47b4a772. [[36m(VLLMActor pid=50643) [[0m INFO 08-17 14:18:16 async_ll...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: aa13/tests/async_engine/test_async_llm_engine.py#L115) ``` def test_asyncio_run(): wait_for_gpu_memory_to_clear( devices=list(range(torch.cuda.device_count())), threshold_bytes=2 * 2**30, timeout_s=60, ) engine = AsyncL...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: ) engine = AsyncLLMEngine.from_engine_args( AsyncEngineArgs(model="facebook/opt-125m")) async def run(prompt: str): sampling_params = SamplingParams( temperature=0, max_tokens=32, ) async for output in engine.generate(p...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: sampling_params, request_id=prompt): final_output = output return final_output async def generate(): return await asyncio.gather( run("test0"), run("test1"), ) results
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: tization;sampling_logits;speculative_decoding cuda;operator;quantization;triton build_error;crash env_dependency 🐛 Describe the bug
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 1: i_build;distributed_parallel;frontend_api;hardware_porting;model_support;quantization;sampling_logits;speculative_decoding cuda;operator;quantization;triton build_error;crash env_dependency 🐛 Describe the bug

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
