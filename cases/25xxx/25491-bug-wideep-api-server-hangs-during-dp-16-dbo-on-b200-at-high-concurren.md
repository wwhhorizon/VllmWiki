# vllm-project/vllm#25491: [Bug][WideEP]: API server hangs during DP=16 + DBO on B200 at high concurrency

| 字段 | 值 |
| --- | --- |
| Issue | [#25491](https://github.com/vllm-project/vllm/issues/25491) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 5; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;frontend_api;gemm_linear;hardware_porting;model_support;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cuda;operator;sampling;triton |
| 症状 | build_error;nan_inf |
| 根因提示 | env_dependency;race_condition |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug][WideEP]: API server hangs during DP=16 + DBO on B200 at high concurrency

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug When running a 2p2d B200 node configuration with Deepseek v3.1 in DP=16 + DBO for decode, the decode node is encountering a hang at high concurrency (saw this at 2k and at 4k) where requests stop completing. 15 of 16 decode DP ranks are on line: ``` File "/app/venv/lib/python3.12/site-packages/torch/cuda/streams.py", line 231, in synchronize super().synchronize() File "/app/vllm/vllm/v1/worker/gpu_model_runner.py", line 4046, in _to_list self.transfer_event.synchronize() ``` and 1 of 16 ranks (rank 7) are at: ``` File "/app/vllm/vllm/model_executor/layers/utils.py", line 92, in default_unquantized_gemm return torch.nn.functional.linear(x, weight, bias) File "/app/vllm/vllm/model_executor/layers/vocab_parallel_embedding.py", line 53, in apply return dispatch_unquantized_gemm()(layer, x, layer.weight, bias) File "/app/vllm/vllm/model_executor/layers/logits_processor.py", line 90, in _get_logits logits = lm_head.quant_method.apply(lm_head, File "/app/vllm/vllm/model_executor/layers/logits_processor.py", line 58, in forward logits = self._get_logits(hidden_states, lm_head, embedding_bias) ``` [Configuration for decode ranks 0-7](http...

## 候选优化模式

- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 4: [Bug][WideEP]: API server hangs during DP=16 + DBO on B200 at high concurrency bug ### Your current environment ### 🐛 Describe the bug When running a 2p2d B200 node configuration with Deepseek v3.1 in DP=16 + DBO for de...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 4: ing a 2p2d B200 node configuration with Deepseek v3.1 in DP=16 + DBO for decode, the decode node is encountering a hang at high concurrency (saw this at 2k and at 4k) where requests stop completing. 15 of 16 decode DP r...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: test/), which can answer lots of frequently asked questions. correctness ci_build;distributed_parallel;frontend_api;gemm_linear;hardware_porting;model_support;sampling_logits;speculative_decoding cuda;operator;sampling;...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 2: ecutor/layers/vocab_parallel_embedding.py", line 53, in apply return dispatch_unquantized_gemm()(layer, x, layer.weight, bias) File "/app/vllm/vllm/model_executor/layers/logits_processor.py", line 90, in _get_logits log...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: nt environment ### 🐛 Describe the bug When running a 2p2d B200 node configuration with Deepseek v3.1 in DP=16 + DBO for decode, the decode node is encountering a hang at high concurrency (saw this at 2k and at 4k) where...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
