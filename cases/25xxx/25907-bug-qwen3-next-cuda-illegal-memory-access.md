# vllm-project/vllm#25907: [Bug]: qwen3-next CUDA illegal memory access

| 字段 | 值 |
| --- | --- |
| Issue | [#25907](https://github.com/vllm-project/vllm/issues/25907) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;sampling_logits;speculative_decoding |
| 子分类 |  |
| Operator 关键词 | cuda;operator;sampling;triton |
| 症状 | build_error;crash |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: qwen3-next CUDA illegal memory access

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug Normal openai server and random benchmark setup on 4x H100 for Qwen3-Next, engine crashes with CUDA illegal memory access in mamba causal_conv1d. This is on an editable build of v0.10.2 plus a cherry pick of [PR #25341](https://github.com/vllm-project/vllm/pull/25341). Not sure if this is reproducible for others, but on my system the error always appears on the 21st request. Server: ``` vllm serve Qwen/Qwen3-Next-80B-A3B-Instruct \ --port 8000 \ --host 0.0.0.0 \ --no-enable-prefix-caching \ --tensor-parallel-size 4 > out.txt 2>&1 ``` Benchmark: ``` vllm bench serve \ --backend vllm \ --model Qwen/Qwen3-Next-80B-A3B-Instruct \ --endpoint /v1/chat/completions \ --endpoint-type openai-chat \ --dataset-name random \ --random-input-len 512 \ --random-output-len 512 \ --num-prompts 21 \ --max-concurrency 1 ``` Traceback: https://gist.github.com/felixzhu555/217a64cb16a9506391c24b32743f1ccc ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently as...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: UDA illegal memory access in mamba causal_conv1d. This is on an editable build of v0.10.2 plus a cherry pick of [PR #25341](https://github.com/vllm-project/vllm/pull/25341). Not sure if this is reproducible for others,...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: [Bug]: qwen3-next CUDA illegal memory access bug;stale ### Your current environment ### 🐛 Describe the bug Normal openai server and random benchmark setup on 4x H100 for Qwen3-Next, engine crashes with CUDA illegal memo...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 3: [Bug]: qwen3-next CUDA illegal memory access bug;stale ### Your current environment ### 🐛 Describe the bug Normal openai server and random benchmark setup on 4x H100 for Qwen3-Next, engine crashes with CUDA illegal memo...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 2: arallel-size 4 > out.txt 2>&1 ``` Benchmark: ``` vllm bench serve \ --backend vllm \ --model Qwen/Qwen3-Next-80B-A3B-Instruct \ --endpoint /v1/chat/completions \ --endpoint-type openai-chat \ --dataset-name random \ --r...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: [Bug]: qwen3-next CUDA illegal memory access bug;stale ### Your current environment ### 🐛 Describe the bug Normal openai server and random benchmark setup on 4x H100 for Qwen3-Next, engine crashes with CUDA illegal memo...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
