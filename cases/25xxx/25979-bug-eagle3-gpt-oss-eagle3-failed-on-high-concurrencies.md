# vllm-project/vllm#25979: [Bug]: EAGLE3 gpt-oss eagle3 failed on high concurrencies

| 字段 | 值 |
| --- | --- |
| Issue | [#25979](https://github.com/vllm-project/vllm/issues/25979) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;quantization;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cuda;operator;quantization;sampling;triton |
| 症状 | build_error;nan_inf |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: EAGLE3 gpt-oss eagle3 failed on high concurrencies

### Issue 正文摘录

### Your current environment Followed standard installation steps on main branch https://docs.vllm.ai/en/latest/getting_started/installation/gpu.html#pre-built-images ### 🐛 Describe the bug ```bash VLLM_USE_TRTLLM_ATTENTION=1 VLLM_USE_FLASHINFER_MOE_MXFP4_MXFP8=1 \ vllm serve openai/gpt-oss-120b \ --no-enable-prefix-caching \ --trust-remote-code \ --speculative-config '{"model": "nvidia/gpt-oss-120b-Eagle3", "num_speculative_tokens": 3, "method":"eagle3", "draft_tensor_parallel_size":1}' \ --port 30000 \ --max-num-seqs 2048 \ -tp 1 & ``` lm_eval command `lm_eval --model local-completions --tasks gsm8k --model_args model=openai/gpt-oss-120b,base_url=http://0.0.0.0:30000/v1/completions,max_retries=3,tokenized_requests=False,timeout=1200,max_gen_toks=2048,max_length=8192 --batch_size 2048 --trust_remote_code --limit 0.8` Attached full log because of word limit [eagle3_high_concur_error.txt](https://github.com/user-attachments/files/22625973/eagle3_high_concur_error.txt) ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), whic...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: [Bug]: EAGLE3 gpt-oss eagle3 failed on high concurrencies bug;stale ### Your current environment Followed standard installation steps on main branch https://docs.vllm.ai/en/latest/getting_started/installation/gpu.html#p...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 4: ibe the bug ```bash VLLM_USE_TRTLLM_ATTENTION=1 VLLM_USE_FLASHINFER_MOE_MXFP4_MXFP8=1 \ vllm serve openai/gpt-oss-120b \ --no-enable-prefix-caching \ --trust-remote-code \ --speculative-config '{"model": "nvidia/gpt-oss...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 4: [Bug]: EAGLE3 gpt-oss eagle3 failed on high concurrencies bug;stale ### Your current environment Followed standard installation steps on main branch https://docs.vllm.ai/en/latest/getting_started/installation/gpu.html#p...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: -tp 1 & ``` lm_eval command `lm_eval --model local-completions --tasks gsm8k --model_args model=openai/gpt-oss-120b,base_url=http://0.0.0.0:30000/v1/completions,max_retries=3,tokenized_requests=False,timeout=1200,max_ge...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: [Bug]: EAGLE3 gpt-oss eagle3 failed on high concurrencies bug;stale ### Your current environment Followed standard installation steps on main branch https://docs.vllm.ai/en/latest/getting_started/installation/gpu.html#p...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
