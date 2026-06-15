# vllm-project/vllm#35706: [Bug]: CUDA illegal memory access on H200 MiniMax-M2.5

| 字段 | 值 |
| --- | --- |
| Issue | [#35706](https://github.com/vllm-project/vllm/issues/35706) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 8; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | distributed_parallel;frontend_api;model_support;quantization;sampling_logits;scheduler_memory |
| 子分类 | kernel_eff |
| Operator 关键词 | cuda;fp8;quantization;sampling |
| 症状 | crash |
| 根因提示 | dtype;env_dependency;race_condition |
| 硬件范围 | nvidia |
| 需要人工复核 | True |

## 源证据

### Issue 标题

> [Bug]: CUDA illegal memory access on H200 MiniMax-M2.5

### Issue 正文摘录

### Your current environment MiniMax-M2.5, FP8 quantization, H200 (TP=4), `vllm/vllm-openai:v0.16.0` image ### 🐛 Describe the bug `vllm serve MiniMaxAI/MiniMax-M2.5 --port 8888 --tensor-parallel-size=4 --gpu-memory-utilization 0.95 --max-model-len 9416 --disable-log-requests --trust-remote-code` Then `python3 -m lm_eval --model local-chat-completions --apply_chat_template --tasks utils/evals/gsm8k.yaml --num_fewshot 2 --output_path /tmp/eval_out-yn0Los --log_samples --model_args 'model=MiniMaxAI/MiniMax-M2.5,base_url=http://0.0.0.0:8888/v1/chat/completions,api_key=EMPTY,eos_string= ,max_retries=5,num_concurrent=8,timeout=600,tokenized_requests=False,max_length=16384' --gen_kwargs max_tokens=8192,temperature=0,top_p=1` ```text Exception raised from c10_cuda_check_implementation at /pytorch/c10/cuda/CUDAException.cpp:44 (most recent call first): frame #0: c10::Error::Error(c10::SourceLocation, std::__cxx11::basic_string , std::allocator >) + 0x80 (0x1546e517cb80 in /usr/local/lib/python3.12/dist-packages/torch/lib/libc10.so) frame #1: + 0x11fb7 (0x1546e5521fb7 in /usr/local/lib/python3.12/dist-packages/torch/lib/libc10_cuda.so) frame #2: c10d::ProcessGroupNCCL::WorkNCCL::finishedGPU...

## 现有链接修复摘要

#4 Use FlashAttention for `multi_query_kv_attention` | #6 Automatically configure KV cache size | #7 Support beam search & parallel generation

## 候选优化模式

- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 3: cess on H200 MiniMax-M2.5 bug ### Your current environment MiniMax-M2.5, FP8 quantization, H200 (TP=4), `vllm/vllm-openai:v0.16.0` image ### 🐛 Describe the bug `vllm serve MiniMaxAI/MiniMax-M2.5 --port 8888 --tensor-par...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: [Bug]: CUDA illegal memory access on H200 MiniMax-M2.5 bug ### Your current environment MiniMax-M2.5, FP8 quantization, H200 (TP=4), `vllm/vllm-openai:v0.16.0` image ### 🐛 Describe the bug `vllm serve MiniMaxAI/MiniMax-...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: --port 8888 --tensor-parallel-size=4 --gpu-memory-utilization 0.95 --max-model-len 9416 --disable-log-requests --trust-remote-code` Then `python3 -m lm_eval --model local-chat-completions --apply_chat_template --tasks u...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 3: -size=4 --gpu-memory-utilization 0.95 --max-model-len 9416 --disable-log-requests --trust-remote-code` Then `python3 -m lm_eval --model local-chat-completions --apply_chat_template --tasks utils/evals/gsm8k.yaml --num_f...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 2: en 9416 --disable-log-requests --trust-remote-code` Then `python3 -m lm_eval --model local-chat-completions --apply_chat_template --tasks utils/evals/gsm8k.yaml --num_fewshot 2 --output_path /tmp/eval_out-yn0Los --log_s...

## 关联 PR 证据

| PR | 链接类型 | 置信度 | PR 标题 | 证据 |
| --- | --- | ---: | --- | --- |
| [#4](https://github.com/vllm-project/vllm/pull/4) | mentioned | 0.45 | Use FlashAttention for `multi_query_kv_attention` | 53 (0x1546ddadc253 in /usr/lib/x86_64-linux-gnu/libstdc++.so.6) frame #4: <unknown function> + 0x94ac3 (0x1546e6294ac3 in /usr/lib/x86_64-linux-gnu/libc.so.6) frame #5: <unknown f… |
| [#6](https://github.com/vllm-project/vllm/pull/6) | mentioned | 0.45 | Automatically configure KV cache size | /local/lib/python3.12/dist-packages/torch/lib/libtorch_cuda.so) frame #6: <unknown function> + 0xdc253 (0x1546ddadc253 in /usr/lib/x86_64-linux-gnu/libstdc++.so.6) frame #7: <unkn… |
| [#7](https://github.com/vllm-project/vllm/pull/7) | mentioned | 0.45 | Support beam search & parallel generation | 53 (0x1546ddadc253 in /usr/lib/x86_64-linux-gnu/libstdc++.so.6) frame #7: <unknown function> + 0x94ac3 (0x1546e6294ac3 in /usr/lib/x86_64-linux-gnu/libc.so.6) frame #8: <unknown f… |

## Wiki 抽取状态

- 后续迭代应在可用时读取完整讨论评论。
