# vllm-project/vllm#8948: [Bug]: AsyncLLMEngine CUDA runtime error 'device-side assert triggered'

| 字段 | 值 |
| --- | --- |
| Issue | [#8948](https://github.com/vllm-project/vllm/issues/8948) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 9; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | attention_kv_cache;ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;quantization;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | attention;cuda;fp8;kernel;operator;quantization;sampling;triton |
| 症状 | build_error;crash;mismatch |
| 根因提示 | dtype;env_dependency;memory_layout |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: AsyncLLMEngine CUDA runtime error 'device-side assert triggered'

### Issue 正文摘录

### Your current environment ### Model Input Dumps _No response_ ### 🐛 Describe the bug I'm running into CUDA runtime error 'device-side assert triggered' error on AsyncLLMEngine. I'm using the latest built vllm with this https://github.com/vllm-project/vllm/pull/6869 PR. I've made this mock test to see if I'm using everything correctly: api side: ``` from vllm.vllm import AsyncLLMEngine, AsyncEngineArgs, SamplingParams from pathlib import Path from fastapi import FastAPI from fastapi.responses import StreamingResponse app = FastAPI() vicuna_path = Path("/media/data/username/models/vicuna-7b-v1.5") args = AsyncEngineArgs() args.model = vicuna_path args.quantization = 'fp8' args.enable_lora = True engine = AsyncLLMEngine.from_engine_args(args) sampling_params = SamplingParams( min_tokens=1, max_tokens=200, top_p=1, repetition_penalty=1.0, length_penalty=1.0, temperature=0 ) @app.get("/test/") async def testing(): i = random.randint(10, 20) test_prompt = f"USER: Count from 1 to {i}. Write all numbers with comma as separator. \nASSISTANT:" results_generator = engine.generate(test_prompt, sampling_params, 1) async def stream_results() -> AsyncGenerator[bytes, None]: async for request_...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 5: o see if I'm using everything correctly: api side: ``` from vllm.vllm import AsyncLLMEngine, AsyncEngineArgs, SamplingParams from pathlib import Path from fastapi import FastAPI from fastapi.responses import StreamingRe...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 4: `` ../aten/src/ATen/native/cuda/Indexing.cu:1284: indexSelectLargeIndex: block: [1,0,0], thread: [80,0,0] Assertion `srcIndex , error_callback= >) handle: , error_callback= >)> Traceback (most recent call last): File "/...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 4: g]: AsyncLLMEngine CUDA runtime error 'device-side assert triggered' bug;stale ### Your current environment ### Model Input Dumps _No response_ ### 🐛 Describe the bug I'm running into CUDA runtime error 'device-side ass...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 3: ^^^^ File "/media/data/username/repos/allm_service/vllm/vllm/attention/backends/flash_attn.py", line 730, in forward prefill_output = torch.ops.vllm.flash_attn_varlen_func( ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ File "/...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 3: /vicuna-7b-v1.5") args = AsyncEngineArgs() args.model = vicuna_path args.quantization = 'fp8' args.enable_lora = True engine = AsyncLLMEngine.from_engine_args(args) sampling_params = SamplingParams( min_tokens=1, max_to...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
