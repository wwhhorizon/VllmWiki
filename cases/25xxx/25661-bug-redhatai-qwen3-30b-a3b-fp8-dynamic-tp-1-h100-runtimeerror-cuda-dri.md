# vllm-project/vllm#25661: [Bug]: RedhatAI/Qwen3-30B-A3B-FP8-dynamic TP=1 H100 RuntimeError: CUDA driver error: an illegal memory access was encountered

| 字段 | 值 |
| --- | --- |
| Issue | [#25661](https://github.com/vllm-project/vllm/issues/25661) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 5; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;hardware_porting;model_support;quantization;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cuda;fp8;operator;sampling;triton |
| 症状 | build_error;nan_inf |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: RedhatAI/Qwen3-30B-A3B-FP8-dynamic TP=1 H100 RuntimeError: CUDA driver error: an illegal memory access was encountered

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug We run into CUDA Runtime Error: Illegal Memory Access while attempting to run a sequence length of just 8k ISL + 2k OSL at concurrency 25 on 1xH100. Serving command : `vllm serve RedHatAI/Qwen3-30B-A3B-FP8-dynamic --port 46005 --host 0.0.0.0` Load Test command : `guidellm benchmark --target http://localhost:46005/v1 --model RedHatAI/Qwen3-30B-A3B-FP8-dynamic --processor RedHatAI/Qwen3-30B-A3B-FP8-dynamic --rate-type concurrent --max-seconds 240 --rate 25 --output-path /tmp/tmp1g1tzy15.json --data='{"prompt_tokens": 8000,"output_tokens": 2000}'` guidellm-0.3.0 [qwen30B-A3B-fail.log](https://github.com/user-attachments/files/22533786/qwen30B-A3B-fail.log) ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: test/), which can answer lots of frequently asked questions. correctness ci_build;distributed_parallel;hardware_porting;model_support;quantization;sampling_logits;speculative_decoding cuda;fp8;operator;sampling;triton b...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 3: [Bug]: RedhatAI/Qwen3-30B-A3B-FP8-dynamic TP=1 H100 RuntimeError: CUDA driver error: an illegal memory access was encountered bug;stale ### Your current environment ### 🐛 Describe the bug We run into CUDA Runtime Error:...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: [Bug]: RedhatAI/Qwen3-30B-A3B-FP8-dynamic TP=1 H100 RuntimeError: CUDA driver error: an illegal memory access was encountered bug;stale ### Your current environment ### 🐛 Describe the bug We run into CUDA Runtime Error:...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: [Bug]: RedhatAI/Qwen3-30B-A3B-FP8-dynamic TP=1 H100 RuntimeError: CUDA driver error: an illegal memory access was encountered bug;stale ### Your current environment ### 🐛 Describe the bug We run into CUDA Runtime Error:...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: meError: CUDA driver error: an illegal memory access was encountered bug;stale ### Your current environment ### 🐛 Describe the bug We run into CUDA Runtime Error: Illegal Memory Access while attempting to run a sequence...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
