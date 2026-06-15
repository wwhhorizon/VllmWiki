# vllm-project/vllm#7878: [Bug]:  Requests larger than 75k input tokens cause `Input prompt (512 tokens) is too long and exceeds the capacity of block_manager` error

| 字段 | 值 |
| --- | --- |
| Issue | [#7878](https://github.com/vllm-project/vllm/issues/7878) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 8; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;quantization;scheduler_memory |
| 子分类 | memory |
| Operator 关键词 | cuda;fp8;operator;quantization;triton |
| 症状 | build_error;oom |
| 根因提示 | dtype;env_dependency;memory_layout |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]:  Requests larger than 75k input tokens cause `Input prompt (512 tokens) is too long and exceeds the capacity of block_manager` error

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug I have a server up and running using this ``` vllm serve Mistral-Nemo-Instruct-2407/ --port 8006 --gpu-memory-utilization 0.9 --max-model-len 128000 --tensor-parallel-size 1 --pipeline-parallel-size 2 --quantization fp8 --uvicorn-log-level debug ``` on two separate `NVidia GPUs`. However recently I have started noticing this error that I do not recall seeing before. I am using `documents` that are up to `125k tokens` in size. ``` Input prompt (512 tokens) is too long and exceeds the capacity of block_manager ``` i have tried looking around the issues list and going through what I think would be the solutions. I have tried the v2 block manager. setting `max_num_batched_tokens` to all possible values (outrageously even the context window of the model) but I keep seeing that error (replace number of tokens with the tokens set at `max_num_batched_tokens`). I have also tried `enabling/disabling chunked prefill` and that didn't help either. I am not sure what's more left to do and looking for help around this problem. ### Before submitting a new issue... - [X] Make sure you already searched for relevant issues, and asked the chatbot li...

## 候选优化模式

- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 4: [Bug]: Requests larger than 75k input tokens cause `Input prompt (512 tokens) is too long and exceeds the capacity of block_manager` error bug;stale ### Your current environment ### 🐛 Describe the bug I have a server up...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: tokens cause `Input prompt (512 tokens) is too long and exceeds the capacity of block_manager` error bug;stale ### Your current environment ### 🐛 Describe the bug I have a server up and running using this ``` vllm serve...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 3: x-model-len 128000 --tensor-parallel-size 1 --pipeline-parallel-size 2 --quantization fp8 --uvicorn-log-level debug ``` on two separate `NVidia GPUs`. However recently I have started noticing this error that I do not re...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: ### Before submitting a new issue... - [X] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 2: cause `Input prompt (512 tokens) is too long and exceeds the capacity of block_manager` error bug;stale ### Your current environment ### 🐛 Describe the bug I have a server up and running using this ``` vllm serve Mistra...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
