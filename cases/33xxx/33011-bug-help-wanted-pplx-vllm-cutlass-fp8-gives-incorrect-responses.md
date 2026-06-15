# vllm-project/vllm#33011: [Bug][Help Wanted]: PPLX + vLLM CUTLASS FP8 Gives Incorrect Responses

| 字段 | 值 |
| --- | --- |
| Issue | [#33011](https://github.com/vllm-project/vllm/issues/33011) |
| 状态 | open |
| 标签 | bug;help wanted;stale |
| 评论 | 6; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug][Help Wanted]: PPLX + vLLM CUTLASS FP8 Gives Incorrect Responses

### Issue 正文摘录

### Your current environment - B200 Issue occurs on: - v0.13.0 - main not sure the earliest version ### 🐛 Describe the bug I get incorrect results with PPLX + vLLM CUTLASS ``` GPUS := "2" PORT := "8004" MODEL := "RedHatAI/Llama-4-Scout-17B-16E-Instruct-FP8-dynamic" launch_dp_ep_pplx: VLLM_USE_FLASHINFER_MOE_FP4=0 \ VLLM_USE_FLASHINFER_MOE_FP8=0 \ VLLM_USE_DEEP_GEMM=0 \ VLLM_FLASHINFER_MOE_BACKEND=throughput \ chg run --gpus {{GPUS}} -- vllm serve {{MODEL}} -dp {{GPUS}} --enable-expert-parallel --port {{PORT}} --enforce-eager --all2all-backend pplx --max-model-len 8192 eval: lm_eval \ --model local-completions \ --tasks gsm8k \ --model_args "model={{MODEL}},base_url=http://localhost:{{PORT}}/v1/completions,num_concurrent=1000,tokenized_requests=False" --limit 1000 ``` ``` local-completions (model=RedHatAI/Llama-4-Scout-17B-16E-Instruct-FP8-dynamic,base_url=http://localhost:8004/v1/completions,num_concurrent=1000,tokenized_requests=False), gen_kwargs: (None), limit: 1000.0, num_fewshot: None, batch_size: 1 |Tasks|Version| Filter |n-shot| Metric | |Value| |Stderr| |-----|------:|----------------|-----:|-----------|---|----:|---|-----:| |gsm8k| 3|flexible-extract| 5|exact_match|↑ |0.3...

## 候选优化模式

- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 3: [Bug][Help Wanted]: PPLX + vLLM CUTLASS FP8 Gives Incorrect Responses bug;help wanted;stale ### Your current environment - B200 Issue occurs on: - v0.13.0 - main not sure the earliest version ### 🐛 Describe the bug I ge...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: ncorrect Responses bug;help wanted;stale ### Your current environment - B200 Issue occurs on: - v0.13.0 - main not sure the earliest version ### 🐛 Describe the bug I get incorrect results with PPLX + vLLM CUTLASS ``` GP...
- [MoE、GEMM 与 Expert Routing](../patterns/moe_gemm_routing.md) - 分数 3: t-17B-16E-Instruct-FP8-dynamic" launch_dp_ep_pplx: VLLM_USE_FLASHINFER_MOE_FP4=0 \ VLLM_USE_FLASHINFER_MOE_FP8=0 \ VLLM_USE_DEEP_GEMM=0 \ VLLM_FLASHINFER_MOE_BACKEND=throughput \ chg run --gpus {{GPUS}} -- vllm serve {{...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 3: SHINFER_MOE_FP8=0 \ VLLM_USE_DEEP_GEMM=0 \ VLLM_FLASHINFER_MOE_BACKEND=throughput \ chg run --gpus {{GPUS}} -- vllm serve {{MODEL}} -dp {{GPUS}} --enable-expert-parallel --port {{PORT}} --enforce-eager --all2all-backend...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 2: [Bug][Help Wanted]: PPLX + vLLM CUTLASS FP8 Gives Incorrect Responses bug;help wanted;stale ### Your current environment - B200 Issue occurs on: - v0.13.0 - main not sure the earliest version ### 🐛 Describe the bug I ge...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
