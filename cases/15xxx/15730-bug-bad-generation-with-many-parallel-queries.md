# vllm-project/vllm#15730: [Bug]: Bad generation with many parallel queries

| 字段 | 值 |
| --- | --- |
| Issue | [#15730](https://github.com/vllm-project/vllm/issues/15730) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 5; 本地原始数据只有评论数量，没有评论正文 |
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

> [Bug]: Bad generation with many parallel queries

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug To repro this I started with a clean venv and `pip install vllm`. I think any test case can be used, but an easily available self-verifying test is MMLU, e.g. [chigkim/Ollama-MMLU-Pro](https://github.com/chigkim/Ollama-MMLU-Pro) Server args: ``` vllm serve --dtype auto --gpu-memory-utilization 0.92 --served-model-name llama3.3:70b \ --disable-log-requests --max-model-len 16384 --tensor-parallel-size 2 --enable-auto-tool-choice \ --tool-call-parser llama3_json --generation-config auto --trust-remote-code --enable-prefix-caching \ --enable-chunked-prefill -- ~/models/Meta-Llama-3.3-70B-Instruct-AWQ-INT4 ``` Note: `--enable-chunked-prefill` doesn't matter, but the problem does seem to go away with `--no-enable-prefix-caching`, but I don't know if that's just because the entire pattern of generation is quite different. Note: Also reproduces with `--tensor-parallel-size 1` (for models that fit) but requires higher parallelism, e.g. 100x Note: Also reproduced with `Qwen2.5-32B-Instruct-GPTQ-Int4` and `Qwen2.5-32B-Instruct` (FP16). `Qwen2.5-72B-Instruct-AWQ` reproduces the problem but it took more than one try (failure rate per request...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: # 🐛 Describe the bug To repro this I started with a clean venv and `pip install vllm`. I think any test case can be used, but an easily available self-verifying test is MMLU, e.g. [chigkim/Ollama-MMLU-Pro](https://githu...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: sed, but an easily available self-verifying test is MMLU, e.g. [chigkim/Ollama-MMLU-Pro](https://github.com/chigkim/Ollama-MMLU-Pro) Server args: ``` vllm serve --dtype auto --gpu-memory-utilization 0.92 --served-model-...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 4: [Bug]: Bad generation with many parallel queries bug;stale ### Your current environment ### 🐛 Describe the bug To repro this I started with a clean venv and `pip install vllm`. I think any test case can be used, but an...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 3: tps://github.com/chigkim/Ollama-MMLU-Pro) Server args: ``` vllm serve --dtype auto --gpu-memory-utilization 0.92 --served-model-name llama3.3:70b \ --disable-log-requests --max-model-len 16384 --tensor-parallel-size 2 -...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: nsor-parallel-size 1` (for models that fit) but requires higher parallelism, e.g. 100x Note: Also reproduced with `Qwen2.5-32B-Instruct-GPTQ-Int4` and `Qwen2.5-32B-Instruct` (FP16). `Qwen2.5-72B-Instruct-AWQ` reproduces...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
