# vllm-project/vllm#16285: [Bug]: Deepseek R1 gives nonsensical tokens during offline Inference

| 字段 | 值 |
| --- | --- |
| Issue | [#16285](https://github.com/vllm-project/vllm/issues/16285) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;quantization;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cuda;operator;quantization;sampling;triton |
| 症状 | build_error;nan_inf |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Deepseek R1 gives nonsensical tokens during offline Inference

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug Here is my code to initialize the model: ``` engine_args = AsyncEngineArgs( model="cognitivecomputations/DeepSeek-R1-AWQ", tensor_parallel_size=8, gpu_memory_utilization=0.92, trust_remote_code=True, dtype=torch.half, max_num_seqs=128, max_model_len=64000, quantization="moe_wna16" ) self.engine = AsyncLLMEngine.from_engine_args(engine_args) ``` And here is my code to do the generation: ``` async for result in self.engine.generate(request.content, sampling_params, request_id=request_id): if result.outputs: output = result.outputs[0] prompt_tokens = len(result.prompt_token_ids) completion_tokens = len(output.token_ids) ``` The outputs are nonsensical think tokens, within nothing else: ```--- Request --- Prompt: Write a short story about a robot discovering emotions. Max Tokens: 200 Temperature: 0.7 Top P: 0.9 --- Response Stream --- s hã [�ể íật states ; ;) c ) ů --- End of Stream ---``` ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: test/), which can answer lots of frequently asked questions. correctness ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;quantization;sampling_logits;speculative_decoding cuda;operator;quantiza...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 3: [Bug]: Deepseek R1 gives nonsensical tokens during offline Inference bug;stale ### Your current environment ### 🐛 Describe the bug Here is my code to initialize the model: ``` engine_args = AsyncEngineArgs( model="cogni...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 2: memory_utilization=0.92, trust_remote_code=True, dtype=torch.half, max_num_seqs=128, max_model_len=64000, quantization="moe_wna16" ) self.engine = AsyncLLMEngine.from_engine_args(engine_args) ``` And here is my code to...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: ``` ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: sampling_logits;speculative_decoding cuda;operator;quantization;sampling;triton build_error;nan_inf dtype;env_dependency Your current environment

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
