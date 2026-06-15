# vllm-project/vllm#11188: [Bug]: Speculative decoding draft acceptance rate decreasing over time

| 字段 | 值 |
| --- | --- |
| Issue | [#11188](https://github.com/vllm-project/vllm/issues/11188) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 8; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;quantization;sampling_logits;scheduler_memory;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cuda;fp8;operator;quantization;sampling;triton |
| 症状 | build_error;nan_inf |
| 根因提示 | dtype;env_dependency;memory_layout |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Speculative decoding draft acceptance rate decreasing over time

### Issue 正文摘录

### Your current environment ### Model Input Dumps _No response_ ### 🐛 Describe the bug I'm testing speculative decoding against our production traffic. We host the `vllm-openai:v0.6.4.post1` Docker image on Akash for our customer traffic. The main model is Llama 3.3 70B, and for the draft model I've tried Llama 3.1 8B, Llama 3.2 3B and Llama 3.2 1B. All three draft models have exhibited the same pathological behavior. On startup they perform very well, with the draft acceptance rate (DAR) between 0.6 & 0.8, and output token generation speed around 2-3 times faster than normal! Incredibly impressive! However, after about 15 minutes of production traffic, the DAR suddenly starts to drop, continues falling for about half an hour, until leveling out at a DAR somewhere between 0.2 and 0.4. By this time generation speed is lower than it is with SD turned off. I attach graphs of this decline for the 1B, 3B and 8B models. We are hosting each vLLM node on Akash with 2xH100 GPUs, 16xCPU cores & 128Gi ram. Here are the CLI args we're using: ``` --model meta-llama/Llama-3.3-70B-Instruct --quantization fp8 --tensor-parallel-size 2 --gpu-memory-utilization 0.99 --max-model-len 32768 --speculat...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: g against our production traffic. We host the `vllm-openai:v0.6.4.post1` Docker image on Akash for our customer traffic. The main model is Llama 3.3 70B, and for the draft model I've tried Llama 3.1 8B, Llama 3.2 3B and...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 4: [Bug]: Speculative decoding draft acceptance rate decreasing over time bug ### Your current environment ### Model Input Dumps _No response_ ### 🐛 Describe the bug I'm testing speculative decoding against our production t
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 3: e CLI args we're using: ``` --model meta-llama/Llama-3.3-70B-Instruct --quantization fp8 --tensor-parallel-size 2 --gpu-memory-utilization 0.99 --max-model-len 32768 --speculative_model meta-llama/Llama-3.2-3B-Instruct...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: the 1B, 3B and 8B models. We are hosting each vLLM node on Akash with 2xH100 GPUs, 16xCPU cores & 128Gi ram. Here are the CLI args we're using: ``` --model meta-llama/Llama-3.3-70B-Instruct --quantization fp8 --tensor-p...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 2: allel_size 1 --num_speculative_tokens 5 --enable-prefix-caching --use-v2-block-manager --enable-auto-tool-choice --tool-call-parser llama3_json --host 0.0.0.0 --api-key REDACTED --disable-log-requests ``` Any suggestion...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
