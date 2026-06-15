# vllm-project/vllm#30204: [Bug]: Harmony parser skips last tokens in speculative decoding in streaming responses

| 字段 | 值 |
| --- | --- |
| Issue | [#30204](https://github.com/vllm-project/vllm/issues/30204) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: Harmony parser skips last tokens in speculative decoding in streaming responses

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug ``` import asyncio from vllm import SamplingParams from vllm.engine.arg_utils import AsyncEngineArgs from vllm.sampling_params import RequestOutputKind from vllm.v1.engine.async_llm import AsyncLLM async def stream_response(engine: AsyncLLM, prompt: str, request_id: str) -> None: sampling_params = SamplingParams(temperature=0.8, top_p=0.95, seed=42, output_kind=RequestOutputKind.DELTA) async for output in engine.generate(request_id=request_id, prompt=prompt, sampling_params=sampling_params): for completion in output.outputs: new_text = completion.text if new_text: print('output:' + new_text, flush=True) async def main(): engine_args = AsyncEngineArgs( model="openai/gpt-oss-20b", speculative_config={"model": "RedHatAI/gpt-oss-20b-speculator.eagle3", "num_speculative_tokens": 2, "method": "eagle3"} ) engine = AsyncLLM.from_engine_args(engine_args) prompt = 'Say hello world' await stream_response(engine, prompt, "request_id") engine.shutdown() if __name__ == "__main__": asyncio.run(main()) ``` When streaming gpt-oss with speculative decoding, the last few tokens are occasionally missed. Harmony parser gets to the last token, and set...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: lush=True) async def main(): engine_args = AsyncEngineArgs( model="openai/gpt-oss-20b", speculative_config={"model": "RedHatAI/gpt-oss-20b-speculator.eagle3", "num_speculative_tokens": 2, "method": "eagle3"} ) engine =...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 3: [Bug]: Harmony parser skips last tokens in speculative decoding in streaming responses bug;stale ### Your current environment ### 🐛 Describe the bug ``` import asyncio from vllm import SamplingParams from vllm.engine.ar...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: s bug;stale ### Your current environment ### 🐛 Describe the bug ``` import asyncio from vllm import SamplingParams from vllm.engine.arg_utils import AsyncEngineArgs from vllm.sampling_params import RequestOutputKind fro...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: ld" ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
