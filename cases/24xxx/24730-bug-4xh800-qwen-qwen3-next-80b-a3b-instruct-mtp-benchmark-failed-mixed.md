# vllm-project/vllm#24730: [Bug]: 4xH800 Qwen/Qwen3-Next-80B-A3B-Instruct MTP, benchmark failed mixed_qkv_spec.view shape '[5, -1, 2048]' is invalid for input of size 104448

| 字段 | 值 |
| --- | --- |
| Issue | [#24730](https://github.com/vllm-project/vllm/issues/24730) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 10; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;moe;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cuda;moe;operator;sampling;triton |
| 症状 | build_error;nan_inf |
| 根因提示 | env_dependency;shape |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: 4xH800 Qwen/Qwen3-Next-80B-A3B-Instruct MTP, benchmark failed mixed_qkv_spec.view shape '[5, -1, 2048]' is invalid for input of size 104448

### Issue 正文摘录

### Your current environment According recipes Guide Use MTP: [[Qwen3-Next]](https://docs.vllm.ai/projects/recipes/en/latest/Qwen/Qwen3-Next.html) ### 🐛 Describe the bug ``` uv venv source .venv/bin/activate uv pip install vllm --extra-index-url https://wheels.vllm.ai/nightly ``` ``` vllm serve Qwen/Qwen3-Next-80B-A3B-Instruct \ --tokenizer-mode auto --gpu-memory-utilization 0.8 \ --speculative-config '{"method": "qwen3_next_mtp", "num_speculative_tokens": 2}' \ --tensor-parallel-size 4 --no-enable-chunked-prefill 2>&1 | tee ./test_mtp.log ``` ``` vllm bench serve \ --backend vllm \ --model Qwen/Qwen3-Next-80B-A3B-Instruct \ --endpoint /v1/completions \ --dataset-name random \ --random-input 2048 \ --random-output 1024 \ --max-concurrency 10 \ --num-prompt 100 ``` Error Log: ``` auto Use moe config 193 ^[[1;36m(Worker_TP0 pid=35966)^[[0;0m WARNING 09-12 06:46:35 [fused_moe.py:727] Using default MoE config. Performance might be sub-optimal! Config f ile not found at ['/root/.cache/cwq/qwen3-next/.venv/lib/python3.12/site-packages/vllm/model_executor/layers/fused_moe/configs/E=512,N=128,device_name=NVIDIA_H800.json'] ``` ``` 313 ^[[1;36m(Worker_TP1 pid=35967)^[[0;0m ERROR 09-12 06:4...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 5: for input of size 104448 bug ### Your current environment According recipes Guide Use MTP: [[Qwen3-Next]](https://docs.vllm.ai/projects/recipes/en/latest/Qwen/Qwen3-Next.html) ### 🐛 Describe the bug ``` uv venv source ....
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: [Bug]: 4xH800 Qwen/Qwen3-Next-80B-A3B-Instruct MTP, benchmark failed mixed_qkv_spec.view shape '[5, -1, 2048]' is invalid for input of size 104448 bug ### Your current environment According recipes Guide Use MTP: [[Qwen...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 3: -A3B-Instruct \ --tokenizer-mode auto --gpu-memory-utilization 0.8 \ --speculative-config '{"method": "qwen3_next_mtp", "num_speculative_tokens": 2}' \ --tensor-parallel-size 4 --no-enable-chunked-prefill 2>&1 | tee ./t...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 3: [Bug]: 4xH800 Qwen/Qwen3-Next-80B-A3B-Instruct MTP, benchmark failed mixed_qkv_spec.view shape '[5, -1, 2048]' is invalid for input of size 104448 bug ### Your current environment According recipes Guide Use MTP: [[Qwen...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 2: hunked-prefill 2>&1 | tee ./test_mtp.log ``` ``` vllm bench serve \ --backend vllm \ --model Qwen/Qwen3-Next-80B-A3B-Instruct \ --endpoint /v1/completions \ --dataset-name random \ --random-input 2048 \ --random-output...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
