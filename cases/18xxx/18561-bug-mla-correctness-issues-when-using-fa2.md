# vllm-project/vllm#18561: [Bug]: MLA correctness issues when using FA2

| 字段 | 值 |
| --- | --- |
| Issue | [#18561](https://github.com/vllm-project/vllm/issues/18561) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 0; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | attention_kv_cache;ci_build;distributed_parallel;frontend_api;gemm_linear;hardware_porting;model_support;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | attention;cuda;operator;sampling;triton |
| 症状 | build_error;nan_inf |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: MLA correctness issues when using FA2

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug When running MLA with FA3 enabled (default on H100), models like `deepseek-ai/DeepSeek-V2-Lite-Chat` work perfectly fine FA3 TritonMLA on H100: ``` VLLM_ATTENTION_BACKEND=TRITON_MLA lm_eval --model vllm --model_args pretrained=deepseek-ai/DeepSeek-V2-Lite-Chat --trust_remote_code --tasks gsm8k --num_fewshot 5 --batch_size auto vllm (pretrained=deepseek-ai/DeepSeek-V2-Lite-Chat,trust_remote_code=True), gen_kwargs: (None), limit: None, num_fewshot: 5, batch_size: auto |Tasks|Version| Filter |n-shot| Metric | |Value | |Stderr| |-----|------:|----------------|-----:|-----------|---|-----:|---|-----:| |gsm8k| 3|flexible-extract| 5|exact_match|↑ |0.6672|± | 0.013| | | |strict-match | 5|exact_match|↑ |0.6603|± | 0.013| ``` FA3 FlashMLA on H100: ``` lm_eval --model vllm --model_args pretrained=deepseek-ai/DeepSeek-V2-Lite-Chat --trust_remote_code --tasks gsm8k --num_fewshot 5 --batch_size auto vllm (pretrained=deepseek-ai/DeepSeek-V2-Lite-Chat,trust_remote_code=True), gen_kwargs: (None), limit: None, num_fewshot: 5, batch_size: auto |Tasks|Version| Filter |n-shot| Metric | |Value | |Stderr| |-----|------:|----------------|-----:|--------...

## 候选优化模式

- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 5: ### 🐛 Describe the bug When running MLA with FA3 enabled (default on H100), models like `deepseek-ai/DeepSeek-V2-Lite-Chat` work perfectly fine FA3 TritonMLA on H100: ``` VLLM_ATTENTION_BACKEND=TRITON_MLA lm_eval --mode...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: gen_kwargs: (None), limit: None, num_fewshot: 5, batch_size: auto |Tasks|Version| Filter |n-shot| Metric | |Value | |Stderr| |-----|------:|----------------|-----:|-----------|---|-----:|---|-----:| |gsm8k| 3|flexible-e...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 3: ur current environment ### 🐛 Describe the bug When running MLA with FA3 enabled (default on H100), models like `deepseek-ai/DeepSeek-V2-Lite-Chat` work perfectly fine FA3 TritonMLA on H100: ``` VLLM_ATTENTION_BACKEND=TR...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 2: ly fine FA3 TritonMLA on H100: ``` VLLM_ATTENTION_BACKEND=TRITON_MLA lm_eval --model vllm --model_args pretrained=deepseek-ai/DeepSeek-V2-Lite-Chat --trust_remote_code --tasks gsm8k --num_fewshot 5 --batch_size auto vll...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: 🐛 Describe the bug When running MLA with FA3 enabled (default on H100), models like `deepseek-ai/DeepSeek-V2-Lite-Chat` work perfectly fine FA3 TritonMLA on H100: ``` VLLM_ATTENTION_BACKEND=TRITON_MLA lm_eval --model vl...

## Wiki 抽取状态

- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
