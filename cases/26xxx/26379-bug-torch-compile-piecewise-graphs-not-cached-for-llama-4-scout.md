# vllm-project/vllm#26379: [Bug][torch.compile]: piecewise graphs not cached for LLaMa-4-Scout

| 字段 | 值 |
| --- | --- |
| Issue | [#26379](https://github.com/vllm-project/vllm/issues/26379) |
| 状态 | closed |
| 标签 | bug;torch.compile;stale |
| 评论 | 6; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;multimodal_vlm;quantization;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cuda;fp8;operator;quantization;sampling;triton |
| 症状 | build_error;nan_inf |
| 根因提示 | dtype;env_dependency;shape |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug][torch.compile]: piecewise graphs not cached for LLaMa-4-Scout

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug For some reason we recompile every subgraph instead of just compiling a few and loading the rest from cache. This only affects cold start and is not bad but still looking into why the subgraphs can't reuse artifacts from a previous subgraph. I think generally with llama we see 3 subgraph (start, end, middle). ``` python examples/offline_inference/basic/generate.py --model=nvidia/Llama-4-Scout-17B-16E-Instruct-FP8 --max-model-len=1024 ``` Output: ``` (EngineCore_DP0 pid=3419510) INFO 10-07 16:12:15 [compilation/backends.py:548] Using cache directory: /home/ProExpertProg/.cache/vllm/torch_compile_cache/597cba1e1f/rank_0_0/backbone for vLLM's torch.compile (EngineCore_DP0 pid=3419510) INFO 10-07 16:12:15 [compilation/backends.py:559] Dynamo bytecode transform time: 5.80 s (EngineCore_DP0 pid=3419510) DEBUG 10-07 16:12:16 [compilation/vllm_inductor_pass.py:63] PostCleanupPass completed in 0.4 ms (EngineCore_DP0 pid=3419510) DEBUG 10-07 16:12:16 [compilation/fix_functionalization.py:119] De-functionalized 0 nodes, removed 0 nodes (EngineCore_DP0 pid=3419510) DEBUG 10-07 16:12:16 [compilation/vllm_inductor_pass.py:63] FixFunctionalizat...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: [Bug][torch.compile]: piecewise graphs not cached for LLaMa-4-Scout bug;torch.compile;stale ### Your current environment ### 🐛 Describe the bug For some reason we recompile every subgraph instead of just compiling a few...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: [Bug][torch.compile]: piecewise graphs not cached for LLaMa-4-Scout bug;torch.compile;stale ### Your current environment ### 🐛 Describe the bug For some reason we recompile every subgraph instead of just compiling a few...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 3: nference/basic/generate.py --model=nvidia/Llama-4-Scout-17B-16E-Instruct-FP8 --max-model-len=1024 ``` Output: ``` (EngineCore_DP0 pid=3419510) INFO 10-07 16:12:15 [compilation/backends.py:548] Using cache directory: /ho...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 3: ompile]: piecewise graphs not cached for LLaMa-4-Scout bug;torch.compile;stale ### Your current environment ### 🐛 Describe the bug For some reason we recompile every subgraph instead of just compiling a few and loading...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 2: utput: ``` (EngineCore_DP0 pid=3419510) INFO 10-07 16:12:15 [compilation/backends.py:548] Using cache directory: /home/ProExpertProg/.cache/vllm/torch_compile_cache/597cba1e1f/rank_0_0/backbone for vLLM's torch.compile...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
