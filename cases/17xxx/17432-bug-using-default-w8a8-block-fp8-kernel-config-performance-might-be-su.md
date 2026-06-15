# vllm-project/vllm#17432: [Bug]: Using default W8A8 Block FP8 kernel config. Performance might be sub-optimal!

| 字段 | 值 |
| --- | --- |
| Issue | [#17432](https://github.com/vllm-project/vllm/issues/17432) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | ci_build;distributed_parallel;hardware_porting;model_support;quantization;sampling_logits;speculative_decoding |
| 子分类 | kernel_eff |
| Operator 关键词 | cuda;fp8;kernel;operator;sampling;triton |
| 症状 | build_error |
| 根因提示 | dtype;env_dependency;memory_layout |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Using default W8A8 Block FP8 kernel config. Performance might be sub-optimal!

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug CUDA_VISIBLE_DEVICES=0,1 python3 -m vllm.entrypoints.openai.api_server --model /workspace/llm_models/Qwen3-30B-A3B-FP8/ --dtype auto --host 0.0.0.0 --port 8012 --trust-remote-code --max-model-len 32000 --max-num-seqs 30 --tensor-parallel-size 2 --gpu-memory-utilization 0.90 --served-model-name Qwen3-30B --disable-log-requests --enable-auto-tool-choice --tool-call-parser hermes ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: test/), which can answer lots of frequently asked questions. performance ci_build;distributed_parallel;hardware_porting;model_support;quantization;sampling_logits;speculative_decoding cuda;fp8;kernel;operator;sampling;t...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 3: [Bug]: Using default W8A8 Block FP8 kernel config. Performance might be sub-optimal! bug;stale ### Your current environment ### 🐛 Describe the bug CUDA_VISIBLE_DEVICES=0,1 python3 -m vllm.entrypoints.openai.api_server -...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: [Bug]: Using default W8A8 Block FP8 kernel config. Performance might be sub-optimal! bug;stale ### Your current environment ### 🐛 Describe the bug CUDA_VISIBLE_DEVICES=0,1 python3 -m vllm.entrypoints.openai.api_server -...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 3: ault W8A8 Block FP8 kernel config. Performance might be sub-optimal! bug;stale ### Your current environment ### 🐛 Describe the bug CUDA_VISIBLE_DEVICES=0,1 python3 -m vllm.entrypoints.openai.api_server --model /workspac...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: imal! bug;stale ### Your current environment ### 🐛 Describe the bug CUDA_VISIBLE_DEVICES=0,1 python3 -m vllm.entrypoints.openai.api_server --model /workspace/llm_models/Qwen3-30B-A3B-FP8/ --dtype auto --host 0.0.0.0 --p...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
