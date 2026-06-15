# vllm-project/vllm#28014: [Bug]: EngineDeadError, illegal memory access error encountered when serving qwen3-vl on h800/h20

| 字段 | 值 |
| --- | --- |
| Issue | [#28014](https://github.com/vllm-project/vllm/issues/28014) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;multimodal_vlm;quantization;sampling_logits;scheduler_memory |
| 子分类 | precision |
| Operator 关键词 | cuda;fp8;gemm;kernel;operator;quantization;sampling;triton |
| 症状 | build_error;crash;mismatch;nan_inf |
| 根因提示 | dtype;env_dependency;race_condition;shape |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: EngineDeadError, illegal memory access error encountered when serving qwen3-vl on h800/h20

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug The server has been running for half an hour around but it always crashes eventually. Looks like some input results in a kernel execution error (might be relevant to deepgemm). My start cmd: ```bash vllm serve /data/cbs/Qwen3-VL-30B-A3B-Instruct-FP8 --host 0.0.0.0 --port 30000 --tensor_parallel_size 1 --gpu_memory_utilization 0.7 --max_model_len 45000 --limit-mm-per-prompt.image 1 --limit-mm-per-prompt.video 0 > /data/cbs/server.log 2>&1 & ``` ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: ]: EngineDeadError, illegal memory access error encountered when serving qwen3-vl on h800/h20 bug;stale ### Your current environment ### 🐛 Describe the bug The server has been running for half an hour around but it alwa...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: test/), which can answer lots of frequently asked questions. correctness ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;multimodal_vlm;quantization;sampling_logits;scheduler_memory cuda;fp8;ge...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 3: ). My start cmd: ```bash vllm serve /data/cbs/Qwen3-VL-30B-A3B-Instruct-FP8 --host 0.0.0.0 --port 30000 --tensor_parallel_size 1 --gpu_memory_utilization 0.7 --max_model_len 45000 --limit-mm-per-prompt.image 1 --limit-m...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: al memory access error encountered when serving qwen3-vl on h800/h20 bug;stale ### Your current environment ### 🐛 Describe the bug The server has been running for half an hour around but it always crashes eventually. Lo...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
