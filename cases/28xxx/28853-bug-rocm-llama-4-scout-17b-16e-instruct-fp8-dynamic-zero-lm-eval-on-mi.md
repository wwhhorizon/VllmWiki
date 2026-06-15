# vllm-project/vllm#28853: [Bug][ROCm]: Llama-4-Scout-17B-16E-Instruct-FP8-dynamic zero Lm_eval on MI300x

| 字段 | 值 |
| --- | --- |
| Issue | [#28853](https://github.com/vllm-project/vllm/issues/28853) |
| 状态 | closed |
| 标签 | bug;rocm |
| 评论 | 4; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;quantization;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cuda;fp8;kernel;operator;sampling;triton |
| 症状 | build_error;nan_inf |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug][ROCm]: Llama-4-Scout-17B-16E-Instruct-FP8-dynamic zero Lm_eval on MI300x

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug `RedHatAI/Llama-4-Scout-17B-16E-Instruct-FP8-dynamic` produces gibberish when running with or without Aiter. Below is the command to run the server and lm_eval score: **vLLM server:** ```bash VLLM_USE_V1=1 \ VLLM_ROCM_USE_AITER=0 \ SAFETENSORS_FAST_GPU=1 \ HIP_VISIBLE_DEVICES=4,5,6,7 \ vllm serve RedHatAI/Llama-4-Scout-17B-16E-Instruct-FP8-dynamic \ --trust-remote-code \ --disable-log-requests \ --tensor-parallel-size 4 \ --gpu-memory-utilization 0.9 ``` **lm_eval score:** ``` |Tasks|Version| Filter |n-shot| Metric | |Value| |Stderr| |-----|------:|----------------|-----:|-----------|---|----:|---|-----:| |gsm8k| 3|flexible-extract| 5|exact_match|↑ | 0|± | 0| | | |strict-match | 5|exact_match|↑ | 0|± | 0| ``` ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 7: [Bug][ROCm]: Llama-4-Scout-17B-16E-Instruct-FP8-dynamic zero Lm_eval on MI300x bug;rocm ### Your current environment ### 🐛 Describe the bug `RedHatAI/Llama-4-Scout-17B-16E-Instruct-FP8-dynamic` produces gibberish when r...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: size 4 \ --gpu-memory-utilization 0.9 ``` **lm_eval score:** ``` |Tasks|Version| Filter |n-shot| Metric | |Value| |Stderr| |-----|------:|----------------|-----:|-----------|---|----:|---|-----:| |gsm8k| 3|flexible-extr...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 3: [Bug][ROCm]: Llama-4-Scout-17B-16E-Instruct-FP8-dynamic zero Lm_eval on MI300x bug;rocm ### Your current environment ### 🐛 Describe the bug `RedHatAI/Llama-4-Scout-17B-16E-Instruct-FP8-dynamic` produces gibberish when r...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 2: 6E-Instruct-FP8-dynamic` produces gibberish when running with or without Aiter. Below is the command to run the server and lm_eval score: **vLLM server:** ```bash VLLM_USE_V1=1 \ VLLM_ROCM_USE_AITER=0 \ SAFETENSORS_FAST...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: [Bug][ROCm]: Llama-4-Scout-17B-16E-Instruct-FP8-dynamic zero Lm_eval on MI300x bug;rocm ### Your current environment ### 🐛 Describe the bug `RedHatAI/Llama-4-Scout-17B-16E-Instruct-FP8-dynamic` produces gibberish when r...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
