# vllm-project/vllm#25647: [Bug]: 4xH800 Qwen/Qwen3-Next-80B-A3B-Instruct MTP, assert error, assert (m.num_reqs * (self.num_spec + 1) <= m.num_actual_tokens

| 字段 | 值 |
| --- | --- |
| Issue | [#25647](https://github.com/vllm-project/vllm/issues/25647) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 8; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | attention_kv_cache;ci_build;distributed_parallel;frontend_api;model_support;speculative_decoding |
| 子分类 | cold_start |
| Operator 关键词 | attention;cuda |
| 症状 | crash |
| 根因提示 | env_dependency |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: 4xH800 Qwen/Qwen3-Next-80B-A3B-Instruct MTP, assert error, assert (m.num_reqs * (self.num_spec + 1) <= m.num_actual_tokens

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug ### Your current environment main branch According recipes Guide Use MTP: [[Qwen3-Next]](https://docs.vllm.ai/projects/recipes/en/latest/Qwen/Qwen3-Next.html) ``` but "num_speculative_tokens": 3 works well ``` `checkout to 072d7e53e534d337b41262dd44ded9b44aa699ef "num_speculative_tokens": 2 works well` ### 🐛 Describe the bug ``` uv venv source .venv/bin/activate uv pip install vllm --extra-index-url https://wheels.vllm.ai/nightly ``` ``` vllm serve Qwen/Qwen3-Next-80B-A3B-Instruct \ --tokenizer-mode auto --gpu-memory-utilization 0.8 \ --speculative-config '{"method": "qwen3_next_mtp", "num_speculative_tokens": 2}' \ --tensor-parallel-size 4 --no-enable-chunked-prefill 2>&1 | tee ./test_mtp.log ``` ``` vllm bench serve \ --backend vllm \ --model Qwen/Qwen3-Next-80B-A3B-Instruct \ --endpoint /v1/completions \ --dataset-name random \ --random-input 2048 \ --random-output 1024 \ --max-concurrency 10 \ --num-prompt 100 ``` Error Log: ``` Capturing CUDA graphs (mixed prefill-decode, PIECEWISE): 100%|██████████| 67/67 [00:07 (APIServer pid=68859) sys.exit(main()) (APIServer pid=68859) ^^^^^^ (APIServer pid=68859) File "/root/.cache/cwq/...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 5: escribe the bug ### Your current environment main branch According recipes Guide Use MTP: [[Qwen3-Next]](https://docs.vllm.ai/projects/recipes/en/latest/Qwen/Qwen3-Next.html) ``` but "num_speculative_tokens": 3 works we...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: [Bug]: 4xH800 Qwen/Qwen3-Next-80B-A3B-Instruct MTP, assert error, assert (m.num_reqs * (self.num_spec + 1) <= m.num_actual_tokens bug ### Your current environment ### 🐛 Describe the bug ### Your current environment main...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 3: s.vllm.ai/projects/recipes/en/latest/Qwen/Qwen3-Next.html) ``` but "num_speculative_tokens": 3 works well ``` `checkout to 072d7e53e534d337b41262dd44ded9b44aa699ef "num_speculative_tokens": 2 works well` ### 🐛 Describe...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 2: hunked-prefill 2>&1 | tee ./test_mtp.log ``` ``` vllm bench serve \ --backend vllm \ --model Qwen/Qwen3-Next-80B-A3B-Instruct \ --endpoint /v1/completions \ --dataset-name random \ --random-input 2048 \ --random-output...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: --max-concurrency 10 \ --num-prompt 100 ``` Error Log: ``` Capturing CUDA graphs (mixed prefill-decode, PIECEWISE): 100%|██████████| 67/67 [00:07 (APIServer pid=68859) sys.exit(main()) (APIServer pid=68859) ^^^^^^ (APIS...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
