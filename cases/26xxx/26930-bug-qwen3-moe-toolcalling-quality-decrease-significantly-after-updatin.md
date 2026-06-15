# vllm-project/vllm#26930: [Bug]: Qwen3 MoE toolcalling quality decrease significantly after updating to 0.11.0

| 字段 | 值 |
| --- | --- |
| Issue | [#26930](https://github.com/vllm-project/vllm/issues/26930) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 19; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;frontend_api;gemm_linear;hardware_porting;model_support;moe;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cuda;moe;operator;sampling;triton |
| 症状 | build_error;nan_inf |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Qwen3 MoE toolcalling quality decrease significantly after updating to 0.11.0

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug After updating from 0.10.2 to 0.11.0, Qwen3-30B-A3B-Thinking-2507 behaves notably worse especially in toolcalling scenarios. - It generates in English instead of target language more often - It fails to use any tool much more often - Its output fails to format more often - It produces catastrophic repetition from time to time, which never happens with 0.10.2 - Also, it mentions words in the default prompt like "XML tags" often, which never happens with 0.10.2 Here is the main part of my script: ``` params=( --served_model_name "Qwen3-30B-A3B-Thinking-2507" --host 0.0.0.0 --port 8021 --pipeline_parallel_size 3 --gpu_memory_utilization 0.93 --max_num_seqs 8 --max_model_len 32768 --seed 42 --enable-auto-tool-choice --tool-call-parser hermes --enable-log-requests --enable-log-outputs --disable-log-stats --log-error-stack # $ncp # --chat-template ./qwen3_omni_chatmpl.jinja --no-enable-prefix-caching ) vllm serve $bmc "${params[@]}" ``` The model I use here is Qwen3-30B-A3B-Thinking-2507. I don't know if it applies to other models or other scenarios. I have changed nothing but VLLM and necessary dependencies to produce this issue. ###...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: 0.10.2 to 0.11.0, Qwen3-30B-A3B-Thinking-2507 behaves notably worse especially in toolcalling scenarios. - It generates in English instead of target language more often - It fails to use any tool much more often - Its o...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: [Bug]: Qwen3 MoE toolcalling quality decrease significantly after updating to 0.11.0 bug ### Your current environment ### 🐛 Describe the bug After updating from 0.10.2 to 0.11.0, Qwen3-30B-A3B-Thinking-2507 behaves nota...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: ue. ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [MoE、GEMM 与 Expert Routing](../patterns/moe_gemm_routing.md) - 分数 2: [Bug]: Qwen3 MoE toolcalling quality decrease significantly after updating to 0.11.0 bug ### Your current environment ### 🐛 Describe the bug After updating from 0.10.2 to 0.11.0, Qwen3-30B-A3B-Thinking-2507 behaves nota...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: --enable-auto-tool-choice --tool-call-parser hermes --enable-log-requests --enable-log-outputs --disable-log-stats --log-error-stack # $ncp # --chat-template ./qwen3_omni_chatmpl.jinja --no-enable-prefix-caching ) vllm...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
