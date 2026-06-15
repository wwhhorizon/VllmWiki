# vllm-project/vllm#22843: [Bug]: vLLM (AsyncLLMEngine, LLM) engine initialization fails when using runai_streamer

| 字段 | 值 |
| --- | --- |
| Issue | [#22843](https://github.com/vllm-project/vllm/issues/22843) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 36; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | attention_kv_cache;ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cache;cuda;operator;sampling;triton |
| 症状 | build_error;crash;nan_inf |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: vLLM (AsyncLLMEngine, LLM) engine initialization fails when using runai_streamer

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug When I use vllm serve with runai_streamer, everything works as expected, however, trying to initialize the LLM or AsyncLLMEngine in python code with runai_streamer will lead to engine failure because it seems like it doesn't download the config.json/other model files to the tmp model directory created. It properly uses runai_streamer to first stream the model from s3, and then we get a failure regarding the HuggingFace validation of the tmp directory, and after some digging it is related to that directory not having the config.json. I think we need to similarly download the s3 files into the tmp directory like it is being done for online serve. Refer to the following code snippet and error: ```python from vllm import SamplingParams, LLM, AsyncEngineArgs, AsyncLLMEngine tests = ["hello what is your name?"] sampling_params = SamplingParams(temperature=0.8, top_p=0.95) kwargs = { "model": "s3://path/to/model/qwen3-32b/", "tensor_parallel_size": 8, "max_model_len": 20000, "load_format": "runai_streamer", } engine_args = AsyncEngineArgs( **kwargs, ) # Trying to launch AsyncLLMEngine fails engine = AsyncLLMEngine.from_engine_args(engin...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 6: ill lead to engine failure because it seems like it doesn't download the config.json/other model files to the tmp model directory created. It properly uses runai_streamer to first stream the model from s3, and then we g...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: ve. Refer to the following code snippet and error: ```python from vllm import SamplingParams, LLM, AsyncEngineArgs, AsyncLLMEngine tests = ["hello what is your name?"] sampling_params = SamplingParams(temperature=0.8, t...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: ` t ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 2: n from vllm import SamplingParams, LLM, AsyncEngineArgs, AsyncLLMEngine tests = ["hello what is your name?"] sampling_params = SamplingParams(temperature=0.8, top_p=0.95) kwargs = { "model": "s3://path/to/model/qwen3-32...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: upport;sampling_logits;speculative_decoding cache;cuda;operator;sampling;triton build_error;crash;nan_inf env_dependency Your current environment

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
