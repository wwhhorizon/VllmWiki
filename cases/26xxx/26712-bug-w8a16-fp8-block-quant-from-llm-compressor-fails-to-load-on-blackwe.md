# vllm-project/vllm#26712: [Bug]: W8A16-FP8_Block Quant from llm_Compressor Fails to load on Blackwell SM12.0

| 字段 | 值 |
| --- | --- |
| Issue | [#26712](https://github.com/vllm-project/vllm/issues/26712) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 9; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | distributed_parallel;hardware_porting;model_support;multimodal_vlm;quantization |
| 子分类 | wrong_output |
| Operator 关键词 | cuda;operator;quantization |
| 症状 | crash;mismatch |
| 根因提示 | env_dependency;shape |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: W8A16-FP8_Block Quant from llm_Compressor Fails to load on Blackwell SM12.0

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug Here's the relevant section: ``` AttributeError: 'QKVParallelLinear' object has no attribute 'orig_dtype' ... in compressed_tensors/schemes/compressed_tensors_w8a8_fp8.py ... -> maybe_post_process_fp8_weight_block(...) -> fp8_utils.py ``` FULL Error Code here: ``` Loading safetensors checkpoint shards: 0% Completed | 0/26 [00:00 [1m[36m(APIServer pid=71476)[0m sys.exit(main()) [1m[36m(APIServer pid=71476)[0m ^^^^^^ [1m[36m(APIServer pid=71476)[0m File "/home/phaedawg/vllm/venv/lib/python3.12/site-packages/vllm/entrypoints/cli/main.py", line 54, in main [1m[36m(APIServer pid=71476)[0m args.dispatch_function(args) [1m[36m(APIServer pid=71476)[0m File "/home/phaedawg/vllm/venv/lib/python3.12/site-packages/vllm/entrypoints/cli/serve.py", line 57, in cmd [1m[36m(APIServer pid=71476)[0m uvloop.run(run_server(args)) [1m[36m(APIServer pid=71476)[0m File "/home/phaedawg/vllm/venv/lib/python3.12/site-packages/uvloop/__init__.py", line 109, in run [1m[36m(APIServer pid=71476)[0m return __asyncio.run( [1m[36m(APIServer pid=71476)[0m ^^^^^^^^^^^^^^ [1m[36m(APIServer pid=71476)[0m File "/usr/lib/python3.12/asyncio...

## 候选优化模式

- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 4: [Bug]: W8A16-FP8_Block Quant from llm_Compressor Fails to load on Blackwell SM12.0 bug;stale ### Your current environment ### 🐛 Describe the bug Here's the relevant section: ``` AttributeError: 'QKVParallelLinear' objec...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: gs [1m[36m(APIServer pid=71476)[0m async_llm = AsyncLLM.from_vllm_config( [1m[36m(APIServer pid=71476)[0m ^^^^^^^^^^^^^^^^^^^^^^^^^^ [1m[36m(APIServer pid=71476)[0m File "/home/phaedawg/vllm/venv/lib/python3.12...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: y", line 109, in run [1m[36m(APIServer pid=71476)[0m return __asyncio.run( [1m[36m(APIServer pid=71476)[0m ^^^^^^^^^^^^^^ [1m[36m(APIServer pid=71476)[0m File "/usr/lib/python3.12/asyncio/runners.py", line 194,...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 3: [Bug]: W8A16-FP8_Block Quant from llm_Compressor Fails to load on Blackwell SM12.0 bug;stale ### Your current environment ### 🐛 Describe the bug Here's the relevant section: ``` AttributeError: 'QKVParallelLinear' objec...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: i/main.py", line 54, in main [1m[36m(APIServer pid=71476)[0m args.dispatch_function(args) [1m[36m(APIServer pid=71476)[0m File "/home/phaedawg/vllm/venv/lib/python3.12/site-packages/vllm/entrypoints/cli/serve.py",...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
