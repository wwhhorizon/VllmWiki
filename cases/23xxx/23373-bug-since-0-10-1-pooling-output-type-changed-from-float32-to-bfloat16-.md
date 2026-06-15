# vllm-project/vllm#23373: [Bug]: since 0.10.1, Pooling output type changed from float32 to bfloat16 (and different numeric results)

| 字段 | 值 |
| --- | --- |
| Issue | [#23373](https://github.com/vllm-project/vllm/issues/23373) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 4; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: since 0.10.1, Pooling output type changed from float32 to bfloat16 (and different numeric results)

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug ``` import vllm import asyncio async def vllm_emb_smolvlm_256m(text): """Generate text using SmolVLM-256M model via vLLM""" engine = vllm.AsyncLLMEngine.from_engine_args( vllm.AsyncEngineArgs( model="HuggingFaceTB/SmolVLM-256M-Instruct", task="embed", ) ) # Generate text output async for request_output in engine.generate( text, sampling_params=vllm.PoolingParams( task="embed", ), request_id="embd-1234" ): request_output: vllm.PoolingRequestOutput if request_output.finished: outputs = request_output.outputs return outputs.data, outputs.data.dtype if __name__ == "__main__": # Input text for generation text = "Hello, world! How are you today?" # Generate text result = asyncio.run(vllm_emb_smolvlm_256m(text)) print(result) ``` vllm 0.10.0 and 0.10.1 has different result ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 4: [Bug]: since 0.10.1, Pooling output type changed from float32 to bfloat16 (and different numeric results) bug;stale ### Your current environment ### 🐛 Describe the bug ``` import vllm import asyncio async def vllm_emb_s...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: Describe the bug ``` import vllm import asyncio async def vllm_emb_smolvlm_256m(text): """Generate text using SmolVLM-256M model via vLLM""" engine = vllm.AsyncLLMEngine.from_engine_args( vllm.AsyncEngineArgs( model="Hu...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: ) bug;stale ### Your current environment ### 🐛 Describe the bug ``` import vllm import asyncio async def vllm_emb_smolvlm_256m(text): """Generate text using SmolVLM-256M model via vLLM""" engine = vllm.AsyncLLMEngine.fr...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: # 🐛 Describe the bug ``` import vllm import asyncio async def vllm_emb_smolvlm_256m(text): """Generate text using SmolVLM-256M model via vLLM""" engine = vllm.AsyncLLMEngine.from_engine_args( vllm.AsyncEngineArgs( model...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: ype changed from float32 to bfloat16 (and different numeric results) bug;stale ### Your current environment ### 🐛 Describe the bug ``` import vllm import asyncio async def vllm_emb_smolvlm_256m(text): """Generate text u...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
