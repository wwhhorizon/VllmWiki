# vllm-project/vllm#13066: [Bug]: Deepseek-R1 performance issue on 2*8*H100

| 字段 | 值 |
| --- | --- |
| Issue | [#13066](https://github.com/vllm-project/vllm/issues/13066) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 9; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cuda;operator;sampling;triton |
| 症状 | build_error;nan_inf;slowdown |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Deepseek-R1 performance issue on 2*8*H100

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug During inference on a 2×8*H100 machine, Deepseek-R1 occasionally experiences a sudden drop in throughput (output tokens/s) to below 1 token/s, while GPU utilization remains at 100%. this is my launch script: ``` vllm serve /root/.cache/huggingface/hub/deepseek-ai/DeepSeek-R1 --served-model-name deepseek-r1 --enable-prefix-caching --max-model-len 32768 --gpu-memory-utilization 0.95 --tensor-parallel-size 8 --pipeline-parallel-size 2 --enable-chunked-prefill --max-num-batched-tokens 32768 --trust-remote-code --port 8000 ``` ![Image](https://github.com/user-attachments/assets/d6aa030d-89cd-4201-8df1-f2b30d92da21) When the input prompt is longer, the likelihood of encountering this issue increases significantly. Moreover, due to the persistence of such ultra-slow requests, subsequent incoming requests are also severely slowed down, achieving an average generation speed of only 7-8 tokens/s per request. Normal throughput resumes only after the problematic slow request fully completes its output. During such episodes, we observed through node_exporter that massive network traffic appeared on Ethernet NICs instead of InfiniBand (IB) NIC...

## 候选优化模式

- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 4: [Bug]: Deepseek-R1 performance issue on 2*8*H100 bug;stale ### Your current environment ### 🐛 Describe the bug During inference on a 2×8*H100 machine, Deepseek-R1 occasionally experiences a sudden drop in throughput (ou...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: LLM for a year and are big fans of the project, so we would greatly appreciate any assistance in troubleshooting this issue. ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues,...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: [Bug]: Deepseek-R1 performance issue on 2*8*H100 bug;stale ### Your current environment ### 🐛 Describe the bug During inference on a 2×8*H100 machine, Deepseek-R1 occasionally experiences a sudden drop in throughput (ou...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: remains at 100%. this is my launch script: ``` vllm serve /root/.cache/huggingface/hub/deepseek-ai/DeepSeek-R1 --served-model-name deepseek-r1 --enable-prefix-caching --max-model-len 32768 --gpu-memory-utilization 0.95...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 2: 2×8*H100 machine, Deepseek-R1 occasionally experiences a sudden drop in throughput (output tokens/s) to below 1 token/s, while GPU utilization remains at 100%. this is my launch script: ``` vllm serve /root/.cache/huggi...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
