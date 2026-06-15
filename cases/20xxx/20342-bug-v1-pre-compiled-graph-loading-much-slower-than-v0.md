# vllm-project/vllm#20342: [Bug]: V1 pre-compiled graph loading much slower than V0

| 字段 | 值 |
| --- | --- |
| Issue | [#20342](https://github.com/vllm-project/vllm/issues/20342) |
| 状态 | closed |
| 标签 | bug;torch.compile;unstale |
| 评论 | 7; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;hardware_porting;model_support;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cuda;operator;sampling;triton |
| 症状 | build_error;nan_inf;slowdown |
| 根因提示 | env_dependency;shape |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: V1 pre-compiled graph loading much slower than V0

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug When using V0, loading compilation artifacts typically takes single-digit seconds. However, with V1 it takes around 30x longer, e.g. 70s for the graph for a single shape for a larger model. This can be tested by observing the compilation graph load times when running the same command a 2nd time (allowing vLLM to load the pre-compiled graphs from the cache rather than compiling from scratch): ```bash export VLLM_USE_V1=1 MODEL_NAME="deepseek-ai/DeepSeek-R1-Distill-Qwen-1.5B" echo "Running with compilation config " python3 -m vllm.entrypoints.openai.api_server \ --port 8080 \ --model $MODEL_NAME \ --served-model-name $MODEL_NAME \ --gpu-memory-utilization 0.95 \ --disable-custom-all-reduce \ --tensor-parallel-size 1 \ --enable-chunked-prefill \ --disable-log-requests \ --enable-reasoning \ --compilation-config '{"compile_sizes": [1], "level": 3, "cudagraph_capture_sizes": [256, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 144, 136, 16, 152, 24, 128, 160, 32, 168, 40, 176, 48, 184, 56, 192, 64, 200, 72, 208, 80, 216, 88, 120, 224, 96, 232, 104, 240, 112, 248, 248]}' \ --reasoning-parser deepseek_r1 ``` If one sets `export VLLM...

## 现有链接修复摘要

#34648 [Feature] Add VLLM_TRITON_AUTOTUNE with functional autotune control

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: [Bug]: V1 pre-compiled graph loading much slower than V0 bug;torch.compile;unstale ### Your current environment ### 🐛 Describe the bug When using V0, loading compilation artifacts typically takes single-digit seconds. H...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: round 30x longer, e.g. 70s for the graph for a single shape for a larger model. This can be tested by observing the compilation graph load times when running the same command a 2nd time (allowing vLLM to load the pre-co...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 4: ]: V1 pre-compiled graph loading much slower than V0 bug;torch.compile;unstale ### Your current environment ### 🐛 Describe the bug When using V0, loading compilation artifacts typically takes single-digit seconds. Howev...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 2: ains why it's so slow to initialize. V0: ```bash DEBUG 07-01 21:11:24 [backends.py:123] Directly load the 0-th graph for shape 1 from inductor via handle ('fn7nwql5utlkjsob3xnghodbg4wpmfszfp4t5rbntqa4tjau3wp5', '/root/....
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: -reasoning \ --compilation-config '{"compile_sizes": [1], "level": 3, "cudagraph_capture_sizes": [256, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 144, 136, 16, 152, 24, 128, 160, 32, 168, 40, 176, 48, 184, 56, 1...

## 关联 PR 证据

| PR | 链接类型 | 置信度 | PR 标题 | 证据 |
| --- | --- | ---: | --- | --- |
| [#34648](https://github.com/vllm-project/vllm/pull/34648) | mentioned | 0.6 | [Feature] Add VLLM_TRITON_AUTOTUNE with functional autotune control | conds to minutes depending on kernel count and shape variety (#19824, #20342) 3. **Cross-run instability** — same model + same hardware can produce different results (#26381) ###… |

## Wiki 抽取状态

- 后续迭代应在可用时读取完整讨论评论。
