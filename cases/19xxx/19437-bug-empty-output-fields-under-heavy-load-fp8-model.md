# vllm-project/vllm#19437: [Bug]: Empty Output fields under heavy load - FP8 Model

| 字段 | 值 |
| --- | --- |
| Issue | [#19437](https://github.com/vllm-project/vllm/issues/19437) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 6; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | attention_kv_cache;ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;quantization;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | attention;cuda;fp8;operator;sampling;triton |
| 症状 | build_error;nan_inf |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Empty Output fields under heavy load - FP8 Model

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug I am serving the [RedHatAI/Llama-4-Scout-17B-16E-Instruct-FP8-dynamic](https://huggingface.co/RedHatAI/Llama-4-Scout-17B-16E-Instruct-FP8-dynamic) model via the CLI. ``` vllm serve \ $MODEL_NAME \ --tensor-parallel-size \ --port 8000 \ --no-enable-prefix-caching \ --disable-log-requests \ --max-model-len 8192 --kv-cache-dtype ``` When the vLLM serving instance is hit with a heavy load - **enough to cause preemptions**, the following requests are all returned with empty outputs. The serving returns usage metrics as if it did generate the full sequence length(In our case, about 2048 output tokens). This happens irrespective of : - kv-cache-dtype - cascade-attention (enabled/disabled) This happens with vLLM 0.8.4 and 0.8.5(haven't been able to test top of main yet and fp8 was broken in 0.9.0 docker image). The issue does not surface if the server isn't hit with enough load to cause preemptions in the first place. ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: .5(haven't been able to test top of main yet and fp8 was broken in 0.9.0 docker image). The issue does not surface if the server isn't hit with enough load to cause preemptions in the first place. ### Before submitting...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 3: [Bug]: Empty Output fields under heavy load - FP8 Model bug;stale ### Your current environment ### 🐛 Describe the bug I am serving the [RedHatAI/Llama-4-Scout-17B-16E-Instruct-FP8-dynamic](https://huggingface.co/RedHatA...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: [Bug]: Empty Output fields under heavy load - FP8 Model bug;stale ### Your current environment ### 🐛 Describe the bug I am serving the [RedHatAI/Llama-4-Scout-17B-16E-Instruct-FP8-dynamic](https://huggingface.co/RedHatA...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 3: [Bug]: Empty Output fields under heavy load - FP8 Model bug;stale ### Your current environment ### 🐛 Describe the bug I am serving the [RedHatAI/Llama-4-Scout-17B-16E-Instruct-FP8-dynamic](https://huggingface.co/RedHatA...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: e. ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), whi...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
